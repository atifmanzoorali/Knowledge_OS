# AI_Engineering

An autonomous skill for processing AI development content from YouTube videos. Transforms technical videos about agentic workflows, new frameworks, and automation patterns into structured reference profiles.

## Workflow

1. **Process_Link** extracts transcript → saves to Raw_Data
2. **ai-engineering skill** triggers automatically → analyzes transcript
3. **Profile saved** to Process_data with structured template
4. **INDEX.md updated** with new entry
5. **Pushed to GitHub** automatically
6. **Search index rebuilt**

## Trigger

This skill triggers when Process_Link saves a transcript to the AI_Engineering folder.

## Input

- Raw transcript from: `Knowledge_OS/AI_Engineering/Raw_Data/[video_id]_[title].md`

## Output

- Structured profile: `Knowledge_OS/AI_Engineering/Process_data/[FrameworkOrConcept]-YYYY.md`

## Categories

| Code | Description |
|------|-------------|
| agentic-ai | Agentic AI patterns, multi-agent systems |
| vibe-coding | No-code/Low-code AI building, UI-based dev |
| automation | Workflow automation, AI agents in production |
| llm-patterns | LLM patterns, prompting, fine-tuning |
| tool-use | MCP, function calling, tool integration |

## File Naming

- Single concept: `Agentic-RAG-2026.md`
- Framework: `LangChain-2026.md`
- Multi-topic: `AI-Agent-Workflows-2026.md`

## GitHub Push

After saving profile:
```bash
git add Knowledge_OS/AI_Engineering/Process_data/[filename].md
git add Knowledge_OS/AI_Engineering/INDEX.md
git commit -m "Add AI Engineering: [Framework/Concept]"
git push origin main
python search/index.py
```

## Skills Chain

| Folder | Skill Triggered |
|--------|----------------|
| AI_Engineering | ai-engineering |