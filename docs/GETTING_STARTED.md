# Getting Started with Knowledge OS

A quick guide to get you up and running with Knowledge OS in under 5 minutes.

---

## Prerequisites

Before you begin, ensure you have:

| Requirement | Version | Check Command |
|-------------|---------|---------------|
| Python | 3.10+ | `python --version` |
| Git | Any recent | `git --version` |
| Internet | Required | For YouTube access |

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/atifmanzoorali/Knowledge_OS.git
cd Knowledge_OS
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a requirements.txt, install manually:

```bash
pip install yt-dlp youtube-transcript-api chromadb sentence-transformers
```

**Verify installation:**

```bash
python -c "import yt_dlp, youtube_transcript_api, chromadb; print('All dependencies installed!')"
```

---

## Step 3: Process Your First Video

### Using Process_Link (Recommended)

When running in an AI assistant (like Claude Code), simply provide a YouTube URL:

```
User: Process this: https://www.youtube.com/watch?v=dQw4w9WgXcQ
System: Which folder?
User: Starter_Story
```

### Using the Script Directly

```bash
python Transcript_Extraction.py "https://www.youtube.com/watch?v=VIDEO_ID" "Starter_Story/Raw_Data"
```

**Available folders:**
- `Starter_Story`
- `AI_Leaders`
- `Founders`
- `My_First_Million`
- `AI_Engineering`
- `Inner_Work`

---

## Step 4: Rebuild Search Index

After adding new content, rebuild the search index:

```bash
python search/index.py
```

**Expected output:**
```
============================================================
Knowledge OS - Semantic Search Indexer
============================================================

[1/4] Loading embedding model: all-MiniLM-L6-v2...
      Model loaded successfully!

[2/4] Scanning for markdown files...
      Found X files

[3/4] Reading file contents...
      ...

[4/4] Creating embeddings and storing in Chroma...
============================================================
Indexing complete!
  - Indexed X documents
  - Database stored at: search/knowledge_db
============================================================
```

---

## Step 5: Search Your Knowledge Base

```bash
python search/answer_search.py "your search query"
```

**Example:**

```bash
python search/answer_search.py "how do solopreneurs validate ideas"
```

**Expected output:**
```
============================================================
Knowledge OS - Search
============================================================

Searching for: "how do solopreneurs validate ideas"
------------------------------------------------------------

Found 2 relevant section(s):

============================================================

--- RESULT 1 ---
Source: Starter_Story/Process_data/Marc_Lou-35_Startups-2026.md [profile]
Category: Starter_Story | Relevance: 92%

"The only way to validate an idea is to ship it with a buy button..."
============================================================
```

---

## Understanding the Workflow

```
┌────────────┐    ┌─────────────┐    ┌────────────┐
│  YouTube   │───▶│ Transcript  │───▶│   Skill    │
│   URL      │    │ Extraction  │    │  Analysis  │
└────────────┘    └─────────────┘    └─────┬──────┘
                                           │
        ┌──────────────────────────────────┼──────────────────┐
        ▼                                  ▼                  ▼
┌──────────────┐               ┌─────────────────┐   ┌─────────────┐
│ Process_data │               │  ChromaDB       │   │   GitHub    │
│ (Profiles)   │               │  (Search Index) │   │   (Backup)  │
└──────────────┘               └─────────────────┘   └─────────────┘
```

1. **YouTube URL** → Provide a video URL
2. **Transcript Extraction** → Automatic transcript retrieval
3. **Skill Analysis** → Content processed into structured profile
4. **Storage** → Saved to appropriate category folder
5. **Indexing** → Searchable via semantic search
6. **Backup** → Automatically pushed to GitHub

---

## Content Folders Explained

| Folder | What Goes Here | Example |
|--------|---------------|---------|
| **Starter_Story** | Startup founder interviews | How Marc Lou built 35 startups |
| **AI_Leaders** | AI industry leaders | Evan Spiegel on Snap innovation |
| **Founders** | Business history | Roger Federer's mental models |
| **My_First_Million** | Business podcast | Chad Gruns' $1B exit |
| **AI_Engineering** | AI tutorials | Andrej Karpathy on agentic AI |
| **Inner_Work** | Personal growth | Rabbi Friedman on love & marriage |

---

## What Happens After Processing?

When you process a video, the system:

1. ✅ Extracts transcript from YouTube
2. ✅ Saves raw transcript to `Raw_Data/`
3. ✅ Triggers appropriate analysis skill
4. ✅ Generates structured profile in `Process_data/`
5. ✅ Updates `INDEX.md` with new entry
6. ✅ Commits and pushes to GitHub
7. ✅ Rebuilds search index

---

## Common Tasks

### Add a New Video

```bash
python Transcript_Extraction.py "https://www.youtube.com/watch?v=..." "Folder/Raw_Data"
```

### Update Search Index

```bash
python search/index.py
```

### Search Everything

```bash
python search/answer_search.py "deep work"
```

### View All Indexed Files

Check the output of `python search/index.py` - it lists all 77+ indexed files.

---

## Troubleshooting

### "Transcript not available"

Some videos don't have transcripts. Try a different video or use auto-generated captions.

### "Invalid YouTube URL"

Make sure the URL is in format:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`

### "No results found"

Run the indexer first:
```bash
python search/index.py
```

### "Module not found"

Reinstall dependencies:
```bash
pip install -r requirements.txt
```

---

## Next Steps

Now that you're set up, you can:

- 📺 **Process more videos** - Add to your knowledge base
- 🔍 **Explore semantic search** - Try different queries
- 📖 **Read the profiles** - Check `Process_data/` folders
- 🛠️ **Customize skills** - Modify analysis templates in `Skills/`
- 📊 **Review architecture** - See [ARCHITECTURE.md](ARCHITECTURE.md)

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `python Transcript_Extraction.py [url] [folder]` | Process a video |
| `python search/index.py` | Rebuild search index |
| `python search/answer_search.py "[query]"` | Search knowledge base |
| `git status` | Check for uncommitted changes |

---

## Getting Help

- 📖 **Full Documentation:** See [ARCHITECTURE.md](ARCHITECTURE.md)
- 🐛 **Report Issues:** GitHub Issues
- 💡 **Contribute:** Submit a PR

---

*Ready to build your personal knowledge base!*
*Last Updated: 2026-05-02*