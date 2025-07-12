
# ♾️ Recursive

**Self-Refining Prompt Optimization System — Featuring Iris, the Recursive Prompt Agent**

---

## Overview

**Recursive** is an AI research agent that automatically optimizes, clarifies, and refines prompts for large language models (LLMs) using structured, recursive prompting loops.

At its core is **Iris** — the recursive prompt optimization agent.

Iris performs self-improvement by:
- Analyzing prompts for clarity, length, and effectiveness.
- Providing structured reviews with clarity ratings and specific suggestions.
- Rewriting prompts to reduce ambiguity and improve precision.
- Logging every review and rewrite cycle for traceability.
- Auto-stopping when clarity improvements stabilize.

This project explores **recursive prompting** — where an LLM teaches itself to write better prompts through feedback, iteration, and memory.

---

## Technologies Used

### Core
- **Python** — Core logic and orchestration.
- **OpenAI API** — Prompt evaluation and embeddings (`text-embedding-3-small`).
- **Docker + Docker Compose** — Containerization and environment management.

### Database
- **PostgreSQL** — Persistent memory storage for prompt histories.
- **pgvector** — Semantic vector search extension for PostgreSQL (now fully integrated for vector memory storage).

---

## Features

- Recursive, multi-pass prompt optimization.
- Automatic clarity scoring and rewriting.
- Auto-stop mechanism when clarity stabilizes.
- Memory table for storing prompt embeddings.
- Dockerized backend and database.
- Planned: Prompt recall and memory-augmented refinement.
- Planned: Web UI for prompt testing.

---

## Vector Memory Testing

Iris now has a fully functional vector memory backend using PostgreSQL + pgvector.

The included `test_memory.py` script demonstrates:
- Fetching real text embeddings from OpenAI’s Embedding API.
- Saving vectorized memories into the database.
- Querying stored memories from the DB.

Example command to enter the DB and inspect:
```bash
docker-compose exec db psql -U iris_user -d iris_memory
```

Inside the DB terminal:
```sql
SELECT id, description FROM memories;
```

This system is ready for semantic recall and memory-augmented prompt refinement.

---

## Docker Usage

Recursive runs inside Docker for consistent dev and testing environments.

### Start (Backend + Vector Database):
```bash
docker-compose up --build -d
```

### Run Iris (Manually, On-Demand):
```bash
docker-compose exec backend python iris_agent.py
```

### Run Vector Memory Test:
```bash
docker-compose exec backend python test_memory.py
```

---

## Roadmap

### **Phase 1:** Prompt Refinement Core
- [x] Clarity scoring
- [x] Auto-rewriting
- [x] Recursive cycles
- [x] Auto-stop logic

### **Phase 2:** Embedding + Memory Storage
- [x] Integrate OpenAI embedding API
- [x] PostgreSQL + pgvector storage
- [x] Manual insert/query test

### **Phase 3:** Memory-Assisted Refinement (In Progress)
- [x] Integrate pgvector for semantic memory storage
- [ ] Enable prompt recall and prevent redundant refinements
- [ ] Memory-assisted prompt optimization

### **Phase 4:** Auto-Chaining Recommender (Planned)
- [ ] Detect multi-goal prompts and suggest task decomposition.
- [ ] Auto-generate sub-prompts for chained reasoning.

---
## Author

Created and maintained by [Cyberbot777](https://github.com/Cyberbot777).


