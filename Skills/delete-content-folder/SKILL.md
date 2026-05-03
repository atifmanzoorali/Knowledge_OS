---
name: delete-content-folder
description: "When the user wants to 'delete a folder', 'remove content folder', 'delete skill', or needs to delete a content folder along with its related skill and all references. This is a CRITICAL operation that requires user confirmation."
---

# Delete Content Folder

Deletes a content folder, its related skill, and all references. This is a CRITICAL operation - user MUST confirm before any deletion.

---

## Trigger Phrases

- "delete a folder"
- "remove content folder"
- "delete skill"
- "delete [Folder_Name] folder"

---

## Protected Folders (Cannot be deleted)

- Process_Link
- add-content-folder
- delete-content-folder

---

## Workflow

### --- AWAITING INPUT ---

Please provide the **folder name to delete**.

> 💡 **Example:** `AI_Products` or `Inner_Work`

**List of deletable folders:**
- Starter_Story
- Inner_Work
- AI_Leaders
- Founders
- My_First_Million
- AI_Engineering

**After folder name is provided, I will:**

1. Validate folder exists
2. Verify folder is not protected
3. Show contents and ask for confirmation
4. If confirmed: Delete folder, skill, and all references
5. If not confirmed: Cancel gracefully

---

### --- CONFIRMING ---

Show contents and ask for confirmation:

```
⚠️ DELETE: {Folder_Name}

Contents in folder:
- {X} Raw transcripts in Raw_Data/
- {X} Processed profiles in Process_data/

This will DELETE:
- Knowledge_OS/{Folder_Name}/ (entire folder)
- Skills/{Folder_Name}/ (skill folder)

This will UPDATE:
- Skills/Process_Link/SKILL.md
- Knowledge_OS/AGENTS.md
- Skills/AGENTS.md
- Skills/README.md

After this, search index will be rebuilt.

Type "{Folder_Name}" to confirm deletion:
```

---

### --- DELETING ---

Deleting files:

- ❌ Deleting `Knowledge_OS/{Folder_Name}/`
- ❌ Deleting `Skills/{Folder_Name}/`

---

### --- UPDATING REFERENCES ---

Updating process files:

- 📝 Updating `Skills/Process_Link/SKILL.md`
- 📝 Updating `Knowledge_OS/AGENTS.md`
- 📝 Updating `Skills/AGENTS.md`
- 📝 Updating `Skills/README.md`

---

### --- REBUILDING INDEX ---

Rebuilding search index:

```bash
python search/index.py
```

---

### --- COMPLETE ---

✅ **Folder deleted:** `Knowledge_OS/{Folder_Name}/`
✅ **Skill deleted:** `Skills/{Folder_Name}/`
✅ **References updated**
✅ **Search index rebuilt**
✅ **Pushed to GitHub**

---

## Step-by-Step Process

### Step 1: Get Folder Name

1. Ask user for folder name to delete
2. Validate: folder exists in Knowledge_OS/
3. Verify: folder is not protected

### Step 2: List Contents

1. Count files in `Raw_Data/`
2. Count files in `Process_data/`
3. Show summary to user

### Step 3: Get Confirmation (CRITICAL)

1. Display deletion warning
2. Ask user to type folder name exactly
3. If mismatch: Cancel operation
4. If match: Proceed with deletion

### Step 4: Delete Folder

Delete: `Knowledge_OS/{Folder_Name}/`

```bash
rm -rf Knowledge_OS/{Folder_Name}/
```

### Step 5: Delete Skill

Delete: `Skills/{Folder_Name}/`

```bash
rm -rf Skills/{Folder_Name}/
```

### Step 6: Update Process_Link

Update `Skills/Process_Link/SKILL.md`:

1. Remove from "Available Folders" list
2. Remove from "Skill Chaining" table

### Step 7: Update AGENTS.md

Update `Knowledge_OS/AGENTS.md`:

1. Remove from "Available Folders" list (lines 15-22)
2. Remove from "Skill Chaining" table (lines 39-46)

### Step 8: Update Skills AGENTS.md

Update `Skills/AGENTS.md`:

1. Remove skill section

### Step 9: Update Skills README.md

Update `Skills/README.md`:

1. Remove from skills table
2. Remove skill section (if exists)

### Step 10: Rebuild Search Index

```bash
python search/index.py
```

### Step 11: Git Push

```bash
cd Knowledge_OS
git add -A
git commit -m "Delete folder: {Folder_Name}"
git push origin main
```

---

## Error Handling

| Error | Action |
|-------|--------|
| Folder doesn't exist | Show error, list valid folders |
| Protected folder | Show error, cannot delete |
| User cancels | Show message, no changes made |
| Git conflict | Show error, resolve manually |

---

## References

- Existing folder AGENTS.md for content reference: `Starter_Story/AGENTS.md`, `Inner_Work/AGENTS.md`
- Process_Link skill: `Skills/Process_Link/SKILL.md`

---

*Last Updated: 2026-05-03*