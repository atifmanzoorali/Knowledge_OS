# Docs Folder Organization Plan

## Goal
Organize the docs folder into clear categories for easier navigation and maintenance.

---

## Current Structure

```
docs/
├── Plans/
│   ├── Self_Heal_Plan.md
│   ├── Code_Qqality_Plan.md
│   └── DB_Plan.md
├── Root level (14 files):
  - Design_Philosophy.md
  - ARCHITECTURE.md, system-overview.md
  - testing-guide.md, Capacity_Analysis.md
  - workflow.md, GETTING_STARTED.md, index.md
  - Improvement.md, Rating_Assessment.md, Rating_Assessment_v2.md
```

---

## Proposed Structure

```
docs/
├── Philosophy/
│   └── Design_Philosophy.md
├── Technical/
│   ├── ARCHITECTURE.md
│   ├── system-overview.md
│   ├── testing-guide.md
│   └── Capacity_Analysis.md
├── User_Guide/
│   ├── workflow.md
│   ├── GETTING_STARTED.md
│   └── index.md
├── Planning/
│   ├── Improvement.md
│   ├── Rating_Assessment.md
│   └── Rating_Assessment_v2.md
└── Plans/
    ├── Self_Heal_Plan.md
    ├── Code_Qqality_Plan.md
    └── DB_Plan.md
```

---

## Category Descriptions

| Category | Purpose | Files |
|----------|---------|-------|
| **Philosophy** | Why we built it, design decisions | Design_Philosophy.md |
| **Technical** | Architecture, system details, testing | ARCHITECTURE.md, system-overview.md, testing-guide.md, Capacity_Analysis.md |
| **User_Guide** | How to use the system | workflow.md, GETTING_STARTED.md, index.md |
| **Planning** | Future work, assessments | Improvement.md, Rating_Assessment.md, Rating_Assessment_v2.md |
| **Plans/** | Implementation plans (already done) | Self_Heal_Plan.md, Code_Qqality_Plan.md, DB_Plan.md |

---

## Implementation Steps

### Step 1: Create Category Folders
- Create `docs/Philosophy/`
- Create `docs/Technical/`
- Create `docs/User_Guide/`
- Create `docs/Planning/`

### Step 2: Move Files
- Move Design_Philosophy.md → Philosophy/
- Move ARCHITECTURE.md, system-overview.md, testing-guide.md, Capacity_Analysis.md → Technical/
- Move workflow.md, GETTING_STARTED.md, index.md → User_Guide/
- Move Improvement.md, Rating_Assessment.md, Rating_Assessment_v2.md → Planning/

### Step 3: Verify
- Check all files are in correct folders
- Verify no files left in docs root (except README if exists)

---

## Success Criteria

- [ ] All docs organized into 5 categories
- [ ] No orphaned files in docs root
- [ ] Clear navigation purpose for each category

---

*Plan Created: 2026-05-03*