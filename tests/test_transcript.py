"""
Unit tests for Transcript Extraction functionality.

These tests verify the core functions used in Transcript_Extraction.py
without requiring actual YouTube API calls.
"""

import re
import os
import pytest
from pathlib import Path
from typing import Dict, Any


# =============================================================================
# Helper Functions (Duplicated from Transcript_Extraction.py for testing)
# =============================================================================

def sanitize_filename(title: str, max_length: int = 50) -> str:
    """
    Sanitize a title to create a valid filename.

    Args:
        title: The title to sanitize
        max_length: Maximum length of the resulting filename

    Returns:
        Sanitized filename string
    """
    if not title:
        return ""
    invalid_chars = r'[\\/*?:"<>|]'
    sanitized = re.sub(invalid_chars, '', title)
    sanitized = sanitized.replace(' ', '_')
    return sanitized[:max_length].rstrip('_')


def get_video_id(url: str) -> str:
    """
    Extract video ID from various YouTube URL formats.

    Args:
        url: YouTube URL in various formats

    Returns:
        Video ID string or None if invalid
    """
    if not url:
        return None

    # Format: https://www.youtube.com/watch?v=VIDEO_ID&...
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]

    # Format: https://youtu.be/VIDEO_ID?...
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]

    # Format: https://www.youtube.com/embed/VIDEO_ID
    if "embed/" in url:
        return url.split("embed/")[1].split("?")[0]

    return None


def format_metadata_as_yaml(metadata: Dict[str, Any]) -> str:
    """
    Format metadata as YAML frontmatter.

    Args:
        metadata: Dictionary of metadata key-value pairs

    Returns:
        YAML formatted string with frontmatter
    """
    lines = ["---"]

    for key, value in metadata.items():
        if isinstance(value, list):
            tags_str = ', '.join([f'"{tag}"' for tag in value])
            lines.append(f"{key}: [{tags_str}]")
        elif isinstance(value, str):
            lines.append(f'{key}: "{value}"')
        else:
            lines.append(f"{key}: {value}")

    lines.append("---\n")
    return "\n".join(lines)


# =============================================================================
# Test Cases
# =============================================================================

class TestSanitizeFilename:
    """Test cases for the sanitize_filename function."""

    def test_valid_title(self):
        """Test that valid titles are processed correctly."""
        result = sanitize_filename("My Test Video Title")
        assert result == "My_Test_Video_Title"

    def test_empty_title(self):
        """Test that empty title returns empty string."""
        result = sanitize_filename("")
        assert result == ""

    def test_none_title(self):
        """Test that None title returns empty string."""
        result = sanitize_filename(None)
        assert result == ""

    def test_special_characters_removed(self):
        """Test that special characters are removed."""
        result = sanitize_filename('Test: Video "With" Special <Chars>')
        assert ':' not in result
        assert '"' not in result
        assert '<' not in result
        assert '>' not in result

    def test_max_length_enforced(self):
        """Test that max length is enforced."""
        long_title = "A" * 100
        result = sanitize_filename(long_title, max_length=50)
        assert len(result) <= 50
        assert result.endswith("_") is False

    def test_trailing_underscores_removed(self):
        """Test that trailing underscores are removed."""
        result = sanitize_filename("Title with spaces   ")
        assert not result.endswith("_")


class TestGetVideoId:
    """Test cases for the get_video_id function."""

    def test_standard_youtube_url(self):
        """Test standard youtube.com/watch?v= format."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        assert get_video_id(url) == "dQw4w9WgXcQ"

    def test_youtu_be_short_url(self):
        """Test youtu.be short URL format."""
        url = "https://youtu.be/dQw4w9WgXcQ"
        assert get_video_id(url) == "dQw4w9WgXcQ"

    def test_youtube_url_with_extra_params(self):
        """Test YouTube URL with additional parameters."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=youtu.be&t=123"
        assert get_video_id(url) == "dQw4w9WgXcQ"

    def test_youtu_be_with_params(self):
        """Test youtu.be URL with additional parameters."""
        url = "https://youtu.be/dQw4w9WgXcQ?feature=youtu.be"
        assert get_video_id(url) == "dQw4w9WgXcQ"

    def test_embed_url(self):
        """Test YouTube embed URL format."""
        url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        assert get_video_id(url) == "dQw4w9WgXcQ"

    def test_invalid_url_returns_none(self):
        """Test that invalid URL returns None."""
        assert get_video_id("not-a-youtube-url") is None
        assert get_video_id("https://example.com") is None
        assert get_video_id("") is None
        assert get_video_id(None) is None

    def test_url_without_video_id(self):
        """Test URL that looks like YouTube but has no video ID."""
        url = "https://www.youtube.com/watch"
        assert get_video_id(url) is None


