"""
Pytest configuration and fixtures for Knowledge OS tests.

This module provides shared fixtures and configuration for all tests.
"""

import os
import sys
import pytest
from pathlib import Path
from typing import Any, Dict, List

# Ensure the project root is in the path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
sys.path.insert(0, str(PROJECT_ROOT / "search"))


# ============================================================================
# Path Fixtures
# ============================================================================

@pytest.fixture
def project_root() -> Path:
    """Return the project root directory."""
    return PROJECT_ROOT


@pytest.fixture
def scripts_dir(project_root: Path) -> Path:
    """Return the scripts directory."""
    return project_root / "scripts"


@pytest.fixture
def search_dir(project_root: Path) -> Path:
    """Return the search directory."""
    return project_root / "search"


@pytest.fixture
def test_fixtures_dir(project_root: Path) -> Path:
    """Return the test fixtures directory."""
    return Path(__file__).parent / "fixtures"


# ============================================================================
# Category Fixtures
# ============================================================================

@pytest.fixture
def categories() -> List[str]:
    """Return list of content categories."""
    return [
        "Starter_Story",
        "Inner_Work",
        "AI_Leaders",
        "Founders",
        "My_First_Million",
        "AI_Engineering"
    ]


@pytest.fixture
def content_folders(project_root: Path, categories: List[str]) -> Dict[str, Path]:
    """Return dictionary of content folder paths."""
    return {
        cat: project_root / cat for cat in categories
    }


# ============================================================================
# Mock Data Fixtures
# ============================================================================

@pytest.fixture
def sample_youtube_url() -> str:
    """Return a sample YouTube URL for testing."""
    return "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


@pytest.fixture
def sample_video_id() -> str:
    """Return a sample video ID."""
    return "dQw4w9WgXcQ"


@pytest.fixture
def sample_metadata() -> Dict[str, Any]:
    """Return sample video metadata."""
    return {
        "video_id": "dQw4w9WgXcQ",
        "title": "Test Video Title",
        "channel": "Test Channel",
        "duration": 300,
        "view_count": 10000,
        "upload_date": "20240115",
        "tags": ["test", "sample"],
        "thumbnail": "https://example.com/thumbnail.jpg"
    }


@pytest.fixture
def sample_transcript_text() -> str:
    """Return sample transcript text."""
    return (
        "Hello everyone, welcome to this test video. "
        "Today we're going to discuss something interesting. "
        "First, let me explain the basics. "
        "Then we'll move to advanced topics. "
        "Finally, we'll wrap up with key takeaways."
    )


@pytest.fixture
def sample_markdown_with_frontmatter(sample_metadata: Dict, sample_transcript_text: str) -> str:
    """Return sample markdown with YAML frontmatter."""
    tags_str = ', '.join([f'"{tag}"' for tag in sample_metadata["tags"]])
    return f"""---
video_id: {sample_metadata['video_id']}
title: "{sample_metadata['title']}"
channel: "{sample_metadata['channel']}"
duration: {sample_metadata['duration']}
view_count: {sample_metadata['view_count']}
upload_date: {sample_metadata['upload_date']}
tags: [{tags_str}]
thumbnail: {sample_metadata['thumbnail']}
---

{sample_transcript_text}
"""


@pytest.fixture
def sample_profile_content() -> str:
    """Return sample processed profile content."""
    return """# Executive Summary

This is a test profile summary.

## Product

Test product description.

## Tech Stack

- Python
- FastAPI
- PostgreSQL

## Distribution

Test distribution strategy.

## Key Frameworks

Framework 1: Description
Framework 2: Description

## Metrics

- User count: 1000
- Revenue: $10K/month
"""


# ============================================================================
# Temporary Directory Fixtures
# ============================================================================

@pytest.fixture
def temp_output_dir(tmp_path: Path) -> Path:
    """Return a temporary directory for test outputs."""
    output_dir = tmp_path / "output"
    output_dir.mkdir(exist_ok=True)
    return output_dir


@pytest.fixture
def temp_raw_data_dir(tmp_path: Path) -> Path:
    """Return a temporary Raw_Data directory."""
    raw_data = tmp_path / "Raw_Data"
    raw_data.mkdir(exist_ok=True)
    return raw_data


# ============================================================================
# Mock Objects
# ============================================================================

@pytest.fixture
def mock_youtube_response() -> Dict[str, Any]:
    """Return mock YouTube API response."""
    return {
        "id": "dQw4w9WgXcQ",
        "title": "Mock Video Title",
        "channel": "Mock Channel",
        "duration": 600,
        "view_count": 50000,
        "upload_date": "20240101",
        "tags": ["mock", "test"],
        "thumbnail": "https://example.com/mock.jpg"
    }


@pytest.fixture
def mock_transcript_response() -> List[Dict[str, Any]]:
    """Return mock transcript API response."""
    return [
        {"text": "This is the first sentence of the transcript.", "start": 0.0, "duration": 5.0},
        {"text": "This is the second sentence.", "start": 5.0, "duration": 3.0},
        {"text": "And this is the third sentence.", "start": 8.0, "duration": 4.0}
    ]


# ============================================================================
# Configuration
# ============================================================================

def pytest_configure(config: pytest.Config) -> None:
    """
    Configure pytest with custom markers.

    Args:
        config: Pytest Config object.
    """
    config.addinivalue_line(
        "markers", "unit: Unit tests for individual functions"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests for component interactions"
    )
    config.addinivalue_line(
        "markers", "e2e: End-to-end workflow tests"
    )
    config.addinivalue_line(
        "markers", "slow: Tests that take longer to run"
    )


def pytest_collection_modifyitems(
    config: pytest.Config,
    items: list[Any],
) -> None:
    """
    Modify test collection to add markers automatically.

    Args:
        config: Pytest Config object.
        items: List of collected test items.
    """
    for item in items:
        # Add markers based on test file name
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        elif "e2e" in item.nodeid:
            item.add_marker(pytest.mark.e2e)
        elif "test_" in item.nodeid:
            item.add_marker(pytest.mark.unit)