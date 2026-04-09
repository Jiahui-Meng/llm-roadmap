# Health Agent 2.0

## What is this
A flagship LLM system project that demonstrates advanced RAG, hybrid retrieval, evidence grounding, and observability in a healthcare context.

## Architecture
```
query → intent understanding → hybrid retrieval (dense + graph + timeline)
     → evidence merge + rerank → grounded generation → cited answer + evidence panel
```

## Components
- `architecture.md` — system design overview
- `retrieval_design.md` — hybrid retrieval strategy (dense + graph + timeline)
- `evidence_panel.md` — citation and evidence traceability design
- `eval/testset_v1.json` — evaluation set (5 query types)
- `observability.md` — metrics and logging plan
- `prototype/` — first working retrieval path

## Why this project
Healthcare is a domain where:
- Grounding is safety-critical
- Multiple retrieval strategies are naturally needed
- Temporal and relational queries are common
- Evaluation and observability are non-negotiable

## Status
Design complete. Prototype scaffolded. Ready for implementation.

## Skills demonstrated
- RAG architecture design
- Hybrid retrieval (dense + graph + timeline)
- Evidence grounding and citation
- Evaluation design
- Observability planning
- System design thinking
