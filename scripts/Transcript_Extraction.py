"""
YouTube Transcript Extraction Module.

Extracts video metadata and transcripts from YouTube URLs.
Saves results as markdown files with YAML frontmatter.

Usage:
    python Transcript_Extraction.py <youtube_url> <output_folder>

Example:
    python Transcript_Extraction.py "https://youtube.com/watch?v=abc123" "./Raw_Data"
"""

import argparse
import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from tenacity import retry, stop_after_attempt, wait_exponential

from yt_dlp import YoutubeDL
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    CouldNotRetrieveTranscript,
    TranscriptsDisabled,
    NoTranscriptFound,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


class TranscriptExtractionError(Exception):
    """Base exception for transcript extraction errors."""

    pass


class InvalidURLError(TranscriptExtractionError):
    """Raised when YouTube URL is invalid."""

    pass


class TranscriptNotAvailableError(TranscriptExtractionError):
    """Raised when transcript cannot be retrieved."""

    pass


class MetadataExtractionError(TranscriptExtractionError):
    """Raised when video metadata cannot be fetched."""

    pass


def sanitize_filename(title: str, max_length: int = 50) -> str:
    """
    Sanitize a title for use as a filename.

    Removes invalid characters and replaces spaces with underscores.
    Truncates to specified maximum length.

    Args:
        title: The original title string.
        max_length: Maximum length of the sanitized title.

    Returns:
        Sanitized title safe for use in filenames.

    Examples:
        >>> sanitize_filename("My Video: Episode 1")
        'My_Video_Episode_1'
    """
    if not title:
        return ""

    invalid_chars = r'[\\/*?:"<>|]'
    sanitized = re.sub(invalid_chars, "", title)
    sanitized = sanitized.replace(" ", "_")
    return sanitized[:max_length].rstrip("_")


def get_video_id(url: str) -> Optional[str]:
    """
    Extract video ID from a YouTube URL.

    Supports both standard watch URLs and short youtu.be URLs.

    Args:
        url: A valid YouTube URL.

    Returns:
        The 11-character video ID, or None if URL format not recognized.

    Examples:
        >>> get_video_id("https://youtube.com/watch?v=abc123defgh")
        'abc123defgh'
        >>> get_video_id("https://youtu.be/abc123defgh")
        'abc123defgh'
    """
    # Standard YouTube URL: youtube.com/watch?v=VIDEO_ID
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]

    # Short URL: youtu.be/VIDEO_ID
    if "be/" in url:
        return url.split("be/")[1].split("?")[0]

    return None


LANGUAGE_CODES = ["en-US", "en-GB", "en", "auto", "es", "pt"]


def _user_alert(message: str, prefix: str = "ℹ️") -> None:
    """Print user-facing alert message."""
    print(f"\n{prefix} {message}\n")
    logger.info(message)


def _get_healing_log_path() -> Path:
    """Get path to healing log file."""
    from search.config import get_config
    config = get_config()
    return config.log_dir / "healing_log.json"


def _load_healing_log() -> dict:
    """Load existing healing log or create new one."""
    log_path = _get_healing_log_path()
    if log_path.exists():
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"session_date": datetime.now().strftime("%Y-%m-%d"), "healing_events": []}


def _save_healing_log(log_data: dict) -> None:
    """Save healing log to file."""
    from search.config import get_config
    config = get_config()
    config.log_dir.mkdir(parents=True, exist_ok=True)
    log_path = _get_healing_log_path()
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=2)


def _log_healing_event(
    error_type: str,
    error_message: str,
    fixes_tried: list[dict],
    outcome: str,
    next_agent_note: str = "",
) -> None:
    """Log a self-healing event for future agent sessions."""
    log_data = _load_healing_log()
    event = {
        "timestamp": datetime.now().isoformat(),
        "module": "scripts.Transcript_Extraction",
        "error_type": error_type,
        "error_message": error_message,
        "fixes_tried": fixes_tried,
        "outcome": outcome,
        "next_agent_note": next_agent_note,
    }
    log_data["healing_events"].append(event)
    _save_healing_log(log_data)


