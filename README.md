# Knowledge OS

<p align="center">
  <img src="assets/icon.png" alt="Knowledge OS Logo" width="120" />
</p>

<p align="center">
  <a href="https://python.org/">
    <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python" />
  </a>
  <a href="https://github.com/atifmanzoorali/Knowledge_OS/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" />
  </a>
  <a href="https://github.com/atifmanzoorali/Knowledge_OS/actions">
    <img src="https://img.shields.io/badge/Build-Passing-brightgreen.svg" alt="Build" />
  </a>
</p>

> AI-powered knowledge management system that transforms content from podcasts, videos, and interviews into structured, searchable profiles.

---

## What is Knowledge OS?

Knowledge OS is an autonomous agent system that ingests content from YouTube, extracts transcripts, and transforms them into structured knowledge profiles using AI-powered analysis skills. It builds a personal knowledge base with semantic search capabilities.

### Key Features

- **Automated Transcript Extraction** - Pull transcripts from any YouTube video
- **Skill-Based Analysis** - 6 specialized skills that process different content types
- **Structured Profiles** - Consistent, searchable markdown profiles
- **Semantic Search** - Find relevant knowledge using natural language
- **GitHub Integration** - Automatic version control and backup

---

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/atifmanzoorali/Knowledge_OS.git
cd Knowledge_OS
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Requirements include:
- `yt-dlp` - YouTube video extraction
- `youtube-transcript-api` - Transcript retrieval
- `chromadb` - Vector database for search
- `sentence-transformers` - Semantic embeddings

### 3. Process Your First Video

```bash
python Transcript_Extraction.py "https://www.youtube.com/watch?v=VIDEO_ID" "Starter_Story/Raw_Data"
```

### 4. Rebuild Search Index

```bash
python search/index.py
```

### 5. Search Your Knowledge Base

```bash
python search/answer_search.py "your search query"
```

---

## Project Structure

```
Knowledge_OS/
├── Starter_Story/          # Startup founder interviews
│   ├── Raw_Data/          # Original transcripts
│   ├── Process_data/      # Analyzed profiles
│   └── INDEX.md
├── AI_Leaders/            # AI industry leader interviews
│   ├── Raw_Data/
│   ├── Process_data/
│   └── INDEX.md
├── Founders/              # David Senra's Founders Podcast
│   ├── Raw_Data/
│   ├── Process_data/
│   └── INDEX.md
├── My_First_Million/      # My First Million podcast
│   ├── Raw_Data/
│   ├── Process_data/
│   └── INDEX.md
├── AI_Engineering/        # AI development tutorials
│   ├── Raw_Data/
│   ├── Process_data/
│   └── INDEX.md
├── Inner_Work/            # Spiritual & personal growth
│   ├── Raw_Data/
│   ├── Process_data/
│   └── INDEX.md
├── search/                # Semantic search system
│   ├── index.py           # Build search index
│   ├── answer_search.py   # Query the knowledge base
│   └── knowledge_db/      # ChromaDB vector store
├── Skills/                # Analysis skills
├── Transcript_Extraction.py
├── DB_Plan.md
└── README.md
```

---

## Content Categories

| Folder | Content Type | Example |
|--------|-------------|---------|
| Starter_Story | Startup founder interviews | Marc Lou, Jordan |
| AI_Leaders | AI industry leaders | Evan Spiegel, Cat Wu |
| Founders | Business history & analysis | Roger Federer, Elon Musk |
| My_First_Million | Business podcast | Chad Gruns, Arvid |
| AI_Engineering | AI development | Andrej Karpathy, Matt Pocock |
| Inner_Work | Personal growth | Rabbi Friedman, David G |

---

## How It Works

```
┌──────────────┐     ┌─────────────────┐     ┌───────────────┐
│  YouTube     │────▶│  Transcript     │────▶│  Skill        │
│  URL         │     │  Extraction     │     │  Router       │
└──────────────┘     └─────────────────┘     └───────┬───────┘
                                                      │
        ┌─────────────────────────┬────────┬────────┼───────┐
        ▼                         ▼        ▼        ▼       ▼
   ┌─────────┐             ┌──────────┐ ┌────────┐ ┌──────┐ ┌──────┐
   │ Starter │             │   AI      │ │Founders│ │Inner │ │My    │
   │ Story   │             │Leaders   │ │        │ │Work  │ │FirstM│
   └────┬────┘             └────┬─────┘ └───┬────┘ └──┬────┘ └──┬───┘
        │                       │           │        │         │
        ▼                       ▼           ▼        ▼         ▼
   ┌─────────────────────────────────────────────────────────┐
   │              Process_data/ (Structured Profiles)        │
   └─────────────────────────────────────────────────────────┘
                            │
                            ▼
   ┌─────────────────────────────────────────────────────────┐
   │              ChromaDB + Sentence-Transformers           │
   │                    (Semantic Search)                    │
   └─────────────────────────────────────────────────────────┘
```

1. **Ingest** - Provide a YouTube URL
2. **Extract** - Transcript pulled automatically
3. **Route** - Content routed to appropriate skill
4. **Analyze** - Skill transforms transcript into structured profile
5. **Store** - Profile saved to category folder
6. **Index** - Content indexed for semantic search
7. **Search** - Query using natural language

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| Transcript Extraction | yt-dlp, youtube-transcript-api |
| Vector Search | ChromaDB |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Storage | Markdown + Git |
| Search UI | CLI |

---

## Usage Examples

### Process a Starter Story

```
User: "Process this: https://www.youtube.com/watch?v=..."
System: Which folder?
User: "Starter_Story"
System: [Extracts transcript, runs starter-story skill, creates profile, pushes to GitHub]
```

### Search the Knowledge Base

```bash
$ python search/answer_search.py "how did marc lou validate his ideas"

Found 3 relevant section(s):

--- RESULT 1 ---
Source: Starter_Story/Process_data/Marc_Lou-35_Startups-2026.md [profile]
Category: Starter_Story | Relevance: 92%
"The only way to validate an idea is to ship it with a buy button..."
```

---

## Contributing

Contributions welcome! Please read our contributing guidelines before submitting PRs.

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Related Documentation

- [Architecture Overview](ARCHITECTURE.md)
- [Getting Started Guide](GETTING_STARTED.md)
- [Skills Documentation](Skills/)
- [System Workflow](docs/workflow.md)

---

<p align="center">
  Built with Claude Code | Knowledge OS v1.0
</p>