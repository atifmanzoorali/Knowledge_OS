---
name: founders
description: "When the user wants to 'process founders', 'analyze this founder', 'add [Person] founder', or 'Founders podcast'. Transforms raw Founders Podcast transcripts (both live interviews and book-based analysis) into structured founder profile documents with books as mandatory section."
---

# Founders

Transforms raw YouTube transcripts from David Senra's Founders Podcast into structured founder profiles. Handles two episode types: **interviews** (live conversations with founders) and **analysis** (book-based insights about historical figures).

---

## Storage Location

- **Input:** `Knowledge_OS/Founders/Raw_Data/[filename].md` (from Process_Link)
- **Output:** `Knowledge_OS/Founders/Process_data/[FounderName]-[CompanyOrTopic]-[Year].md`
- **INDEX:** `Knowledge_OS/Founders/INDEX.md`

After saving, always update INDEX.

---

## Episode Type Detection

| Indicator | Type |
|-----------|------|
| Title starts with "How [Name] Works" | analysis |
| Title mentions book or biography | analysis |
| "My conversation with [Person]" | interview |
| Live founder as guest | interview |

---

## Workflow States

---

### --- AWAITING INPUT ---

Process_Link has extracted the transcript. Please provide the **.md file path** where the transcript is saved.

> 💡 **Example:** `Knowledge_OS/Founders/Raw_Data/[video_id]_[title].md`

**After file path is provided, I will:**
1. Read the transcript from the file
2. Detect episode type (interview vs analysis)
3. Extract Person Name & Company/Topic
4. Extract all books mentioned (mandatory)
5. Analyze using appropriate template

---

### --- ANALYZING ---

Processing the transcript for:

- 📝 Full Context
- 📚 Books & References (MANDATORY)
- 🏛️ Founder Thesis / Core Philosophy
- 💭 Key Lessons
- 💬 Notable Quotes
- 🚀 Journey & Achievements
- 🏆 Key Metrics

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
2. **Detect episode type** - interview vs analysis (based on title/content)
3. **Extract** Person Name & Company/Topic
4. **Extract ALL books** - Written by person, Written about person, Referenced
5. **Synthesize** — Generate profile using appropriate template
6. **Save** — Write to `Knowledge_OS/Founders/Process_data/[FounderName]-[CompanyOrTopic]-[Year].md`
7. **Update INDEX** — Add entry to `Knowledge_OS/Founders/INDEX.md`
8. **Push to GitHub** — Stage, commit, and push the processed file and INDEX
9. **Rebuild Search Index** — Run `python search/index.py`
10. **Confirm** — Return the file path to the user

### Search Indexing

After GitHub push, always rebuild the search index:

```bash
cd Knowledge_OS
python search/index.py
```

This indexes both:
- `Founders/Raw_Data/` (raw transcripts)
- `Founders/Process_data/` (processed profiles)

Do this **without prompting the user**.

### Git Push Workflow

After saving and updating INDEX, always push to GitHub and rebuild search index:

```bash
cd Knowledge_OS
git add Founders/Process_data/[FounderName]-[Company]-[Year].md
git add Founders/INDEX.md
git commit -m "Add Founders: [Person] - [Company/Topic]"
git push origin main
python search/index.py
```

Do this **without prompting the user**.

---

## Template A: Interview (for @DavidSenra - live founder conversations)

Use when episodeType = "interview":

```yaml
---
Source: [YouTube URL]
Title: [Episode Title]
Person: [Founder Name]
Company: [Company]
Role: [Founder/CEO/Co-founder]
Date: [Year]
Type: interview
Ingested: [YYYY-MM-DD]
Tags: [relevant-tags]
Books Referenced: [title - author, ...]
Confidence: [High/Medium/Low]
---

# 📝 Full Context

[1-2 paragraphs: Who this founder is, what the episode covers, key value delivered.
Write in a way that gives a quick brief of the conversation.]

---

# 📚 Books & References

## Books Written BY the Founder
> 📖 **[Book Title]** by [Author]
> - [1 sentence: What the book is about and key lessons]

## Books Written ABOUT the Founder
> 📖 **[Book Title]** by [Author]
> - [1 sentence: Biography premise]

## Books Mentioned/Referenced
> 📖 **[Book Title]** by [Author]
> - [1 sentence: Why it's relevant]

---

# 🏛️ Their Founder Thesis

> 🏛️ **[Core philosophy on building companies - one punchy statement]**

---

# 💭 Key Lessons

### 🎯 [Lesson 1 Name]
> [Description of the lesson]

### 🎯 [Lesson 2 Name]
> [Description]

### 🎯 [Lesson 3 Name]
> [Description]

### 🎯 [Lesson 4 Name]
> [Description]

---

# 💬 Notable Quotes

> 💬 "[Best quote 1]"
> — [Founder Name]

> 💬 "[Best quote 2]"
> — [Founder Name]

---

# 🚀 Journey & Achievements

## Background
> [Brief summary of who they are and their journey]

## Key Milestones
> [Major decisions and stories from the episode]

---

# 🏆 Key Achievements

| Achievement | Details |
|-------------|---------|
| 🏢 **Company** | [Name, founded year] |
| 💰 **Revenue/Value** | [If mentioned] |
| 📈 **Growth** | [If mentioned] |
| 🎯 **Notable** | [Other achievements] |

---

*Source: [Episode Title](YouTube URL)*

*Last Updated: [YYYY-MM-DD]*
```

