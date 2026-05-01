# Skills

## Process_Link

A skill to extract YouTube transcripts and save them to the appropriate category folder in Knowledge_OS.

**Trigger phrases:** "Process_Link", "process link", "extract transcript", "get transcript from youtube"

**Folder structure:**
- Process_Link/
  - SKILL.md
  - references/
    - folder_structure.md

### Features

- Takes YouTube URL as input
- Asks user to select from 6 category folders
- Checks for duplicates before processing
- Runs Transcript_Extraction.py script
- Saves .md file with YAML frontmatter + transcript
- **Skill chaining:** Automatically triggers analysis skill for the selected folder

---

## starter-story

A skill to transform raw founder interview transcripts into structured startup profiles.

**Trigger phrases:** "analyze this starter story", "turn this transcript into a startup profile", "deconstruct this founder story", "process starter story"

**Workflow:** Receives input from Process_Link, analyzes transcript using 6-section template, saves to Knowledge_OS/Starter_Story/

**Folder structure:**
- starter-story/
  - SKILL.md

### Features

- Input: .md file from Process_Link (with transcript)
- Output: Structured startup profile with Executive Summary, Product, Tech Stack, Distribution, Frameworks, Metrics
- Updates INDEX.md after saving