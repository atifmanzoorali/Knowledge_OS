---
Source: https://www.youtube.com/watch?v=-QFHIoCo-Ko
Title: "Full Walkthrough: Workflow for AI Coding — Matt Pocock"
Creator: Matt Pocock
Date: 2026
Framework: Claude Code, Ralph Loop, Tracer Bullets, TDD, Kanban Board
Category: agentic-ai
Ingested: 2026-05-02
Tags: llm-workflow, prompt-engineering, software-architecture, agentic-workflows, afk-agents, tdd, vertical-slices
Confidence: High
---

# 📝 Executive Summary

This is a live workshop from Matt Pocock covering how to effectively work with LLMs for software engineering. The core thesis: AI is a new paradigm, but **software engineering fundamentals** — small tasks, alignment, vertical slices, test-driven development — work better than ever with AI. Matt demonstrates a complete workflow from idea → grilling session → PRD → Kanban board → AFK implementation using Claude Code. Key insight: "Bad codebases make bad agents" — the quality of your feedback loops determines the quality of AI output.

---

# 🏗️ Core Framework: LLM Constraints

## What It Is

> 🏗️ **Two fundamental constraints that shape all AI engineering work:**

1. **Smart Zone vs Dumb Zone**: LLMs work best in the first ~100K tokens. Beyond that, they "get dumber" — attention relationships scale quadratically. Whether using 200K or 1M context window, performance degrades around 100K tokens.

2. **Memento Effect**: LLMs forget. Every new session starts from the system prompt — no persistent context unless explicitly passed in.

## When To Use

> ✅ **Use this when:** Building any feature with AI — size tasks to fit in the smart zone

> ❌ **Don't use when:** Passing massive context expecting perfect reasoning — it won't work

## Key Components

> ⚙️ **Token tracking**: Always monitor token usage in every coding session (Matt shows a status line in Claude Code)

> ⚙️ **Compacting vs Clearing**: Compacting squeezes conversation into a summary; clearing resets to system prompt. Matt prefers clearing because "state is always the same" — more predictable.

> ⚙️ **Sub-agents**: Delegating tasks to separate LLM contexts with isolated windows, then summarizing back to parent agent. Example from workshop: sub-agent burned 93.7K tokens while parent context stayed small (~25K).

---

# 📚 Step-by-Step Implementation

## Step 1: Grilling Session (Alignment Phase) — Human in the Loop

> 🔹 **What to do:** Use the "grill me" skill to relentlessly question every aspect of the plan before starting

> 💡 **Why:** Reach "shared understanding" with the AI — the design concept. This is more valuable than a written plan.

```
Invoke: /grill-me with client brief
Answer questions one at a time
Let AI ask 40-100 questions
Save the conversation as an asset
```

**Example from workshop:** Sarah Chen wants gamification in a course platform. The grilling session uncovered: points economy, retroactive backfill, streak mechanics, level progression curves, UI location.

**Key insight**: Frederick P. Brooks' "design concept" — the shared idea between team members that can't be fully documented — applies to AI collaboration.

## Step 2: Create PRD (Destination Document)

> 🔹 **What to do:** Summarize the design concept into a Product Requirements Document

> 💡 **Why:** Documents the destination — what "done" looks like. Matt doesn't read PRDs closely because summarization is what LLMs do well.

**PRD sections needed:**
- Problem statement
- Solution description
- User stories
- Implementation decisions
- Testing decisions
- **Out of scope** (critical for defining done)

## Step 3: Kanban Board with Vertical Slices

> 🔹 **What to do:** Convert PRD into issues using tracer bullets (vertical slices), not horizontal phases

> 💡 **Why:** Horizontal coding (all database first, then all API, then all frontend) delays feedback until phase 3. Vertical slices give feedback after each phase.

**Vertical slice example:**
- ❌ Horizontal: 1) Schema, 2) Service, 3) API, 4) Frontend
- ✅ Vertical: "Award points for lesson completion visible on dashboard" — crosses all layers, visible immediately

**Kanban structure:**
- Each issue = independently grabbable task
- Blocking relationships between issues
- Enables parallelization: multiple agents can work on unblocked issues simultaneously

## Step 4: AFK Implementation (Ralph Loop) — Human Out of the Loop

> 🔹 **What to do:** Run an iterative loop where AI picks the next task, implements it, runs feedback loops, then picks the next

> 💡 **Why:** Human leaves the loop after planning. AI works "AFK" (away from keyboard) on the backlog.

```
For each task:
1. Explore codebase
2. Use TDD (Red → Green → Refactor)
3. Run feedback loops (tests, type check)
4. Create commit with summary
5. Pick next unblocked task
```

**Matt's Ralph Loop priorities:**
1. Critical bug fixes
2. Development infrastructure
3. Tracer bullets (vertical slices)
4. Polish / quick wins
5. Refactors

## Step 5: QA and Code Review — Back to Human in the Loop

> 🔹 **What to do:** Review in a fresh context (clear first) — not in the same session that wrote the code

