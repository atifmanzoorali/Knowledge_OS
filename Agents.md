# Knowledge OS

An autonomous agent system for processing YouTube transcripts and creating structured knowledge assets.

## GitHub Repository

https://github.com/atifmanzoorali/Knowledge_OS

## Folder Structure

```
Knowledge_OS/
├── AGENTS.md                    # This file - system overview
├── Transcript_Extraction.py     # Script to extract YouTube transcripts
├── DB_Plan.md               # Semantic search implementation plan
├── search/                  # Semantic search capabilities
│   ├── index.py            # Builds the vector index
│   ├── search.py           # CLI search interface
│   ├── knowledge_db/        # Local Chroma database
│   └── requirements.txt    # Dependencies
├── Skills/                      # Skills for the autonomous agent
│   ├── AGENTS.md                # Skills documentation
│   ├── README.md
│   ├── Process_Link/            # Extracts transcripts from YouTube
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── folder_structure.md
│   └── starter-story/           # Analyzes founder interviews
│       └── SKILL.md
│   ├── ai-leaders/              # Analyzes AI leader interviews
│       └── SKILL.md
│   └── my-first-million/        # Analyzes My First Million episodes
│       └── SKILL.md
├── Starter_Story/               # Starter Story content (fully operational)
│   ├── AGENTS.md                # Detailed workflow documentation
│   ├── INDEX.md                 # Master index of processed profiles
│   ├── Raw_Data/                # Raw transcripts
│   └── Process_data/            # Analyzed startup profiles
├── Inner_Work/                  # (Reserved for future skills)
│   ├── AGENTS.md
│   └── Raw_Data/
├── AI_Leaders/                  # AI Leaders content (operational)
│   ├── AGENTS.md
│   ├── INDEX.md
│   ├── Raw_Data/                # Raw transcripts
│   └── Process_data/            # Analyzed AI leader profiles
├── Founders/                    # (Reserved for future skills)
│   ├── AGENTS.md
│   └── Raw_Data/
├── My_First_Million/            # My First Million content (operational)
│   ├── AGENTS.md
│   ├── INDEX.md
│   ├── Raw_Data/                # Raw transcripts
│   └── Process_data/            # Analyzed business profiles
└── AI_Engineering/              # (Reserved for future skills)
    ├── AGENTS.md
    └── Raw_Data/
```

## How the System Works

### Processing Flow

1. **User provides YouTube URL**
2. **Process_Link skill** extracts transcript and saves to Raw_Data
3. **Skill chaining** automatically triggers analysis skill (if available)
4. **Analysis skill** creates structured profile and saves to Process_data
5. **INDEX.md** updated with new entry
6. **All changes pushed to GitHub** automatically

### Skills

| Skill | Purpose | Status |
|-------|---------|--------|
| Process_Link | Extract transcripts from YouTube URLs | ✅ Working |
| starter-story | Analyze Starter Story interviews | ✅ Working |
| (TBD) | Inner_Work content | 🔜 Planned |
| ai-leaders | Analyze AI Leaders interviews | ✅ Working |
| (TBD) | Founders content | 🔜 Planned |
| my-first-million | Analyze My First Million episodes | ✅ Working |
| (TBD) | AI_Engineering content | 🔜 Planned |

### Skill Chaining

When Process_Link saves to a folder with a corresponding analysis skill, it auto-triggers:

| Folder | Skill Triggered |
|--------|----------------|
| Starter_Story | starter-story |
| Inner_Work | (TBD) |
| AI_Leaders | ai-leaders |
| Founders | (TBD) |
| My_First_Million | my-first-million |
| AI_Engineering | (TBD) |

### GitHub Integration

- All changes automatically pushed to GitHub
- Process_Link pushes raw transcripts
- starter-story pushes processed profiles + INDEX
- ai-leaders pushes AI leader profiles + INDEX
- my-first-million pushes business insight profiles + INDEX
- Commit messages follow format: "Add transcript: [title]", "Add starter story: [founder] - [company]", "Add AI Leaders: [Person] - [Topic]", or "Add My First Million: [Guest/Topic]"

## Current Contents

### Starter_Story (Fully Operational)

**Raw_Data/** (2 transcripts):
- D4fkiQfzw_I_How_I_Work_$77KMonth_Solopreneur.md (Marc Lou)
- iVy5J7iE-3Q_Most_Successful_Solopreneur_OAT.md (Jeremy Redman)

**Process_data/** (2 profiles):
- Marc_Lou-35_Startups-2026.md
- Jeremy_Redman-Taskmagic-2026.md

**INDEX.md:**
| Founder | Company | Year | Date Added |
|---------|---------|------|----------|
| Marc Lou | 35 Startups | 2026 | 2026-05-02 |
| Jeremy Redman | Taskmagic | 2026 | 2026-05-02 |

## Starting a New Session

In a new session, the agent should:

1. **First**, read `Knowledge_OS/AGENTS.md` for system overview
2. **For Starter_Story queries**, also read `Knowledge_OS/Starter_Story/AGENTS.md` for detailed workflow
3. **For skills**, read `Knowledge_OS/Skills/AGENTS.md` for skill documentation
4. **Check GitHub** for latest updates if needed: `git pull origin main`

## Processing a New Transcript

**Command format:**
```
Process_Link <YouTube_URL>
```

The skill will:
1. Ask for folder selection (select Starter_Story)
2. Extract transcript to Raw_Data
3. Auto-trigger starter-story skill
4. Create profile in Process_data
5. Update INDEX.md
6. Push all changes to GitHub

## Scripts

- **Transcript_Extraction.py** - Extracts transcripts using yt-dlp and YouTubeTranscriptApi, saves .md with YAML frontmatter

## Semantic Search

The system includes semantic search capabilities using ChromaDB (local vector database) and sentence-transformers.

### Setup

```bash
pip install -r search/requirements.txt
```

### Indexing

Build or update the search index:

```bash
python search/index.py
```

This scans all folders (Starter_Story, Inner_Work, AI_Leaders, Founders, My_First_Million, AI_Engineering) and indexes both Raw_Data and Process_data folders.

### Searching

```bash
python search/search.py "your search query"
```

Example:
```bash
python search/search.py "how did marc lou validate his idea"
```

### Tech Stack

| Component | Choice |
|-----------|--------|
| Vector DB | Chroma (embedded, local-only) |
| Embeddings | all-MiniLM-L6-v2 |
| Index Location | search/knowledge_db/ |

### Notes

- Run `index.py` whenever you add new content to search
- Search is 100% local - no data leaves your machine
- The knowledge_db folder is in .gitignore (local only - rebuild with `python search/index.py` after cloning)

## Notes

- This is a fully autonomous agent system
- All skills include automatic GitHub push
- Each category folder can have its own analysis skill
- INDEX files track all processed content
- AGENTS.md files document workflows for new sessions