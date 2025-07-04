# 🌌 Prompt Fractal

**Recursive Prompt Optimization Agent — Refines, Simplifies, and Self-Evolves Prompts through Iterative LLM Self-Prompting Loops**

---

## Overview

**Prompt Fractal** is an advanced AI agent designed to automatically optimize, clarify, and refine prompts for large language models (LLMs) using recursive, self-referential prompting loops.

It performs prompt self-improvement by:
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

## Why Prompt Fractal?

Most prompts written by humans — even advanced users — suffer from:
- Overcomplexity
- Ambiguity
- Ineffective or redundant instructions
- Hallucination-prone structures

While prompt chaining and few-shot prompting help, **Prompt Fractal** takes a different approach:
- It **automatically rewrites prompts** to be shorter, clearer, and more effective, using its own recursive loops.
- It can optionally recommend chaining when appropriate, offering both prompt optimization and structural decomposition.

This approach allows LLM agents to *self-train their prompting ability* over time — minimizing manual engineering.

---

## Core Workflow

```
flowchart TD
  A[User provides raw prompt] --> B[Agent analyzes prompt]
  B --> C[Agent rewrites prompt for clarity & brevity]
  C --> D[Test improved prompt (optional)] 
  D --> E{Max iterations reached?}
  E -- No --> B
  E -- Yes --> F[Save prompt & results to memory]
```

---

## Technologies

| Component            | Description                                          | Tools/Tech                             |
|----------------------|------------------------------------------------------|---------------------------------------|
| LLM Engine           | Language model for self-refinement loops             | GPT-3.5 Turbo (initial prototype)     |
| Agent Framework      | Prompt chaining & control logic                      | LangChain                             |
| Memory Storage       | Stores prompts, revisions, and results               | PostgreSQL + pgvector (semantic memory) |
| Future Models        | Advanced reasoning & fine-tuning                     | Claude Opus, GPT-4 (optional later)   |

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

**Early Research & Development Stage** — Experimental and evolving.  
The system is being built to function as both a research lab and practical tool for advanced AI prompt engineering.

---

## License

MIT License — Use freely, modify, and contribute.

---

## Author

Created and maintained by [Cyberbot777](https://github.com/Cyberbot777).
