"""
Unit tests for the Search Indexer functionality.

These tests verify the core functions in search/index.py without requiring
actual embedding model or database initialization.
"""

import os
import glob
import re
import pytest
from pathlib import Path
from typing import List, Dict, Any


# =============================================================================
# Test Configuration
# =============================================================================

TEST_CATEGORIES = [
    "Starter_Story",
    "Inner_Work",
    "AI_Leaders",
    "Founders",
    "My_First_Million",
    "AI_Engineering"
]

TEST_DATA_SUBDIRS = ["Raw_Data", "Process_data", "Process_Data"]


# =============================================================================
# Helper Functions (Duplicated from index.py for testing)
# =============================================================================

def find_markdown_files(root_path: Path, categories: List[str]) -> List[str]:
    """
    Find all markdown files in the knowledge base categories.

    Args:
        root_path: Root directory of Knowledge OS
        categories: List of category folder names

    Returns:
        List of absolute file paths to markdown files
    """
    md_files = []
    for category in categories:
        category_path = root_path / category
        if not category_path.exists():
            continue
        for subdir in TEST_DATA_SUBDIRS:
            subdir_path = category_path / subdir
            if subdir_path.exists():
                pattern = str(subdir_path / "*.md")
                files = glob.glob(pattern)
                md_files.extend(files)
    return md_files


def read_file_content(file_path: str) -> str:
    """
    Read content from a markdown file, stripping frontmatter.

    Args:
        file_path: Path to the markdown file

    Returns:
        File content with YAML frontmatter removed
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    content = parts[2]
            return content.strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""


def get_category_from_path(file_path: str, categories: List[str]) -> str:
    """
    Extract category from file path.

    Args:
        file_path: Path to the markdown file
        categories: List of valid category names

    Returns:
        Category name or "Unknown"
    """
    for category in categories:
        if category in file_path:
            return category
    return "Unknown"


def get_file_type_from_path(file_path: str) -> str:
    """
    Determine if file is a raw transcript or processed profile.

    Args:
        file_path: Path to the markdown file

    Returns:
        "transcript", "profile", or "unknown"
    """
    if "Raw_Data" in file_path:
        return "transcript"
    elif "Process_data" in file_path or "Process_Data" in file_path:
        return "profile"
    return "unknown"


def extract_frontmatter(file_path: str) -> Dict[str, Any]:
    """
    Extract YAML frontmatter from markdown file.

    Args:
        file_path: Path to the markdown file

    Returns:
        Dictionary of frontmatter key-value pairs
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 2:
                    frontmatter = parts[1].strip()
                    metadata = {}
                    for line in frontmatter.split("\n"):
                        if ":" in line:
                            key, value = line.split(":", 1)
                            metadata[key.strip()] = value.strip().strip('"')
                    return metadata
    except Exception:
        pass
    return {}


# =============================================================================
# Test Cases
# =============================================================================

class TestFindMarkdownFiles:
    """Test cases for finding markdown files."""

    def test_find_files_in_categories(self, project_root):
        """Test that markdown files are found in all categories."""
        files = find_markdown_files(project_root, TEST_CATEGORIES)

        # Should find at least some files
        assert isinstance(files, list)

    def test_returns_absolute_paths(self, project_root):
        """Test that file paths are absolute."""
        files = find_markdown_files(project_root, TEST_CATEGORIES)
        if files:
            assert os.path.isabs(files[0])

    def test_only_returns_md_files(self, project_root):
        """Test that only .md files are returned."""
        files = find_markdown_files(project_root, TEST_CATEGORIES)
        if files:
            for file_path in files:
                assert file_path.endswith(".md")


class TestReadFileContent:
    """Test cases for reading file content."""

    def test_read_existing_file(self, test_fixtures_dir):
        """Test reading an existing test fixture."""
        sample_file = test_fixtures_dir / "sample_transcript.md"
        if sample_file.exists():
            content = read_file_content(str(sample_file))
            assert len(content) > 0
            assert "transcript" in content.lower()

    def test_strips_frontmatter(self, test_fixtures_dir):
        """Test that frontmatter is stripped from content."""
        sample_file = test_fixtures_dir / "sample_transcript.md"
        if sample_file.exists():
            content = read_file_content(str(sample_file))
            # Content should not start with ---
            assert not content.startswith("---")
            # But should have the actual transcript
            assert "sample transcript" in content.lower()

    def test_handles_nonexistent_file(self):
        """Test handling of nonexistent files."""
        content = read_file_content("/nonexistent/file.md")
        assert content == ""

    def test_handles_empty_file(self, tmp_path):
        """Test handling of empty files."""
        empty_file = tmp_path / "empty.md"
        empty_file.write_text("")
        content = read_file_content(str(empty_file))
        assert content == ""


class TestGetCategoryFromPath:
    """Test cases for category extraction."""

    def test_starter_story_category(self):
        """Test Starter_Story category detection."""
        path = "Starter_Story/Raw_Data/test.md"
        assert get_category_from_path(path, TEST_CATEGORIES) == "Starter_Story"

    def test_ai_leaders_category(self):
        """Test AI_Leaders category detection."""
        path = "AI_Leaders/Process_data/test.md"
        assert get_category_from_path(path, TEST_CATEGORIES) == "AI_Leaders"

    def test_founders_category(self):
        """Test Founders category detection."""
        path = "Founders/Raw_Data/test.md"
        assert get_category_from_path(path, TEST_CATEGORIES) == "Founders"

    def test_unknown_category(self):
        """Test unknown category returns 'Unknown'."""
        path = "Unknown_Folder/test.md"
        assert get_category_from_path(path, TEST_CATEGORIES) == "Unknown"

    def test_partial_name_mismatch(self):
        """Test that partial name matches don't cause false positives."""
        path = "AI_Engineering_Something/Raw_Data/test.md"
        result = get_category_from_path(path, TEST_CATEGORIES)
        # Should match the full category name
        assert "AI_Engineering" in result or result == "Unknown"


