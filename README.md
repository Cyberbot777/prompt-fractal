
# ♾️ Recursive

**Self-Refining Prompt Optimization System — Featuring Iris, the Recursive Prompt Agent**

---

## Overview

**Recursive** is an AI project that automatically optimizes, clarifies, and refines prompts for large language models (LLMs) using recursive, self-referential prompting loops.

At its core is **Iris** — the recursive prompt optimization agent.

Iris performs prompt self-improvement by:
- Analyzing prompts for clarity, length, and effectiveness.
- Providing detailed reviews with a clarity rating and specific improvement suggestions.
- Automatically rewriting prompts to improve focus, reduce ambiguity, and increase precision.
- Logging each review and rewrite cycle with timestamps for testing and analysis.
- Auto-stopping once a stable clarity rating is achieved to prevent over-refinement.

This project explores **recursive prompting** — where an LLM effectively teaches itself to write better prompts through structured self-review and refinement cycles.

---

## Key Features

- **Self-Reflective Prompt Review:**  
  Iris evaluates prompts for clarity, complexity, and ambiguity, providing detailed analysis.

- **Automatic Prompt Rewriting:**  
  Iris generates fully rewritten versions of prompts based on its review feedback.

- **Structured Test Logging:**  
  Logs test results with timestamps and phase labels for reproducible analysis.

- **Stability-Based Auto-Stop:**  
  Stops the refinement loop once stable clarity ratings (≥8) are detected across passes.

- **Modular, Extensible Design:**  
  Built for scalability with future multi-phase refinements and memory integrations.

---

## Technologies Used

### Backend
- **Python 3.11** — Core programming language.
- **OpenAI GPT-3.5 Turbo** — Current LLM used for analysis and rewriting.
- **Docker** — Containerization for reproducible, isolated environments.
- **dotenv** — Secure API key management.

### Frontend (Planned)
- **React (Vite)** — Fast frontend framework for interactive UI.
- **Tailwind CSS** — Utility-first CSS for sleek, dark-themed styling.
- **Framer Motion** — Smooth animations and transitions.
- **React Markdown** — Clean LLM output rendering.

### Database (Planned)
- **PostgreSQL** — Persistent memory storage for prompt histories.
- **pgvector** — Semantic vector search extension for PostgreSQL (for future memory recall).

### DevOps / Infrastructure
- **Docker Compose** (Planned) — For orchestrating multi-service environments.

---

## Docker Usage

Recursive runs fully inside Docker for consistency and isolation.

### Build the Docker Image:
```bash
docker build -t recursive-backend ./backend
```

### Run the Iris Agent:
```bash
docker run --rm --env-file ./backend/.env recursive-backend
```

---

## Testing & Stability Notes

For consistent auto-stop and test stability:
- All testing prompts **must include this instruction to Iris**:
  > Provide a clarity rating as a whole number from 1 to 10.

This ensures compatibility with the current score parser and prevents auto-stop issues.

---

## Roadmap

### **Phase 1:** Prompt Review + Rewriting Agent (Completed)
- [x] Single-pass prompt review and rewriting.
- [x] Test logging with timestamps and phase tracking.

### **Phase 2:** Multi-Pass Refinement + Auto-Stop (Active)
- [x] Multi-pass refinement loop with auto-stop.
- [x] Auto-stopping once stable high clarity rating is achieved.
- [ ] Additional case studies and dataset evaluation.

### **Phase 3:** Memory-Assisted Refinement (Planned)
- [ ] Integrate pgvector for semantic memory search.
- [ ] Enable prompt recall and prevent redundant refinements.

### **Phase 4:** Auto-Chaining Recommender (Planned)
- [ ] Detect multi-goal prompts and suggest task decomposition.
- [ ] Auto-generate sub-prompts for chained reasoning.

### **Phase 5:** PromptPilot Integration (Optional)
- [ ] Connect Recursive to PromptPilot as an advanced lab feature.

---

## Status

**Active Research & Development** — Experimental, but increasingly stable.

Recursive is now in active Phase 2 testing, capable of fully automated multi-pass refinement with intelligent auto-stop logic for real-world prompt optimization tasks.

---

## License

MIT License — Open for personal and commercial use, modification, and contributions.

---

## Author

Created and maintained by [Cyberbot777](https://github.com/Cyberbot777).
