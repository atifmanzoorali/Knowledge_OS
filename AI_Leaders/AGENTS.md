# AI_Leaders

An autonomous agent system for processing AI leader interviews and creating deep-dive intelligence profiles.

## GitHub Repository

https://github.com/atifmanzoorali/Knowledge_OS

## Folder Structure

```
AI_Leaders/
├── AGENTS.md                # This file - system overview
├── INDEX.md                # Master index of processed profiles
├── Raw_Data/               # Raw transcripts from Process_Link
└── Process_data/           # Analyzed AI leader profiles
```

## Processing Flow

1. **User inputs YouTube URL** via Process_Link skill
2. **Process_Link** extracts transcript → saves to Raw_Data
3. **ai-leaders skill auto-triggers** (skill chaining)
4. **Analyzes** transcript → creates intelligence profile → saves to Process_data
5. **Updates** INDEX.md
6. **Pushes** to GitHub
7. **Rebuilds** search index

## Processing Commands

### Via Process_Link (Recommended)

```bash
Process_Link <YouTube_URL>
# Select "AI_Leaders" folder when prompted
```

The skill chain will:
1. Extract transcript to AI_Leaders/Raw_Data
2. Automatically trigger ai-leaders skill
3. Create profile in AI_Leaders/Process_data
4. Update INDEX.md
5. Push to GitHub
6. Rebuild search index

## Output Format

Processed files saved to: `AI_Leaders/Process_data/[Year]-[Person]-[Topic].md`

Example:
- Evan_Spiegel-Snap_Product_Innovation-2026.md
- Cat_Wu-Anthropic_Product_Management-2026.md

## INDEX Format

```markdown
| Person | Topic | Date Added |
|--------|-------|------------|
```

## Search

All AI_Leaders content is indexed for semantic search:

```bash
python search/index.py        # Rebuild index
python search/search.py "your query"  # Search
```

## Related Skills

| Skill | Purpose |
|-------|---------|
| Process_Link | Extract transcripts |
| ai-leaders | Analyze AI leader content |

## Current Contents

### Raw_Data/
- PplmzlgE0kg_Introduction_to_Cat_Wu.md
- -7Yol5vX5xw_Introduction_to_Evan_Spiegel.md

### Process_data/
- 2026-Cat_Wu-Anthropic_Product_Management.md
- 2026-Evan_Spiegel-Snap_Product_Innovation.md

### INDEX.md
| Person | Topic | Date Added |
|--------|-------|------------|
| Evan Spiegel | Snap Product Innovation | 2026-05-02 |
| Cat Wu | Anthropic Product Management | 2026-05-02 |

## Notes

- Each profile captures: AI thesis, key mental models, contrarian views, what they're building
- Profiles stored permanently in the vault
- All changes pushed to GitHub automatically
- Search index rebuilt after each new entry