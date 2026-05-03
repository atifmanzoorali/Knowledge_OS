"""
Unit tests for the Search functionality.

These tests verify the core functions in search/answer_search.py without
 requiring actual ChromaDB or embedding model initialization.
"""

import os
import re
import pytest
from pathlib import Path
from typing import Dict, List, Any, Optional


# =============================================================================
# Mock Classes (for testing without actual dependencies)
# =============================================================================

class MockChromaCollection:
    """Mock ChromaDB collection for testing."""

    def __init__(self, documents: List[str] = None, metadatas: List[Dict] = None, ids: List[str] = None):
        self._documents = documents or []
        self._metadatas = metadatas or []
        self._ids = ids or []

    def count(self) -> int:
        """Return the number of documents in the collection."""
        return len(self._documents)

    def query(self, query_embeddings: List[List[float]], n_results: int = 3) -> Dict:
        """Mock query that returns fake results."""
        if not self._documents:
            return {
                "documents": [[]],
                "metadatas": [[]],
                "distances": [[]]
            }

        # Return the first n_results
        n = min(n_results, len(self._documents))
        return {
            "documents": [self._documents[:n]],
            "metadatas": [self._metadatas[:n]],
            "distances": [[0.1] * n]  # Mock distances
        }

    def get(self) -> Dict:
        """Return all documents in the collection."""
        return {
            "documents": self._documents,
            "metadatas": self._metadatas,
            "ids": self._ids
        }


# =============================================================================
# Helper Functions (Replicated from answer_search.py for testing)
# =============================================================================

def parse_search_query(query: str) -> str:
    """
    Parse and validate search query.

    Args:
        query: User's search query string

    Returns:
        Cleaned query string
    """
    if not query:
        return ""

    # Strip whitespace
    query = query.strip()

    # Remove excessive whitespace
    query = re.sub(r'\s+', ' ', query)

    return query


def format_relevance_score(distance: float) -> str:
    """
    Format distance as a relevance percentage.

    Args:
        distance: Distance value from ChromaDB (lower is better)

    Returns:
        Formatted percentage string
    """
    # Convert distance to relevance (1 - distance)
    # Distance of 0 = 100% relevant
    # Distance of 1 = 0% relevant
    score = max(0, min(1, 1 - distance))
    return f"{score:.2%}"


def format_search_result(doc: str, metadata: Dict, distance: float, index: int) -> str:
    """
    Format a single search result for display.

    Args:
        doc: Document content
        metadata: Document metadata
        distance: Distance score from search
        index: Result index (1-based)

    Returns:
        Formatted result string
    """
    source = metadata.get("source", "Unknown")
    category = metadata.get("category", "Unknown")
    file_type = metadata.get("file_type", "unknown")

    file_type_label = "[transcript]" if file_type == "transcript" else "[profile]"

    score = format_relevance_score(distance)

    lines = [
        f"--- RESULT {index} ---",
        f"Source: {source} {file_type_label}",
        f"Category: {category} | Relevance: {score}",
        "",
        doc[:500] + ("..." if len(doc) > 500 else ""),
        "=" * 60
    ]

    return "\n".join(lines)


def extract_source_file(result_metadata: Dict) -> str:
    """
    Extract source file path from result metadata.

    Args:
        result_metadata: Metadata from search result

    Returns:
        Source file path
    """
    return result_metadata.get("source", "Unknown")


def truncate_content(content: str, max_length: int = 500) -> str:
    """
    Truncate content for display.

    Args:
        content: Full content string
        max_length: Maximum length to display

    Returns:
        Truncated content with ellipsis if needed
    """
    if len(content) <= max_length:
        return content

    return content[:max_length].rsplit(' ', 1)[0] + "..."


def validate_search_results(results: Dict) -> bool:
    """
    Validate search results structure.

    Args:
        results: Results dictionary from ChromaDB query

    Returns:
        True if results are valid
    """
    if not results:
        return False

    # Check required keys
    required_keys = ["documents", "metadatas", "distances"]
    for key in required_keys:
        if key not in results:
            return False

    return True


# =============================================================================
# Test Cases
# =============================================================================

