---
name: me493b-course-structure
description: >
  Reference for all structural, naming, and repository conventions for
  ME 493B "AI in Product Development" at UW Bothell (Spring 2026).
  Consult this file before creating any course file, notebook, folder,
  or spec document. Covers repo layout, file naming, notebook structure,
  spec document format, GitHub Classroom workflow, Canvas integration,
  and Copilot interaction patterns.
---

# ME 493B Course Structure Reference

## Course identity
- **Course:** ME 493B — AI in Product Development
- **Institution:** University of Washington Bothell
- **Term:** Spring 2026 (March 30 – June 5, 20 sessions, TTh 3:30–5:30 PM)
- **Instructor:** Scott Thielman, PhD (thielman@uw.edu)
- **Room:** UW1 041
- **Enrollment:** 24 students max
- **Credits:** 4

---

## Course architecture

### The Five Pillars (recurring vocabulary and rubric dimensions)

| Pillar | Short definition |
|--------|----------------|
| **Goal & Direction** | Specifying intent, writing requirements, directing AI toward outcomes |
| **Context Management** | RAG, memory, information architecture — what the model knows |
| **Tools & Integration** | MCP, APIs, function calling, skills, connections to engineering systems |
| **Centaur Engineering** | Human-AI collaboration where the combination exceeds either alone |
| **Evaluation & Trust** | Verifying AI outputs at every scale, from response to full workflow |

### The Five Building Blocks (foundational concepts from "How AI Thinks" module)

These are the cognitive operations that underpin all AI systems. Taught in
MP1 Part A and referenced throughout the course:

| Building Block | What it means | Where it recurs |
|---|---|---|
| **Representation** | Turning real things into numbers | Embeddings in RAG (MP2), JSON tool schemas (MP3), multimodal image encoding (MP3-MP4) |
| **Similarity** | Measuring how alike two things are | Document retrieval (MP2), tool selection by description (MP3), output evaluation (MP4) |
| **Prediction** | Estimating unknowns from patterns | LLM next-token prediction, generative design, AI tool-call decisions (MP3) |
| **Classification** | Sorting things into categories | Routing decisions, quality evaluation, trust calibration (MP4) |
| **Search & Retrieval** | Finding relevant items in a large space | RAG (MP2), RAG-as-tool exposed to AI agents (MP3), attention in Transformers |

### Product Development Spine

The course follows the engineering development lifecycle. Each phase maps to a
mini-project as the primary scope, though pillars recur across all MPs:

1. **Foundation: How AI Thinks** (Weeks 1-2, Sessions 1-4) → MP1 (Goal & Direction)
2. **Discover & Frame** (Weeks 3-4, Sessions 5-8) → MP2 (Context Management)
3. **Design & Explore** (Weeks 5-6, Sessions 9-12) → MP3 (Tools & Integration)
4. **Build & Integrate** (Weeks 7-8, Sessions 13-16) → MP4 (Centaur Engineering)
5. **Test & Trust** (Week 9, Sessions 17-18) → MP4 continued (Evaluation & Trust)
6. **Present & Reflect** (Week 10) → MP5 (team final, all pillars)

This module structure mirrors the Canvas module organization:
Module 1: Foundation · Module 2: Discover & Frame · Module 3: Design & Explore ·
Module 4: Build & Integrate · Module 5: Test & Trust · Module 6: Present & Reflect

### Foundation Module: "How AI Thinks" (Weeks 1-2, Sessions 1-4)

Sessions 1-4 teach ML fundamentals as background for engineering decisions:
- Session 1: "Welcome to the Future" — course vision, AI timeline, five pillars
- Session 2: "From Data to Representations" — vectors, embeddings, training
- Session 3: "The Architecture of Intelligence" — tokens, Transformers, attention
- Session 4: "Mythos and ML Regression" — Mythos discussion + regression / loss / overfitting in a notebook

---

## Assessment structure

