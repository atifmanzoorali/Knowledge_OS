# Inner Work

An autonomous agent system for processing spiritual, philosophical, and personal growth YouTube transcripts into actionable wisdom profiles.

## GitHub Repository

https://github.com/atifmanzoorali/Knowledge_OS

## Folder Structure

```
Inner_Work/
├── AGENTS.md                # This file - system overview
├── INDEX.md                # Master index of processed profiles
├── Raw_Data/               # Raw transcripts from Process_Link
└── Process_data/          # Analyzed wisdom profiles
```

## Processing Flow

1. **User inputs YouTube URL** via Process_Link skill
2. **Process_Link** extracts transcript → saves to Raw_Data
3. **inner-work skill auto-triggers** (skill chaining)
4. **Analyzes** transcript → creates wisdom profile → saves to Process_data
5. **Updates** INDEX.md
6. **Pushes** to GitHub
7. **Rebuilds** search index

## Available Categories

| Category | Emoji | Examples |
|----------|-------|----------|
| Spirituality | 🕉️ | General spiritual teachings |
| Philosophy | 📜 | Stoicism, Buddhism |
| Psychology | 🧠 | Mindset, behavior |
| Personal Growth | 🌱 | Self-improvement, habits |
| Kabbalah | 🕯️ | Jewish mysticism |
| Mysticism | 🔮 | Esoteric traditions |

## Content Types

The skill handles diverse topics:

- **Teachers:** Ram Dass, Eckhart Tolle, Brené Brown, Deepak Chopra, etc.
- **Topics:** Mindfulness, meditation, self-awareness, purpose, relationships
- **Traditions:** Zen, Stoicism, Kabbalah, modern spirituality

## Processing Commands

### Via Process_Link (Recommended)

```bash
Process_Link <YouTube_URL>
# Select "Inner_Work" folder when prompted
```

The skill chain will:
1. Extract transcript to Inner_Work/Raw_Data
2. Automatically trigger inner-work skill
3. Create profile in Inner_Work/Process_data
4. Update INDEX.md
5. Push to GitHub

### Manual Trigger

```bash
# Not recommended - use Process_Link instead
```

## Output Format

Processed files saved to: `Inner_Work/Process_data/[Teacher]-[Topic]-[Year].md`

Example:
- `Ram_Dass-Be_Here_Now-2026.md`
- `Eckhart_Tolle-Power_of_Now-2026.md`

## INDEX Format

```markdown
| Teacher | Topic | Category | Date Added |
|---------|-------|----------|------------|
```

## Search

All Inner_Work content is indexed for semantic search:

```bash
python search/index.py        # Rebuild index
python search/search.py "your query"  # Search
```

## Related Skills

| Skill | Purpose |
|-------|---------|
| Process_Link | Extract transcripts |
| inner-work | Analyze wisdom content |

## Current Contents

### Raw_Data/
- oAQqomDe8tc_David_G-Why_Isnt_Everyone_Receiving_Limitless_Abundance.md

### Process_data/
- David_G-Abundance_Spirituality-2024.md

### INDEX.md
| Teacher | Topic | Category | Date Added |
|---------|-------|----------|------------|
| David G. | Abundance & Spirituality | kabbalah | 2026-05-02 |

## Notes

- Teacher tracking: First column in INDEX
- Categories: Auto-detected from content
- Balance: Both philosophical depth + practical application
- Search: Indexes both Raw_Data and Process_data