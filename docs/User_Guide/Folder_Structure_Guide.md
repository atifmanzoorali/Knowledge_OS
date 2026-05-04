# Folder Structure Guide

Learn how content is organized and when to use each folder.

---

## Available Folders

Knowledge OS has 6 content folders, each designed for a specific type of content.

| Folder | Purpose | Best For |
|--------|---------|----------|
| **Starter_Story** | Startup founders | First-time founders sharing their journey |
| **My_First_Million** | Business podcast | My First Million podcast episodes |
| **Founders** | Business analysis | Founder interviews, business lessons |
| **AI_Leaders** | AI industry | Interviews with AI executives, researchers |
| **AI_Engineering** | Technical content | AI tutorials, engineering workflows |
| **Inner_Work** | Personal growth | Meditation, spirituality, philosophy |

---

## Folder Details

### Starter_Story

**What goes here:** Interviews with first-time founders sharing how they started.

**Example content:**
- How a founder validating their idea
- First customer acquisition story
- Early struggles and lessons learned

**Output:** Startup profile with validation strategies, traction metrics, key lessons

---

### My_First_Million

**What goes here:** Episodes from the My First Million podcast.

**Example content:**
- Business ideas and strategies
- Guest interviews
- Market analysis

**Output:** Business insight profile with actionable strategies

---

### Founders

**What goes here:** In-depth founder interviews and business analysis.

**Example content:**
- David Senra's Founders Podcast
- Book-based founder analysis
- Long-form business interviews

**Output:** Founder profile with company history, key lessons, **book recommendations** (mandatory section)

---

### AI_Leaders

**What goes here:** Interviews with AI industry leaders.

**Example content:**
- Andrej Karpathy on AI
- AI product leadership interviews
- Machine learning researchers

**Output:** Intelligence profile with AI thesis, mental models, contrarian views, what they're building

---

### AI_Engineering

**What goes here:** Technical AI development content.

**Example content:**
- LangChain tutorials
- Agent workflow tutorials
- AI automation patterns
- Code implementation guides

**Output:** Technical profile with frameworks, step-by-step guides, code examples, book references

---

### Inner_Work

**What goes here:** Personal growth, spiritual, and philosophical content.

**Example content:**
- Meditation teachings
- Zen Buddhism
- Kabbalah wisdom
- Psychology and self-improvement

**Output:** Wisdom profile with key concepts, practices, notable quotes

---

## How to Choose

Use this decision tree:

```
Is it about starting a company?
├─ Yes → Is it a first-time founder's story?
│   └─ Yes → Starter_Story
│   └─ No → Founders
└─ No → Is it about AI?
    ├─ Yes → Is it technical/engineering?
    │   └─ Yes → AI_Engineering
    │   └─ No → AI_Leaders
    └─ No → Is it business/podcast?
        ├─ Yes → My_First_Million
        └─ No → Inner_Work
```

---

## Folder Structure

Each folder follows the same structure:

```
Folder_Name/
├── Raw_Data/           # Original transcripts
│   └── video_id_title.md
├── Process_data/       # AI-generated profiles
│   └── Person-Topic-YYYY.md
├── INDEX.md            # List of all content
├── AGENTS.md           # Folder-specific instructions
└── README.md           # (optional)
```

---

## What's in Each Index

The INDEX.md file in each folder lists:
- All videos processed
- Date added
- Brief description
- Link to profile

---

## Adding New Folders

To add a new content category:
1. Use the **add-content-folder** skill
2. System creates folder structure automatically
3. Creates corresponding analysis skill
4. Updates all references

---

*Last Updated: 2026-05-04*