| Assignment | Type | Points | Timeline | Pillar emphasis |
|-----------|------|--------|----------|----------------|
| hello_world | Setup (pass/fail) | 10 | Week 1 | Goal & Direction (intro) |
| MP1 | Individual, 2 weeks | 100 | Weeks 1-2 | Goal & Direction |
| MP2 | Individual, 2 weeks | 100 | Weeks 3-4 | Context Management |
| MP3 | Individual, 2 weeks | 100 | Weeks 5-6 | Tools & Integration |
| MP4 | Individual, 2 weeks | 100 | Weeks 7-9 | Centaur Engineering + Eval & Trust |
| Quiz 1 | In-class | 100 | Session 10 (Apr 30) | Foundation + Pillars 1-2 |
| Quiz 2 | In-class | 100 | Thu, May 28 (Session 18) | Pillars 3-5 |
| News Discussion | Rotating | 100 | All quarter | All pillars |
| MP5 / Final Presentation | Team (3-4), live | 300 | Week 10 | All pillars |
| **Total** | | **1,000** | | |

### Mini-project structure (MP1-MP4)

Each MP = **100 points**, **two-week timeline**, two parts:
- **Part A (50 pts):** Guided instructional exercise (Jupyter notebook) with
  learn→explore→solve pattern. Includes HOMEWORK cells with verifiable answers.
- **Part B (50 pts):** Applied engineering design problem evaluated across all
  five pillars with weighted emphasis. Constrained shared scenario for MP1-MP3;
  more open for MP4-MP5.

**Both Part A and Part B share a single due date** — 13 days after assignment,
due at 11:59 PM. There is no separate Part A checkpoint.

MP1-MP3 use multi-part guided format. MP4-MP5 give students more freedom.
Mini-projects ARE the homework — there is no separate homework category.

### Mini-project schedule

| MP | Assigned | Due (11:59 PM) | Pillar emphasis |
|----|----------|----------------|-----------------|
| MP1 | Tue, March 31 (Session 1) | Mon, April 13, 11:59 PM | Goal & Direction |
| MP2 | Tue, April 14 (Session 5) | Mon, April 27, 11:59 PM | Context Management |
| MP3 | Tue, April 28 (Session 9) | Fri, May 15, 11:59 PM | Tools & Integration |
| MP4 | Tue, May 12 (Session 13) | Fri, May 29, 11:59 PM | Centaur + Eval & Trust |
| MP5 | Fri, May 29 (kickoff after MP4 closes) | Thu, June 4 (presentation day) | All pillars (team) |

Note: MP1–MP3 each follow a two-week Tuesday-to-Friday cycle (assigned
Tuesday, due 11:59 PM eleven days later on the Friday before the next
MP launches). MP4 was extended by three days (due Fri May 29 instead of
Tue May 26) to give students an extra weekend after the MP3 deadline
shift; MP5 kicks off the day MP4 closes and presents Thursday June 4.

### Part A notebook pattern: Learn → Explore → Solve

Every section in a Part A notebook follows this arc:
1. **TEACH:** Pre-written code with rich commentary. Student runs and observes.
   Start at lowest dimensionality (2D), use intuitive data first.
2. **EXPLORE:** `# ✏️ YOUR TURN` cells with guided experiments.
3. **SOLVE:** `# 🎯 HOMEWORK` cells where students write code to answer a
   specific question with a verifiable answer (a name, number, or ranking).

**Pattern shift starting MP2:** From MP2 onward, students write most of the
code themselves rather than running pre-written cells. Code cells are empty
with clear instructions in the preceding markdown. The Setup cell remains
pre-written. The "TEACH/EXPLORE/SOLVE" structure is preserved conceptually but
the student is the author of the SOLVE code, not just the writer of the answer.
This shift is appropriate as students gain comfort with the toolchain.

**Visibility-as-deliverable pattern starting MP3:** From MP3 onward, when the
notebook involves AI tool use (function calling, agent loops, MCP), the
proof-of-work is a printed transcript captured by a logging helper. The
transcript IS the evidence. Graders look at structured cell output showing
[TOOL CALL] / [TOOL RESULT] / [AI RESPONSE] lines. For host-side workflows
(vision review, CAD interaction), the visibility evidence shifts to
markdown + screenshot + response text — same principle, different medium.

### Part A grading (50 points)

| Component | Points | Criteria |
|-----------|--------|----------|
| Completion & Experimentation | 30 | All cells run. YOUR TURN cells show experimentation. HOMEWORK cells have working code with correct answers. |
| Reflections | 20 | Thoughtful reflections demonstrating observation and connection to course concepts. |

