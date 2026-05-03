# Knowledge OS - Structure Guide

This file explains how Knowledge OS is organized. Read this to understand the entire project structure.

---

## Quick Overview

```
Knowledge_OS/
├── docs/              # All documentation
├── Skills/            # All skills (analysis + system)
├── scripts/           # Python scripts
├── search/            # RAG search system
├── tests/             # Test suite
├── logs/              # Error and healing logs
└── [Content Folders]/ # Your knowledge base
```

---

## Detailed Structure

### docs/ - Documentation

Organized into 5 categories:

| Folder | Purpose | Contents |
|--------|---------|----------|
| **Philosophy** | Why we built it | Design decisions, motivations |
| **Technical** | How it works | Architecture, system details, testing |
| **User_Guide** | How to use | Workflow, getting started, index |
| **Planning** | Future work | Improvements, assessments |
| **Plans/** | Implementation plans | Specific feature plans |

### Skills/ - All Skills

**System Skills (Meta-Operations):**
| Skill | Purpose |
|-------|---------|
| add-content-folder | Create new folder + skill |
| delete-content-folder | Delete folder + skill + cleanup |
| Process_Link | Extract YouTube transcripts |

**Analysis Skills (Content Transformation):**
| Skill | Output Folder |
|-------|---------------|
| starter-story | Starter_Story/Process_data |
| my-first-million | My_First_Million/Process_data |
| founders | Founders/Process_data |
| ai-leaders | AI_Leaders/Process_data |
| inner-work | Inner_Work/Process_data |
| ai-engineering | AI_Engineering/Process_data |

### Content Folders - Your Knowledge Base

Each folder follows the same structure:

```
[FOLDER_NAME]/
├── AGENTS.md          # Folder-specific instructions
├── INDEX.md           # List of all content
├── Raw_Data/          # Raw transcripts
└── Process_data/       # Analyzed profiles
```

**Available Folders:**
| Folder | Category |
|--------|----------|
| Starter_Story | Startup profiles |
| My_First_Million | Business insights |
| Founders | Founder profiles with books |
| AI_Leaders | AI intelligence profiles |
| AI_Engineering | Technical frameworks |
| Inner_Work | Wisdom/philosophy |

### search/ - RAG Search System

| File | Purpose |
|------|---------|
| ask.py | RAG query with DeepSeek |
| answer_search.py | Semantic search (no LLM) |
| index.py | Build search index |
| config.py | Configuration settings |

### logs/ - Error & Healing Logs

| File | Purpose |
|------|---------|
| errors.log | Raw error details |
| healing_log.json | Self-healing events for future sessions |

---

## How Content Flows

### Adding New Content (You → System)

1. You provide a YouTube URL
2. Process_Link extracts transcript → saves to Raw_Data
3. Analysis skill transforms transcript → creates profile in Process_data
4. INDEX.md updated
5. Search index rebuilt
6. Changes pushed to GitHub

### Querying Knowledge (You → Answer)

1. You ask a question: `python search/ask.py "your question"`
2. System searches vector database (semantic search)
3. DeepSeek synthesizes answer from relevant documents
4. You get AI-powered answer with sources

---

## Self-Healing System

The system can automatically recover from errors:

| Error Type | Auto-Fix |
|------------|----------|
| API Rate Limit | Wait 5s → 10s → 20s, retry |
| API Timeout | Reduce max_tokens, retry |
| Transcript Language | Try: en-US → en-GB → en → auto → es → pt |
| Index Empty | Auto-rebuild |

**Healing Log:** All healing events are saved to `logs/healing_log.json` so future sessions can continue where this one left off.

---

## Key Files

| File | Purpose |
|------|---------|
| AGENTS.md | Agent instructions (read this first in new session) |
| Skills/AGENTS.md | All available skills |
| docs/Structure_Guide.md | This file |

---

## Important Notes

1. **Human-in-the-Loop:** You decide what goes in (URL + folder). System handles everything else.
2. **Depth over Breadth:** YouTube-only for v1. We perfect one thing before adding more.
3. **Self-Maintaining:** The system can add/delete folders, update references, rebuild index automatically.
4. **Git-Based:** All content is version-controlled and lives in GitHub.

---

*Last Updated: 2026-05-03*