# System Overview

## What is Knowledge OS?

Knowledge OS is an **autonomous agent system** that transforms unstructured content from YouTube videos into structured, searchable knowledge profiles. It combines AI-powered transcript extraction, analysis skills, vector-based semantic search, and Git-based version control.

---

## The Problem

You're probably consuming a lot of content:
- 📺 YouTube videos from podcasters, educators, and industry leaders
- 🎧 Podcasts with valuable insights
- 📚 Books and interviews

**The challenge:** This content is hard to search, easy to forget, and difficult to connect with other ideas you learn.

---

## The Solution

Knowledge OS automates the entire pipeline:

1. **Ingest** - You paste a YouTube URL
2. **Extract** - Transcript pulled automatically
3. **Analyze** - AI skill transforms content into structured profile
4. **Store** - Markdown file in category folder
5. **Index** - Searchable via semantic similarity
6. **Search** - Find relevant insights using natural language

---

## Key Features

### 1. Automated Transcript Extraction

```bash
python Transcript_Extraction.py "https://www.youtube.com/watch?v=..." "Starter_Story/Raw_Data"
```

- Fetches video metadata (title, channel, duration, views)
- Retrieves transcript from YouTube
- Saves as markdown with YAML frontmatter

### 2. Skill-Based Analysis

8 specialized skills process different content types:

| Skill | Input | Output |
|-------|-------|--------|
| add-content-folder | Folder name | Creates new folder structure |
| delete-content-folder | Folder name | Deletes folder + updates references |
| starter-story | Founder interviews | Startup profiles |
| ai-leaders | AI leader interviews | Intelligence profiles |
| founders | Business analysis | Founder profiles with books |
| my-first-million | Business podcast | Business insights |
| ai-engineering | Tech tutorials | Technical frameworks |
| inner-work | Personal growth | Wisdom profiles |

### 3. Structured Templates

Every profile follows a consistent structure:

```
# 📝 Executive Summary
[High-level overview]

# 🚀 Key Insights
[Main takeaways]

# 🛠️ Practical Application
[Actionable steps]

# 💬 Notable Quotes
[Best quotes]

# 📚 Resources
[Books, tools, references]
```

### 4. Semantic Search

Find relevant knowledge using natural language:

```bash
python search/answer_search.py "how do founders validate ideas"
```

- Uses sentence-transformers (all-MiniLM-L6-v2)
- ChromaDB vector database
- Relevance scoring

### 5. Version Control

- Automatic Git commits
- Structured commit messages
- GitHub backup

---

## Use Cases

### Personal Knowledge Management

- Build a searchable database of content you consume
- Never lose track of valuable insights
- Connect ideas across different sources

### Research

- Track developments in specific fields (AI, startups, philosophy)
- Compare perspectives from different sources
- Identify patterns and connections

### Content Creation

- Repurpose insights into articles, tweets, newsletters
- Quick reference for writing
- Citation-ready quotes and frameworks

### Learning

- Structured notes from videos and podcasts
- Actionable frameworks to implement
- Resources for deeper study

---

## Target Users

| User | Benefit |
|------|---------|
| **Builders** | Learn from startup founders systematically |
| **AI Enthusiasts** | Track AI industry developments |
| **Researchers** | Build searchable knowledge bases |
| **Content Creators** | Repurpose insights efficiently |
| **Lifelong Learners** | Organize and retain knowledge |

---

## Philosophy

### Core Principles

1. **Automation First** - Minimize manual work
2. **Structured Output** - Consistent format enables search
3. **Local-First** - Your data stays on your machine
4. **Git-Backed** - Version control for everything
5. **Human-Readable** - Markdown files work in Obsidian

### Design Decisions

| Decision | Rationale |
|----------|-----------|
| YouTube only | Reliable transcript API, most content available |
| Markdown storage | Obsidian-compatible, human-readable |
| Local vector DB | Privacy, no cloud costs |
| CLI interface | Simple, maintainable |
| Skill architecture | Extensible, modular |

---

## Comparison to Alternatives

| System | Knowledge OS | Notion | Obsidian | Readwise |
|--------|-------------|--------|----------|----------|
| **Transcript Extraction** | ✅ Auto | ❌ Manual | ❌ Manual | ✅ Auto |
| **AI Analysis** | ✅ Skills | ❌ Manual | ❌ Manual | ❌ |
| **Semantic Search** | ✅ Built-in | ❌ | ⚠️ Plugins | ✅ |
| **Cost** | Free | $10/mo | Free | $8/mo |
| **Data Storage** | Local | Cloud | Local | Cloud |
| **Custom Skills** | ✅ | ❌ | ❌ | ❌ |

---

## Technical Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| Transcript | yt-dlp, youtube-transcript-api |
| Vector DB | ChromaDB |
| Embeddings | sentence-transformers |
| Storage | Markdown + Git |
| Search | CLI |

---

## Limitations

| Limitation | Current State |
|------------|---------------|
| Content sources | YouTube only |
| Interface | CLI (no web UI) |
| Multi-user | Single user |
| Real-time sync | Manual push to GitHub |

*See [Improvement.md](../Improvement.md) for the roadmap to address these.*

---

## Success Stories

Knowledge OS has been used to build knowledge bases on:

- 🎯 **Startups** - 35+ founder profiles, validation strategies
- 🤖 **AI** - Andrej Karpathy, Evan Spiegel, AI product leadership
- 📚 **Business** - David Senra's Founders Podcast analysis
- 🧘 **Personal Growth** - Rabbi Friedman, David G, Kabbalah teachings

---

## Getting Started

Ready to start? Head to [GETTING_STARTED.md](../GETTING_STARTED.md) for the quick start guide.

---

*Last Updated: 2026-05-02*