(MP3+ adjusts the breakdown by section based on proof-of-work transcripts;
see the per-MP spec for exact point allocation.)

### Part B grading (50 points)

Evaluated across all five pillars with weighted emphasis:

| Pillar | MP1 | MP2 | MP3 | MP4 |
|--------|-----|-----|-----|-----|
| Goal & Direction | ★★★ | ★★ | ★★ | ★★ |
| Context Mgmt | ★ | ★★★ | ★★ | ★★ |
| Tools & Integration | ★ | ★ | ★★★ | ★★ |
| Centaur Engineering | ★★ | ★ | ★★ | ★★★ |
| Evaluation & Trust | ★★ | ★★ | ★★ | ★★★ |

---

## MP1 specifics (completed)

### MP1 Part A: "Under the Hood — How AI Thinks"
- Jupyter notebook teaching five building blocks (representation, similarity,
  prediction, classification, search)
- Five HOMEWORK problems with verifiable answers, progressing in complexity
- Uses fruits/movies/snacks for concept teaching, engineering data for application
- Real embedding model: `sentence-transformers` with `all-MiniLM-L6-v2`
- Capstone homework integrates all five sections into a mini search engine
- Spec: `specs/SPEC_MP1_PartA.md`

### MP1 Part B: "MiniClaw Gear Train Design"
- Framed as a design brief from "Jordan Chen, Engineering Manager, ACME Robotics"
- Students design a scaled-down 3D-printable version of the Hiwonder BigClaw gripper
- Key constraints: ~20% scale-down, PLA/PETG, hand-driven input wheel, 5-8N grip
- Deliverables: goal statement, design iteration log, calculation script, trust assessment
- Reference: https://www.hiwonder.com/products/bigclaw-mechanical-gripper
- Separate design brief document provided alongside assignment document

---

## MP2 specifics (completed)

### MP2 Part A: "The Information Problem — Building a RAG Pipeline"
- Jupyter notebook teaching the full RAG pipeline: tokens, embeddings,
  chunking, vector storage, retrieval, generation
- Pattern shift: students author the code themselves with proof-of-work outputs
- Document corpus: fictional "Ridgeline Engineering Partners" (~20 documents
  with buried specific facts students retrieve)
- Stack: `tiktoken` (tokens) → `sentence-transformers` (embeddings) →
  `chromadb` (vector store) → GitHub Models API via `openai` SDK (generation)
- Capstone: query "Attention Is All You Need" with the RAG pipeline they built
- Spec: `specs/SPEC_MP2_PartA.md`

### MP2 Part B: "Context Management for the MiniClaw Project"
- In-world follow-up memo from Jordan Chen (research directive after the
  initial gear design from MP1)
- Students apply RAG skills to a MiniClaw-specific corpus (`acme_miniclaw_corpus.py`,
  ~15 fictional ACME documents with project-specific facts)
- Deliverables: project intake document (PCS framework), information strategy,
  context package with before/after demo, research synthesis, working PRD
- Spec: `specs/SPEC_MP2_PartB.md`

---

## MP3 specifics (current project)

### MP3 Part A: "Tools, Skills, and the AI as Conductor"
- Jupyter notebook teaching: function calling, skill anatomy and authoring,
  RAG-as-tool wrapping, host-based vision review, and skill-driven composition
  of multiple programmatic tools
- Centerpiece: the `run_with_logging()` helper provided in the Setup cell.
  Wraps GitHub Models API calls, captures multi-turn tool-use loops, and
  prints structured transcripts. Sections 1, 2, 3, 5 are graded from these
  transcripts. Section 4 uses host-side evidence (markdown + screenshot +
  response text) instead.
- Sections: (1) Function Calling, (2) Anatomy of a Skill, (3) Wrap Your RAG
  as a Tool [centerpiece], (4) Vision in the Loop (host-based — Copilot Chat,
  Claude.ai, etc., not API), (5) Composition Capstone (programmatic tools
  only — RAG + unit converter), (6) Reflections
- Stack additions: GitHub Models API for function calling. Reuses MP2's RAG
  via a starter ChromaDB collection. **No new Python dependencies for MP3
  Part A.**
- Vision is delivered through the AI host UI of the student's choice
  (Copilot Chat in VS Code is the default; Claude.ai, Claude Desktop,
  Cursor, ChatGPT all accepted). No vision API plumbing in Python — the
  same workflow Part B uses for CAD review.
