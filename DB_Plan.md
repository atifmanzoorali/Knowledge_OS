# Knowledge OS - Semantic Search Implementation Plan

## Overview

Adding semantic search capabilities to the Knowledge OS system for efficient retrieval across hundreds of knowledge files.

---

## Tech Stack

| Component | Choice | Why |
|-----------|--------|-----|
| **Vector DB** | Chroma (embedded mode) | Local-only, no server needed, Python-based, easiest setup |
| **Embeddings** | sentence-transformers + `all-MiniLM-L6-v2` | Fast (~40ms), small model (2.8M params), excellent quality |
| **Interface** | Python CLI | Simple, no extra dependencies |

---

## Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────┐
│  User       │ ──▶ │  Embed Query    │ ──▶ │  Chroma DB  │
│  CLI Input  │     │  (all-MiniLM)   │     │  (local)    │
└─────────────┘     └──────────────────┘     └─────────────┘
                                                      │
                                                      ▼
                                              ┌─────────────┐
                                              │  Ranked     │
                                              │  Results    │
                                              └─────────────┘
```

---

## What Gets Indexed

| Source | Content | Why |
|--------|---------|-----|
| **Processed profiles** | Full content | Already distilled insights, less noise, better semantic matches |
| **Raw transcripts** | Full content | Complete context, full conversations |

---

## Folder Coverage

System-wide indexing across all categories:
- Starter_Story
- Inner_Work
- AI_Leaders
- Founders
- My_First_Million
- AI_Engineering

---

## Implementation Files

```
Knowledge_OS/
├── search/                     # Search capabilities
│   ├── index.py               # Builds the vector index
│   ├── search.py              # CLI search interface
│   ├── knowledge_db/          # Local Chroma database
│   └── requirements.txt       # Dependencies
├── (existing folders...)
```

---

## CLI Usage

### Build/Update Index
```bash
python search/index.py
```

### Search
```bash
python search/search.py "how did marc lou validate his idea"
```

### Output Example
```
1. Marc_Lou-35_Startups-2026.md (score: 0.89)
   "He validated by building in public and getting paid upfront..."

2. Jeremy_Redman-Taskmagic-2026.md (score: 0.72)
   "Similar validation approach..."
```

---

## Performance

| Metric | Value |
|--------|-------|
| Setup time | ~15 minutes |
| Indexing 100 files | ~30 seconds |
| Per search | <100ms |

---

## Pros & Cons

| Pros | Cons |
|------|------|
| 100% local, private | Initial index takes time |
| Free, no subscription | Must re-index when adding new files |
| Simple to maintain | CLI only (for now) |
| GitHub backup works | |

---

## Key Decisions

- Vector DB: Chroma (embedded - no server needed)
- Model: all-MiniLM-L6-v2 (2.8M parameters - fast!)
- Storage: Local folder `search/knowledge_db/`
- Update frequency: Manual (run index.py when you add new content)
- Content: Both raw transcripts AND processed profiles
- Results: File name + relevance score + 2-3 text snippets