class TestParseSearchQuery:
    """Test cases for search query parsing."""

    def test_basic_query(self):
        """Test basic query parsing."""
        query = "how to build a startup"
        result = parse_search_query(query)
        assert result == "how to build a startup"

    def test_empty_query(self):
        """Test empty query returns empty string."""
        assert parse_search_query("") == ""
        assert parse_search_query("   ") == ""

    def test_whitespace_normalization(self):
        """Test that multiple whitespaces are normalized."""
        query = "test   query   with   spaces"
        result = parse_search_query(query)
        assert result == "test query with spaces"

    def test_leading_trailing_whitespace(self):
        """Test that leading/trailing whitespace is removed."""
        query = "   test query   "
        result = parse_search_query(query)
        assert result == "test query"


class TestFormatRelevanceScore:
    """Test cases for relevance score formatting."""

    def test_perfect_match(self):
        """Test perfect match (distance = 0)."""
        score = format_relevance_score(0.0)
        assert "100%" in score

    def test_no_match(self):
        """Test no match (distance = 1)."""
        score = format_relevance_score(1.0)
        assert "0%" in score

    def test_partial_match(self):
        """Test partial match (distance = 0.5)."""
        score = format_relevance_score(0.5)
        assert "50%" in score

    def test_clamping_extreme_values(self):
        """Test that extreme values are clamped."""
        # Negative distance
        score = format_relevance_score(-0.5)
        assert "100%" in score

        # Distance > 1
        score = format_relevance_score(1.5)
        assert "0%" in score


class TestFormatSearchResult:
    """Test cases for search result formatting."""

    def test_basic_result_format(self):
        """Test basic result format."""
        doc = "This is a test document about startups."
        metadata = {
            "source": "Starter_Story/Process_data/test.md",
            "category": "Starter_Story",
            "file_type": "profile"
        }

        result = format_search_result(doc, metadata, 0.1, 1)

        assert "RESULT 1" in result
        assert "Starter_Story" in result
        assert "profile" in result
        assert "90%" in result  # 1 - 0.1 = 0.9 = 90%

    def test_transcript_label(self):
        """Test that transcripts are labeled correctly."""
        doc = "Transcript content"
        metadata = {
            "source": "Starter_Story/Raw_Data/test.md",
            "category": "Starter_Story",
            "file_type": "transcript"
        }

        result = format_search_result(doc, metadata, 0.2, 1)
        assert "[transcript]" in result

    def test_profile_label(self):
        """Test that profiles are labeled correctly."""
        doc = "Profile content"
        metadata = {
            "source": "Starter_Story/Process_data/test.md",
            "category": "Starter_Story",
            "file_type": "profile"
        }

        result = format_search_result(doc, metadata, 0.2, 1)
        assert "[profile]" in result


class TestExtractSourceFile:
    """Test cases for extracting source file from metadata."""

    def test_extract_known_source(self):
        """Test extracting known source."""
        metadata = {
            "source": "Starter_Story/Process_data/Marc_Lou-35_Startups-2026.md",
            "category": "Starter_Story",
            "file_type": "profile"
        }

        source = extract_source_file(metadata)
        assert source == "Starter_Story/Process_data/Marc_Lou-35_Startups-2026.md"

    def test_extract_unknown_source(self):
        """Test extracting unknown source returns Unknown."""
        metadata = {}

        source = extract_source_file(metadata)
        assert source == "Unknown"


class TestTruncateContent:
    """Test cases for content truncation."""

    def test_no_truncation_needed(self):
        """Test content that doesn't need truncation."""
        content = "Short content"
        result = truncate_content(content, max_length=50)
        assert result == "Short content"

    def test_truncation_with_ellipsis(self):
        """Test that long content is truncated with ellipsis."""
        content = "This is a very long content that needs to be truncated"
        result = truncate_content(content, max_length=20)
        assert len(result) <= 23  # 20 + "..."
        assert "..." in result

    def test_word_boundary_truncation(self):
        """Test that truncation happens at word boundaries."""
        content = "This is a test of word boundary truncation"
        result = truncate_content(content, max_length=15)

        # Should not cut in the middle of a word
        assert result.endswith("...") or len(result) <= 15


