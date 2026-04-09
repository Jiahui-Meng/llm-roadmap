# Health Agent 2.0 — Retrieval Design

## Goal
Design a hybrid retrieval system that combines three complementary retrieval strategies.

## Strategy 1: Vector Retrieval (Dense)
- Embed clinical notes, summaries, and discharge reports
- Use for semantic similarity queries
- Example: "What were the patient's main complaints?"

## Strategy 2: Graph Retrieval
- Build a knowledge graph of entities and relationships
- Nodes: medications, conditions, procedures, labs
- Edges: prescribed_for, interacts_with, caused_by, measured_by
- Use for relationship queries
- Example: "What medications is the patient on for diabetes?"

## Strategy 3: Timeline Retrieval
- Index events with timestamps
- Use for temporal queries
- Example: "What changed between the January and March visits?"

## Fusion
- Each strategy returns scored candidates
- Merge using weighted reciprocal rank fusion or similar
- Rerank merged results before generation

## Fallback
- If graph index is empty → fall back to dense only
- If timeline metadata missing → fall back to dense only
- Always have at least one retrieval path available
