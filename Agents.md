# Knowledge OS

## Folder Structure

- **Skills/** - Skills folder
  - AGENTS.md
  - README.md
  - Process_Link/ - Skill to extract and process YouTube transcripts
  - starter-story/ - Skill to analyze founder interviews
- **Starter_Story/** - Starter Story podcast transcripts
  - AGENTS.md
  - INDEX.md
  - Raw_Data/
  - Process_data/
- **Inner_Work/** - Inner Work content
  - AGENTS.md
  - Raw_Data/
- **AI_Leaders/** - AI Leaders content
  - AGENTS.md
  - Raw_Data/
- **Founders/** - Founders content
  - AGENTS.md
  - Raw_Data/
- **My_First_Million/** - My First Million content
  - AGENTS.md
  - Raw_Data/
- **AI_Engineering/** - AI Engineering content
  - AGENTS.md
  - Raw_Data/
- **Raw_Data/** - Root level raw data

## Scripts

- **Transcript_Extraction.py** - Extracts transcripts and metadata from YouTube videos using yt-dlp and YouTubeTranscriptApi, saves .md with YAML frontmatter to Raw_Data folder