- Spec: `specs/SPEC_MP3_PartA.md`

### MP3 Part B: "Productize Your Engineering Stack"
- In-world memo from Jordan Chen — productize MP2 work for the team. New
  juniors and Maria Santos in fab need access to your context without you.
- Four deliverables:
  1. Two skills minimum (markdown files codifying student's MiniClaw workflow)
  2. MCP server exposing MiniClaw RAG as a tool, connected to a host
     (Copilot agent mode recommended; Claude Desktop / Cursor accepted)
  3. CAD interaction documentation — 3 checkpoints on a real subassembly,
     using any CAD tool, with AI review at each
  4. Reflection with "trust ledger"
- Visibility evidence: server logs (`logs/server.log`), host UI screenshots
  showing tool calls, exported conversation transcripts
- Starter packages provided: `miniclaw_starter_rag/` (corpus + retrieval),
  `mcp_server_starter/` (working server.py + host configs), `cad_demo_reference.md`
- Spec: `specs/SPEC_MP3_PartB.md`

### MP3 stack at a glance

| Layer | What students build | Where it lives |
|-------|--------------------|----------------|
| Skills | Markdown files codifying workflow | `MP3/Part B/skills/*.md` |
| MCP server | Python script exposing RAG as a tool | `MP3/Part B/mcp_server/server.py` |
| Logs | Auto-generated proof of tool invocations | `MP3/Part B/mcp_server/logs/server.log` |
| Host | Copilot agent mode / Claude Desktop / Cursor | (configured externally; config snippet committed) |
| RAG | Their MP2 work or the provided starter | `MP3/Part B/miniclaw_starter_rag/` or their MP2 path |
| CAD | Whatever they have access to | Screenshots in `MP3/Part B/cad_review/` |

---

## MP4 framing (planned)

### MP4: "Centaur Engineering — From Stack to Subassembly"
- Pillar emphasis: Centaur ★★★ + Evaluation & Trust ★★★
- Students inherit their own MP3 stack: 2+ skills, MCP server with RAG tool,
  configured host
- Deliverable: a documented design iteration on a MiniClaw subassembly using
  the stack
- Required: minimum 5 documented centaur loops. Each loop = goal stated, AI
  consulted with skills active, AI output captured, human evaluation,
  decision, next iteration
- Required: explicit evaluation pass — at least one design check the AI got
  wrong and they caught, and at least one place the AI added genuine value
  beyond what they would have caught alone
- Output: a subassembly that's spec-complete (CAD model + drawing or
  annotated screenshots + verified key calcs)
- Spec: TBD (not yet drafted)

---

## GitHub infrastructure

### Accounts and repos
- **Instructor GitHub:** dr-thielman
- **Classroom org:** me493b-spring2026
- **Template repo:** dr-thielman/ai-in-pd-spring2026 (must be public)
- **Student repos:** Private, auto-created in me493b-spring2026 org

### Critical GitHub Classroom lessons learned
- Template repo must live under **dr-thielman** (personal account),
  NOT under the classroom org (circular reference error)
- Do NOT set "Supported editor" when creating assignments (causes save error)
- Starter code can only be set during initial assignment creation —
  cannot be added or changed afterward; delete and recreate if needed
- Students do NOT need to be pre-added to the org — invitation link
  grants access automatically

---

## Repository folder structure

