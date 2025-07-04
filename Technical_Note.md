# Technical Note: Recursive Prompt Optimization System

**Project Codename:** Recursive\
**GitHub Repo:** [Cyberbot777/recursive](https://github.com/Cyberbot777/recursive)

---

## Overview

This document provides a full technical snapshot of the Recursive project, including:

- Current architecture & capabilities
- Completed features and experiments
- Auto-stop mechanism (design + behavior)
- Planned features and next phases
- Recovery guidance for future developers

It serves as a permanent reference for future development, debugging, and continuity.

---

## Project Summary

Recursive is a self-refining prompt optimization system designed to:

- Analyze LLM prompts for clarity, complexity, and ambiguity
- Provide clarity ratings and improvement suggestions
- Automatically rewrite prompts for increased focus and precision
- Run recursive, multi-pass refinement cycles

At its core is **Iris**, the recursive prompt optimization agent.

---

## Current Backend Structure

```
recursive/
├── backend/
│   ├── iris_agent.py       # Core Iris Agent logic (multi-pass refinement + auto-stop)
│   ├── requirements.txt    # Backend dependencies
│   ├── Dockerfile          # Container setup for backend
│   └── .env.example        # Example env file for API keys
│
├── tests/                  # Folder for manual logs and experiment results (manual copy/paste)
│
├── docs/                   # Documentation folder (planned)
│
└── Technical_Note.md       # This file
```

---

## Key Features (Completed)

### Phase 1: Single-Pass Prompt Review + Rewrite

- Clarity analysis
- Suggestions for improvement
- Rewritten prompt output
- Timestamped console output

### Phase 2: Multi-Pass Refinement (Recursive Loop)

- Recursive prompt refinement up to N passes
- Auto-stop mechanism based on clarity score stability
- Configurable number of passes and stop threshold
- Debugging logs for clarity score flow
- Supports both Phase 1 (single-pass) and Phase 2 (multi-pass)

---

## Auto-Stop Mechanism: Technical Explanation

### Purpose

Stops recursive refinement when clarity stabilizes, saving resources.

### Logic

- Extracts numeric **Clarity Rating** from LLM output (integer 1-10)
- Stops automatically if two consecutive passes satisfy:

```
current_score >= auto_stop_score
AND
previous_score >= auto_stop_score - 1
```

Default `auto_stop_score`: **9**

### Rationale

Allows early stop with flexibility (tolerates slight scoring shifts).

### Debugging Behavior

- Prints current/previous scores after each pass
- Prints an auto-stop message when triggered

---

## Case Studies & Testing Logs

### Purpose

To study Iris' real-world performance:

- Evaluate stability, clarity gains, and recursive behavior
- Compare messy vs refined prompts

### Data Sources

- Manual test logs stored in `/tests/`
- Structured case studies (Phase 2 Auto-Stop Experiments)

### Example Topics Tested:

- Becoming a lawyer
- Driver's license application

---

## Known Limitations (Documented)

- Clarity ratings can slightly fluctuate due to LLM variability
- Recursive refinement beyond 9/10 can sometimes over-optimize (overly verbose prompts)
- Logs must currently be copied manually from the console

---

## Planned Roadmap (Next Phases)

### Phase 3: Semantic Memory (Planned)

- Integrate PostgreSQL + pgvector
- Store prompt refinements for retrieval and learning

### Phase 4: Auto-Chaining Recommender (Planned)

- Detect multi-goal prompts
- Suggest task decomposition

### Phase 5: Frontend & Multi-Model Support (Planned)

- React + Tailwind frontend
- Model selector for GPT-3.5, GPT-4, Claude, etc.

---

## Development Notes & Recovery Guidance

### How to Resume Development

1. Clone repo from GitHub
2. Start backend via Docker:

```bash
docker build -t recursive-backend ./backend
docker run --rm --env-file ./backend/.env recursive-backend
```

3. Code entrypoint: `backend/iris_agent.py`

### Key Files To Know

- `iris_agent.py` — Main recursive agent logic
- `/tests/` — Manual logs + test results
- `/docs/` — Future documentation area

### Environment Variables

```
OPENAI_API_KEY=your-api-key
```

---

## Summary

Recursive is currently an experimental but functional backend tool for recursive prompt refinement, with auto-stop capabilities and a clear technical direction.

This file serves as the authoritative, technical reference for the project.

---

Maintained by: [Cyberbot777](https://github.com/Cyberbot777)