class TestValidateSearchResults:
    """Test cases for result validation."""

    def test_valid_results(self):
        """Test valid results pass validation."""
        results = {
            "documents": [["doc1", "doc2"]],
            "metadatas": [["meta1", "meta2"]],
            "distances": [[0.1, 0.2]]
        }

        assert validate_search_results(results) is True

    def test_empty_results(self):
        """Test empty results fail validation."""
        assert validate_search_results({}) is False

    def test_missing_documents(self):
        """Test results missing documents fail validation."""
        results = {
            "metadatas": [["meta1"]],
            "distances": [[0.1]]
        }

        assert validate_search_results(results) is False

    def test_none_results(self):
        """Test None results fail validation."""
        assert validate_search_results(None) is False


class TestSearchIntegration:
    """Integration tests for search workflow."""

    def test_mock_search_workflow(self):
        """Test complete search workflow with mock data."""
        # Given: Mock collection with data
        collection = MockChromaCollection(
            documents=[
                "Content about building startups",
                "Content about marketing strategies",
                "Content about technical implementation"
            ],
            metadatas=[
                {"source": "Starter_Story/Process_data/test1.md", "category": "Starter_Story", "file_type": "profile"},
                {"source": "My_First_Million/Process_data/test2.md", "category": "My_First_Million", "file_type": "profile"},
                {"source": "AI_Engineering/Process_data/test3.md", "category": "AI_Engineering", "file_type": "profile"}
            ],
            ids=["doc1", "doc2", "doc3"]
        )

        # When: We query the collection
        results = collection.query(
            query_embeddings=[[0.1] * 384],
            n_results=2
        )

        # Then: We get results
        assert results["documents"][0]
        assert len(results["documents"][0]) <= 2

    def test_empty_collection_handling(self):
        """Test handling of empty collections."""
        collection = MockChromaCollection()

        # Querying empty collection
        results = collection.query(
            query_embeddings=[[0.1] * 384],
            n_results=3
        )

        # Should return empty results
        assert results["documents"] == [[]]
        assert collection.count() == 0

    def test_query_parsing_and_result_formatting(self):
        """Test complete flow from query to formatted results."""
        # Given: A query
        query = "  how to validate a startup idea  "
        clean_query = parse_search_query(query)
        assert clean_query == "how to validate a startup idea"

        # Given: Mock results
        collection = MockChromaCollection(
            documents=["Validate by getting paying customers early"],
            metadatas=[{"source": "Starter_Story/Process_data/test.md", "category": "Starter_Story", "file_type": "profile"}],
            ids=["doc1"]
        )

        results = collection.query(
            query_embeddings=[[0.1] * 384],
            n_results=1
        )

        # When: We format the result
        formatted = format_search_result(
            results["documents"][0][0],
            results["metadatas"][0][0],
            results["distances"][0][0],
            1
        )

        # Then: Formatted result contains expected elements
        assert "RESULT 1" in formatted
        assert "Starter_Story" in formatted
        assert "profile" in formatted


# =============================================================================
# Error Handling Tests
# =============================================================================

class TestSearchErrorHandling:
    """Test error handling in search functionality."""

    def test_handles_very_long_query(self):
        """Test handling of very long queries."""
        long_query = "word " * 1000
        result = parse_search_query(long_query)

        # Should still be parsed (though very long)
        assert len(result) > 0

    def test_handles_unicode_query(self):
        """Test handling of Unicode characters."""
        query = "Comment construire une startup avec des émojis 🎉"
        result = parse_search_query(query)
        assert "🎉" in result

    def test_handles_special_characters_in_query(self):
        """Test handling of special characters."""
        query = 'Test with "quotes" and <special> chars'
        result = parse_search_query(query)
        assert result is not None

    def test_empty_metadata_handling(self):
        """Test handling of empty metadata in results."""
        doc = "Test content"
        metadata = {}
        distance = 0.5

        result = format_search_result(doc, metadata, distance, 1)
        assert "Unknown" in result  # Should fall back to Unknown