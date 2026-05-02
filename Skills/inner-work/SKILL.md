---
name: inner-work
description: This skill should be used when the user wants to "analyze inner work content", "process spiritual transcript", "extract wisdom from [topic]", "add [Teacher/Topic] inner work", or after Process_Link saves to Inner_Work folder. Transforms personal growth, spiritual, and philosophical transcripts into actionable wisdom profiles.
---

# Inner Work

Transforms raw YouTube transcripts about spiritual, philosophical, and personal growth content into actionable wisdom profiles. Handles diverse topics including Kabbalah, Zen, Stoicism, mindfulness, self-improvement, and general spirituality.

---

## Storage Location

- **Input:** `Knowledge_OS/Inner_Work/Raw_Data/[filename].md` (from Process_Link)
- **Output:** `Knowledge_OS/Inner_Work/Process_data/[Teacher]-[Topic]-[Year].md`
- **INDEX:** `Knowledge_OS/Inner_Work/INDEX.md`

After saving, always update INDEX.

---

## Category Detection

| Category | Emoji | Examples |
|----------|-------|----------|
| Spirituality | 🕉️ | General spiritual teachings, consciousness |
| Philosophy | 📜 | Stoicism, Buddhism, existentialism |
| Psychology | 🧠 | Mindset, behavior, emotional intelligence |
| Personal Growth | 🌱 | Self-improvement, habits, mindset |
| Kabbalah | 🕯️ | Jewish mysticism, Zohar, spiritual laws |
| Mysticism | 🔮 | Sufism, Hermeticism, esoteric traditions |

Auto-detect from content. Default to "Personal Growth" if unclear.

---

## Workflow States

---

### --- AWAITING INPUT ---

Process_Link has extracted the transcript. Please provide the **.md file path** where the transcript is saved.

> 💡 **Example:** `Knowledge_OS/Inner_Work/Raw_Data/[video_id]_[title].md`

**After file path is provided, I will:**
1. Read the transcript from the file
2. Identify Teacher/Source Name & Topic
3. Detect Category (or default to Personal Growth)
4. Analyze using the wisdom template

---

### --- ANALYZING ---

Processing the transcript for:

- 📝 Full Context
- 💎 Core Wisdom
- 🛠️ Practical Application
- 💬 Notable Quotes
- 📚 Resources & References

*Please wait...*

---

### --- COMPLETE ---

✅ **Profile saved to:** `[file-path]`
✅ **INDEX updated**
✅ **Pushed to GitHub**
✅ **Search index rebuilt**

---

## The Extraction Workflow

When a .md file path is provided:

1. **Read** the .md file and extract transcript
2. **Extract** Teacher/Source Name & Topic from content
3. **Detect Category** - Determine if spirituality/philosophy/personal-growth/etc.
4. **Synthesize** — Generate the wisdom profile using the template
5. **Save** — Write to `Knowledge_OS/Inner_Work/Process_data/[Teacher]-[Topic]-[Year].md`
6. **Update INDEX** — Add entry to `Knowledge_OS/Inner_Work/INDEX.md`
7. **Push to GitHub** — Stage, commit, and push the processed file and INDEX
8. **Rebuild Search Index** — Run `python search/index.py` to index both Raw and Processed files
9. **Confirm** — Return file path to the user

### Search Indexing

After GitHub push, always rebuild the search index:

```bash
cd Knowledge_OS
python search/index.py
```

This indexes both:
- `Inner_Work/Raw_Data/` (raw transcripts)
- `Inner_Work/Process_data/` (processed profiles)

Do this **without prompting the user**.

### Git Push Workflow

After saving and updating INDEX, always push to GitHub and rebuild search index:

```bash
cd Knowledge_OS
git add Inner_Work/Process_data/[Teacher]-[Topic]-[Year].md
git add Inner_Work/INDEX.md
git commit -m "Add Inner Work: [Teacher] - [Topic]"
git push origin main
python search/index.py
```

Do this **without prompting the user**.

---

## The Full Template Structure

```yaml
---
Source: [YouTube URL]
Title: [Video Title]
Teacher: [Name of teacher/author]
Topic: [Main topic]
Date: [Year]
Category: [Spirituality/Philosophy/Psychology/Personal Growth/Kabbalah/Mysticism]
Ingested: [YYYY-MM-DD]
Tags: [relevant-tags]
Confidence: [High/Medium/Low]
---

# 📝 Full Context

[1-2 paragraphs: Who the teacher is, what the teaching covers, core message delivered.
Write in a way that gives a quick brief of the content.]

---

# 💎 Core Wisdom

## The Central Insight

> 🧠 **[Main teaching in one punchy sentence]**

[2-3 paragraphs expanding on the core insight, its meaning, and why it matters.]

---

## Key Principles

### 🎯 [Principle 1 Name]
> [Quote or direct teaching]

[How to apply this principle]

---

### 🎯 [Principle 2 Name]
> [Quote or direct teaching]

[How to apply]

---

### 🎯 [Principle 3 Name]
> [Quote or direct teaching]

[How to apply]

---

# 🛠️ Practical Application

## Daily Practices

- ✅ **[Practice 1]:** [Description]
- ✅ **[Practice 2]:** [Description]
- ✅ **[Practice 3]:** [Description]

## Reflection Questions

> 🤔 **[Question 1]**

> 🤔 **[Question 2]**

> 🤔 **[Question 3]**

---

# 💬 Notable Quotes

> 💬 "[Quote 1]"
> — [Source]

> 💬 "[Quote 2]"
> — [Source]

> 💬 "[Quote 3]"
> — [Source]

---

# 📚 Resources & References

> 📚 **Works mentioned:** [Books, texts, or resources discussed]
> 🎯 **For deeper study:** [Next steps for learning]
> 🔗 **Related traditions:** [Other schools/traditions that connect]

---

# 🏷️ Content Connections

> 🏷️ **For LinkedIn:** [A hook angle for content repurposing]
> 🏷️ **Contrarian Angle:** [Another hook angle]

---

*Source: [Video Title](YouTube URL)*

*Last Updated: [YYYY-MM-DD]*
```

---

## INDEX Format

```markdown
# Inner Work INDEX

| Teacher | Topic | Category | Date Added |
|---------|-------|----------|------------|
```

**Add new entries in this format:**
```
| Ram Dass | Be Here Now | spirituality | 2026-05-02 |
```

---

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| ✅ **High** | Full transcript, clear narrative, teacher identified, actionable content |
| ⚠️ **Medium** | Partial transcript, some gaps, topic identifiable |
| ❌ **Low** | Thin transcript, major gaps, unclear what the teaching is about |

---

## Tag Categories

Add relevant tags based on content:

**Category Tags:**
- `spirituality`
- `philosophy`
- `psychology`
- `personal-growth`
- `kabbalah`
- `mysticism`

**Topic Tags:**
- `meditation`, `mindfulness`, `awareness`
- `self-improvement`, `habits`, `discipline`
- `ancient-wisdom`, `modern-interpretation`
- `consciousness`, `enlightenment`
- `relationships`, `love`, `purpose`

---

## Formatting Rules

- **Heavy white space** between sections — use `---` as separators
- **Emojis** on every section header for visual scanning
- **Blockquotes** for quoted advice or key insights
- **Bold** key terms and important numbers
- **Core wisdom** should capture the essence in a memorable way
- Maximum 3 key principles
- Maximum 3 daily practices
- Pull 3-5 of the best quotes
- Always include Resources section with books mentioned

---

*Last Updated: 2026-05-02*