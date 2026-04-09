# Health Agent 2.0 — Prototype

## Goal
Implement one upgraded retrieval path end-to-end as a working prototype.

## Chosen path: Dense + Rerank
Start with the most straightforward upgrade:
1. Ingest sample clinical notes
2. Chunk and embed
3. Retrieve top-k by dense similarity
4. Rerank candidates
5. Generate grounded answer with citations

## Why start here
- Dense retrieval is the most mature path
- Reranking adds measurable quality improvement
- Graph and timeline can be added incrementally

## Success criteria
- Can answer a sample question from testset_v1
- Answer includes at least one citation
- Latency is logged

## Next steps after prototype
- Add graph retrieval path
- Add timeline retrieval path
- Run full testset evaluation
