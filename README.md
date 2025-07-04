# ♾️ Recursive

**Self-Refining Prompt Optimization System — Featuring Iris, the Recursive Prompt Agent**

---

## Overview

**Recursive** is an AI project designed to automatically optimize, clarify, and refine prompts for large language models (LLMs) through recursive, self-referential prompting loops.

At its core is **Iris** — the recursive prompt optimization agent within Recursive.

Iris performs prompt self-improvement by:
- Analyzing prompts for clarity, length, and effectiveness.
- Providing detailed reviews with a clarity rating and specific improvement suggestions.
- Automatically rewriting prompts to improve focus, reduce ambiguity, and increase precision.
- Logging each review and rewrite cycle with timestamps for future analysis.
- Auto-stopping once a stable clarity rating is achieved to prevent over-refinement.

This project explores **recursive prompting** — where an LLM effectively teaches itself to write better prompts through structured self-review and refinement cycles.

---

## Key Features

- **Self-Reflective Prompt Review:**  
  Iris evaluates prompts for clarity, complexity, and ambiguity, providing detailed analysis.

- **Automatic Prompt Rewriting:**  
  Iris generates fully rewritten versions of prompts based on its review feedback.

- **Structured Test Logging:**  
  Logs test results with timestamps and phase labels for future reference.

- **Stability-Based Auto-Stop:**  
  Stops the refinement loop once stable clarity ratings (≥8) are detected across passes.

- **Modular, Extensible Design:**  
  Built for scalability to support multi-phase refinement and future integrations.

---

## Technologies Used

### Backend
- **Python 3.11** — Core programming language.
- **OpenAI GPT-3.5 Turbo** — Current LLM used for analysis and rewriting.
- **Docker** — Containerization for a reproducible, isolated environment.
- **dotenv** — Secure API key management.

### Frontend (Planned)
- **React (Vite)** — Fast frontend framework for interactive UI.
- **Tailwind CSS** — Utility-first CSS for sleek, dark-themed styling.
- **Framer Motion** — Smooth animations and transitions.
- **React Markdown** — For clean LLM output rendering.

### Database (Planned)
- **PostgreSQL** — Persistent memory storage for prompt histories.
- **pgvector** — Semantic vector search extension for PostgreSQL (future memory recall).

### DevOps / Infrastructure
- **Docker Compose** (Planned) — For orchestrating multi-service setups.

---

## Docker Usage

Recursive runs fully inside Docker.

### Build the Docker Image:
```bash
docker build -t recursive-backend ./backend
```

### Run the Iris Agent:
```bash
docker run --rm --env-file ./backend/.env recursive-backend
```

Docker ensures that Iris operates in a clean, reproducible environment without requiring local virtual environments.

---

## Roadmap

### **Phase 1:** Prompt Review + Rewriting Agent (Completed)
- [x] Single-pass prompt review and rewriting.
- [x] Test logging with timestamps and phase tracking.

### **Phase 2:** Multi-Pass Refinement + Auto-Stop (Active)
- [x] Multi-pass refinement loop with auto-stop.
- [x] Auto-stopping once stable high clarity rating is achieved.
- [ ] Additional case studies and dataset evaluation.

### **Phase 3:** Auto-Chaining Recommender
- [ ] Detect multi-goal prompts and suggest chaining.
- [ ] Auto-generate optimized sub-prompts for subtasks.

### **Phase 4:** Semantic Memory + Retrieval
- [ ] Integrate pgvector for semantic memory search.
- [ ] Enable recall and knowledge transfer between similar prompts.

### **Phase 5:** PromptPilot Integration (Optional)
- [ ] Connect Recursive to PromptPilot as an advanced lab feature.

---

## Status

**Active Research & Development** — Experimental but increasingly stable.

Recursive is now in Phase 2 development, capable of fully automated multi-pass refinement with intelligent auto-stop logic, making it usable for real-world prompt optimization.

---

## License

MIT License — Open for personal and commercial use, modification, and contribution.

---

## Author

Created and maintained by [Cyberbot777](https://github.com/Cyberbot777).
