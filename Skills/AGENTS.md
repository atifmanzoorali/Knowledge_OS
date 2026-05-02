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
- **Auto-push to GitHub:** Raw transcript pushed automatically (or passed to next skill)

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
- **Auto-push to GitHub:** Processed profile + INDEX pushed automatically

---

## ai-leaders

A skill to transform raw AI leader interview transcripts into deep-dive intelligence profiles.

**Trigger phrases:** "AI Leaders", "analyze this AI leader", "add [Person] interview", "process AI leaders"

**Workflow:** Receives input from Process_Link, analyzes transcript using template, saves to Knowledge_OS/AI_Leaders/Process_data/

**Folder structure:**
- ai-leaders/
  - SKILL.md

### Features

- Input: .md file from Process_Link (with transcript)
- Output: Intelligence profile with AI Thesis, Mental Models, Quotes, Contrarian Views, What They're Building, Blind Spots, Naval-Style Maxim
- Updates INDEX.md after saving
- Rebuilds search index
- **Auto-push to GitHub:** Processed profile + INDEX pushed automatically

---

## my-first-million

A skill to transform raw My First Million podcast transcripts into structured business insight profiles.

**Trigger phrases:** "process my first million", "analyze this My First Million episode", "add My First Million transcript", "My First Million interview", "process MFM episode"

**Workflow:** Receives input from Process_Link, analyzes transcript using unified template (adapts for brainstorm/interview/breakdown), saves to Knowledge_OS/My_First_Million/Process_data/

**Folder structure:**
- my-first-million/
  - SKILL.md

### Features

- Input: .md file from Process_Link (with transcript)
- Output: Business insight profile with Executive Summary, Key Insights, Lessons, Quotes, Resources (includes books)
- Unified template adapts based on episode type (brainstorm/interview/breakdown)
- Updates INDEX.md after saving
- Rebuilds search index
- **Auto-push to GitHub:** Processed profile + INDEX pushed automatically

---

## founders

A skill to transform raw David Senra's Founders Podcast transcripts into structured founder profile documents.

**Trigger phrases:** "process founders", "analyze this founder", "add [Person] founder", "Founders podcast"

**Workflow:** Receives input from Process_Link, detects episode type (interview vs analysis), analyzes transcript using appropriate template, saves to Knowledge_OS/Founders/Process_data/

**Folder structure:**
- founders/
  - SKILL.md

### Features

- **Two episode types:** Interview (@DavidSenra) and Analysis (@founderspodcast1)
- Input: .md file from Process_Link (with transcript)
- Output: Founder profile with Books section (MANDATORY)
- Template adapts based on episode type
- Updates INDEX.md after saving
- Rebuilds search index
- **Auto-push to GitHub:** Processed profile + INDEX pushed automatically