```
ai-in-pd-spring2026/                 ← lives under dr-thielman
├── hello_world.ipynb                ← setup lesson, repo root
├── README.md                        ← student-facing setup instructions
├── requirements.txt                 ← shared Python deps
├── SKILL_me493b_course_structure.md ← this file (visible to students; teaching artifact for MP3+)
├── .devcontainer/
│   └── devcontainer.json            ← Codespaces config
│
├── specs/                           ← visible to students (Goal & Direction examples)
│   ├── SPEC_hello_world.md
│   ├── SPEC_MP1_PartA.md
│   ├── SPEC_MP2_PartA.md
│   ├── SPEC_MP2_PartB.md
│   ├── SPEC_MP3_PartA.md
│   ├── SPEC_MP3_PartB.md
│   └── ...
│
├── MP1/
│   ├── Part A/
│   │   └── MP1_PartA_Under_the_Hood.ipynb
│   └── Part B/
│       └── (reference data, BigClaw specs, etc.)
│
├── MP2/
│   ├── Part A/
│   │   └── MP2_PartA_The_Information_Problem.ipynb
│   └── Part B/
│       ├── acme_miniclaw_corpus.py
│       └── ...
│
├── MP3/
│   ├── Part A/
│   │   ├── MP3_PartA_Tools_Skills_Conductor.ipynb
│   │   ├── skills/
│   │   ├── images/
│   │   ├── starter_rag/
│   │   ├── transcripts/
│   │   └── section4_screenshots/
│   └── Part B/
│       ├── miniclaw_starter_rag/
│       ├── mcp_server_starter/
│       ├── skills/                  ← student-authored
│       ├── mcp_server/              ← student's working server
│       ├── cad_review/              ← student's CAD interaction docs
│       └── cad_demo_reference.md
│
├── MP4/
│   ├── Part A/
│   └── Part B/
│
└── MP5/
```

---

## File naming conventions

### Notebooks
| Convention | Example |
|-----------|---------|
| `MP{N}_Part{X}_Descriptive_Name.ipynb` | `MP1_PartA_Under_the_Hood.ipynb` |
| `hello_world.ipynb` | Setup lesson at repo root |

### Spec documents
| Convention | Example |
|-----------|---------|
| `SPEC_MP{N}_Part{X}.md` | `SPEC_MP1_PartA.md` |

- All specs live in `specs/` folder
- UPPERCASE prefix `SPEC_` makes them visually distinct

### Assignment documents (Word)

Two documents per MP, distributed via Canvas (NOT committed to the GitHub repo):

| Convention | Example |
|-----------|---------|
| `MP{N}_{Title}.docx` (course-facing assignment) | `MP1_The_First_Build.docx`, `MP2_Context_Management.docx`, `MP3_The_Engineering_Stack.docx` |
| `MP{N}_PartB_{Scenario}.docx` (in-world memo from Jordan Chen) | `MP1_PartB_Design_Brief.docx`, `MP2_PartB_Research_Directive.docx`, `MP3_PartB_Productize_Memo.docx` |

The course-facing assignment doc covers Part A summary + Part B details + rubric.
The in-world memo is a standalone professional engineering document with no
course mechanics — it's what Jordan Chen would actually send to a team.

### Skills (MP3+)

| Convention | Example |
|-----------|---------|
| `skills/{snake_case_name}.md` (or `.cursorrules`, `.github/copilot-instructions.md` etc.) | `skills/miniclaw_context_query.md` |

Format isn't standardized across hosts (Anthropic SKILL.md, Cursor rules,
Copilot custom instructions all do similar things). Students may use any
host-appropriate format; the course evaluates the *concept* (codified
reusable orchestration), not a specific filename convention.

---

## Spec document format

Every notebook must have a corresponding spec in `specs/`. Specs serve
two purposes: (1) build instructions for Claude Code to generate the
notebook, and (2) visible to students as Goal & Direction examples.

### Required spec sections (see SPEC_hello_world.md for a complete example)

1. **Header:** Notebook filename, course, author, file locations
2. **Purpose:** What this notebook teaches (1-3 sentences)
3. **Primary pillar emphasis**
4. **Student prerequisites**
5. **Tone**
6. **Session alignment:** Which lecture sessions this connects to
7. **Notebook structure:** Section-by-section breakdown with:
   - The question the section answers
   - Data to use (self-contained, no external files)
   - Concepts to teach (start low-dimensional, intuitive data first)
   - YOUR TURN experiments (specific things to try)
   - HOMEWORK problems (definite verifiable answers)
   - Dig Deeper keywords and AI prompts
   - Forward connections to later course content
8. **Grading alignment**
9. **Technical requirements**
10. **Build notes for Claude Code**

---

## Notebook authoring rules

### Code cells
- Pre-written TEACH cells: full working code with rich inline comments
- YOUR TURN cells: clear instructions with specific things to try
- HOMEWORK cells: starter scaffolding with `# YOUR CODE HERE` placeholders
  and `print()` statements so cells run without errors but produce
  placeholder output students must replace
