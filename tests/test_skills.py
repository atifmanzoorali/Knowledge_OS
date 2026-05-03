"""
Unit tests for Skill output validation.

These tests verify that each skill produces the expected output format
 according to its defined template.
"""

import re
import pytest
from pathlib import Path
from typing import Dict, List, Any, Optional


# =============================================================================
# Skill Templates (Expected Output Formats)
# =============================================================================

SKILL_TEMPLATES = {
    "starter-story": {
        "required_sections": [
            "Executive Summary",
            "Product",
            "Tech Stack",
            "Distribution"
        ],
        "optional_sections": [
            "Key Frameworks",
            "Metrics"
        ],
        "description": "Startup founder interview profile"
    },
    "ai-leaders": {
        "required_sections": [
            "AI Thesis",
            "Mental Models"
        ],
        "optional_sections": [
            "Contrarian Views",
            "What They're Building"
        ],
        "description": "AI industry leader intelligence profile"
    },
    "founders": {
        "required_sections": [
            "Books",
            "Key Lessons"
        ],
        "optional_sections": [
            "Notable Quotes",
            "Journey"
        ],
        "description": "Business founder profile (Books mandatory)"
    },
    "my-first-million": {
        "required_sections": [
            "Key Insights"
        ],
        "optional_sections": [
            "Lessons",
            "Resources"
        ],
        "description": "Business podcast insight profile"
    },
    "ai-engineering": {
        "required_sections": [
            "Core Framework",
            "Step-by-Step Implementation"
        ],
        "optional_sections": [
            "Tools",
            "Books"
        ],
        "description": "AI development technical profile"
    },
    "inner-work": {
        "required_sections": [
            "Core Wisdom",
            "Key Principles"
        ],
        "optional_sections": [
            "Practical Application",
            "Quotes"
        ],
        "description": "Personal growth wisdom profile"
    }
}


# =============================================================================
# Helper Functions
# =============================================================================

def extract_headings(content: str) -> List[str]:
    """
    Extract all headings from markdown content.

    Args:
        content: Markdown content string

    Returns:
        List of heading texts (without # symbols)
    """
    headings = []
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('#'):
            # Remove # symbols and whitespace
            heading = line.lstrip('#').strip()
            headings.append(heading)
    return headings


def check_section_exists(content: str, section_name: str) -> bool:
    """
    Check if a section exists in the content.

    Args:
        content: Markdown content
        section_name: Name of section to check

    Returns:
        True if section exists
    """
    headings = extract_headings(content)
    return any(section_name.lower() in heading.lower() for heading in headings)


def extract_section_content(content: str, section_name: str) -> Optional[str]:
    """
    Extract content under a specific section.

    Args:
        content: Full markdown content
        section_name: Name of section to extract

    Returns:
        Content under the section, or None if not found
    """
    lines = content.split('\n')
    in_section = False
    section_content = []

    # Normalize section name for matching
    search_name = section_name.lower()

    for line in lines:
        # Check if we're entering the target section
        if line.strip().lower().startswith('#') and search_name in line.strip().lower():
            in_section = True
            continue

        # If we're in the section and hit another heading, stop
        if in_section and line.strip().startswith('#'):
            break

        # Collect content while in section
        if in_section:
            section_content.append(line)

    return '\n'.join(section_content).strip() if section_content else None


def validate_skill_output(content: str, skill_name: str) -> Dict[str, Any]:
    """
    Validate that skill output matches expected format.

    Args:
        content: Processed profile content
        skill_name: Name of the skill

    Returns:
        Dictionary with validation results
    """
    template = SKILL_TEMPLATES.get(skill_name)
    if not template:
        return {
            "valid": False,
            "errors": [f"Unknown skill: {skill_name}"]
        }

    errors = []
    warnings = []

    # Check required sections
    for section in template["required_sections"]:
        if not check_section_exists(content, section):
            errors.append(f"Missing required section: {section}")

    # Check optional sections
    for section in template["optional_sections"]:
        if not check_section_exists(content, section):
            warnings.append(f"Missing optional section: {section}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "required_sections_found": [s for s in template["required_sections"] if check_section_exists(content, s)],
        "optional_sections_found": [s for s in template["optional_sections"] if check_section_exists(content, s)]
    }


