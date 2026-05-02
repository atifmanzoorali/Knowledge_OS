---
name: my-first-million
description: "When the user wants to 'process my first million', 'analyze this My First Million episode', 'add My First Million transcript', 'My First Million interview', or 'process MFM episode'. Transforms raw My First Million podcast transcripts into structured business insight profiles."
---

# My First Million

Transforms raw YouTube transcripts from My First Million podcast into structured business insight profiles. My First Million is hosted by Sam Parr (founder of The Hustle) and Shaan Puri (serial entrepreneur). The podcast features three formats: brainstorm episodes (business ideas), guest interviews (founder/investor deep dives), and business breakdowns (company case studies).

---

## Storage Location

- **Input:** `Knowledge_OS/My_First_Million/Raw_Data/[filename].md` (from Process_Link)
- **Output:** `Knowledge_OS/My_First_Million/Process_data/[GuestOrTopic]-[Date].md`
- **INDEX:** `Knowledge_OS/My_First_Million/INDEX.md`

After saving, always update INDEX.

---

## Workflow States

---

### --- AWAITING INPUT ---

Process_Link has extracted the transcript. Please provide the **.md file path** where the transcript is saved.

> 💡 **Example:** `Knowledge_OS/My_First_Million/Raw_Data/[video_id]_[title].md`

**After file path is provided, I will:**
1. Read the transcript from the file
2. Identify episode type (brainstorm/interview/breakdown)
3. Extract Guest Name or Topic
4. Analyze using the unified template

---

### --- ANALYZING ---

Processing the transcript for:

- 📊 Executive Summary
- 💡 Key Insights
- 🏢 Business Ideas / Opportunities
- 👤 Guest Background (if interview)
- 🚀 Lessons & Frameworks
- 💰 Investment Insights
- ⚡ Contrarian Views
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
2. **Detect episode type** - Determine if brainstorm/interview/breakdown based on content
3. **Extract** Guest Name or Topic from content
4. **Synthesize** — Generate the profile using the unified template (adapts based on episode type)
5. **Save** — Write to `Knowledge_OS/My_First_Million/Process_data/[GuestOrTopic]-[Date].md`
6. **Update INDEX** — Add entry to `Knowledge_OS/My_First_Million/INDEX.md`
7. **Push to GitHub** — Stage, commit, and push the processed file and INDEX
8. **Rebuild Search Index** — Run `python search/index.py` to index both Raw and Processed files
9. **Confirm** — Return the file path to the user

### Search Indexing

After GitHub push, always rebuild the search index:

```bash
cd Knowledge_OS
python search/index.py
```

This indexes both:
- `My_First_Million/Raw_Data/` (raw transcripts)
- `My_First_Million/Process_data/` (processed profiles)

Do this **without prompting the user**.

### Git Push Workflow

After saving and updating INDEX, always push to GitHub and rebuild search index:

```bash
cd Knowledge_OS
git add My_First_Million/Process_data/[filename].md
git add My_First_Million/INDEX.md
git commit -m "Add My First Million: [Guest/Topic]"
git push origin main
python search/index.py
```

Do this **without prompting the user**.

---

## Unified Template Structure

The template adapts based on episode type. Use only relevant sections for each episode:

### For All Episodes:

```yaml
---
Source: [YouTube URL]
Title: [Episode Title]
Episode: [Ep. #]
Host: Sam Parr & Shaan Puri
Guest: [Name if interview, else none]
Date: [Year]
Category: [brainstorm/interview/breakdown]
Ingested: [YYYY-MM-DD]
Tags: [relevant-tags]
Confidence: [High/Medium/Low]
---

# 📊 Executive Summary

[1-2 paragraphs summarizing what this episode covers, main topic/guest, and key value delivered. Write in a way that gives a quick brief of the episode.]

---

# 💡 Key Insights

[3-5 bullet points of the most valuable takeaways from this episode. Focus on actionable insights.]

---

# 💬 Notable Quotes

> 💬 "[Best quote 1]"
> — [Speaker]

> 💬 "[Best quote 2]"
> — [Speaker]

> 💬 "[Best quote 3]"
> — [Speaker]

---

# 📚 Resources & References

> 📚 **Books:** [List all books mentioned with title and author]
> 🛠️ **Tools:** [Tools/software mentioned]
> 📰 **Newsletters:** [Newsletters mentioned]
> 🎙️ **Podcasts:** [Other podcasts mentioned]
> 🏛️ **Communities:** [Communities/courses mentioned]

---

# 🏷️ Content Connections

> 🏷️ **For LinkedIn:** [A hook angle for content repurposing]
> 🏷️ **Contrarian Angle:** [Another hook angle]

---

*Source: [Episode Title](YouTube URL)*

*Last Updated: [YYYY-MM-DD]*
```

