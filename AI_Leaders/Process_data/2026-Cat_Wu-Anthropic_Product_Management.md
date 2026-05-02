---
Source: https://www.youtube.com/watch?v=PplmzlgE0kg
Person: Cat Wu
Role: Head of Product
Company: Anthropic
Date: 2026
Category: AI Product Management
Ingested: 2026-05-02
Tags: Claude Code, Co-work, product management, AI native, engineering
---

# 📝 Full Context

Cat Wu is the Head of Product for Claude Code and Co-work at Anthropic—building the tools that are fundamentally changing how developers and knowledge workers build products. She works alongside Boris Cherny (tech lead and product visionary), where the PM role has evolved into something radically different from traditional product management. With ~30-40 PMs at Anthropic across research, cloud developer platform, cloud code, enterprise, and growth teams, Cat's team ships features daily—sometimes in a week, sometimes in a day. The key insight from this interview: as code becomes cheaper to write, product taste becomes more valuable than ever, and the PM role is merging with engineering and design. The hardest skill for AI PMs is figuring out for the current model how to elicit maximum capability—it's easy to build for super AGI, hard to build for today's model.

---

# 🏛️ Their AI Thesis

> 🏛️ **The hard thing is figuring out for the current model, how do you elicit the maximum capability?** It's very easy to build the product for the super AGI strong model where you just give it a text box and it adds any tool or integration it needs. The real skill is understanding how users can interact with the model's strengths and patch its weaknesses right now—not in some hypothetical future.

---

# 💭 Key Mental Models

---

### 🎯 Model 1: Product Taste as the Core Skill

> 🧠 **The Concept:** As code becomes much cheaper to write, the thing that becomes more valuable is deciding *what* to write. Tens of thousands of GitHub issues come in requesting every feature under the sun—it takes real taste to figure out what's worth building and the right way to build it.

> 💡 **The Truth:** This skill can come from any background (engineering, design, product), but it's the rare skill that determines success. Engineering background helps estimate effort, but the core is understanding UX, what's delightful, and what creates value.

> ⚡ **Maxim:** *"As code becomes much cheaper to write, the thing that becomes more valuable is deciding what to write."*

---

### 🔄 Model 2: The Merging of Roles

> 🧠 **The Concept:** PMs are doing engineering work, engineers are doing PM work, designers are also PMing and landing code. The Venn diagrams are combining. You can either hire more engineers with great product taste or hire more PMs to guide engineering—both work.

> 💡 **The Truth:** On Cat's team, they focus on hiring engineers with great product taste because it reduces overhead. Many engineers can go end-to-end from seeing user feedback on Twitter to shipping a product by end of week with almost no PM involvement. This is the most efficient way to ship.

> ⚡ **Maxim:** *"All of the roles are merging."*

---

### ⚙️ Model 3: Ship in Research Preview

> 🧠 **The Concept:** Anthropic ships almost all features in "research preview"—clearly branded so users know it's early, potentially not supported forever. This reduces commitment and allows getting something out in a week or two rather than months.

> 💡 **The Truth:** This creates a tight feedback loop. Features that are buggy get shipped, people complain, and they fix it in the next release. The cost is some product consistency overlap, but the speed of learning far outweighs the cost.

> ⚡ **Maxim:** *"We want to remove every single barrier to shipping things."*

---

### 🛑 Model 4: Clear QEQ Goals

> 🧠 **The Concept:** LLMs are so general that they create ambiguity about who you're building for and what problems you're solving. A great PM sets crystal clear goals: "Our key user is professional developers. The main problem is too many permission prompts. The use case is enterprises to safely get to zero permission prompts." This rules out approaches and sets direction.

> 💡 **The Truth:** Clear goals let the team make decisions without blocking on PM. They also help the model understand what success looks like, improving outputs. Without this, you get feature sprawl and confusion.

> ⚡ **Maxim:** *"It's very easy to build the product for the super AGI strong model. The hard thing is figuring out for the current model, how do you elicit the maximum capability?"*

---

### 🧠 Model 5: First Principles Thinking

> 🧠 **The Concept:** The work is becoming more amorphous—great PMs need to understand what gaps exist, prioritize them, then either learn that skill or apply existing skills to fix the hole. You need to be able to wear many hats, swap them, and have low ego about what work you do to help the team move faster.

> 💡 **The Truth:** The value now is in people who can do first principles thinking: figure out how the tech landscape is changing, what the team really needs, and jump in to fix gaps. This changes every few months as models get better.

> ⚡ **Maxim:** *"Just do things."* (Her life motto)

---

# 💬 Notable Quotes

---