def check_frontmatter(content: str) -> bool:
    """
    Check if content has YAML frontmatter.

    Args:
        content: Markdown content

    Returns:
        True if frontmatter exists
    """
    return content.startswith("---")


def extract_frontmatter_keys(content: str) -> Dict[str, str]:
    """
    Extract keys from YAML frontmatter.

    Args:
        content: Markdown content

    Returns:
        Dictionary of frontmatter key-value pairs
    """
    if not check_frontmatter(content):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 2:
        return {}

    frontmatter = parts[1].strip()
    keys = {}

    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            keys[key.strip()] = value.strip().strip('"')

    return keys


def validate_profile_structure(content: str) -> Dict[str, Any]:
    """
    Validate general profile structure.

    Args:
        content: Profile content

    Returns:
        Validation results
    """
    results = {
        "has_title": False,
        "has_headings": False,
        "has_content": False,
        "heading_count": 0,
        "content_length": 0
    }

    # Check for title (first H1)
    lines = content.split('\n')
    for line in lines[:5]:  # Check first few lines
        if line.strip().startswith('# '):
            results["has_title"] = True
            break

    # Count headings
    headings = extract_headings(content)
    results["heading_count"] = len(headings)
    results["has_headings"] = len(headings) > 0

    # Check for content (non-heading lines with text)
    content_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
    results["has_content"] = len(content_lines) > 0
    results["content_length"] = len(''.join(content_lines))

    return results


# =============================================================================
# Test Cases
# =============================================================================

class TestExtractHeadings:
    """Test cases for heading extraction."""

    def test_single_h1(self):
        """Test extracting single H1."""
        content = "# Title\n\nSome content"
        headings = extract_headings(content)
        assert "Title" in headings

    def test_multiple_headings(self):
        """Test extracting multiple headings."""
        content = "# Title\n## Section 1\n### Subsection\n## Section 2"
        headings = extract_headings(content)
        assert len(headings) == 4

    def test_no_headings(self):
        """Test content with no headings."""
        content = "Just some text without headings"
        headings = extract_headings(content)
        assert len(headings) == 0


class TestCheckSectionExists:
    """Test cases for section existence checking."""

    def test_existing_section(self):
        """Test checking existing section."""
        content = "# Title\n## Executive Summary\nContent here"
        assert check_section_exists(content, "Executive Summary") is True

    def test_nonexistent_section(self):
        """Test checking nonexistent section."""
        content = "# Title\n## Some Section"
        assert check_section_exists(content, "Missing Section") is False

    def test_case_insensitive(self):
        """Test case insensitive matching."""
        content = "# Title\n## Executive Summary"
        assert check_section_exists(content, "EXECUTIVE SUMMARY") is True


class TestExtractSectionContent:
    """Test cases for section content extraction."""

    def test_extract_simple_section(self):
        """Test extracting a simple section."""
        content = """# Title

## Executive Summary

This is the executive summary content.

## Product

This is the product section.
"""
        result = extract_section_content(content, "Executive Summary")
        assert result is not None
        assert "executive summary content" in result.lower()

    def test_extract_nonexistent_section(self):
        """Test extracting nonexistent section."""
        content = "# Title\n## Section One"
        result = extract_section_content(content, "Missing Section")
        assert result is None


class TestValidateSkillOutput:
    """Test cases for skill output validation."""

    def test_valid_starter_story(self):
        """Test valid Starter Story profile."""
        content = """# Profile Title

## Executive Summary

Summary content here.

## Product

Product description.

## Tech Stack

- Python
- React

## Distribution

Distribution strategy.
"""
        result = validate_skill_output(content, "starter-story")
        assert result["valid"] is True
        assert len(result["errors"]) == 0

    def test_missing_required_section(self):
        """Test profile with missing required section."""
        content = """# Profile Title

## Executive Summary

Summary content.

## Product

Product description.
"""
        result = validate_skill_output(content, "starter-story")
        assert result["valid"] is False
        assert "Tech Stack" in str(result["errors"])

    def test_founders_requires_books(self):
        """Test that Founders requires Books section."""
        content = """# Profile Title

## Key Lessons

Some lessons here.
"""
        result = validate_skill_output(content, "founders")
        assert result["valid"] is False
        assert any("Books" in err for err in result["errors"])

    def test_valid_ai_leaders(self):
        """Test valid AI Leaders profile."""
        content = """# AI Leader Profile

## AI Thesis

Thesis content.

## Mental Models

Model content.
"""
        result = validate_skill_output(content, "ai-leaders")
        assert result["valid"] is True


