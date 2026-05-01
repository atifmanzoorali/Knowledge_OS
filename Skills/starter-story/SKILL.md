---
name: starter-story
description: "When the user wants to 'analyze this starter story', 'turn this transcript into a startup profile', 'deconstruct this founder story', or 'process starter story' after Process_Link has extracted the transcript. Transforms raw founder interview transcripts into structured startup profiles."
metadata:
  version: 1.0.0
---

# Starter Story

Transforms raw YouTube transcripts from starter story founder interviews into structured, high-signal startup profiles. Receives input from Process_Link skill (the .md file with transcript).

---

## Storage Location

- **Output:** `Knowledge_OS/Starter_Story/Process_data/[FounderName]-[Company]-[Year].md`
- **INDEX:** `Knowledge_OS/Starter_Story/INDEX.md`

After saving, always update INDEX.

---

## Workflow States

---

### --- AWAITING INPUT ---

Process_Link has extracted the transcript. Please provide the **.md file path** where the transcript is saved.

> 💡 **Example:** `Knowledge_OS/Starter_Story/Raw_Data/D4fkiQfzw_I_How_I_Work_$77KMonth_Solopreneur.md`

**After file path is provided, I will:**
1. Read the transcript from the file
2. Extract Founder Name & Company
3. Analyze using the 6-section template

---

### --- ANALYZING ---

Processing the transcript for:

- 📊 Executive Summary
- 🚀 The Product & Value Prop
- 🛠️ Tech Stack & Process
- 🎯 Distribution Playbook
- 🧠 Frameworks & Lessons
- 📈 Key Metrics

*Please wait...*

---

### --- COMPLETE ---

✅ **Story saved to:** `[file-path]`
✅ **INDEX updated**

---

## The Analysis Workflow

When a .md file path is provided:

1. **Read** the .md file and extract transcript
2. **Extract** Founder Name & Company from content
3. **Analyze** — Generate the 6-section report using the template below
4. **Save** — Write to `Knowledge_OS/Starter_Story/[FounderName]-[Company]-[Year].md`
5. **Update INDEX** — Add entry to `Knowledge_OS/Starter_Story/INDEX.md`
6. **Confirm** — Return the file path to the user

---

## The Full Template Structure

```yaml
---
Source: [YouTube URL]
Title: [Video Title]
Founder: [Name]
Company: [Company]
Date: [Year]
Category: [SaaS / E-commerce / Service / Agency / etc.]
Ingested: [YYYY-MM-DD]
Tags: [relevant-tags]
Confidence: [High / Medium / Low]
---

# 🚀 [Founder Name]: [Company]

**Founder:** [Name] | **Company:** [Company] | **Revenue:** [MRR/ARR if mentioned]

---

# 📊 Executive Summary

[1-2 professional paragraphs summarizing the story. Focus on the founder's "Why," the core mission, and the overall scale of the achievement.]

---

# 🚀 The Product & Value Prop

---

## What Was Built

> 🏗️ **[Core functionality description]**

---

## The Gap

> 💡 **[Specific pain point or market gap this filled]**

---

## Unfair Advantage

> 🏆 **[What makes this hard to clone?]**

---

# 🛠️ Tech Stack & Process

---

## The Tools

> 🔧 **Languages/Frameworks:** [List mentioned]
> 🧩 **Platforms:** [List mentioned]
> 💳 **Payments:** [List mentioned]
> 📊 **Analytics:** [List mentioned]

---

## Build Process

> ⏱️ **Time to MVP:** [Duration mentioned]
> 👥 **Team:** [Solo / Team of N]
> 🎯 **Build Style:** [Detailed description]

---

# 🎯 Distribution Playbook

---

## First 100 Users

> 🎣 **[The "Unscalable" tactics that worked]**

---

## Scaling Engine

> 📈 **Primary Channel:** [SEO / Viral / Paid / Content / etc.]
> 📊 **Secondary Channels:** [Other mentioned channels]

---

# 🧠 Frameworks & Lessons

---

## Mental Models

> 🧩 **[Philosophy or approach mentioned]**

---

## The Gold

> ✨ **"The single most important piece of advice for other founders from this story."**

---

# 📈 Key Metrics

---

| Metric | Value |
|--------|-------|
| 💰 **Revenue** | [MRR / ARR if mentioned] |
| 👥 **Team Size** | [Number of people] |
| ⏰ **Time to Profit** | [Duration] |
| 📅 **Founded** | [Year if mentioned] |
| 🔥 **Growth Rate** | [Monthly / yearly growth if mentioned] |

---

*Source: [YouTube Video Title](YouTube URL)*

*Last Updated: [YYYY-MM-DD]*
```

---

## INDEX Format

```markdown
# Starter Story INDEX

| Founder | Company | Year | Date Added |
|---------|---------|------|----------|
```

**Add new entries in this format:**
```
| Marc Lou | - | 2026 | 2026-05-02 |
```

---

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| ✅ **High** | Full transcript, timestamps, revenue numbers, clear narrative |
| ⚠️ **Medium** | Partial transcript, some gaps, key metrics missing |
| ❌ **Low** | Thin transcript, major gaps, incomplete story |

---

## Formatting Rules

- **Heavy white space** between sections — use `---` as separators
- **Emojis** on every section header for visual scanning
- **Blockquotes** for quoted advice or key insights
- **Tables** for metrics and tool comparisons
- **Bold** key terms and important numbers
- Maximum 5 mental models or frameworks
- Pull 3-5 of the best founder quotes

*Last Updated: 2026-05-02*