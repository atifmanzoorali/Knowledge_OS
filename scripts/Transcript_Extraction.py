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
import logging
import re
import sys
from pathlib import Path
from typing import Any, Optional

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


def get_transcript(video_id: str) -> str:
    """
    Fetch transcript text from a YouTube video.

    Attempts to find manual transcript first, then falls back to auto-generated.
    Returns empty string if no transcript available.

    Args:
        video_id: YouTube video ID (11 characters).

    Returns:
        Transcript text with sentences joined by spaces.

    Raises:
        TranscriptNotAvailableError: If transcript cannot be retrieved.
    """
    try:
        transcript_api = YouTubeTranscriptApi()
        transcript_list = transcript_api.list(video_id)

        # Try manual transcript first, then auto-generated
        try:
            transcript = transcript_list.find_manually_created_transcript(["en"])
        except NoTranscriptFound:
            try:
                transcript = transcript_list.find_generated_transcript(["en"])
            except NoTranscriptFound as e:
                raise TranscriptNotAvailableError(
                    f"No transcript found for video {video_id}"
                ) from e

        # Fetch and join all text segments
        segments = transcript.fetch()
        return " ".join(segment.text for segment in segments)

    except TranscriptsDisabled as e:
        raise TranscriptNotAvailableError(
            f"Transcripts are disabled for video {video_id}"
        ) from e
    except CouldNotRetrieveTranscript as e:
        raise TranscriptNotAvailableError(
            f"Could not retrieve transcript for video {video_id}"
        ) from e
    except Exception as e:
        raise TranscriptNotAvailableError(
            f"Unexpected error retrieving transcript: {e}"
        ) from e


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
    # Validate URL and extract video ID
    video_id = get_video_id(url)
    if not video_id:
        raise InvalidURLError(f"Invalid YouTube URL: {url}")

    logger.info(f"Processing video: {video_id}")

    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Fetch metadata
    metadata = fetch_video_metadata(url, video_id)

    # Fetch transcript
    transcript_text = get_transcript(video_id)
    if not transcript_text:
        logger.warning(f"No transcript available for video {video_id}")
        return

    # Generate filename
    sanitized_title = sanitize_filename(metadata.get("title", ""))
    filename = f"{video_id}_{sanitized_title}.md" if sanitized_title else f"{video_id}.md"

    # Save to disk
    save_transcript(output_path / filename, metadata, transcript_text)


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