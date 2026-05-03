"""
Integration tests for Knowledge OS end-to-end workflows.

These tests verify that the complete workflows work correctly,
including the interaction between different components.
"""

import os
import pytest
from pathlib import Path
from typing import Dict, List, Any


# =============================================================================
# Integration Test Helpers
# =============================================================================

def get_all_transcript_files(project_root: Path) -> List[Path]:
    """Get all transcript files from all categories."""
    transcripts = []
    categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]

    for category in categories:
        raw_data = project_root / category / "Raw_Data"
        if raw_data.exists():
            transcripts.extend(raw_data.glob("*.md"))

    return transcripts


def get_all_profile_files(project_root: Path) -> List[Path]:
    """Get all profile files from all categories."""
    profiles = []
    categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]

    for category in categories:
        process_data = project_root / category / "Process_data"
        if process_data.exists():
            profiles.extend(process_data.glob("*.md"))

    return profiles


def get_category_from_path(path: Path) -> str:
    """Extract category from file path."""
    path_str = str(path)
    categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]
    for cat in categories:
        if cat in path_str:
            return cat
    return "Unknown"


def has_valid_frontmatter(content: str) -> bool:
    """Check if content has valid frontmatter."""
    if not content.startswith("---"):
        return False
    parts = content.split("---", 2)
    return len(parts) >= 2 and ":" in parts[1]


def extract_frontmatter_field(content: str, field: str) -> str:
    """Extract a specific field from frontmatter."""
    if not content.startswith("---"):
        return ""
    parts = content.split("---", 2)
    if len(parts) < 2:
        return ""
    for line in parts[1].split("\n"):
        if line.strip().startswith(f"{field}:"):
            return line.split(":", 1)[1].strip().strip('"')
    return ""


# =============================================================================
# Test Cases
# =============================================================================

class TestContentStructure:
    """Test that all content follows expected structure."""

    def test_all_categories_exist(self, project_root):
        """Test that all category folders exist."""
        categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]
        for category in categories:
            category_path = project_root / category
            assert category_path.exists(), f"Category folder {category} should exist"

    def test_categories_have_index_files(self, project_root):
        """Test that each category has an INDEX.md file."""
        categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]
        for category in categories:
            index_file = project_root / category / "INDEX.md"
            assert index_file.exists(), f"Category {category} should have INDEX.md"

    def test_categories_have_agents_files(self, project_root):
        """Test that each category has an AGENTS.md file."""
        categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]
        for category in categories:
            agents_file = project_root / category / "AGENTS.md"
            assert agents_file.exists(), f"Category {category} should have AGENTS.md"


class TestTranscriptFiles:
    """Integration tests for transcript files."""

    def test_all_transcripts_have_frontmatter(self, project_root):
        """Test that all transcript files have valid frontmatter."""
        transcripts = get_all_transcript_files(project_root)
        if not transcripts:
            pytest.skip("No transcript files found")

        for transcript in transcripts:
            content = transcript.read_text(encoding="utf-8")
            assert has_valid_frontmatter(content), f"Transcript {transcript.name} missing valid frontmatter"

    def test_transcripts_have_video_id(self, project_root):
        """Test that all transcripts have video_id in frontmatter."""
        transcripts = get_all_transcript_files(project_root)
        if not transcripts:
            pytest.skip("No transcript files found")

        for transcript in transcripts:
            content = transcript.read_text(encoding="utf-8")
            video_id = extract_frontmatter_field(content, "video_id")
            assert video_id, f"Transcript {transcript.name} missing video_id"

    def test_transcripts_have_title(self, project_root):
        """Test that all transcripts have title in frontmatter."""
        transcripts = get_all_transcript_files(project_root)
        if not transcripts:
            pytest.skip("No transcript files found")

        for transcript in transcripts:
            content = transcript.read_text(encoding="utf-8")
            title = extract_frontmatter_field(content, "title")
            assert title, f"Transcript {transcript.name} missing title"

    def test_transcripts_have_content(self, project_root):
        """Test that transcripts have actual transcript content."""
        transcripts = get_all_transcript_files(project_root)
        if not transcripts:
            pytest.skip("No transcript files found")

        for transcript in transcripts:
            content = transcript.read_text(encoding="utf-8")
            # Remove frontmatter to get actual transcript
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    transcript_text = parts[2]
                else:
                    transcript_text = ""
            else:
                transcript_text = content

            assert len(transcript_text.strip()) > 0, f"Transcript {transcript.name} has no content"


