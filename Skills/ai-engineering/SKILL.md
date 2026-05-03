---
name: ai-engineering
description: This skill should be used when the user wants to "analyze AI engineering content", "process AI dev video", "extract frameworks from AI tutorial", "add AI workflow transcript", or provides a YouTube link about AI development, agentic workflows, or automation patterns. Transforms technical videos into structured reference profiles with frameworks, step-by-step guides, books, and implementation details.
metadata:
  version: 1.0.0
---

# AI_Engineering

⚠️ **This skill is AUTOMATICALLY TRIGGERED by Process_Link**

> **DO NOT run this skill manually.** Always use Process_Link first:
> ```
> Process_Link <YouTube_URL>
> → Select: AI_Engineering folder
> ```
>
> Process_Link will:
> 1. Extract transcript → save to Raw_Data
> 2. Auto-trigger this skill
> 3. This skill creates profile in Process_data

---

Transforms YouTube videos about AI development, agentic workflows, and automation into structured technical knowledge profiles. Every profile captures frameworks, step-by-step implementations, books, tools, and concepts you can reference when building your own AI applications.

---

## Storage Location

`Knowledge_OS/AI_Engineering/Process_data/[FrameworkOrConcept]-YYYY.md`

- **Location-specific INDEX:** Always update `Knowledge_OS/AI_Engineering/INDEX.md`
- **GitHub:** After saving, push to GitHub and rebuild search index:
  ```bash
  git add Knowledge_OS/AI_Engineering/Process_data/[filename].md Knowledge_OS/AI_Engineering/INDEX.md
  git commit -m "Add AI Engineering: [Framework/Concept]"
  git push origin main
  python search/index.py
  ```

---

## Workflow States

⚠️ **This skill is AUTO-TRIGGERED by Process_Link**

> Do NOT run this skill manually. Use Process_Link instead:
> ```
> Process_Link <YouTube_URL>
> Select: AI_Engineering
> ```

---

### --- STARTED (Auto-triggered from Process_Link) ---

✅ Raw transcript found in Raw_Data folder

Processing the transcript for:

- 📝 Executive Summary
- 🏗️ Core Framework / Concept
- 📚 Step-by-Step Implementation
- 🛠️ Tools & Technologies
- 📖 Books & Resources
- 💡 Key Insights

---

### --- ANALYZING ---

Processing the transcript for:

- 📝 Executive Summary
- 🏗️ Core Framework / Concept
- 📚 Step-by-Step Implementation
- 🛠️ Tools & Technologies
- 📖 Books & Resources
- 💡 Key Insights

*Please wait...*

---

### --- COMPLETE --- 

✅ **Transcript processed from:** Raw_Data folder
✅ **Profile saved to:** `Process_data/[filename].md`
✅ **INDEX updated**
✅ **Pushed to GitHub**
✅ **Search index rebuilt**

---

## The Analysis Workflow

⚠️ **IMPORTANT: This skill is triggered AUTOMATICALLY by Process_Link**

> Do NOT run this skill directly. Always use Process_Link first:
> ```
> Process_Link <YouTube_URL>
> → Select: AI_Engineering
> → Transcript saved to Raw_Data
> → ai-engineering skill auto-triggers
> ```

When triggered by Process_Link, the raw transcript is already in Raw_Data. The workflow:

1. **Validate Raw Transcript** — Check that transcript exists in `Knowledge_OS/AI_Engineering/Raw_Data/`
   - If NOT found: ❌ Error — "Please run Process_Link first to extract transcript to Raw_Data"
   - If found: ✅ Continue with step 2
2. **Read Raw Transcript** — Load from Raw_Data folder
3. **Detect Category** — Determine primary category (agentic-ai / vibe-coding / automation / llm-patterns / tool-use)
4. **Determine Title** — Extract framework or concept name for filename
5. **Analyze** — Generate profile using the template below
6. **Save** — Write to `Knowledge_OS/AI_Engineering/Process_data/[FrameworkOrConcept]-YYYY.md`
7. **Update INDEX** — Add entry to `Knowledge_OS/AI_Engineering/INDEX.md`
8. **Push to GitHub** — Stage, commit, and push
9. **Rebuild Search Index** — Run `python search/index.py`
10. **Confirm** — Return the file path to the user

---

## Category Detection

| Keywords in Transcript | Category |
|------------------------|----------|
| agent, multi-agent, autonomous, self-driving | agentic-ai |
| vibe, bolt, cursor, Lovable, breeze | vibe-coding |
| automation, workflow, n8n, zapier, production | automation |
| LLM, prompt, fine-tune, context window, token | llm-patterns |
| MCP, function calling, tools, API integration | tool-use |

---

## The Full Template Structure

