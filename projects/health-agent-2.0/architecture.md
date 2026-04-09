# Health Agent 2.0 — Architecture

## Vision
Re-scope Health Agent as a flagship LLM system that demonstrates multiple advanced techniques working together:
- RAG with hybrid retrieval
- Graph-based knowledge relationships
- Timeline-aware querying
- Evidence grounding and citation
- Observability

## Architecture Overview

```
user query
-> query understanding (intent + entity extraction)
-> hybrid retrieval
   ├── vector retrieval (dense embeddings)
   ├── graph retrieval (entity relationships)
   └── timeline retrieval (temporal ordering)
-> evidence merge + rerank
-> grounded generation with citations
-> evidence panel output
```

## Why Health Agent is a good flagship project
1. It naturally requires multiple retrieval strategies
2. Medical data has strong temporal and relational structure
3. Grounding and citation are not optional — they're safety-critical
4. It showcases RAG, structured generation, tool calling, and evaluation in one system

## Core modules
- **Ingestion**: parse clinical notes, lab results, medication lists
- **Indexing**: vector index + knowledge graph + timeline index
- **Retrieval**: hybrid retrieval with configurable weights
- **Generation**: grounded answers with citation references
- **Evaluation**: correctness, citation quality, hallucination rate
- **Observability**: latency, token usage, tool selection logging

## Design principles
- Every answer must cite its source
- Temporal queries (e.g., "what changed since last visit?") must use timeline retrieval
- Relationship queries (e.g., "what medications interact?") must use graph retrieval
- System must degrade gracefully if any retrieval path fails
