# Knowledge OS

An autonomous agent system for processing YouTube transcripts and creating structured knowledge assets.

## GitHub Repository

https://github.com/atifmanzoorali/Knowledge_OS

## Folder Structure

```
Knowledge_OS/
├── AGENTS.md                    # This file - system overview
├── Transcript_Extraction.py     # Script to extract YouTube transcripts
├── DB_Plan.md                  # Semantic search implementation plan
├── search/                     # Semantic search capabilities
│   ├── index.py               # Builds the vector index
│   ├── search.py              # CLI search interface
│   ├── knowledge_db/          # Local Chroma database
│   └── requirements.txt       # Dependencies
├── Skills/                     # Skills for the autonomous agent
│   ├── AGENTS.md              # Skills documentation
│   ├── README.md
│   ├── Process_Link/          # Extracts transcripts from YouTube
│   │   └── SKILL.md
│   ├── starter-story/         # Analyzes Starter Story interviews
│   │   └── SKILL.md
│   ├── ai-leaders/            # Analyzes AI leader interviews
│   │   └── SKILL.md
│   ├── founders/              # Analyzes Founders Podcast
│   │   └── SKILL.md
│   ├── my-first-million/      # Analyzes My First Million episodes
│   │   └── SKILL.md
│   ├── inner-work/            # Analyzes Inner Work content
│   │   └── SKILL.md
│   └── ai-engineering/        # Analyzes AI Engineering content
│       └── SKILL.md
├── Starter_Story/             # Starter Story content (operational)
│   ├── AGENTS.md
│   ├── INDEX.md
│   ├── Raw_Data/
│   └── Process_data/
├── My_First_Million/          # My First Million content (operational)
│   ├── AGENTS.md
│   ├── INDEX.md
│   ├── Raw_Data/
│   └── Process_data/
├── Founders/                  # Founders Podcast content (operational)
│   ├── AGENTS.md
│   ├── INDEX.md
│   ├── Raw_Data/
│   └── Process_data/
├── AI_Engineering/            # AI Engineering content (operational)
│   ├── AGENTS.md
│   ├── INDEX.md
│   ├── Raw_Data/
│   └── Process_data/
├── AI_Leaders/                # AI Leaders content (operational)
│   ├── AGENTS.md
│   ├── INDEX.md
│   ├── Raw_Data/
│   └── Process_data/
└── Inner_Work/                # Inner Work content (operational)
    ├── AGENTS.md
    ├── INDEX.md
    ├── Raw_Data/
    └── Process_data/
```

## How the System Works

### Processing Flow

1. **User provides YouTube URL** (with optional transcript)
2. **Process_Link skill** extracts transcript and saves to Raw_Data
3. **Skill chaining** automatically triggers analysis skill (if available)
4. **Analysis skill** creates structured profile and saves to Process_data
5. **INDEX.md** updated with new entry
6. **All changes pushed to GitHub** automatically
7. **Search index rebuilt**

### Skills

| Skill | Purpose | Status |
|-------|---------|--------|
| Process_Link | Extract transcripts from YouTube URLs | ✅ Working |
| starter-story | Analyze Starter Story interviews | ✅ Working |
| founders | Analyze Founders Podcast (interviews & analysis) | ✅ Working |
| ai-leaders | Analyze AI Leaders interviews | ✅ Working |
| my-first-million | Analyze My First Million episodes | ✅ Working |
| inner-work | Analyze Inner Work content | ✅ Working |
| ai-engineering | Analyze AI Engineering content | ✅ Working |

All skills are stored locally in `Knowledge_OS/Skills/` and are triggered by Process_Link.

### Skill Chaining

When Process_Link saves to a folder with a corresponding analysis skill, it auto-triggers:

| Folder | Skill Triggered |
|--------|----------------|
| Starter_Story | starter-story |
| My_First_Million | my-first-million |
| Founders | founders |
| AI_Leaders | ai-leaders |
| Inner_Work | inner-work |
| AI_Engineering | ai-engineering |

### GitHub Integration

- All changes automatically pushed to GitHub
- Commit messages follow format:
  - "Add transcript: [title]"
  - "Add starter story: [founder] - [company]"
  - "Add Founders: [Person] - [Topic]"
  - "Add AI Leaders: [Person] - [Topic]"
  - "Add My First Million: [Guest/Topic]"
  - "Add AI Engineering: [Framework/Concept]"
  - "Add Inner Work: [Teacher] - [Topic]"

## Current Contents

### Starter_Story (Fully Operational)

