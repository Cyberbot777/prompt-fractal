# 🌌 Prompt Fractal

**Recursive Prompt Optimization Project — Featuring Iris, a Self-Reflective Prompt Agent**

---

## Overview

**Prompt Fractal** is an advanced AI project designed to automatically optimize, clarify, and refine prompts for large language models (LLMs) using recursive, self-referential prompting loops.

At its core is **Iris** — the self-reflective prompt optimization agent within Prompt Fractal.

Iris performs prompt self-improvement by:
- Analyzing a given prompt’s clarity, length, and effectiveness.
- Suggesting targeted improvements.
- Iteratively rewriting the prompt for maximum precision and minimal ambiguity.
- Saving its learning history to a memory system, allowing for continual evolution and optimization over time.

This project explores **recursive prompting** — where an LLM effectively teaches itself to write better prompts via structured self-review and refinement cycles.

---

## Key Features

- **Recursive Self-Improvement:**  
  Multi-pass prompt refinement via LLM-driven analysis and rewriting.

- **Prompt Simplification:**  
  Automatically removes unnecessary complexity, jargon, and vague phrasing.

- **Auto-Chaining Detection (Planned):**  
  Identifies when prompts should be split into smaller subtasks and suggests chaining.

- **Memory & Semantic Recall (Planned):**  
  Uses PostgreSQL + pgvector for semantic memory of prior prompt refinements.

- **Modular Design:**  
  Built for extensibility with LangChain as the core framework for agent logic and memory handling.

---

## Technologies Used

### Backend
- **Python 3.11** — Core programming language.
- **LangChain** — Agent framework for prompt chaining and task workflows.
- **OpenAI GPT-3.5 Turbo** — Initial language model for prompt refinement.
- **Docker** — Containerization for reproducible, isolated environments.

### Frontend (Planned)
- **React (Vite)** — Fast frontend framework for reactive UI.
- **Tailwind CSS** — Utility-first CSS for sleek, dark-themed styling.
- **Framer Motion** — Smooth animations and transitions.
- **React Markdown** — Renders LLM outputs in readable format.

### Database (Planned)
- **PostgreSQL** — Persistent memory storage for prompt histories.
- **pgvector** — Semantic vector search extension for PostgreSQL (future memory recall).

### DevOps / Infrastructure
- **Docker Compose** (Planned) — For multi-service orchestration (backend + DB + frontend).

---

## Docker Usage

Prompt Fractal uses Docker to containerize its backend environment.

### Build the Docker Image:
```bash
docker build -t prompt-fractal-backend ./backend
```

### Run the Iris Agent:
```bash
docker run --rm prompt-fractal-backend
```

Docker ensures that Iris runs in a clean, reproducible environment with all dependencies isolated — no local virtual environments required.

---

## Roadmap

### **Phase 1:** Prompt Simplification Agent (Active)
- [x] Multi-pass prompt simplification loop (3–5 iterations)
- [x] Meta-prompt templates for review and rewriting
- [ ] Initial memory schema (PostgreSQL)

### **Phase 2:** Auto-Chaining Recommender
- [ ] Agent detects multi-goal prompts and suggests chaining
- [ ] Auto-generates optimized sub-prompts (subtasks)

### **Phase 3:** Semantic Memory + Retrieval
- [ ] Integrate pgvector for semantic search of past prompts
- [ ] Enable knowledge transfer between similar prompts

### **Phase 4:** PromptPilot Integration (Optional)
- [ ] Connect Prompt Fractal to PromptPilot as an advanced lab feature

---

## Status

⚙️ **Early Research & Development Stage** — Experimental and evolving.  
The system is being built to function as both a research lab and practical tool for advanced AI prompt engineering.

---

## License

MIT License — Use freely, modify, and contribute.

---

## Author

Created and maintained by [Cyberbot777](https://github.com/Cyberbot777).