- Variable names and data that carry forward must be noted in the spec
- **MP2+ pattern:** code cells in non-Setup sections are mostly empty;
  students author the code with clear instructions in the markdown above.
  Setup cell, helpers (e.g., `run_with_logging`), and data-loading cells
  remain pre-written.

### Markdown cells
- Cells students must edit: prefix with **✏️ YOUR TURN** or **🎯 HOMEWORK**
- Every formula shown alongside a concrete numerical example
- No jargon without inline definition on first use
- Forward connection callouts: "You'll see this again when..."
- Include Codespace save warning in submission section

### Copilot interaction — platform agility
Students explore inline completion, Copilot Chat, Copilot CLI, and from
MP3 onward, Copilot agent mode (or alternative hosts like Claude Desktop /
Cursor for MCP work). Do NOT prescribe a single mode. The ability to find
effective AI interaction patterns is itself a learning objective.

### Cell ordering
- All notebooks must run top-to-bottom without errors in a fresh Codespace
- No hidden state dependencies
- Package installs use try/except with `--break-system-packages`

---

## Devcontainer configuration

```json
{
  "name": "ME 493B — AI in Product Development",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "customizations": {
    "vscode": {
      "extensions": [
        "GitHub.copilot",
        "GitHub.copilot-chat",
        "ms-python.python",
        "ms-toolsai.jupyter"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "editor.inlineSuggest.enabled": true,
        "github.copilot.enable": { "*": true, "jupyter": true }
      }
    }
  },
  "postCreateCommand": "pip install -r requirements.txt"
}
```

## Standard requirements.txt

Cumulative across MPs (each MP may rely on dependencies introduced earlier):

```
# Foundation (MP1)
numpy
pandas
matplotlib
scikit-learn
sentence-transformers
jupyter

# RAG pipeline (MP2)
tiktoken
chromadb
openai

# Tools & Integration (MP3 Part B only — MCP server starter)
mcp
fastmcp
```

`mcp` and `fastmcp` are needed only for MP3 Part B (the MCP server starter).
**MP3 Part A introduces no new Python dependencies** — it uses the existing
`openai` SDK against GitHub Models for function calling, and delivers vision
review through the AI host UI rather than a Python image library.
Authentication for the GitHub Models API uses the student's existing GitHub
PAT with `models:read` scope (no new dependency, just an environment
variable).

---

## External APIs and authentication

### GitHub Models API (introduced in MP2, central to MP3 Part A)
- Free tier available to all GitHub accounts (rate-limited)
- OpenAI-compatible — used via the `openai` Python SDK
- Authentication: GitHub Personal Access Token (PAT) with `models:read` scope
- **Recommend a tier, not a SKU.** As of April 2026 the verified-stable
  choice for tool-calling is `openai/gpt-4.1` (capabilities include
  `tool-calling` and large context). Cost-sensitive alternatives if
  exposed: `openai/gpt-4.1-mini`, `openai/gpt-5-mini`. The catalog
  evolves; verify at https://models.github.ai/catalog/models when
  building any MP that depends on a specific model and pin the ID at
  build time.
- **Anthropic Claude models are NOT in the GitHub Models catalog.**
  Claude is accessed through host-side tools (Copilot Chat, Claude.ai,
  Claude Desktop) — not through the programmatic API students hit from
  notebooks. Note that Claude availability in the GitHub Student
  Developer Pack via Copilot has been unstable as of April 2026; do
  not assume Claude availability for required work.