**Raw_Data/** (2 transcripts):
- D4fkiQfzw_I_How_I_Work_$77KMonth_Solopreneur.md (Marc Lou)
- iVy5J7iE-3Q_Most_Successful_Solopreneur_OAT.md (Jeremy Redman)

**Process_data/** (3 profiles):
- Marc_Lou-35_Startups-2026.md
- Jeremy_Redman-Taskmagic-2026.md
- Jordan-Parakeet_Chat-2026.md

**INDEX.md:**
| Founder | Company | Year | Date Added |
|---------|---------|------|----------|
| Marc Lou | 35 Startups | 2026 | 2026-05-02 |
| Jeremy Redman | Taskmagic | 2026 | 2026-05-02 |
| Jordan | Parakeet Chat | 2026 | 2026-05-02 |

---

### My_First_Million (Fully Operational)

**Raw_Data/** (2 transcripts):
- _cA9WEcBLH0_Follow_your_bliss.md (Ep. 818 - Career Advice)
- I8j_yBfAepY_Gruns_1B_Exit.md (Ep. 820 - Chad/Grüns $1B Exit)

**Process_data/** (2 profiles):
- Follow_Your_Bliss-2026.md
- Chad_Gruns_1B_Exit-2026.md

**INDEX.md:**
| Episode | Guest/Topic | Category | Date Added |
|---------|-------------|----------|------------|
| Ep. 818 | Follow your bliss - Career Advice | brainstorm | 2026-05-02 |
| Ep. 820 | Chad - Grüns $1B Exit | interview | 2026-05-02 |

---

### Founders (Fully Operational)

**Raw_Data/** (2 transcripts):
- -dh-QNlX12k_Arnold_Education_of_a_Bodybuilder.md
- mHE37R0aBUA_The_Infinity_Machine.md

**Process_data/** (2 profiles):
- Arnold_Schwarzenegger-Education_of_a_Bodybuilder-2026.md
- Demis_Hassabis-The_Infinity_Machine-2026.md

**INDEX.md:**
| Person | Company/Topic | Type | Primary Book | Date Added |
|--------|---------------|------|--------------|------------|
| Arnold Schwarzenegger | The Education of a Bodybuilder | analysis | Arnold: The Education of a Bodybuilder | 2026-05-02 |
| Demis Hassabis | The Infinity Machine | analysis | The Infinity Machine | 2026-05-02 |

---

### AI_Engineering (Fully Operational)

**Raw_Data/** (2 transcripts):
- -QFHIoCo-Ko_Full_Walkthrough_Workflow_for_AI_Coding_—_Matt_Poc.md
- v4F1gFy-hqg_Why_Software_Fundamentals_Matter_More_Than_Ever.md

**Process_data/** (2 profiles):
- AI-Engineering-Workflow-Matt-Pocock-2026.md
- Software-Fundamentals-Matter-More-Than-Ever-2026.md

**INDEX.md:**
| Framework/Concept | Category | Date Added |
|-------------------|----------|------------|
| AI Engineering Workflow (Matt Pocock) | agentic-ai | 2026-05-02 |
| Software Fundamentals Matter More Than Ever | agentic-ai | 2026-05-02 |

---

### AI_Leaders (Fully Operational)

**Raw_Data/** (2 transcripts):
- kJJ9uCD8-1A_Evan_Spiegel_on_Snap.md
- 3i1tMdm5Xnw_Cat_Wu_Anthropic.md

**Process_data/** (2 profiles):
- Evan_Spiegel-Snap_Product_Innovation-2026.md
- Cat_Wu-Anthropic_Product_Management-2026.md

**INDEX.md:**
| Person | Topic | Date Added |
|--------|-------|------------|
| Evan Spiegel | Snap Product Innovation | 2026-05-02 |
| Cat Wu | Anthropic Product Management | 2026-05-02 |

---

### Inner_Work (Fully Operational)

**Raw_Data/** (1 transcript):
- oAQqomDe8tc_David_G-Why_Isnt_Everyone_Receiving_Limitless_Abundance.md

**Process_data/** (1 profile):
- David_G-Abundance_Spirituality-2024.md

**INDEX.md:**
| Teacher | Topic | Category | Date Added |
|---------|-------|----------|------------|
| David G. | Abundance & Spirituality | kabbalah | 2026-05-02 |

---

## Starting a New Session

In a new session, the agent should:

1. **First**, read `Knowledge_OS/AGENTS.md` for system overview
2. **For Starter_Story queries**, also read `Knowledge_OS/Starter_Story/AGENTS.md` for detailed workflow
3. **For My_First_Million queries**, also read `Knowledge_OS/My_First_Million/AGENTS.md` for detailed workflow
4. **For Founders queries**, also read `Knowledge_OS/Founders/AGENTS.md` for detailed workflow
5. **For AI_Leaders queries**, also read `Knowledge_OS/AI_Leaders/AGENTS.md` if available
6. **For AI_Engineering queries**, also read `Knowledge_OS/AI_Engineering/AGENTS.md` for detailed workflow
7. **For Inner_Work queries**, also read `Knowledge_OS/Inner_Work/AGENTS.md` for detailed workflow
8. **For skills**, read `Knowledge_OS/Skills/AGENTS.md` for skill documentation
9. **Check GitHub** for latest updates if needed: `git pull origin main`

## Processing a New Transcript

### Option 1: Process_Link Skill (Recommended)

```
Process_Link <YouTube_URL>
```

The skill will:
1. Ask for folder selection (Starter_Story, My_First_Million, AI_Leaders, Founders, AI_Engineering, Inner_Work, etc.)
2. Extract transcript to Raw_Data
3. Auto-trigger corresponding analysis skill (if available)
4. Create profile in Process_data
5. Update INDEX.md
6. Push all changes to GitHub
7. Rebuild search index

### Option 2: Provide Transcript Directly

If you already have a transcript, provide:
- YouTube URL
- Raw transcript text
- Desired folder

The system will save to Raw_Data and optionally trigger the appropriate analysis skill.

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

This scans all folders (Starter_Story, My_First_Million, Founders, AI_Engineering, AI_Leaders, Inner_Work) and indexes both Raw_Data and Process_data folders.

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
- All skills are stored in the global `.agents/skills/` folder (for the skill tool to work)
- All skills include automatic GitHub push
- Each category folder can have its own analysis skill
- INDEX files track all processed content
- AGENTS.md files document workflows for new sessions
- The format-transcript skill can also be used to save transcripts to the Source folder in the knowledge base
- Inner_Work handles spiritual, philosophical, and personal growth content (not just spiritual teachers - also psychology, philosophy, personal growth)