### For Brainstorm Episodes (add these sections):

```markdown
# 🏢 Business Ideas / Opportunities

> 💡 **[Idea 1]:** [Description of the business opportunity discussed]

> 💡 **[Idea 2]:** [Description]

> 💡 **[Idea 3]:** [Description]

---

# 🎯 Why Now

> ⏰ **[Timing factor 1]:** [Why this opportunity exists right now]

---

# 💰 Business Model

> 💵 **[Model]:** [How this business could make money]
```

### For Interview Episodes (add these sections):

```markdown
# 👤 Guest Background

> 🎯 **Name:** [Guest Name]
> 🏢 **Company:** [Their company]
> 💰 **Exit/Value:** [If mentioned - e.g., "$100M exit"]
> 📖 **Background:** [Brief summary of who they are and their journey]

---

# 🚀 Lessons & Frameworks

> 🧠 **[Lesson 1 - Name]:** [Description of the lesson or framework]

> 🧠 **[Lesson 2 - Name]:** [Description]

> 🧠 **[Lesson 3 - Name]:** [Description]

---

# 💼 Startup Advice

> 🏃 **[Advice 1]:** [Specific guidance for founders]

> 🏃 **[Advice 2]:** [Specific guidance]

---

# 💰 Investment Insights

> 📈 **[Insight 1]:** [Any investing advice or portfolio tips shared]

---

# ⚡ Contrarian Views

> 🚩 **[Bold take]:** [Their contrarian view that challenges conventional wisdom]

> 🚩 **[Second view]:** [Another contrarian take]
```

### For Business Breakdown Episodes (add these sections):

```markdown
# 🏢 Company Profile

> 🏢 **Company:** [Company name]
> 💰 **Revenue/Value:** [If mentioned]
> 📅 **Founded:** [Year]
> 👤 **Founder:** [Founder name]

---

# 📈 Business Model

> 💵 **[How they make money]:** [Description of revenue model]

---

# 🚀 Key Growth Tactics

> 📈 **[Tactic 1]:** [Specific growth strategy]

> 📈 **[Tactic 2]:** [Specific growth strategy]

---

# 🧠 Lessons for Founders

> 🏃 **[Lesson 1]:** [Actionable takeaway]

> 🏃 **[Lesson 2]:** [Actionable takeaway]
```

---

## Episode Type Detection

When processing a transcript, detect the episode type:

| Indicator | Episode Type |
|-----------|--------------|
| No guest, two hosts discussing ideas | brainstorm |
| Single guest being interviewed | interview |
| Discussion of specific company/brand | breakdown |

Check the title and content to determine:
- Brainstorm: "idea", "opportunity", "hidden"
- Interview: Guest name in title, "interview", "conversation"
- Breakdown: Company name in title, "analysis", "breakdown"

---

## INDEX Format

```markdown
# My First Million INDEX

| Episode | Guest/Topic | Category | Date Added |
|---------|-------------|----------|------------|
```

**Add new entries in this format:**
```
| Ep. 813 | Jon McNeill - Tesla Hypergrowth | interview | 2026-05-02 |
| Ep. 819 | Hidden Opportunity | brainstorm | 2026-05-02 |
```

---

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| ✅ **High** | Full transcript, timestamps, clear narrative, guest/topic clearly identified |
| ⚠️ **Medium** | Partial transcript, some gaps, topic identifiable |
| ❌ **Low** | Thin transcript, major gaps, unclear episode type |

---

## Tag Categories

Add relevant tags based on content:

**Episode Type:**
- `brainstorm`
- `interview`
- `breakdown`

**Topics:**
- `ai`, `investing`, `startup`, `side-hustle`, `solopreneur`
- `business-ideas`, `growth`, `sales`, `marketing`
- `real-estate`, `saas`, `ecommerce`, `content`

---

## Formatting Rules

- **Heavy white space** between sections — use `---` as separators
- **Emojis** on every section header for visual scanning
- **Blockquotes** for quoted advice or key insights
- **Bold** key terms and important numbers
- Maximum 5-7 key insights or lessons
- Pull 5-8 of the best quotes
- Always include Resources section with books (user requirement)

---

*Last Updated: 2026-05-02*