---

## Template B: Analysis (for @founderspodcast1 - book-based insights)

Use when episodeType = "analysis":

```yaml
---
Source: [YouTube URL]
Title: [Episode Title]
Person: [Person Being Analyzed]
Role: [What they are known for: Founder/Investor/Athlete/Artist/etc.]
Date: [Year]
Type: analysis
Ingested: [YYYY-MM-DD]
Tags: [relevant-tags]
Primary Book: [title - author - brief description]
Confidence: [High/Medium/Low]
---

# 📝 Full Context

[1-2 paragraphs: Who this person is, what the analysis covers.
David Senra's key insights from reading the book.]

---

# 📖 Primary Book Analysis

## Primary Reference
> 📖 **[Book Title]** by [Author]
> - [2-3 sentences: What the book is about, David Senra's key takeaways]

---

# 📚 Additional References

> 📖 **[Book Title]** by [Author]
> - [Brief description - why it's relevant to this person]

> 📖 **[Book Title]** by [Author]
> - [Brief description]

---

# 🏛️ Their Core Philosophy

> 🏛️ **[Key philosophy or mental model from the book]**

---

# 💭 Key Lessons from the Book

### 🎯 [Lesson 1 Name]
> [Lesson drawn from the book content]

### 🎯 [Lesson 2 Name]
> [Lesson]

### 🎯 [Lesson 3 Name]
> [Lesson]

### 🎯 [Lesson 4 Name]
> [Lesson]

---

# 💬 Notable Quotes from the Book

> 💬 "[Quote 1]"
> — [Author], [Book Title]

> 💬 "[Quote 2]"
> — [Author], [Book Title]

---

# 🏆 Key Achievements

| Achievement | Details |
|-------------|---------|
| 🏢 **Role** | [Primary role/company] |
| 📅 **Era** | [Time period if relevant] |
| 🎯 **Notable** | [Major achievement] |
| 📈 **Impact** | [Legacy] |

---

*Source: [Episode Title](YouTube URL)*

*Last Updated: [YYYY-MM-DD]*
```

---

## INDEX Format

```markdown
# Founders INDEX

| Person | Company/Topic | Type | Primary Book | Date Added |
|--------|---------------|------|--------------|------------|
```

**Add new entries in this format:**
```
| Evan Spiegel | Snap Inc. | interview | - | 2026-05-02 |
| Elon Musk | SpaceX/Tesla | analysis | The Book of Elon | 2026-05-02 |
```

---

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| ✅ **High** | Full transcript, clear narrative, books clearly identified |
| ⚠️ **Medium** | Partial transcript, some gaps, books mentioned but not detailed |
| ❌ **Low** | Thin transcript, major gaps, unclear who/what |

---

## Tag Categories

**Episode Type:**
- `interview`
- `analysis`

**Topics:**
- `saas`, `hardware`, `consumer`, `fintech`, `entertainment`, `sports`
- `biography`, `company-building`, `leadership`

---

## Formatting Rules

- **Heavy white space** between sections — use `---` as separators
- **Emojis** on every section header for visual scanning
- **Blockquotes** for quoted advice or key insights
- **Bold** key terms and important numbers
- **Books are MANDATORY** - Every profile must include Books section
- Maximum 4-5 key lessons
- Pull 4-6 of the best quotes
- For interviews: Include both "Written BY" and "Written ABOUT" books if available
- For analysis: Always highlight the primary book being discussed

---

*Last Updated: 2026-05-02*