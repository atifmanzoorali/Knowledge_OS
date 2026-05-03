---
name: add-content-folder
description: "When the user wants to 'add a new folder', 'create new content category', 'add new skill folder', or needs to create a new category folder with corresponding analysis skill for organizing Knowledge_OS content."
---

# Add Content Folder

Creates a new folder structure with corresponding analysis skill for organizing Knowledge_OS content. Follows the same pattern as existing folders.

---

## Trigger Phrases

- "add a new folder"
- "create new content category"
- "add new skill folder"
- "create folder for [topic]"
- "[topic] folder"

---

## Workflow

### --- AWAITING INPUT ---

Please provide the **new folder name**.

> 💡 **Example:** `AI_Products` or `Fitness` or `Book_Summaries`

**After folder name is provided, I will:**

1. Validate folder doesn't already exist
2. Ask for optional description/purpose
3. Ask if user wants custom sections in the analysis skill
4. Create folder structure
5. Create analysis skill
6. Update Process_Link skill
7. Update main AGENTS.md

---

### --- CREATING FOLDER ---

Creating folder structure:

- `{Folder_Name}/`
  - AGENTS.md
  - INDEX.md
  - Raw_Data/
  - Process_data/

---

### --- CREATING SKILL ---

Creating analysis skill:

- `Skills/{folder_name}/SKILL.md`

---

### --- UPDATING REFERENCES ---

Updating:

- `Skills/Process_Link/SKILL.md` (add folder to available folders & skill chaining)
- `Knowledge_OS/AGENTS.md` (add folder to list)

---

### --- COMPLETE ---

✅ **Folder created:** `Knowledge_OS/{Folder_Name}/`
✅ **Skill created:** `Skills/{Folder_Name}/SKILL.md`
✅ **Process_Link updated** with new folder
✅ **AGENTS.md updated**
✅ **Changes pushed to GitHub**

---

## Step-by-Step Process

### Step 1: Get Folder Name

1. Ask user for new folder name
2. Validate: folder name format (Pascal_Case or snake_case)
3. Check folder doesn't already exist in Knowledge_OS/

### Step 2: Get Optional Customizations

Ask user:

1. **Description (optional):** What is this folder for?
2. **Custom sections (optional):** Any specific sections to add in the analysis skill template beyond defaults?

**Default sections:**
- Executive Summary
- Key Insights
- Action Items
- Resources

### Step 3: Create Folder Structure

Create:
```
Knowledge_OS/{Folder_Name}/
├── AGENTS.md
├── INDEX.md
├── Raw_Data/
└── Process_data/
```

### Step 4: Create Analysis Skill

Create: `Knowledge_OS/Skills/{Folder_Name}/SKILL.md`

Template sections:
- name, description (with trigger phrases)
- Storage Location
- Workflow States (AWAITING INPUT → ANALYZING → COMPLETE)
- Extraction Workflow
- Template Structure
- INDEX Format
- Confidence Scoring
- Formatting Rules

### Step 5: Update Process_Link Skill

Update `Skills/Process_Link/SKILL.md`:

1. Add folder to "Available Folders" list
2. Add to Skill Chaining table

### Step 6: Update AGENTS.md

Update `Knowledge_OS/AGENTS.md`:

1. Add folder to "Available Folders" list (line 15-22)
2. Add to "Skill Chaining" table (line 39-46)

### Step 7: Git Push

```bash
cd Knowledge_OS
git add {Folder_Name}/
git add Skills/{Folder_Name}/
git add Skills/Process_Link/SKILL.md
git add AGENTS.md
git commit -m "Add folder: {Folder_Name} with analysis skill"
git push origin main
```

---

## Error Handling

- **Folder exists:** Show error, ask for different name
- **Invalid name:** Show error, suggest Pascal_Case format
- **Git conflict:** Show error, ask to resolve manually

---

## References

- Existing skills for reference: `Skills/starter-story/SKILL.md`, `Skills/my-first-million/SKILL.md`
- Folder AGENTS.md templates: `Starter_Story/AGENTS.md`, `Inner_Work/AGENTS.md`

---

*Last Updated: 2026-05-03*