> 💬 *"As code becomes much cheaper to write, the thing that becomes more valuable is deciding what to write."*
> — Cat Wu, Lenny's Podcast

---

> 💬 *"I think all of the roles are merging. PMs are doing some engineering work, engineers are doing PM work, designers are PMing and also landing code."*
> — Cat Wu, Lenny's Podcast

---

> 💬 *"We want to remove every single barrier to shipping things."*
> — Cat Wu, Lenny's Podcast

---

> 🚀 *"The timelines for a lot of our product features have gone down from 6 months to 1 month and sometimes to even one day."*
> — Cat Wu, Lenny's Podcast

---

> 📈 *"The hardest skill is being able to define what the product should look like a month from now."*
> — Cat Wu, Lenny's Podcast

---

> 🧠 *"If an automation doesn't work 100% of the time, it's not really an automation. There's just not much value in a 95% automation."*
> — Cat Wu, Lenny's Podcast

---

> 🎯 *"Just do things."*
> — Cat Wu, Lenny's Podcast

---

> 💡 *"Build apps that you're actually using every single day. Because only through that usage are you actually getting the value."*
> — Cat Wu, Lenny's Podcast

---

# 🚩 Contrarian Views

---

> ⚡ **95% automation is worthless.**

Most people build automations that work 90-95% of the time and then give up. Cat argues this is essentially useless—an automation must work 100% to be reliable. The last 5-10% takes more time, but it's critical to put in that elbow grease, teach the model your preferences, give feedback, and get it to 100%. Then you can actually rely on it.

---

# 🛠️ What They're Building / Focused On

---

## 🤖 Claude Code

> 🚀 **Multi-tasking Agents:** Moving from single tasks to running 50-100 tasks simultaneously. Need to build infrastructure for managing this remotely (not local RAM).

> 🏃 **Code Review:** New capability unlocked with Opus 4.5/4.6 and Sonnet 4.6—now runs multiple code review agents simultaneously across the codebase, synthesizes real issues for engineers before merge.

> 🧹 **Removing Crutches:** As models get smarter, features added as "crutches" (like to-do lists for early models) get removed. Model now naturally does what earlier models needed prompting for.

---

## 💬 Co-work

> 📊 **Slide Deck Creation:** Cat used Co-work to create a 20-page presentation for a conference by connecting Google Drive, Slack, and giving it the narrative. It pulled Twitter data, looked at launch channels, and synthesized a deck in an hour—then she refined it.

> 🔗 **Data Source Integration:** Connect Google Calendar, Slack, Gmail, Google Drive so Co-work has context to be useful.

> 🎯 **Non-code Work:** Everything from inbox zero to slide decks to docs to customer meeting prep—output isn't code, use Co-work.

---

## 🏗️ Internal Tools

> 🛠️ **Sales Custom Apps:** Salesperson built a web app that pulls from Salesforce/Gong to automatically customize customer decks based on their context (using Bedrock vs. Console, concerned about code review, needs HIPAA compliance, etc.). Takes seconds instead of 20-30 minutes.

---

# 📚 Recommended Books

---

## How Asia Works

> 📚 **Why recommended:** Recommended in lightning round as favorite book

> 📖 **What it's about:** About governments that make long lasting successful economies

---

## Paper Menagerie

> 📚 **Why recommended:** Recommended in lightning round as a fun read

> 📖 **What it's about:** A book of short stories

---

# 👁️ Their Blind Spot

---

> 👁️ **Product consistency sacrificed for speed.** With features shipping daily, there's overlap between features, and new users may not know the best path. Education is needed to explain core features and best practices.

---

> 👁️ **Customization can distract.** People spend too much time customizing workflows (MCPs, skills) instead of shipping products. There's a limit to how much customization is useful.

---

# 💎 Naval-Style Maxim

> 💎 *"As code becomes much cheaper to write, the thing that becomes more valuable is deciding what to write."*

---

# 🏷️ Content Connections

---

> 🏷️ **Related Knowledge Asset:** Evan Spiegel profile (AI Leaders)

> 🏷️ **Mental Model for LinkedIn:** "The PM role is dead, long live the PM role"

> 🏷️ **Contrarian Angle:** "Why 95% automation is worthless"

---

## 💎 Maxim Collection for Content

> 1💎 *"As code becomes much cheaper to write, the thing that becomes more valuable is deciding what to write."*

> 2💎 *"All of the roles are merging."*

> 3💎 *"We want to remove every single barrier to shipping things."*

> 4💎 *"The hardest skill is being able to define what the product should look like a month from now."*

> 5💎 *"If an automation doesn't work 100% of the time, it's not really an automation."*

> 6💎 *"Just do things."*

---

*Last Updated: 2026-05-02*