class TestFrontmatterValidation:
    """Test cases for frontmatter validation."""

    def test_has_frontmatter(self):
        """Test content with frontmatter."""
        content = """---
video_id: abc123
title: "Test"
---

# Content
"""
        assert check_frontmatter(content) is True

    def test_no_frontmatter(self):
        """Test content without frontmatter."""
        content = "# Title\n\nContent"
        assert check_frontmatter(content) is False

    def test_extract_frontmatter_keys(self):
        """Test extracting frontmatter keys."""
        content = """---
video_id: test123
title: "Test Video"
channel: "Test Channel"
---

# Content
"""
        keys = extract_frontmatter_keys(content)
        assert "video_id" in keys
        assert keys["video_id"] == "test123"


class TestValidateProfileStructure:
    """Test cases for general profile structure validation."""

    def test_complete_structure(self):
        """Test profile with complete structure."""
        content = """# Complete Profile

## Section 1

Content for section 1.

## Section 2

Content for section 2.
"""
        result = validate_profile_structure(content)
        assert result["has_title"] is True
        assert result["has_headings"] is True
        assert result["has_content"] is True

    def test_minimal_structure(self):
        """Test profile with minimal structure."""
        content = "# Title Only"
        result = validate_profile_structure(content)
        assert result["has_title"] is True
        assert result["heading_count"] >= 1


class TestSkillTemplates:
    """Test cases for skill template definitions."""

    def test_all_skills_have_templates(self):
        """Test that all skills have defined templates."""
        skills = ["starter-story", "ai-leaders", "founders", "my-first-million", "ai-engineering", "inner-work"]
        for skill in skills:
            assert skill in SKILL_TEMPLATES

    def test_templates_have_required_fields(self):
        """Test that all templates have required fields."""
        for skill, template in SKILL_TEMPLATES.items():
            assert "required_sections" in template
            assert "optional_sections" in template
            assert isinstance(template["required_sections"], list)
            assert isinstance(template["optional_sections"], list)


class TestRealSkillOutputs:
    """Test real skill outputs from the knowledge base."""

    def test_starter_story_profiles(self, project_root):
        """Test Starter_Story profiles have correct structure."""
        process_data = project_root / "Starter_Story" / "Process_data"

        if process_data.exists() and any(process_data.glob("*.md")):
            for profile_file in list(process_data.glob("*.md"))[:3]:  # Test first 3
                content = profile_file.read_text(encoding="utf-8")
                result = validate_skill_output(content, "starter-story")

                # Should have required sections
                assert "Executive Summary" in result.get("required_sections_found", []), f"Profile {profile_file.name} missing Executive Summary"

    def test_ai_leaders_profiles(self, project_root):
        """Test AI_Leaders profiles have correct structure."""
        process_data = project_root / "AI_Leaders" / "Process_data"

        if process_data.exists() and any(process_data.glob("*.md")):
            for profile_file in list(process_data.glob("*.md"))[:3]:
                content = profile_file.read_text(encoding="utf-8")
                result = validate_skill_output(content, "ai-leaders")

                assert "AI Thesis" in result.get("required_sections_found", []), f"Profile {profile_file.name} missing AI Thesis"

    def test_founders_profiles(self, project_root):
        """Test Founders profiles have Books section."""
        process_data = project_root / "Founders" / "Process_data"

        if process_data.exists() and any(process_data.glob("*.md")):
            for profile_file in list(process_data.glob("*.md"))[:3]:
                content = profile_file.read_text(encoding="utf-8")
                result = validate_skill_output(content, "founders")

                # Founders MUST have Books section
                assert "Books" in result.get("required_sections_found", []), f"Profile {profile_file.name} missing Books section"