# Folder Structure

## Root Folders

- **Knowledge_OS/Skills/** - Skills folder
  - Process_Link/
  - starter-story/
- **Knowledge_OS/Starter_Story/** - Starter Story podcast transcripts
  - AGENTS.md
  - INDEX.md
  - Raw_Data/
- **Knowledge_OS/Inner_Work/** - Inner Work content
  - AGENTS.md
  - Raw_Data/
- **Knowledge_OS/AI_Leaders/** - AI Leaders content
  - AGENTS.md
  - Raw_Data/
- **Knowledge_OS/Founders/** - Founders content
  - AGENTS.md
  - Raw_Data/
- **Knowledge_OS/My_First_Million/** - My First Million content
  - AGENTS.md
  - Raw_Data/
- **Knowledge_OS/AI_Engineering/** - AI Engineering content
  - AGENTS.md
  - Raw_Data/

## Skill Chaining

| Folder | Skill Triggered |
|--------|----------------|
| Starter_Story | starter-story |
| Inner_Work | (TBD) |
| AI_Leaders | (TBD) |
| Founders | (TBD) |
| My_First_Million | (TBD) |
| AI_Engineering | (TBD) |

## Scripts

- **Knowledge_OS/Transcript_Extraction.py** - Extracts transcripts and metadata from YouTube videos

## Usage

```bash
python Transcript_Extraction.py <youtube_url> <output_folder>
```

Example:
```bash
python Transcript_Extraction.py "https://www.youtube.com/watch?v=xxx" "Knowledge_OS/Starter_Story/Raw_Data"
```