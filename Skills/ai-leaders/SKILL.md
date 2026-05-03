---
name: ai-leaders
description: Transforms podcast, video, and interview transcripts into deep-dive intelligence profiles from top AI leaders. Every profile captures the person's AI thesis, key mental models, contrarian views, and what they're building — stored permanently in the vault. Triggers: "AI Leaders," "Add [Person] interview," or mention a specific person with a transcript.
---

# AI Leaders

Transforms podcast, video, and interview transcripts into deep-dive intelligence profiles from top AI leaders. Every profile captures the person's AI thesis, key mental models, contrarian views, and what they're building — stored permanently in the vault.

## Storage Location

- **Input:** `Knowledge_OS/AI_Leaders/Raw_Data/[filename].md` (from Process_Link)
- **Output:** `Knowledge_OS/AI_Leaders/Process_data/[Date]-[Person]-[Topic].md`
- **INDEX:** `Knowledge_OS/AI_Leaders/INDEX.md`

After saving, always update INDEX.

---

## Workflow States

---

### --- AWAITING INPUT ---

Process_Link has extracted the transcript. Please provide the **.md file path** where the transcript is saved.

> 💡 **Example:** `Knowledge_OS/AI_Leaders/Raw_Data/[video_id]_[title].md`

**After file path is provided, I will:**
1. Read the transcript from the file
2. Extract Person Name & Topic
3. Analyze using the template

---

### --- ANALYZING ---

Processing the transcript for:

- 📝 Full Context
- 🏛️ Their AI Thesis
- 💭 Key Mental Models
- 💬 Notable Quotes
- 🚩 Contrarian Views
- 🛠️ What They're Building
- 👁️ Their Blind Spots
- 💎 Naval-Style Maxim

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
2. **Extract** Person Name & Topic from content
3. **Synthesize** — Generate the full profile using the template
4. **Save** — Write to `Knowledge_OS/AI_Leaders/Process_data/[Date]-[Person]-[Topic].md`
5. **Update INDEX** — Add entry to `Knowledge_OS/AI_Leaders/INDEX.md`
6. **Push to GitHub** — Stage, commit, and push the processed file and INDEX
7. **Rebuild Search Index** — Run `python search/index.py` to index both Raw and Processed files
8. **Confirm** — Return the file path to the user

### Search Indexing

After GitHub push, always rebuild the search index:

```bash
cd Knowledge_OS
python search/index.py
```

This indexes both:
- `AI_Leaders/Raw_Data/` (raw transcripts)
- `AI_Leaders/Process_data/` (processed profiles)

Do this **without prompting the user**.

### Git Push Workflow

After saving and updating INDEX, always push to GitHub and rebuild search index:

```bash
cd Knowledge_OS
git add AI_Leaders/Process_data/[Date]-[Person]-[Topic].md
git add AI_Leaders/INDEX.md
git commit -m "Add AI Leaders: [Person] - [Topic]"
git push origin main
python search/index.py
```

Do this **without prompting the user**.

---

## The Full Template Structure

Copy and use this exact format for every entry:

```yaml
---
Source: [Podcast/Video Title with URL]
Person: [Full Name]
Role: [Their Role]
Company: [Their Company]
Date: [Year of Recording]
Category: [Topic Tags]
Ingested: [YYYY-MM-DD]
Tags: [relevant-tags]
---

# 📝 Full Context

[1-2 paragraphs summarizing the ENTIRE interview. Who the person is, what 
they discuss, their main argument, key moments, and overall conclusion.
Write in first-person narrative so you can read it like a quick brief.]

---

# 🏛️ Their AI Thesis

> 🏛️ [One-paragraph thesis capturing the person's core view on AI, technology, or their field]

---

# 💭 Key Mental Models

---

### [Emoji] Model 1: [Name]

> [Emoji] **The Concept:** [What it is]

> [Emoji] **The Truth:** [Why it matters]

> ⚡ **Maxim:** *"[Punchy one-liner]"*

---

### [Emoji] Model 2: [Name]
...

### [Emoji] Model 3: [Name]
...

### [Emoji] Model 4: [Name]
...

### [Emoji] Model 5: [Name]
...

---

# 💬 Notable Quotes

---

> [Emoji] "[Quote 1]"
> — [Speaker], [Source]

---

> [Emoji] "[Quote 2]"
> — [Speaker], [Source]

---

# 🚩 Contrarian Views

---

> ⚡ **[Bold statement of their most contrarian view]**

[2-3 sentences explaining why this challenges conventional wisdom]

---

# 🛠️ What They're Building / Focused On

---

## [Emoji] [Category Name]

> [Emoji] **[Key initiative 1]:** [Description]

> [Emoji] **[Key initiative 2]:** [Description]

> [Emoji] **[Key initiative 3]:** [Description]

---

## [Emoji] [Second Category]

> [Emoji] [Item 1]

> [Emoji] [Item 2]

---

# 👁️ Their Blind Spot

---

> 👁️ **[Blind spot 1]:** [Explanation]

---

> 👁️ **[Blind spot 2]:** [Explanation]

---

# 💎 Naval-Style Maxim

---

> 💎 *"[One punchy, quotable maxim that captures their worldview]"*

---

# 🏷️ Content Connections

---

> 🏷️ **Related Knowledge Asset:** [Other relevant file in knowledge-base]

> 🏷️ **Mental Model for LinkedIn:** [A hook angle for content repurposing]

> 🏷️ **Contrarian Angle:** [A second hook angle]

---

## 💎 Maxim Collection for Content

> 1💎 *"[Maxim 1]"*

> 2💎 *"[Maxim 2]"*

> 3💎 *"[Maxim 3]"*

> 4💎 *"[Maxim 4]"*

---

*Last Updated: [YYYY-MM-DD]*

---

## INDEX Format

```markdown
# AI Leaders INDEX