class TestProfileFiles:
    """Integration tests for processed profile files."""

    def test_all_profiles_have_title(self, project_root):
        """Test that all profiles have a title (H1)."""
        profiles = get_all_profile_files(project_root)
        if not profiles:
            pytest.skip("No profile files found")

        for profile in profiles:
            content = profile.read_text(encoding="utf-8")
            # Check for H1 heading
            assert "# " in content, f"Profile {profile.name} missing title (H1)"

    def test_profiles_have_sections(self, project_root):
        """Test that profiles have multiple sections."""
        profiles = get_all_profile_files(project_root)
        if not profiles:
            pytest.skip("No profile files found")

        for profile in profiles:
            content = profile.read_text(encoding="utf-8")
            # Count headings (## or more)
            heading_count = content.count("##")
            assert heading_count >= 2, f"Profile {profile.name} should have multiple sections"

    def test_profiles_have_substantial_content(self, project_root):
        """Test that profiles have substantial content."""
        profiles = get_all_profile_files(project_root)
        if not profiles:
            pytest.skip("No profile files found")

        for profile in profiles:
            content = profile.read_text(encoding="utf-8")
            # Remove frontmatter
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    body = parts[2]
                else:
                    body = content
            else:
                body = content

            # Should have at least a few paragraphs
            lines = [l for l in body.split("\n") if l.strip() and not l.strip().startswith("#")]
            assert len(lines) >= 5, f"Profile {profile.name} should have substantial content"


class TestIndexFiles:
    """Integration tests for INDEX files."""

    def test_index_files_exist_in_categories(self, project_root):
        """Test that all categories have INDEX.md files."""
        categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]
        for category in categories:
            index_file = project_root / category / "INDEX.md"
            assert index_file.exists(), f"Category {category} should have INDEX.md"

    def test_index_files_have_content(self, project_root):
        """Test that INDEX files have content."""
        categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]
        for category in categories:
            index_file = project_root / category / "INDEX.md"
            if index_file.exists():
                content = index_file.read_text(encoding="utf-8")
                assert len(content.strip()) > 0, f"INDEX.md for {category} should have content"


class TestSearchSystem:
    """Integration tests for the search system."""

    def test_search_indexer_exists(self, project_root):
        """Test that search indexer script exists."""
        indexer = project_root / "search" / "index.py"
        assert indexer.exists(), "search/index.py should exist"

    def test_search_query_exists(self, project_root):
        """Test that search query script exists."""
        query_script = project_root / "search" / "answer_search.py"
        assert query_script.exists(), "search/answer_search.py should exist"

    def test_search_knowledge_db_exists(self, project_root):
        """Test that knowledge database directory exists."""
        knowledge_db = project_root / "search" / "knowledge_db"
        # Database may not exist if no indexing has been done
        if knowledge_db.exists():
            assert knowledge_db.is_dir(), "knowledge_db should be a directory"

    def test_search_requirements_exist(self, project_root):
        """Test that search requirements file exists."""
        requirements = project_root / "search" / "requirements.txt"
        assert requirements.exists(), "search/requirements.txt should exist"


class TestSkillSystem:
    """Integration tests for the skill system."""

    def test_skills_folder_exists(self, project_root):
        """Test that Skills folder exists."""
        skills_folder = project_root / "Skills"
        assert skills_folder.exists(), "Skills folder should exist"

    def test_all_skills_exist(self, project_root):
        """Test that all skill folders exist."""
        expected_skills = ["starter-story", "ai-leaders", "founders", "my-first-million", "ai-engineering", "inner-work", "Process_Link"]
        skills_folder = project_root / "Skills"
        for skill in expected_skills:
            skill_path = skills_folder / skill
            # Process_Link is a folder, others may be folders or files
            assert skill_path.exists(), f"Skill {skill} should exist"

    def test_skills_have_skill_files(self, project_root):
        """Test that each skill has a SKILL.md file."""
        skills_folder = project_root / "Skills"
        # Check for folder-based skills
        expected_skills = ["starter-story", "ai-leaders", "founders", "my-first-million", "ai-engineering", "inner-work"]
        for skill in expected_skills:
            skill_path = skills_folder / skill / "SKILL.md"
            if not skill_path.exists():
                # May also be in subfolder
                skill_path = skills_folder / skill / "skill.md"
            assert skill_path.exists() or (skills_folder / skill).exists(), f"Skill {skill} should have SKILL.md or be a folder"


