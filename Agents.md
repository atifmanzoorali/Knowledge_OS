# Knowledge OS - Agent Instructions

## Critical Rules (MUST ALWAYS FOLLOW)

1. **Use Local Skills Only** - All skills must be loaded from `.agents/skills/` folder using the skill tool
2. **Always Ask for Folder** - When running Process_Link, you MUST ask the user which folder to save content to before proceeding

## Available Folders

1. Starter_Story
2. My_First_Million
3. Founders
4. AI_Engineering
5. AI_Leaders
6. Inner_Work

## Processing Flow (Step by Step)

1. **User provides YouTube URL + transcript**
2. **Load Process_Link skill** from local folder using skill tool
3. **Ask user:** "Which folder should I save this to?" (CRITICAL STEP)
4. **Check for duplicates** in the selected folder's Raw_Data
5. **Save transcript** to selected folder's Raw_Data
6. **Auto-trigger** corresponding analysis skill (if available)
7. **Analysis skill creates** profile in Process_data folder
8. **Update INDEX.md** with new entry
9. **Push to GitHub** with proper commit message
10. **Rebuild search index** - run `python search/index.py`

## Skill Chaining

| Folder | Skill Triggered |
|--------|----------------|
| Starter_Story | starter-story |
| My_First_Million | my-first-million |
| Founders | founders |
| AI_Leaders | ai-leaders |
| Inner_Work | inner-work |
| AI_Engineering | ai-engineering |

## GitHub Commit Message Format

- "Add transcript: [title]"
- "Add starter story: [founder] - [company]"
- "Add Founders: [Person] - [Topic]"
- "Add AI Leaders: [Person] - [Topic]"
- "Add My First Million: [Guest/Topic]"
- "Add AI Engineering: [Framework/Concept]"
- "Add Inner Work: [Teacher] - [Topic]"

## Starting a New Session

1. Read `Knowledge_OS/AGENTS.md`
2. Check for updates: `git pull origin main`