def _try_transcript_with_language(video_id: str, lang_code: str, transcript_list: Any, fix_type: str = "manual") -> Optional[Any]:
    """Try to get transcript with a specific language code."""
    try:
        if lang_code == "auto":
            transcript = transcript_list.find_generated_transcript([])
        elif fix_type == "manual":
            transcript = transcript_list.find_manually_created_transcript([lang_code])
        else:
            transcript = transcript_list.find_generated_transcript([lang_code])
        return transcript
    except NoTranscriptFound:
        return None


def get_transcript(video_id: str, attempt: int = 1, fixes_tried: list | None = None) -> str:
    """
    Fetch transcript text from a YouTube video with language fallback.

    Attempts to find manual transcript first, then falls back to auto-generated.
    Tries multiple language codes if initial attempts fail.

    Args:
        video_id: YouTube video ID (11 characters).
        attempt: Current attempt number (for logging).
        fixes_tried: List of fixes already attempted (for logging).

    Returns:
        Transcript text with sentences joined by spaces.

    Raises:
        TranscriptNotAvailableError: If transcript cannot be retrieved.
    """
    if fixes_tried is None:
        fixes_tried = []

    try:
        transcript_api = YouTubeTranscriptApi()
        transcript_list = transcript_api.list(video_id)

        for i, lang_code in enumerate(LANGUAGE_CODES):
            if lang_code == "auto":
                _user_alert(f"Trying any available language transcript...", "🌐")
            else:
                _user_alert(f"Trying language: {lang_code}...", "🌐")

            transcript = _try_transcript_with_language(video_id, lang_code, transcript_list, "manual")
            if transcript is None:
                transcript = _try_transcript_with_language(video_id, lang_code, transcript_list, "generated")

            if transcript:
                fixes_tried.append({"action": f"lang_{lang_code}_success", "result": "success"})
                segments = transcript.fetch()
                return " ".join(segment.text for segment in segments)

            fixes_tried.append({"action": f"lang_{lang_code}", "result": "not_found"})

        raise TranscriptNotAvailableError(f"No transcript found for video {video_id} in any language")

    except TranscriptsDisabled:
        _user_alert(f"Transcripts are disabled for video {video_id}. Skipping...", "⚠️")
        _log_healing_event("TRANSCRIPT_DISABLED", f"Video {video_id}", fixes_tried, "skipped", "Transcripts disabled by uploader. Cannot auto-fix.")
        return ""

    except CouldNotRetrieveTranscript as e:
        if attempt < 2:
            _user_alert(f"Error retrieving transcript (retry {attempt + 1}/2)...", "⚠️")
            import time
            time.sleep(2)
            fixes_tried.append({"attempt": attempt, "action": "retry", "result": "failed"})
            return get_transcript(video_id, attempt + 1, fixes_tried)

        _log_healing_event("COULD_NOT_RETRIEVE", str(e), fixes_tried, "failed", "Network or API error persisted after retry.")
        raise TranscriptNotAvailableError(f"Could not retrieve transcript for video {video_id}") from e

    except Exception as e:
        _log_transcript_error("get_transcript", video_id, type(e).__name__, str(e))
        _log_healing_event(type(e).__name__, str(e), fixes_tried, "failed", f"Unexpected error: {type(e).__name__}")
        raise TranscriptNotAvailableError(f"Unexpected error retrieving transcript: {e}") from e