> 💡 **Why:** If you review in the same context, you're reviewing in the "dumb zone" — the reviewer is dumber than the implementer. Clear context = review in the smart zone.

---

# 🛠️ Tools & Technologies

| Tool | Purpose | When Used |
|------|---------|-----------|
| Claude Code | AI coding assistant | Primary tool for workshop |
| Claude (CLI) | Preferred over Claude app | UI is "broken in a ton of ways" |
| Docker | Sandbox for AFK agents | Running Ralph loop in isolation |
| Sand Castle | TypeScript library for parallel AFK loops | Matt's custom solution for running multiple agents in parallel |
| npx vitest | Test runner | TDD feedback loops |
| npm run test | Test suite | Run after every implementation |
| npm run type-check | Type checking | Catch errors before commits |
| GitHub Issues | Issue tracking | Managing the Kanban board |
| Slido | Q&A tool | Live audience questions |

---

# 📖 Books & Resources

> 📚 **The Pragmatic Programmer** by David Thomas & Andrew Hunt
> - Why relevant: "Don't bite off more than you can chew" — applies to AI task sizing
> - Best for: Foundational software engineering principles that work with AI

> 📚 **The Design of Design** by Frederick P. Brooks
> - Why relevant: "Shared design concept" — the idea that a team shares an understanding that can't be fully documented
> - Best for: Understanding why grilling sessions work better than specs-to-code

> 📚 **Philosophy of Software Design** by John Ousterhout
> - Why relevant: Deep modules vs shallow modules — AI tends to produce shallow modules, need to guide toward deep
> - Best for: Designing codebases that AI can actually work with

---

# 💡 Key Insights

> 💡 **Specs-to-code doesn't work**: "The code is your battleground" — you can't ignore the code and just edit specs. You need to stay aligned with what's actually being written.

> 💡 **Bad codebases make bad agents**: If your codebase has poor feedback loops (no tests, no type checking), AI will produce garbage. The quality of your feedback loops is the ceiling for AI output.

> 💡 **AI loves to code horizontally** — you need to actively push for vertical slices or you'll wait until phase 3 for any feedback.

> 💡 **Deep modules are easier to test**: Large interface, small surface area. Shallow modules (many small files with many exports) are hard for AI to navigate and test. Design for deep modules.

> 💡 **Keep your system in mind**: Don't let AI blindly reshape your codebase. You need to know the shapes of your modules even if you delegate implementation.

> 💡 **Human in the loop vs AFK**: Planning/alignment MUST be human in the loop. Implementation CAN be AFK. QA MUST be human in the loop.

> 💡 **Review in fresh context**: Always clear context before reviewing — review in the smart zone, not the dumb zone.

---

# 🔄 Comparison: Traditional vs AI-Enhanced

| Concept | Traditional | AI-Enhanced |
|---------|-------------|-------------|
| Planning | Write detailed spec | Grilling session (40-100 questions) |
| Task breakdown | Linear phases | Vertical slices (tracer bullets) |
| Implementation | Sequential | Parallel via Kanban board |
| Testing | Manual | TDD + automated feedback loops |
| Code review | Same context | Fresh context (smart zone) |

---

# 🎯 Action Items for Your Projects

> 🚀 **Try the "grill me" skill** on your next feature idea — before writing any code, spend 30-60 minutes being relentlessly questioned

> 🚀 **Switch to vertical slices** — when breaking down work, ensure each piece crosses all layers and produces something visible

> 🚀 **Run improve-codebase-architecture skill** on your repo to find opportunities to deepen modules

> 🚀 **Add feedback loops** if missing — at minimum: type checking + tests. Without these, AI is coding blind

> 🚀 **Clear context before reviewing** — never review in the same session that wrote the code

> 🚀 **Design module interfaces, delegate implementation** — know the shapes of your modules without needing to know every line of code inside them

---

# 🔗 Related Concepts

> 🔗 **Sub-agents**: Using separate LLM contexts for exploration, then summarizing back to parent. The workshop showed a sub-agent burn 93.7K tokens while parent context stayed small.

> 🔗 **Sand Castle**: Matt's parallelization library — runs multiple agents on different issues simultaneously, then merges results.

> 🔗 **MCP (Model Context Protocol)**: Mentioned for frontend work (agent browser, Playwright MCP) — currently "not very good" for creating nice frontends.

> 🔗 **Push vs Pull for coding standards**: Push instructions to the AI (in context), pull from skills when needed. Use push for reviewer, pull for implementer.

---

# 📊 Key Metrics from Workshop

- Sub-agent token usage: 93.7K tokens (separate context)
- Parent context after sub-agent: ~25K tokens (still in smart zone)
- Test count after implementation: 284 tests
- Workshop duration: ~2 hours

---

*Source: [Full Walkthrough: Workflow for AI Coding](https://www.youtube.com/watch?v=-QFHIoCo-Ko)*

*Last Updated: 2026-05-02*