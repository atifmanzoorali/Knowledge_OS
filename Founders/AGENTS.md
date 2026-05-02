# Founders

Workflow documentation for processing David Senra's Founders Podcast.

---

## Overview

| Component | Details |
|-----------|---------|
| **Skill** | `founders` |
| **Source** | @DavidSenra and @founderspodcast1 |
| **Input** | Raw transcript from Process_Link |
| **Output** | Structured founder profile |

---

## Episode Types

| Type | Channel | Description |
|------|---------|-------------|
| **Interview** | @DavidSenra | Live conversation with current founder |
| **Analysis** | @founderspodcast1 | Book-based insights about historical figure |

---

## Workflow

1. **Process_Link** → User selects "Founders" folder → Raw transcript saved
2. **Skill chaining** → `founders` skill auto-triggers
3. **Founders skill** → Detects type → Applies template → Extracts books (mandatory)
4. **Output** → Profile saved to Process_data
5. **INDEX** → Updated
6. **GitHub** → Pushed
7. **Search** → Index rebuilt

---

## Books (Mandatory)

Every profile MUST include books section:
- Books written BY the person
- Books written ABOUT the person  
- Books mentioned/referenced

---

## Storage

```
Founders/
├── AGENTS.md
├── INDEX.md
├── Raw_Data/       # Transcripts from Process_Link
└── Process_data/  # Analyzed profiles
```

---

*Last Updated: 2026-05-02*