| Person | Topic | Date Added |
|--------|-------|------------|
```

**Add new entries in this format:**
```
| Sam Altman | AI Futures | 2026-05-02 |
```

---

## 💡 Emoji Style Guide

Use **colorful emojis** to break up monotony and enhance readability. Each section and key element should have an emoji prefix.

### Mental Model Emojis
| Model Type | Emoji |
|------------|-------|
| Strategy/Concept | 🧠 |
| Process/Loop | 🔄 |
| Discovery | 💡 |
| Analysis | 📊 |
| Action/Force | 💪 |
| Insight | 🪄 |
| Discipline | 🎯 |
| System | 🏗️ |
| Human Element | 🫀 |
| Constraint | 🛑 |
| Chaos | 🌪️ |
| Balance | ⚖️ |
| Bet/Gamble | 🎰 |
| Team | 🦊 |

### Quote Emojis
| Quote Type | Emoji |
|------------|-------|
| General | 💬 |
| Data/Metrics | 📈 |
| Growth | 🚀 |
| Philosophy | 🧭 |
| Quote from other | 👤 |
| Customer | 🧑‍💼 |
| Warning | ⚠️ |
| Success | 🏆 |
| Product | 🏃 |
| Humor | 😂 |
| Time | ⏰ |
| Education | 📚 |
| Storytelling | 📖 |

### Section Emojis
| Section | Emoji |
|---------|-------|
| Full Context | 📝 |
| AI Thesis | 🏛️ |
| Mental Models | 💭 |
| Notable Quotes | 💬 |
| Contrarian Views | 🚩 |
| What They're Building | 🛠️ |
| Blind Spot | 👁️ |
| Naval-Style Maxim | 💎 |
| Content Connections | 🏷️ |
| Maxim Collection | 💎 |

### Item Emojis
| Item Type | Emoji |
|-----------|-------|
| Process | ⚙️ |
| Structure | 🏗️ |
| Initiative | 🚀 |
| Product | 🏃 |
| Win | ✅ |
| Warning/Tradeoff | ⚠️ |
| Speed | ⚡ |
| Philosophy | 🧭 |
| Talent | 🌟 |
| Role | 🎭 |
| Layer | 🧱 |

### Number Emojis for Lists
- 1💎 2💎 3💎 4💎 5💎 6💎 7💎 8💎 9💎 10💎

---

## Formatting Rules

- **Heavy white space** between sections — use `---` as separators
- **Colorful emojis** on every section header and key element
- Use `---` between major sections
- **Bold** the contrarian views and key truths
- One insight per bullet point
- Max 5 mental models
- Pull 5-8 of the best quotes
- Naval-style maxims should be short, punchy, and quotable
- Put quotes in blockquote format with emoji prefix
- Each mental model should have its own emoji that fits its theme

---

## Example Output (from Amol Aharon entry)

```markdown
# 💭 Model 1: Success Disasters

> 🧠 **The Concept:** When growth happens so fast that systems break...

> 💡 **The Truth:** Green charts everywhere while the team is emotionally exhausted...

> ⚡ **Maxim:** *"Linear charts are just not cool. Everything is log linear."*
```

---

> ⚠️ **Maintenance Note:** After ANY edits to this skill file, immediately stage, commit, and push changes:
> ```bash
> git add Skills/ai-leaders/SKILL.md
> git commit -m "Update ai-leaders skill"
> git push
> ```

*Last Updated: 2026-04-17*