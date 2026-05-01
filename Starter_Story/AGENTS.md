# Starter_Story Folder

This folder contains Starter Story podcast transcripts and their processed startup profiles.

## Folder Structure

```
Starter_Story/
├── AGENTS.md           # This file
├── INDEX.md            # Master index of all processed profiles
├── Raw_Data/           # Raw transcripts from Process_Link skill
│   └── [video_id]_[title].md
└── Process_data/       # Analyzed profiles from starter-story skill
    ├── AGENTS.md
    └── [Founder]-[Company]-[Year].md
```

## Workflow

### Full Processing Flow

1. **Process_Link Skill** receives a YouTube URL
2. User selects "Starter_Story" folder
3. Process_Link extracts transcript and saves to `Raw_Data/`
4. Process_Link auto-triggers **starter-story** skill
5. starter-story skill analyzes transcript and creates profile
6. Profile saved to `Process_data/`
7. INDEX.md updated with new entry
8. Changes pushed to GitHub

### Skills Involved

- **Process_Link** (in Knowledge_OS/Skills/Process_Link/)
  - Extracts transcripts from YouTube
  - Saves to Raw_Data folder
  - Auto-triggers analysis skills

- **starter-story** (in Knowledge_OS/Skills/starter-story/)
  - Analyzes raw transcripts
  - Creates structured startup profiles
  - Updates INDEX.md
  - Pushes to GitHub

## Files Format

### Raw Transcript (.md)
```markdown
---
video_id: [YouTube video ID]
title: "Video Title"
channel: "Starter Story"
duration: [seconds]
view_count: [number]
upload_date: [YYYYMMDD]
tags: []
thumbnail: [URL]
---

[Transcript text]
```

### Processed Profile (.md)
```markdown
---
Source: [YouTube URL]
Title: [Video Title]
Founder: [Name]
Company: [Company]
Date: [Year]
Category: [SaaS / E-commerce / etc.]
Ingested: [YYYY-MM-DD]
Tags: [relevant-tags]
Confidence: [High / Medium / Low]
---

# 🚀 [Founder Name]: [Company]

[Full profile with sections: Executive Summary, Product, Tech Stack, Distribution, Frameworks, Metrics]
```

## INDEX.md Format

```markdown
# Starter Story INDEX

| Founder | Company | Year | Date Added |
|---------|---------|------|----------|
| Marc Lou | 35 Startups | 2026 | 2026-05-02 |
| Jeremy Redman | Taskmagic | 2026 | 2026-05-02 |
```

## Current Contents

### Raw_Data/
- D4fkiQfzw_I_How_I_Work_$77KMonth_Solopreneur.md (Marc Lou)
- iVy5J7iE-3Q_Most_Successful_Solopreneur_OAT.md (Jeremy Redman)

### Process_data/
- Marc_Lou-35_Startups-2026.md
- Jeremy_Redman-Taskmagic-2026.md

## How to Process a New Transcript

1. Provide YouTube URL to Process_Link skill
2. Select "Starter_Story" when asked for folder
3. Process_Link will extract transcript → auto-trigger starter-story
4. starter-story will analyze and create profile
5. Profile saved to Process_data/, INDEX updated
6. All changes pushed to GitHub automatically

## GitHub Repository

https://github.com/atifmanzoorali/Knowledge_OS

Starter_Story folder is at: `Knowledge_OS/Starter_Story/`

## Notes

- Raw_Data contains original transcripts with metadata
- Process_data contains analyzed startup profiles
- All new entries are automatically pushed to GitHub
- INDEX.md must be updated when adding new profiles
- Confidence scoring: High (full transcript), Medium (partial), Low (incomplete)