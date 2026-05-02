# My_First_Million Folder

This folder contains My First Million podcast transcripts and their processed business insight profiles.

## Folder Structure

```
My_First_Million/
├── AGENTS.md           # This file
├── INDEX.md            # Master index of all processed profiles
├── Raw_Data/           # Raw transcripts from Process_Link skill
│   └── [video_id]_[title].md
└── Process_data/       # Analyzed profiles from my-first-million skill
    └── [GuestOrTopic]-[Date].md
```

## About My First Million

**Hosts:** Sam Parr (founder of The Hustle) & Shaan Puri (serial entrepreneur)

**Format:** Three episode types:
- **Brainstorm** - Sam & Shaan brainstorm business ideas
- **Interview** - Guest interviews with founders/investors
- **Business Breakdowns** - Case studies on specific companies

**Source:** https://www.youtube.com/c/MyFirstMillionPod

## Workflow

### Full Processing Flow

1. **Process_Link Skill** receives a YouTube URL
2. User selects "My_First_Million" folder
3. Process_Link extracts transcript and saves to `Raw_Data/`
4. Process_Link auto-triggers **my-first-million** skill
5. my-first-million skill analyzes transcript (adapts template based on episode type)
6. Profile saved to `Process_data/`
7. INDEX.md updated with new entry
8. Changes pushed to GitHub
9. Search index rebuilt

### Skills Involved

- **Process_Link** (in Knowledge_OS/Skills/Process_Link/)
  - Extracts transcripts from YouTube
  - Saves to Raw_Data folder
  - Auto-triggers analysis skills

- **my-first-million** (in Knowledge_OS/Skills/my-first-million/)
  - Analyzes raw transcripts
  - Creates structured business insight profiles
  - Updates INDEX.md
  - Rebuilds search index
  - Pushes to GitHub

## Files Format

### Raw Transcript (.md)
```markdown
---
video_id: [YouTube video ID]
title: "Episode Title"
channel: "My First Million"
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
Title: [Episode Title]
Episode: [Ep. #]
Host: Sam Parr & Shaan Puri
Guest: [Name if interview]
Date: [Year]
Category: [brainstorm/interview/breakdown]
Ingested: [YYYY-MM-DD]
Tags: [relevant-tags]
Confidence: [High/Medium/Low]
---

# 📊 Executive Summary

[Full profile with sections based on episode type]
```

## INDEX.md Format

```markdown
# My First Million INDEX

| Episode | Guest/Topic | Category | Date Added |
|---------|-------------|----------|------------|
```

## Notes

- Raw_Data contains original transcripts with metadata
- Process_data contains analyzed business insight profiles
- All new entries are automatically pushed to GitHub
- INDEX.md must be updated when adding new profiles
- Search index is rebuilt after each new entry
- Template adapts based on episode type (brainstorm/interview/breakdown)
- Books are always included in Resources section (user requirement)