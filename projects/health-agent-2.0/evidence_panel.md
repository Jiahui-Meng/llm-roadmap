# Health Agent 2.0 — Evidence Panel

## Goal
Design an evidence / citation panel that makes every answer traceable.

## What the panel shows
For each generated answer:
1. **Source chunks** — the actual text passages used
2. **Source metadata** — document name, date, section
3. **Confidence signal** — how well the evidence supports the claim
4. **Retrieval path** — which retrieval strategy found it (dense / graph / timeline)

## Why this matters
In healthcare contexts:
- Trust requires traceability
- Hallucination is not acceptable
- Users need to verify claims against source material

## UI considerations
- Side panel or expandable citations
- Click-to-highlight source passage
- Flag unsupported claims visually

## Implementation approach
- Tag each chunk with retrieval metadata during fusion
- Pass metadata through to generation prompt
- Format output with inline citation markers [1], [2], etc.
- Render evidence panel from citation metadata