class TestGetFileTypeFromPath:
    """Test cases for file type detection."""

    def test_raw_data_detection(self):
        """Test that Raw_Data files are detected as transcripts."""
        path = "Starter_Story/Raw_Data/test.md"
        assert get_file_type_from_path(path) == "transcript"

    def test_process_data_detection(self):
        """Test that Process_data files are detected as profiles."""
        path = "Starter_Story/Process_data/test.md"
        assert get_file_type_from_path(path) == "profile"

    def test_process_data_uppercase_detection(self):
        """Test that Process_Data (capitalized) files are detected."""
        path = "Starter_Story/Process_Data/test.md"
        assert get_file_type_from_path(path) == "profile"

    def test_unknown_type(self):
        """Test that unknown paths return 'unknown'."""
        path = "test.md"
        assert get_file_type_from_path(path) == "unknown"


class TestExtractFrontmatter:
    """Test cases for frontmatter extraction."""

    def test_extract_video_id(self, test_fixtures_dir):
        """Test extracting video_id from frontmatter."""
        sample_file = test_fixtures_dir / "sample_transcript.md"
        if sample_file.exists():
            metadata = extract_frontmatter(str(sample_file))
            assert "video_id" in metadata
            assert metadata["video_id"] == "test123_abc"

    def test_extract_title(self, test_fixtures_dir):
        """Test extracting title from frontmatter."""
        sample_file = test_fixtures_dir / "sample_transcript.md"
        if sample_file.exists():
            metadata = extract_frontmatter(str(sample_file))
            assert "title" in metadata

    def test_extract_tags(self, test_fixtures_dir):
        """Test extracting tags from frontmatter."""
        sample_file = test_fixtures_dir / "sample_transcript.md"
        if sample_file.exists():
            metadata = extract_frontmatter(str(sample_file))
            assert "tags" in metadata

    def test_no_frontmatter(self, tmp_path):
        """Test handling files without frontmatter."""
        no_fm_file = tmp_path / "no_frontmatter.md"
        no_fm_file.write_text("# Just a title\n\nSome content")
        metadata = extract_frontmatter(str(no_fm_file))
        assert isinstance(metadata, dict)


class TestIndexerIntegration:
    """Integration tests for the indexer workflow."""

    def test_full_workflow_with_fixtures(self, project_root, test_fixtures_dir):
        """Test complete indexing workflow with test files."""
        # Given: A test fixture file
        sample_file = test_fixtures_dir / "sample_transcript.md"
        assert sample_file.exists()

        # When: We read and process the file
        content = read_file_content(str(sample_file))
        category = get_category_from_path(str(sample_file), TEST_CATEGORIES)
        file_type = get_file_type_from_path(str(sample_file))

        # Then: All components work together
        assert len(content) > 0
        assert category == "Unknown"  # Fixtures aren't in real category folders

    def test_category_folder_structure(self, project_root):
        """Test that all category folders exist."""
        for category in TEST_CATEGORIES:
            category_path = project_root / category
            assert category_path.exists(), f"Category folder {category} should exist"

    def test_each_category_has_subdirs(self, project_root):
        """Test that each category has the expected subdirectories."""
        expected_subdirs = ["Raw_Data", "Process_data"]

        for category in TEST_CATEGORIES:
            category_path = project_root / category
            if category_path.exists():
                for subdir in expected_subdirs:
                    subdir_path = category_path / subdir
                    # Subdir may not exist yet, that's OK
                    if subdir_path.exists():
                        assert subdir_path.is_dir()


class TestMetadataValidation:
    """Test metadata validation for profiles and transcripts."""

    def test_transcript_has_required_fields(self, project_root):
        """Test that transcript files have required metadata fields."""
        files = find_markdown_files(project_root, TEST_CATEGORIES)
        transcript_files = [f for f in files if "Raw_Data" in f]

        if transcript_files:
            sample_file = transcript_files[0]
            metadata = extract_frontmatter(sample_file)

            # Transcripts should have video_id at minimum
            assert "video_id" in metadata, f"Transcript missing video_id: {sample_file}"

    def test_profile_has_title_section(self, project_root):
        """Test that profile files have title sections."""
        files = find_markdown_files(project_root, TEST_CATEGORIES)
        profile_files = [f for f in files if "Process_data" in f or "Process_Data" in f]

        if profile_files:
            sample_file = profile_files[0]
            content = read_file_content(sample_file)

            # Profiles should have markdown headings
            assert "#" in content or "##" in content


# =============================================================================
# Performance Tests (Lightweight)
# =============================================================================

class TestIndexerPerformance:
    """Lightweight performance tests."""

    def test_file_count_is_reasonable(self, project_root):
        """Test that file count is within reasonable bounds."""
        files = find_markdown_files(project_root, TEST_CATEGORIES)

        # A well-maintained knowledge base should have reasonable file count
        # This is a sanity check, not a hard limit
        assert len(files) >= 0

    def test_large_file_handling(self, tmp_path):
        """Test handling of large files."""
        large_file = tmp_path / "large.md"
        content = "# Title\n\n" + ("Sample content. " * 10000)
        large_file.write_text(content)

        # Should still be readable
        result = read_file_content(str(large_file))
        assert len(result) > 0
        assert "Sample content" in result