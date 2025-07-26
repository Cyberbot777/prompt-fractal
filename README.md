# ♾️ Recursive

**Self-Refining Prompt Optimization System — Featuring Iris, the Recursive Prompt Agent**

---

## Overview

**Recursive** is a modular autonomous agent system for prompt optimization and transformation. At its core is **Iris**, an agent that performs iterative self-evaluation, rewriting, and clarity-based refinement of language model prompts. Iris operates independently using a multi-pass loop guided by clarity heuristics, semantic memory recall, and structured feedback.

Each refinement cycle evaluates the prompt for ambiguity, verbosity, or lack of detail, assigns a clarity score, and generates a rewritten version. The loop continues until clarity stabilizes. Final prompts are embedded using OpenAI’s `text-embedding-3-small` model and stored in a PostgreSQL vector database via `pgvector`, enabling long-term semantic memory.

A **Chain-of-Thought Decomposer module** is currently under active integration. This module handles complex or multi-phase prompts by detecting heuristic signal phrases (e.g., “compare and contrast,” “step-by-step,” “list and explain”). When triggered, the decomposer splits the input into discrete subtasks, refines each individually, and recomposes them into a linear CoT-style prompt. This prompt is then routed back into Iris for full recursive refinement and memory storage.

Recursive is designed not only as a standalone agent, but also as a foundational component in larger autonomous LLM systems. Its modular refinement process — including multi-pass scoring, memory-aware editing, and optional CoT preprocessing — can be applied to other agentic workflows, model families, or prompt transformation tasks requiring structure, clarity, and adaptability.

---

## Technologies Used

### Core
- **Python** — Core logic and orchestration.
- **OpenAI API** — Prompt evaluation and embeddings (`text-embedding-3-small`).
- **Docker + Docker Compose** — Containerization and environment management.

### Database
- **PostgreSQL** — Persistent memory storage for prompt histories.
- **pgvector** — Semantic vector search extension for PostgreSQL.

---

## Features

### Prompt Optimization
- Recursive, multi-pass prompt refinement.
- Automatic clarity scoring and rewriting.
- Auto-stop logic halts refinement when clarity score stabilizes.

### Memory Integration
- Final rewritten prompts are stored in a semantic vector database (pgvector).
- Memory-aware refinement uses top-N nearest matches for contextual improvement.
- Semantic similarity scoring avoids repeating previously seen ideas.

### Adaptive Agent Behavior
- **Memory-Aware Refinement**: Iris recalls top-rated prompts from history to guide new rewrites.
- **Adaptive Self-Improvement**: Iris becomes more effective over time using stored refinement examples.
- **Chain-of-Thought Decomposition**: Complex prompts are decomposed into subtasks, refined independently, and recomposed before recursive refinement.
- **Automatic Complexity Detection** *(in development)*: Heuristic signal routing detects multi-part prompts and triggers CoT decomposition.

### Tooling & Infrastructure
- Fully Dockerized backend and database system.
- **Empirical Validation Framework**: Logging and debug tools expose refinement steps, scores, and final outputs.

---

## Vector Memory Testing

Iris now includes a fully operational vector memory backend.

### Completed Milestones
- Final prompt storage confirmed in PostgreSQL using `pgvector`.
- Similarity scoring with cosine distance verified.
- Memory is being embedded using `text-embedding-3-small`.
- Embeddings are now normalized (confirmed via manual test script).
- Vector index (`hnsw` with `vector_cosine_ops`) created for fast retrieval.

### Example: Inspecting the Vector DB

```bash
docker-compose exec db psql -U iris_user -d iris_memory
```

Inside the DB shell:

```sql
-- View most recent stored prompts
SELECT id, description FROM memories ORDER BY id DESC;

-- Inspect vector column metadata
\d+ memories
SELECT * FROM pg_indexes WHERE tablename = 'memories';
```

---

## Semantic Recall Proof of Concept

In July 2025, Iris successfully demonstrated semantic memory recall:

1. A messy, informal prompt about zero-trust security was refined through multi-pass review and stored in memory.
2. A later prompt about firewall-based security produced a semantically similar embedding (distance ≈ 0.256).
3. With the system threshold set at 0.2, Iris chose not to reuse the match — but successfully located it, confirming accurate recall and filtering behavior.

Embeddings are generated using OpenAI’s `text-embedding-3-small`, stored as `vector(1536)` in PostgreSQL, and queried using cosine distance (`<=>`), with a tunable similarity threshold.

### Screenshots

![Semantic Memory Screenshot 1](tests/img/semantic1.png)  
![Semantic Memory Screenshot 2](tests/img/semantic2.png)

---

## Chain-of-Thought Decomposition Validation

In July 2025, we introduced a **Chain-of-Thought Prompt Decomposer** to support complex or multi-focus prompts.