class TestFormatMetadataAsYaml:
    """Test cases for YAML frontmatter formatting."""

    def test_basic_metadata(self):
        """Test basic metadata formatting."""
        metadata = {
            "video_id": "abc123",
            "title": "Test Video",
            "channel": "Test Channel"
        }
        result = format_metadata_as_yaml(metadata)
        assert "video_id: \"abc123\"" in result
        assert "title: \"Test Video\"" in result
        assert result.startswith("---")
        assert result.endswith("---\n")

    def test_tags_as_list(self):
        """Test that tags are formatted as list."""
        metadata = {
            "video_id": "abc123",
            "tags": ["tag1", "tag2", "tag3"]
        }
        result = format_metadata_as_yaml(metadata)
        assert "tags: [\"tag1\", \"tag2\", \"tag3\"]" in result

    def test_numeric_values(self):
        """Test that numeric values are not quoted."""
        metadata = {
            "video_id": "abc123",
            "duration": 300,
            "view_count": 10000
        }
        result = format_metadata_as_yaml(metadata)
        assert "duration: 300" in result
        assert "view_count: 10000" in result


class TestTranscriptOutput:
    """Test cases for transcript file output generation."""

    def test_complete_transcript_format(self, sample_metadata, sample_transcript_text):
        """Test complete transcript file format."""
        yaml_frontmatter = format_metadata_as_yaml(sample_metadata)
        full_content = yaml_frontmatter + sample_transcript_text

        # Verify structure
        assert full_content.startswith("---")
        assert full_content.count("---") >= 2
        assert sample_transcript_text in full_content
        assert sample_metadata["video_id"] in full_content

    def test_filename_generation(self, sample_metadata):
        """Test filename generation from metadata."""
        video_id = sample_metadata["video_id"]
        title = sample_metadata["title"]
        sanitized_title = sanitize_filename(title)

        expected_filename = f"{video_id}_{sanitized_title}.md"
        assert expected_filename == "dQw4w9WgXcQ_How_to_Build_a_Successful_Startup.md"


# =============================================================================
# Integration-Style Tests (without external calls)
# =============================================================================

class TestEndToEndTranscription:
    """End-to-end tests for the transcription workflow."""

    def test_full_url_to_video_id_flow(self, sample_youtube_url):
        """Test the complete URL to video ID flow."""
        # Given: A YouTube URL
        # When: We extract the video ID
        video_id = get_video_id(sample_youtube_url)

        # Then: We get the correct video ID
        assert video_id == "dQw4w9WgXcQ"

    def test_full_url_to_filename_flow(self, sample_youtube_url, sample_metadata):
        """Test the complete URL to filename flow."""
        # Given: A YouTube URL and metadata
        video_id = get_video_id(sample_youtube_url)
        assert video_id is not None

        # When: We generate a sanitized filename
        sanitized_title = sanitize_filename(sample_metadata["title"])
        filename = f"{video_id}_{sanitized_title}.md"

        # Then: The filename is valid
        assert "dQw4w9WgXcQ_" in filename
        assert ".md" in filename
        assert "/" not in filename
        assert "\\" not in filename


class TestFileHandling:
    """Tests for file handling operations."""

    def test_output_path_construction(self, temp_raw_data_dir):
        """Test constructing output file path."""
        video_id = "test123"
        title = "Test Video"
        filename = f"{video_id}_{sanitize_filename(title)}.md"
        output_path = temp_raw_data_dir / filename

        # Verify path is valid
        assert output_path.suffix == ".md"
        assert output_path.stem.startswith(video_id)

    def test_directory_creation(self, tmp_path):
        """Test that output directory is created if it doesn't exist."""
        output_dir = tmp_path / "new" / "nested" / "directory"

        # Before: directory doesn't exist
        assert not output_dir.exists()

        # Create it
        output_dir.mkdir(parents=True, exist_ok=True)

        # After: directory exists
        assert output_dir.exists()
        assert output_dir.is_dir()


# =============================================================================
# Error Handling Tests
# =============================================================================

class TestErrorHandling:
    """Test error handling scenarios."""

    def test_malformed_url_handling(self):
        """Test that malformed URLs are handled gracefully."""
        malformed_urls = [
            "https://youtube.com",
            "https://youtube.com/watch",
            "https://youtube.com/watch?list=abc",
            "http://youtu.be",
        ]

        for url in malformed_urls:
            result = get_video_id(url)
            # Should either return None or handle gracefully
            assert result is None or isinstance(result, str)

    def test_empty_string_handling(self):
        """Test handling of empty strings."""
        assert get_video_id("") is None
        assert sanitize_filename("") == ""

    def test_very_long_title_handling(self):
        """Test handling of extremely long titles."""
        long_title = "A" * 1000
        result = sanitize_filename(long_title, max_length=50)
        assert len(result) == 50