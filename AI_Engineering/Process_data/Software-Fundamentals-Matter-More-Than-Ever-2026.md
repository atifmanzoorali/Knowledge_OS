---
Source: https://www.youtube.com/watch?v=v4F1gFy-hqg
Title: "Why Software Fundamentals Matter More Than Ever"
Creator: Matt Pocock
Date: 2026
Framework: Grill Me Skill, Ubiquitous Language, TDD, Deep Modules
Category: agentic-ai
Ingested: 2026-05-02
Tags: software-fundamentals, tdd, ddd, software-architecture, ai-coding, code-quality
Confidence: High
---

# 📝 Executive Summary

Matt Pocock delivers a keynote arguing that software fundamentals matter MORE in the AI age, not less. The core thesis: "Code is not cheap — bad code is the most expensive it's ever been." He explains why the "specs to code" movement fails, and provides 5 practical tips derived from classic software engineering books (Pragmatic Programmer, Philosophy of Software Design, Domain Driven Design, The Design of Design). The talk connects AI failure modes to fundamental software principles, showing how good codebases enable AI to do great work.

---

# 🏗️ Core Framework: Why Software Fundamentals Matter

## What It Is

> 🏗️ **The thesis:** In the AI age, good codebases matter more than ever because AI performs brilliantly in well-structured code and terribly in messy code.

Key concept: "Bad code is the most expensive it's ever been" — because it prevents you from capturing AI's full potential.

## When To Use

> ✅ **Use this thinking when:** Evaluating your codebase, setting up AI coding workflows, or deciding how to invest your time learning new skills.

> ❌ **Don't use when:** Thinking "code is cheap" and ignoring codebase quality — AI will amplify your problems.

## Key Components

> ⚙️ **Specs to Code Movement**: The idea that you can write specs, feed them to AI, and ignore the code. Matt argues this fails because code quality degrades with each iteration — "garbage in, garbage out."

> ⚙️ **Software Entropy**: From Pragmatic Programmer — every change that doesn't consider system design makes the codebase worse. This is exactly what happens with specs-to-code.

> ⚙️ **Complexity Definition** (John Ousterhout): "Complexity is anything related to the structure of a software system that makes it hard to understand and modify."

---

# 📚 Step-by-Step Implementation

## Tip 1: Use "Grill Me" Skill for Shared Understanding

> 🔹 **What to do:** Before coding, use a skill that makes AI interview you relentlessly until you reach "shared understanding."

> 💡 **Why:** Frederick P. Brooks' "design concept" — the invisible shared idea between collaborators — can't be documented. You must actively align with the AI.

```
Skill: "Interview me relentlessly about every aspect of this plan
until we reach a shared understanding. Walk down each branch of
the design tree, resolving dependencies one by one."
```

**Result:** AI asks 40-100 questions. The conversation becomes an asset you can turn into PRD or directly into issues.

## Tip 2: Create Ubiquitous Language (Shared Vocabulary)

> 🔹 **What to do:** Create a markdown file of terminology that you and AI share — scan your codebase for terms, create definitions, reference in all conversations.

> 💡 **Why:** Domain Driven Design's "ubiquitous language" reduces AI verbosity. When AI uses your shared terms, thinking becomes more precise.

## Tip 3: Use TDD (Test-Driven Development)

> 🔹 **What to do:** Force AI to write tests first (Red → Green → Refactor)

> 💡 **Why:** Pragmatic Programmer's "outrunning your headlights" — the rate of feedback is your speed limit. TDD forces small, deliberate steps.

## Tip 4: Build Deep Modules (Not Shallow)

> 🔹 **What to do:** Use "Improve Codebase Architecture" skill to wrap related code into deep modules with simple interfaces

> 💡 **Why:** AI struggles with shallow modules (many small files with many exports). Deep modules hide complexity behind simple interfaces, making AI more effective.

## Tip 5: Design Interface, Delegate Implementation

> 🔹 **What to do:** Focus on designing module interfaces well; let AI handle the implementation inside

> 💡 **Why:** Kent Beck's "Invest in the design of the system every day." Design the interface, test from outside, treat modules as "gray boxes."

---

# 🛠️ Tools & Skills Mentioned

| Tool/Skill | Purpose | When to Use |
|------------|---------|-------------|
| Grill Me Skill | Reach shared understanding with AI | Before any feature work |
| Ubiquitous Language | Create shared vocabulary | Reduce AI verbosity |
| TDD (Red-Green-Refactor) | Force small steps | When AI tries to do too much |
| Improve Codebase Architecture | Create deep modules | When codebase has shallow modules |
| Claude Code | AI coding tool | Primary tool |

---

# 📖 Books & Resources

> 📚 **The Pragmatic Programmer** by David Thomas & Andrew Hunt
> - Key concepts: Software entropy, DRY, outrunning your headlights
> - Why relevant: Explains why specs-to-code fails

> 📚 **Philosophy of Software Design** by John Ousterhout
> - Key concepts: Deep vs shallow modules, complexity definition
> - Why relevant: Explains what makes codebases hard for AI to navigate

> 📚 **The Design of Design** by Frederick P. Brooks
> - Key concepts: Design concept, design tree
> - Why relevant: Explains why shared understanding matters

> 📚 **Domain Driven Design** by Eric Evans
> - Key concepts: Ubiquitous language, bounded contexts
> - Why relevant: Provides framework for shared vocabulary with AI

> 📚 **Kent Beck** (referenced)
> - Key concept: "Invest in the design of the system every day"
> - Why relevant: Counter to specs-to-code which "divests" from design

---

# 💡 Key Insights

> 💡 **Code is not cheap**: In the AI age, bad code prevents you from capturing AI's full potential. Good codebases let AI do "really, really well."

> 💡 **Specs to Code = Vibe Coding by another name**: Ignoring code and just editing specs produces "garbage" — each iteration makes it worse.

> 💡 **AI amplifies your problems**: If your codebase is hard to change, AI will make it even harder. If it's well-structured, AI makes it better.

> 💡 **AI needs gray boxes**: Design the interface, delegate implementation. You can't review every line — trust the interface.

> 💡 **Planning should mention module changes**: In PRDs, be specific about which modules you're modifying and how their interfaces change.

---

# 🔄 Failure Modes & Solutions

| Failure Mode | Solution (From Classic Books) |
|--------------|--------------------------------|
| AI didn't do what I wanted | Grill Me skill → shared understanding |
| AI is too verbose | Ubiquitous Language (DDD) |
| AI produces code that doesn't work | TDD + feedback loops (types, tests) |
| AI doesn't understand my code | Deep modules (not shallow) |
| Brain can't keep up | Design interface, delegate implementation |

---

# 🎯 Action Items for Your Projects

> 🚀 **Start with Grill Me** — Before any feature, spend 30 min being interviewed by AI until shared understanding reached

> 🚀 **Create Ubiquitous Language** — Scan codebase, create terminology file, reference in all AI conversations

> 🚀 **Insist on TDD** — Force AI to write tests first, not after implementation

> 🚀 **Run Improve Codebase Architecture** — Convert shallow modules to deep modules

> 🚀 **Design interfaces explicitly** — In PRDs, specify module interface changes, not just what to build

---

# 🔗 Related Concepts

> 🔗 **Matt Pocock's Skills** (GitHub: mattpocockuk/skills)
> - Grill Me, Ubiquitous Language, Improve Codebase Architecture

> 🔗 **AIHero** (aihero.dev)
> - Matt's newsletter and training resources

*Source: [Why Software Fundamentals Matter More Than Ever](https://www.youtube.com/watch?v=v4F1gFy-hqg)*

*Last Updated: 2026-05-02*