```yaml
---
Source: [YouTube URL]
Title: [Video Title]
Creator: [Channel Name]
Date: [Year]
Framework: [Primary Framework if applicable]
Category: [agentic-ai / vibe-coding / automation / llm-patterns / tool-use]
Ingested: [YYYY-MM-DD]
Tags: [framework-name, pattern-type, use-case]
Confidence: [High/Medium/Low]
---

# 📝 Executive Summary

[2-3 paragraphs. What is this video about? What problem does it solve?
Why should an AI developer care? Write as a quick brief you can scan in 30 seconds.]

---

# 🏗️ Core Framework / Concept

## What It Is

> 🏗️ **[One-line definition]**

[2-3 sentences explaining the concept in simple terms]

## When To Use

> ✅ **Use this when:** [Specific use case]

> ❌ **Don't use when:** [Contraindications]

## Key Components

> ⚙️ **[Component 1]:** [Brief description]

> ⚙️ **[Component 2]:** [Brief description]

---

# 📚 Step-by-Step Implementation

## Step 1: [Step Name]

> 🔹 **What to do:** [Clear instruction]

> 💡 **Why:** [One sentence on the reasoning]

```
[Code example if applicable]
```

## Step 2: [Step Name]

> 🔹 **What to do:** [Clear instruction]

```
[Code example]
```

## Step 3: [Step Name]

> 🔹 **What to do:** [Clear instruction]

```
[Code example]
```

## Step 4: [Step Name]

> 🔹 **What to do:** [Clear instruction]

---

# 🛠️ Tools & Technologies

| Tool | Purpose | When Used |
|------|---------|-----------|
| [Tool 1] | [What it does] | [Use case] |
| [Tool 2] | [What it does] | [Use case] |

---

# 💰 Cost & Resources

> 💵 **API Costs:** [If mentioned - pricing model, typical costs]
> ⏱️ **Time to Implement:** [Hours/days for basic setup]
> 🧠 **Skill Level:** [Beginner / Intermediate / Advanced]

---

# 📖 Books & Resources

> 📚 **[Book Title]** by [Author]
> - Why relevant: [Brief]
> - Best for: [Use case]

> 🔗 **[Resource/Article/Tool]:** [Link if available]

---

# 💡 Key Insights (3-5 bullet points)

> 💡 **[Insight 1]:** [The main takeaway]

> 💡 **[Insight 2]:** [Another important point]

> 💡 **[Insight 3]:** [Critical consideration]

---

# 💬 Notable Quotes

> 💬 "[Quote about implementation]"
> — [Speaker]

---

# 🔄 Comparison (If Applicable)

| This Approach | vs | Alternative | Why Choose |
|---------------|---|-------------|------------|
| [Approach A] | | [Approach B] | [Reason] |

---

# 🎯 Action Items for Your Projects

> 🚀 **[Action 1]:** Try this in [your project context]

> 🚀 **[Action 2]:** Replace [current approach] with [new approach]

> 🚀 **[Action 3]:** Research [related topic]

---

# 🔗 Related Concepts

> 🔗 **[Related Video/Concept]:** [Brief connection]

---

*Source: [Video Title](YouTube URL)*

*Last Updated: [YYYY-MM-DD]*
```

---

## What to Extract

For every transcript, systematically capture:

| Category | What to Capture |
|----------|----------------|
| **Frameworks** | Name, version, purpose, key features |
| **Step-by-Step** | Numbered steps, code snippets, configs |
| **Books** | Title, author, why recommended |
| **New Concepts** | Definitions, terminology explained |
| **Tools** | Names, use cases, alternatives |
| **Cost/Pricing** | API costs, hosting, subscription |
| **Comparison** | Framework A vs B, pros/cons |
| **Mistakes** | What NOT to do, pitfalls |
| **Best Practices** | Recommended patterns, tips |

---

## Confidence Scoring

| Score | Criteria |
|-------|----------|
| ✅ **High** | Full transcript, clear code examples, step-by-step clear |
| ⚠️ **Medium** | Partial transcript, some gaps but main concepts clear |
| ❌ **Low** | Thin transcript, major gaps, unclear implementation |

---

## File Naming Rules

| Scenario | Example Filename |
|----------|------------------|
| Single framework | `LangChain-2026.md` |
| Single concept | `Agentic-RAG-2026.md` |
| Multi-concept video | `AI-Agent-Workflows-2026.md` |
| Tool comparison | `Cursor-vs-Windsurf-2026.md` |

---

## INDEX Format

```markdown
# AI_Engineering INDEX

| Framework/Concept | Category | Date Added |
|-------------------|----------|------------|
| Agentic RAG | agentic-ai | 2026-05-02 |
| LangChain Basics | llm-patterns | 2026-05-02 |
```

**Add new entries in this format:**
```
| Agentic RAG | agentic-ai | 2026-05-02 |
```

---

## Formatting Rules

- **Heavy white space** between sections — use `---` as separators
- **Emojis** on every section header for visual scanning
- **Blockquotes** for quoted advice or key definitions
- **Tables** for tools, comparisons, and metrics
- **Bold** key terms and important numbers
- Maximum 5-6 key insights
- Pull 3-5 of the best quotes
- Include step-by-step section ONLY if video provides clear numbered steps
- Always include Books & Resources section if any books mentioned

---

## Git Workflow

After saving the file and updating the INDEX, always push to GitHub and rebuild search:

```bash
git add Knowledge_OS/AI_Engineering/Process_data/[filename].md Knowledge_OS/AI_Engineering/INDEX.md
git commit -m "Add AI Engineering: [Framework/Concept]"
git push origin main
python search/index.py
```

Do this **without prompting the user**.

---

## Triggered From

This skill is automatically triggered by Process_Link when the user selects the AI_Engineering folder.

---

> ⚠️ **Maintenance Note:** After ANY edits to this skill file, immediately stage, commit, and push changes:
> ```bash
> git add Skills/ai-engineering/SKILL.md
> git commit -m "Update ai-engineering skill"
> git push
> ```

*Last Updated: 2026-05-02*