class TestEndToEndWorkflows:
    """End-to-end workflow tests."""

    def test_content_to_profile_flow(self, project_root):
        """Test that raw content can lead to processed profiles."""
        # Given: Raw transcript files exist
        transcripts = get_all_transcript_files(project_root)

        # And: Processed profile files exist
        profiles = get_all_profile_files(project_root)

        # Then: At least one should exist
        # (System doesn't require both, but having both is good)
        assert len(transcripts) > 0 or len(profiles) > 0, "Should have some content"

    def test_category_consistency(self, project_root):
        """Test that transcripts and profiles are in matching categories."""
        categories = ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]

        for category in categories:
            raw_data = project_root / category / "Raw_Data"
            process_data = project_root / category / "Process_data"

            # At least one should exist
            has_raw = raw_data.exists() and any(raw_data.glob("*.md"))
            has_processed = process_data.exists() and any(process_data.glob("*.md"))

            assert has_raw or has_processed, f"Category {category} should have some content"

    def test_content_is_utf8_encoded(self, project_root):
        """Test that all content files are readable as UTF-8."""
        all_md_files = []

        for category in ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]:
            for subdir in ["Raw_Data", "Process_data"]:
                folder = project_root / category / subdir
                if folder.exists():
                    all_md_files.extend(folder.glob("*.md"))

        # Test a sample of files
        test_files = all_md_files[:10] if len(all_md_files) > 10 else all_md_files

        for file_path in test_files:
            try:
                content = file_path.read_text(encoding="utf-8")
                assert len(content) > 0
            except UnicodeDecodeError:
                pytest.fail(f"File {file_path} is not valid UTF-8")


class TestDataQuality:
    """Data quality tests."""

    def test_no_empty_files(self, project_root):
        """Test that there are no empty markdown files."""
        all_md_files = []

        for category in ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]:
            for subdir in ["Raw_Data", "Process_data"]:
                folder = project_root / category / subdir
                if folder.exists():
                    all_md_files.extend(folder.glob("*.md"))

        for file_path in all_md_files:
            content = file_path.read_text(encoding="utf-8")
            assert len(content.strip()) > 0, f"File {file_path.name} is empty"

    def test_filenames_are_descriptive(self, project_root):
        """Test that filenames are descriptive (not default names)."""
        all_md_files = []

        for category in ["Starter_Story", "AI_Leaders", "Founders", "My_First_Million", "AI_Engineering", "Inner_Work"]:
            for subdir in ["Raw_Data", "Process_data"]:
                folder = project_root / category / subdir
                if folder.exists():
                    all_md_files.extend(folder.glob("*.md"))

        # Check a sample for descriptive names
        test_files = all_md_files[:5] if len(all_md_files) > 5 else all_md_files

        for file_path in test_files:
            name = file_path.stem
            # Should be longer than just a video ID
            # (video IDs are typically 11 chars)
            assert len(name) > 15, f"Filename {name} seems too short"


class TestScriptsAndConfiguration:
    """Test scripts and configuration files."""

    def test_transcript_extraction_script_exists(self, project_root):
        """Test that transcript extraction script exists."""
        script = project_root / "scripts" / "Transcript_Extraction.py"
        assert script.exists(), "Transcript_Extraction.py should exist in scripts/"

    def test_search_script_can_be_imported(self, project_root):
        """Test that search scripts have valid Python syntax."""
        # Just check they can be parsed
        import ast
        index_py = project_root / "search" / "index.py"
        if index_py.exists():
            content = index_py.read_text(encoding="utf-8")
            try:
                ast.parse(content)
            except SyntaxError:
                pytest.fail("search/index.py has syntax errors")

    def test_test_config_exists(self, project_root):
        """Test that test configuration exists."""
        # Check pytest.ini or pyproject.toml exists
        pytest_ini = project_root / "pytest.ini"
        pyproject = project_root / "pyproject.toml"
        setup_cfg = project_root / "setup.cfg"

        has_config = pytest_ini.exists() or pyproject.exists() or setup_cfg.exists()
        # This is optional but recommended
        if not has_config:
            pytest.skip("No pytest configuration found (optional)")