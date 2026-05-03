# Workflow Documentation

This document provides detailed workflow diagrams and explanations for all system operations.

---

## Table of Contents

1. [Main Processing Workflow](#main-processing-workflow)
2. [Transcript Extraction Flow](#transcript-extraction-flow)
3. [Skill Processing Flow](#skill-processing-flow)
4. [Search Workflow](#search-workflow)
5. [Git Integration Flow](#git-integration-flow)

---

## Main Processing Workflow

### Overview

```mermaid
flowchart TD
    subgraph Input["1. Input"]
        YT[YouTube URL]
        F[Folder Selection]
    end

    subgraph Extract["2. Extraction"]
        TE[Transcript Extractor]
        MD[Markdown Generator]
    end

    subgraph Route["3. Routing"]
        SR[Skill Router]
    end

    subgraph Process["4. Processing"]
        AS[Analysis Skill]
        T[Template Engine]
    end

    subgraph Store["5. Storage"]
        RD[(Raw_Data/)]
        PD[(Process_data/)]
        IX[INDEX.md]
    end

    subgraph Index["6. Indexing"]
        SI[Search Indexer]
        CD[(ChromaDB)]
    end

    subgraph Backup["7. Backup"]
        GC[Git Commit]
        GP[Git Push]
    end

    YT --> TE
    F --> SR
    TE --> MD
    MD --> RD
    RD --> SR
    SR --> AS
    AS --> T
    T --> PD
    PD --> IX
    PD --> SI
    SI --> CD
    IX --> GC
    PD --> GC
    GC --> GP
```

---

## Transcript Extraction Flow

### Sequence Diagram

```mermaid
sequenceDiagram
    participant U as User
    participant P as Transcript_Extraction.py
    participant Y as yt-dlp
    participant T as YouTubeTranscriptApi
    participant F as File System

    U->>P: Run with URL + folder
    P->>P: Parse video_id from URL
    
    P->>Y: Fetch video metadata
    Y-->>P: title, channel, duration
    
    P->>T: Request transcript
    T-->>P: transcript data
    
    P->>F: Generate markdown file
    Note over F: Raw_Data/video_id_title.md
    
    P-->>U: Done! File saved
```

### Code Flow

```python
# Transcript_Extraction.py flow:
1. Parse command line args (url, output_dir)
2. Extract video_id from URL
3. Use yt-dlp to get metadata
4. Use YouTubeTranscriptApi to get transcript
5. Generate markdown with YAML frontmatter
6. Write to file
7. Return success
```

### Error Scenarios

| Error | Cause | Handling |
|-------|-------|----------|
| Invalid URL | Malformed YouTube link | Exit with error message |
| No transcript | Video has no captions | Exit with error message |
| Folder not exists | Invalid folder path | Create folder or exit |

---

## Skill Processing Flow

### Skill Routing Logic

```mermaid
flowchart LR
    subgraph Input["Raw Transcript"]
        RT[.md file]
    end

    subgraph Router["Determine Skill"]
        FI[Folder Name]
        SW{Which Folder?}
    end

    subgraph Skills["Select Skill"]
        SS[starter-story]
        AL[ai-leaders]
        F[founders]
        MFM[my-first-million]
        AE[ai-engineering]
        IW[inner-work]
    end

    RT --> FI
    FI --> SW
    
    SW -->|Starter_Story| SS
    SW -->|AI_Leaders| AL
    SW -->|Founders| F
    SW -->|My_First_Million| MFM
    SW -->|AI_Engineering| AE
    SW -->|Inner_Work| IW
```

### Skill Processing Steps

```mermaid
flowchart TD
    subgraph Input["Skill Input"]
        PF[Profile .md path]
    end

    subgraph Read["1. Read"]
        RF[Read file]
        EP[Extract person/topic]
    end

    subgraph Analyze["2. Analyze"]
        DT[Detect type]
        EK[Extract key info]
    end

    subgraph Generate["3. Generate"]
        GT[Generate using template]
        VA[Validate output]
    end

    subgraph Save["4. Save"]
        WR[Write profile]
        UI[Update INDEX]
    end

    PF --> RF
    RF --> EP
    EP --> DT
    DT --> EK
    EK --> GT
    GT --> VA
    VA --> WR
    WR --> UI
```

### Template Examples

#### Starter Story Template
```markdown
# 🚀 [Founder]: [Company]

[Executive Summary]

# 📊 The Product
[What was built, the gap, unfair advantage]

# 🛠️ Tech Stack & Process
[Tools, build process, time to profit]

# 🎯 Distribution
[First 100 users, scaling engine]

# 🧠 Frameworks & Lessons
[Mental models, key lessons]

# 📈 Key Metrics
[Revenue, growth, team size]
```

#### Founders Template
```markdown
# 📝 Full Context
[Who, what the episode covers]

# 📚 Books & References
[Books written BY, written ABOUT, mentioned]

# 🏛️ Their Founder Thesis
[Core philosophy]

# 💭 Key Lessons
[4-5 main lessons]

# 💬 Notable Quotes
[Best quotes from episode]

# 🚀 Journey & Achievements
[Background, milestones]

# 🏆 Key Metrics
[Company, revenue, growth]
```

---

## Search Workflow

### Index Building Flow

```mermaid
flowchart TD
    subgraph Scan["1. Scan"]
        GF[Find all .md files]
        CF[Category folders]
    end

    subgraph Read["2. Read"]
        OF[Open each file]
        SF[Strip frontmatter]
    end

    subgraph Encode["3. Encode"]
        EM[Load embedding model]
        VE[Vectorize content]
    end

    subgraph Store["4. Store"]
        CC[ChromaDB client]
        CR[Create/Update collection]
    end

    GF --> CF
    CF --> OF
    OF --> SF
    SF --> EM
    EM --> VE
    VE --> CC
    CC --> CR
```

### Search Query Flow

```mermaid
sequenceDiagram
    participant U as User
    participant Q as answer_search.py
    participant M as Sentence-Transformers
    participant C as ChromaDB
    participant F as File System

    U->>Q: "how did marc lou validate"
    Q->>M: encode(query)
    M->>C: query_vectors
    
    C->>Q: top_k results (documents, metadata)
    
    Q->>F: get source file paths
    Q-->>U: Display results with sources
```

### Search Code Logic

```python
# answer_search.py logic:
1. Parse query from CLI
2. Load sentence-transformers model
3. Encode query → vector
4. Query ChromaDB collection
5. Get top K results
6. Display with relevance scores
7. Show source file paths
```

---

## Git Integration Flow

### Automatic Commit Workflow

```mermaid
flowchart TD
    subgraph Trigger["Trigger"]
        NS[New skill processing complete]
    end

    subgraph Prepare["Prepare"]
        GF[git status]
        GD[git diff]
        GM[git log for format]
    end

    subgraph Stage["Stage Files"]
        AFP[Add processed file]
        AIX[Add INDEX.md]
    end

    subgraph Commit["Commit"]
        CM[Create commit message]
        CC[git commit]
    end

    subgraph Push["Push"]
        GP[git push origin main]
    end

    NS --> GF
    GF --> GD
    GM --> AFP
    AFP --> AIX
    AIX --> CM
    CM --> CC
    CC --> GP
```

### Commit Message Format

| Content Type | Format | Example |
|--------------|--------|---------|
| Transcript | `Add transcript: [title]` | Add transcript: How Roger Federer Works |
| Starter Story | `Add starter story: [founder] - [company]` | Add starter story: Marc Lou - 35 Startups |
| AI Leaders | `Add AI Leaders: [Person] - [Topic]` | Add AI Leaders: Evan Spiegel - Snap |
| Founders | `Add Founders: [Person] - [Topic]` | Add Founders: Roger Federer - Tennis |
| My First Million | `Add My First Million: [Guest/Topic]` | Add My First Million: Chad Gruns |
| AI Engineering | `Add AI Engineering: [Framework/Concept]` | Add AI Engineering: Agentic Engineering |
| Inner Work | `Add Inner Work: [Teacher] - [Topic]` | Add Inner Work: Rabbi Friedman - Love |

---

## Error Handling Workflow

### Processing Errors

```mermaid
flowchart TD
    subgraph Try["Try"]
        EX[Execute process]
    end

    subgraph Catch["Catch Errors"]
        CE{Error?}
    end

    subgraph Handle["Handle"]
        E1[Invalid URL] --> UE[Show usage]
        E2[No transcript] --> NE[Notify user]
        E3[Skill failure] --> LE[Log error]
        E4[Git failure] --> RE[Retry or skip]
    end

    subgraph Recovery["Recovery"]
        UC[Continue]
        AN[Ask new URL]
    end

    EX --> CE
    CE -->|Yes| E1
    CE -->|Yes| E2
    CE -->|Yes| E3
    CE -->|Yes| E4
    CE -->|No| UC
    
    UE --> AN
    NE --> AN
    LE --> UC
    RE --> UC
```

---

## Complete End-to-End Example

### Input
```
YouTube URL: https://www.youtube.com/watch?v=g2-duG1-Jxc
Folder: Founders
```

### Steps Executed

| Step | Action | Output |
|------|--------|--------|
| 1 | Extract video_id | `g2-duG1-Jxc` |
| 2 | Fetch metadata | title: "How Roger Federer Works" |
| 3 | Get transcript | Full transcript text |
| 4 | Save to Raw_Data | `g2-duG1-Jxc_How_Roger_Federer_Works..md` |
| 5 | Trigger founders skill | Analyze transcript |
| 6 | Generate profile | Roger-Federer-Tennis-2026.md |
| 7 | Update INDEX | New row added |
| 8 | Commit to Git | "Add Founders: Roger Federer - Tennis" |
| 9 | Push to GitHub | Remote updated |
| 10 | Rebuild index | ChromaDB updated |

### Output Files

**Raw Data:**
```
Founders/Raw_Data/g2-duG1-Jxc_How_Roger_Federer_Works..md
```

**Processed Profile:**
```
Founders/Process_data/Robbi-Federer-Tennis-2026.md
```

**Updated Index:**
```
Founders/INDEX.md (new entry)
```

---

*Last Updated: 2026-05-02*