- **Vision in MP3 Part A is delivered host-side** (Copilot Chat,
  Claude.ai, Claude Desktop, Cursor, ChatGPT — student's choice). The
  notebook does not call vision APIs directly. This both simplifies the
  technical stack and matches the Part B workflow for CAD review.
- Rate limits: verify current limits at build time (typical free-tier
  limits are tight enough that a class of 24 each making ~10–20 calls
  needs to be considered)

### MCP hosts (MP3 Part B)
- **Recommended:** GitHub Copilot agent mode in VS Code (verify configuration
  syntax at MP3 launch — Copilot's user-MCP support has been moving)
- **Accepted alternatives:** Claude Desktop (most stable MCP support),
  Cursor, Continue.dev
- Students document which host they used and commit the relevant config snippet

---

## Student submission workflow

```
1. Canvas: read assignment instructions
2. Canvas: click GitHub Classroom invitation link
3. GitHub: auto-creates private repo
4. GitHub: open repo → Code → Codespaces → New codespace
5. Codespaces: complete notebook
6. Codespaces: commit and push via Source Control GUI
7. Canvas: paste GitHub repo URL as Website URL submission
8. Instructor: review on GitHub, enter grade in Canvas
```

---

## Cumulative lessons learned (across MPs)

These are the meta-patterns that emerged from designing MP1 → MP3.
New MPs should preserve these where they apply.

- **Productize, don't restart.** Each MP builds on the artifacts of the
  prior. MP2's RAG is wrapped as a tool in MP3. MP3's stack is used to run
  the centaur loop in MP4. Avoid the "start from scratch every two weeks"
  pattern that produces shallow work.

- **Start with intuitive data, scale to engineering.** Fruits/movies/snacks
  teach the concept; engineering data shows the application. This applies
  to every MP Part A.

- **Generic Part A, applied Part B.** Part A teaches mechanics on a
  contained generic example. Part B applies the mechanics to the MiniClaw
  scenario. Same pattern across MP1-MP3.

- **Visibility is the lesson for tool use.** When the AI's behavior happens
  inside an API loop or an external host, the deliverable must be a
  captured transcript or log file. Without explicit visibility artifacts,
  graders cannot verify tool use happened. The `run_with_logging()` helper
  in MP3 Part A is the template for programmatic visibility; markdown +
  screenshot + response text is the template for host-side visibility.

- **Skills are the durable abstraction.** MCP, function calling, specific
  models, and specific products will be replaced. The idea of "encoding
  workflow as a reusable orchestration artifact that any AI session can
  apply" is the durable concept. Teach the idea; let the syntax follow.

- **Recommend a tier, not a SKU.** Specific model IDs age fast (sometimes
  in weeks). The course should specify "a current OpenAI tool-calling
  model on GitHub Models" and pin the exact ID at build time. Same logic
  applies to host recommendations and library versions.

- **Don't force ML where physics suffices.** Don't train regression
  models on problems where Lewis bending stress gives the answer. ML
  should add genuine value, not replace straightforward calculations.

- **Constrained scenarios reduce grading burden.** Shared problem
  scenarios (MiniClaw across MP1-MP4) make 24 submissions comparable.
  Open format reserved for MP5.

- **Homework problems must have definite answers.** "Reflect on what you
  observed" doesn't work for engagement or grading. "Which item is most
  similar to X? Report the answer" works.

- **The iteration log / transcript is the real pedagogical artifact.**
  Asking for real-time collaboration documentation teaches that directing
  AI is a process, not a single prompt. This generalizes to any
  AI-augmented engineering work.

- **In-world scenarios beat abstract problem statements.** The "memo from
  Jordan Chen" pattern (engineering manager assigning the next phase of
  work) makes assignments feel real. Maintain across all Part B documents.

- **Provide starters so nobody is blocked.** Each MP that depends on prior
  MP output (MP3 needs MP2's RAG) ships a working starter so a student
  who didn't fully complete the prior MP isn't gated out.

- **Use the host for what hosts do well.** Vision review, image input,
  multimodal grounding — modern AI hosts handle this cleanly with
  paste-and-ask. Don't replicate that in Python just to make it
  "programmatic" if the lesson is the workflow, not the plumbing.

---

## What NOT to do

- Do not put solution code in student-facing notebooks
- Do not commit executed notebooks to the template repo
- Do not use Google Colab — course uses GitHub Codespaces exclusively
- Do not reference Claude Code in student materials — students use Copilot
  (Claude Code is the instructor's authoring tool, not a student tool)
- Do not use hyphens in notebook filenames (use underscores)
- Do not set a Supported editor in Classroom assignments
- Do not host the template repo in the classroom org
- Do not use ML where physics or known equations suffice — ML should
  add genuine value, not replace straightforward calculations
- Do not train models on problems where lookup tables give the answer
- Do not let MP3+ rubrics drift toward grading the CAD output or the
  retrieved-fact accuracy. The graded artifact is the AI interaction
  evidence (transcripts, logs, screenshots) — not the engineering output.
- Do not assume Claude availability through GitHub Copilot for required
  work — Claude availability in the Student Developer Pack has been
  unstable. Recommend Claude as one accepted host option among several,
  not as the prescribed path.
