# Health Agent 2.0 — Observability

## Goal
Make every request through the Health Agent traceable and measurable.

## What to observe

### Per-request metrics
- Total latency (end-to-end)
- Retrieval latency (per strategy)
- Generation latency
- Token count (prompt + completion)
- Retrieval strategy used
- Number of chunks retrieved
- Reranker applied (yes/no)

### System-level metrics
- Requests per minute
- P50 / P95 latency
- Cache hit rate (if applicable)
- Error rate by component

### Quality signals
- Citation count per answer
- Unsupported claim rate (if eval is running)
- User feedback (thumbs up/down if available)

## Implementation approach
- Structured JSON logging per request
- Each component emits timing + metadata
- Aggregate into dashboard or log analysis

## Future
- OpenTelemetry integration
- Distributed tracing across retrieval + generation
- Alerting on latency spikes or quality drops