When Iris detects heuristic signal phrases indicating a multi-step task, she routes the prompt through the decomposer:

1. The decomposer splits the prompt into standalone subtasks.
2. Each subtask is refined independently for clarity and precision.
3. Refined subtasks are recomposed into a coherent CoT-style prompt.
4. The final prompt is then returned to Iris for multi-pass refinement and scoring.

This entire decomposition-to-refinement pipeline was validated using **LangSmith**, confirming proper flow, traceability, and agentic behavior.

### Screenshots

![CoT Output](tests/img/CoTOutput.png)  
![CoT LangSmith Validation](tests/img/CoTvalidation.png)

---

## Docker Usage

Recursive runs entirely inside Docker for consistent development and testing across environments.

### 1. Environment Setup (One-Time Step)

```bash
cp backend/.env.example backend/.env
```

Then open `.env` and set your actual API key and any optional LangSmith variables:

```env
OPENAI_API_KEY=sk-...
LANGSMITH_TRACING=False
# Optional:
# LANGSMITH_ENDPOINT=https://api.smith.langchain.com
# LANGSMITH_API_KEY=your-key
# LANGSMITH_PROJECT=Recursive-Tracing
```

### 2. Start Backend and Vector Database

```bash
docker-compose up --build -d
```

### 3. Run Iris Agent

```bash
docker-compose exec backend python iris_agent.py
```

### 4. Run Chain-of-Thought Decomposer

```bash
docker-compose exec backend python prompt_decomposer.py
```

### 5. Initialize the Vector Database

```bash
docker-compose exec backend python init_db.py
```

### 6. Optional: Vector Norm Validation

```bash
docker-compose exec backend python phases/test_vector_norm.py
```

### 7. Optional: Legacy + Phase Testing

```bash
docker-compose exec backend python phases/single_pass.py
docker-compose exec backend python phases/test_memory.py
```

---

## Debugging and Tracing

Recursive includes two optional development toggles that control runtime logging and agent tracing. These can be configured in `iris_agent.py`, `prompt_decomposer.py`, or via environment variables.

### Available Toggles

```python
# Iris Debug Mode
DEBUG_MODE = True  # Set to False for clean output

# LangSmith Tracing
USE_TRACING = False  # Set to True to enable LangSmith integration
```

- `DEBUG_MODE`: Enables detailed refinement logs (clarity scores, issues, suggestions, rewritten prompts).
- `USE_TRACING`: Activates LangSmith observability for tracing agent flow and CoT pipelines.

### Example `.env` Configuration

```env
LANGSMITH_TRACING=False
LANGSMITH_API_KEY=your-key
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=Recursive-Tracing
```

---

## Roadmap

### **Phase 1: Prompt Refinement Core**
- [x] Implement clarity scoring
- [x] Add automatic rewriting logic
- [x] Enable recursive refinement cycles
- [x] Introduce auto-stop logic

### **Phase 2: Embedding + Memory Storage**
- [x] Integrate OpenAI Embedding API
- [x] Set up PostgreSQL with pgvector
- [x] Validate insert/retrieval of embeddings

### **Phase 3: Memory-Assisted Refinement**
- [x] Store only the final prompt in DB
- [x] Enable semantic recall with cosine similarity
- [x] Inject memory context during refinement
- [x] Tune threshold and top-N scoring
- [x] Prioritize high-scoring past prompts

### **Phase 4: Chain-of-Thought Preprocessing**
- [x] Build CoT decomposer module
- [x] Decompose prompts into subtasks
- [x] Refine/recombine into CoT prompt
- [x] Return to Iris for multi-pass refinement
- [x] Validate with LangSmith

### **Phase 5: Agent Routing Automation** *(In Progress)*
- [ ] Signal-based complexity detection in Iris
- [ ] Auto-route to decomposer
- [ ] Modularize Iris ⇄ Decomposer flow
- [ ] *(Optional)* Use LangGraph/dispatcher framework

### **Phase 6: Frontend + Deployment**
- [ ] Build minimal UI (Vite + Tailwind CSS)
- [ ] Submit prompts and view CoT via browser
- [ ] Add full-stack Docker support
- [ ] Deploy to Render, Fly.io, or VM

### **Phase 7: UX + Agent Insight Tools** *(Stretch)*
- [ ] Visualize refinement stages (scores/diffs)
- [ ] Show semantic memory matches and reuse
- [ ] Add CoT subtask visualization
- [ ] Toggle debug output
- [ ] Save/export refinement sessions

---

## Author

This project is designed and maintained by [Cyberbot777](https://github.com/Cyberbot777), a full stack engineer and AI systems developer specializing in agentic architectures, LLM optimization, and autonomous prompt engineering pipelines.