def _log_transcript_error(function: str, video_id: str, error_type: str, error_message: str) -> None:
    """Log transcript errors to JSON file."""
    from search.config import get_config
    config = get_config()
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "module": "scripts.Transcript_Extraction",
        "function": function,
        "video_id": video_id,
        "error_type": error_type,
        "error_message": error_message,
    }
    config.log_dir.mkdir(parents=True, exist_ok=True)
    error_log_path = config.log_dir / "errors.log"
    with open(error_log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")


def fetch_video_metadata(url: str, video_id: str) -> dict[str, Any]:
    """
    Fetch video metadata using yt-dlp.

    Args:
        url: YouTube URL.
        video_id: Video ID extracted from URL.

    Returns:
        Dictionary containing video metadata.

    Raises:
        MetadataExtractionError: If metadata cannot be fetched.
    """
    ydl_opts = {
        "skip_download": True,
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "video_id": video_id,
                "title": info.get("title", "Untitled"),
                "channel": info.get("channel", "Unknown"),
                "duration": info.get("duration"),
                "view_count": info.get("view_count"),
                "upload_date": info.get("upload_date"),
                "tags": info.get("tags", []),
                "thumbnail": info.get("thumbnail"),
            }
    except Exception as e:
        raise MetadataExtractionError(
            f"Failed to fetch metadata for {video_id}: {e}"
        ) from e


def save_transcript(
    output_path: Path,
    metadata: dict[str, Any],
    transcript_text: str,
) -> None:
    """
    Save transcript as markdown file with YAML frontmatter.

    Args:
        output_path: Path where to save the markdown file.
        metadata: Video metadata dictionary.
        transcript_text: Full transcript text.
    """
    tags_str = ", ".join(f'"{tag}"' for tag in metadata.get("tags", []))

    frontmatter = f"""---
video_id: {metadata['video_id']}
title: "{metadata['title']}"
channel: "{metadata['channel']}"
duration: {metadata['duration']}
view_count: {metadata['view_count']}
upload_date: {metadata['upload_date']}
tags: [{tags_str}]
thumbnail: {metadata['thumbnail']}
---

{transcript_text}
"""

    output_path.write_text(frontmatter, encoding="utf-8")
    logger.info(f"Saved transcript: {output_path.name}")


def process_youtube_url(url: str, output_dir: str) -> None:
    """
    Process a YouTube URL and save transcript to output directory.

    Args:
        url: YouTube video URL.
        output_dir: Directory to save transcript file.

    Raises:
        InvalidURLError: If URL is not a valid YouTube URL.
        TranscriptNotAvailableError: If transcript cannot be retrieved.
        MetadataExtractionError: If metadata cannot be fetched.
    """
    video_id = get_video_id(url)
    if not video_id:
        raise InvalidURLError(f"Invalid YouTube URL: {url}")

    _user_alert(f"Processing video: {video_id}", "📺")

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    metadata = fetch_video_metadata(url, video_id)

    transcript_text = get_transcript(video_id)
    if not transcript_text:
        _user_alert(f"No transcript available for video {video_id}. Saved metadata only.", "⚠️")

    sanitized_title = sanitize_filename(metadata.get("title", ""))
    filename = f"{video_id}_{sanitized_title}.md" if sanitized_title else f"{video_id}.md"

    save_transcript(output_path / filename, metadata, transcript_text)
    _user_alert(f"Successfully saved: {filename}", "✅")


def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        description="Extract YouTube video transcripts and metadata.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://youtube.com/watch?v=abc123" "./Raw_Data"
  %(prog)s "https://youtu.be/abc123" "./Starter_Story/Raw_Data"
        """,
    )
    parser.add_argument(
        "url",
        type=str,
        help="YouTube video URL",
    )
    parser.add_argument(
        "output_dir",
        type=str,
        default="Raw_Data",
        help="Output directory for transcript file (default: Raw_Data)",
    )
    return parser.parse_args()


def main() -> int:
    """
    Main entry point for transcript extraction.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    args = parse_arguments()

    try:
        process_youtube_url(args.url, args.output_dir)
        return 0
    except InvalidURLError as e:
        logger.error(str(e))
        return 1
    except TranscriptNotAvailableError as e:
        logger.error(f"Transcript error: {e}")
        return 1
    except MetadataExtractionError as e:
        logger.error(f"Metadata error: {e}")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())