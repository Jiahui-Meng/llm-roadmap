# Future Topics (Not Yet in Main Plan)

This file tracks important LLM engineering topics that are worth learning, but are intentionally not yet inserted into the main roadmap.

The idea is to keep the main plan focused while preserving a clear backlog of high-value follow-up areas.

---

## Priority 1 — Most Valuable to Add Later

### 1. Evaluation / Benchmarking
Why it matters:
- Real LLM systems need measurable improvement, not just demos.
- Important for RAG, agent workflows, model comparisons, and prompt iteration.

Key subtopics:
- offline vs online evaluation
- retrieval metrics
- answer quality metrics
- faithfulness / grounding
- benchmark design
- failure analysis

Suggested place later:
- after advanced RAG
- before or alongside agent workflows

---

### 2. Observability / Tracing / Logging
Why it matters:
- Essential for debugging and productionizing RAG and agents.
- Makes systems feel like engineering projects rather than demos.

Key subtopics:
- retrieval trace
- tool trace
- prompt trace
- token / latency logging
- failure case capture
- experiment tracking

Suggested place later:
- around agent workflow week
- around flagship project development

---

### 3. Guardrails / Safety / Prompt Injection
Why it matters:
- Required for web-connected RAG and tool-using agents.
- Especially important for higher-trust or health-related systems.

Key subtopics:
- prompt injection basics
- unsafe tool invocation
- output validation
- trust boundaries for retrieved content
- human-in-the-loop checkpoints

Suggested place later:
- alongside agent workflows
- alongside structured output / validation

---

### 4. Structured Output / Validation
Why it matters:
- Many useful LLM systems need structured outputs, not free-form chat.
- Important for tool calls, JSON payloads, reports, and downstream automation.

Key subtopics:
- JSON schema basics
- constrained decoding
- parser recovery
- retry and validation loops
- typed output interfaces

Suggested place later:
- near SGLang / structured generation

---

## Priority 2 — Strong Follow-up Topics

### 5. Data Quality / Dataset Construction
Why it matters:
- RAG, LoRA, and evaluation all depend heavily on data quality.

Key subtopics:
- deduplication
- cleaning pipelines
- instruction formatting
- train/val/test split
- leakage awareness
- synthetic data vs real data

Suggested place later:
- near LoRA / QLoRA work
- near RAG ingestion work

---

### 6. DPO / RLHF / Preference Tuning
Why it matters:
- Important for post-training and alignment-focused roles.
- Less critical than RAG / serving / LoRA for current applied roadmap.

Key subtopics:
- preference data
- reward modeling basics
- DPO overview
- alignment trade-offs

Suggested place later:
- after LoRA / QLoRA
- as a separate post-training mini-module

---

### 7. GraphRAG
Why it matters:
- Especially useful for domains with explicit entities and relationships.
- Very relevant to Health Agent–style systems.

Key subtopics:
- entity extraction
- graph construction
- relation-aware retrieval
- hybrid graph + text pipelines

Suggested place later:
- near Health Agent 2.0

---

## Priority 3 — Useful But Not Current Mainline

### 8. Speculative Decoding / Advanced Decoding Optimization
Why it matters:
- Relevant for deeper inference / serving optimization.
- Better added after vLLM and quantization are already comfortable.

### 9. Multi-modal LLMs
Why it matters:
- Good long-term fit given prior CV / AR background.
- Not necessary before strong text-first LLM foundations are built.

### 10. Pretraining / Tokenizer Training / Scaling Laws
Why it matters:
- Important for foundation-model research directions.
- Lower priority for the current applied LLM engineering roadmap.

---

## Recommendation
If the roadmap is expanded later, the best next additions are:
1. Evaluation / Benchmarking
2. Observability / Tracing
3. Guardrails / Safety
4. Structured Output / Validation

These topics most directly improve project quality, interview depth, and production-readiness.
