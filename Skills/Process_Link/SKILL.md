---
name: Process_Link
description: This skill should be used when the user asks to "Process_Link", "process link", "extract transcript", "get transcript from youtube", or provides a YouTube link to process and save to a category folder.
---

# Process_Link Skill

Extract YouTube transcripts and save them to the appropriate category folder in Knowledge_OS.

## Purpose

This skill takes a YouTube URL, asks the user which category folder to save it in, checks for duplicates, and runs the transcript extraction script.

## Available Folders

1. **Starter_Story** - Starter Story podcast transcripts
2. **Inner_Work** - Inner Work content
3. **AI_Leaders** - AI Leaders content
4. **Founders** - Founders content
5. **My_First_Million** - My First Million content
6. **AI_Engineering** - AI Engineering content

## Process

1. **Get YouTube URL**: If user hasn't provided one, ask for it

2. **Validate URL**: Extract video_id and verify it's a valid YouTube link

3. **Show folder options**: Display the 6 available folders to the user

4. **Ask for folder selection**: Have user specify which folder to save to

5. **Check for duplicates**: 
   - Extract video_id from URL
   - Check if `{video_id}.md` already exists in `Knowledge_OS/<selected_folder>/Raw_Data/`
   - If duplicate found, notify user and ask if they want to overwrite or skip

6. **Run extraction**:
   ```
   python Knowledge_OS/scripts/Transcript_Extraction.py <youtube_url> Knowledge_OS/<selected_folder>/Raw_Data
   ```

7. **Skill chaining** (automatic):
   - After extraction, check if the selected folder has a corresponding analysis skill
   - If yes, automatically trigger that skill with the new .md file path
   - Pass control to the next skill

| Folder | Skill Triggered |
    |--------|----------------|
    | Starter_Story | starter-story |
    | Inner_Work | inner-work |
    | AI_Leaders | ai-leaders |
    | Founders | founders |
    | My_First_Million | my-first-million |
    | AI_Engineering | ai-engineering |

8. **Confirm success**: Report file saved location to user (or pass to next skill)

   **If NO skill chaining triggered** (folder has no analysis skill):
   - Push the transcript file to GitHub

   **If skill chaining IS triggered**:
   - The next skill will handle the Git push after processing
   - starter-story skill will push both the processed file and INDEX

### Git Push Workflow (No skill chaining)

```bash
cd Knowledge_OS
git add <selected_folder>/Raw_Data/<new_transcript_file.md>
git commit -m "Add transcript: <video_title>"
git push origin main
```

### Git Push Workflow (With skill chaining)

When starter-story or my-first-million skill completes, it will push:
```bash
git add <folder>/Process_data/<processed_file.md>
git add <folder>/INDEX.md
git commit -m "Add <skill_name>: <topic/guest>"
git push origin main
```

## Error Handling

- Invalid YouTube URL: Show error and ask for valid URL
- Transcript unavailable: Notify user and skip
- Script failure: Show error message and suggest retry

## Reference Files

- **`references/folder_structure.md`** - List of all folders with descriptions