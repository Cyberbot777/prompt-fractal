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
- Saving final prompts to a vector database with OpenAI embeddings.
- Comparing new prompts to historical memory using semantic similarity.

This project explores **recursive prompting** — where an LLM teaches itself to write better prompts through feedback, iteration, and memory.

---

## Technologies Used

### Core
- **Python** — Core logic and orchestration.
- **OpenAI API** — Prompt evaluation and embeddings (`text-embedding-3-small`).
- **Docker + Docker Compose** — Containerization and environment management.

### Database
- **PostgreSQL** — Persistent memory storage for prompt histories.
- **pgvector** — Semantic vector search extension for PostgreSQL (now fully integrated and operational).

---

## Features

- Recursive, multi-pass prompt optimization.
- Automatic clarity scoring and rewriting.
- Auto-stop mechanism when clarity stabilizes.
- Memory system stores **only the final rewritten prompt** in the vector DB.
- Semantic similarity comparison to detect previously seen ideas.
- Fully Dockerized backend and database system.
- In-progress memory-assisted refinement based on similarity scoring.

---

## Vector Memory Testing

Iris now includes a fully operational vector memory backend.

### Completed Milestones
- Final prompt storage confirmed in PostgreSQL using `pgvector`
- Similarity scoring with cosine distance verified
- Memory is being embedded using `text-embedding-3-small`
- Embeddings are now normalized (confirmed via manual test script)
- Vector index (`hnsw` with `vector_cosine_ops`) created for fast retrieval

### Example: Inspecting the Vector DB

```bash
docker-compose exec db psql -U iris_user -d iris_memory
```

Then inside the DB shell:

```sql
SELECT id, description FROM memories ORDER BY id DESC;
```

To inspect vector column metadata:

```sql
\d+ memories
SELECT * FROM pg_indexes WHERE tablename = 'memories';
```

---

## Semantic Recall Proof of Concept

In July 2025, Iris was successfully tested with automatic semantic memory recall:

1. A messy informal prompt about zero trust security was refined through multi-pass review and stored in memory.
2. A later prompt about firewall-based security was semantically similar (distance ≈ 0.256).
3. Because the system threshold was set to 0.2, Iris chose not to reuse the match — but correctly located it, demonstrating accurate recall behavior.

Memory is embedded via OpenAI’s `text-embedding-3-small`, stored in PostgreSQL as `vector(1536)`, queried using cosine distance via `<=>`, and filtered by a tunable similarity threshold.

### Screenshots

![Semantic Memory Screenshot 1](frontend/public/semantic1.png)
![Semantic Memory Screenshot 2](frontend/public/semantic2.png)

---

## Docker Usage

Recursive runs inside Docker for consistent dev and testing environments.

### Start Backend + Vector DB:

```bash
docker-compose up --build -d
```

### Run Iris Agent:

```bash
docker-compose exec backend python iris_agent.py
```

### Optional: Vector Norm Check

You can run a norm test script to ensure embeddings are unit vectors:

```bash
docker-compose exec backend python test_vector_norm.py
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
- [x] Save only final rewritten prompt to DB
- [x] Enable semantic recall via vector similarity
- [x] Use memory during refinement to avoid repeating known ideas
- [ ] Improve memory recall quality (threshold tuning, N-best ranking, logging)

### **Phase 4:** Auto-Chaining Recommender (Planned)
- [ ] Detect multi-goal prompts and suggest task decomposition
- [ ] Auto-generate sub-prompts for chained reasoning


---

## Author

Created and maintained by [Cyberbot777](https://github.com/Cyberbot777).

