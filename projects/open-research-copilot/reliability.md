# Research Copilot — Reliability

## Goal
Make the research agent more robust in real-world conditions.

## Retry strategy
- search: retry up to 3 times with exponential backoff
- scrape: skip on failure, log warning
- summarize: retry once, fall back to raw evidence

## Fallback
- if all external search fails, use local retrieval only
- if summarization fails, return evidence list instead

## Citation support
- every claim in the summary should reference a source
- sources should include URL or document ID

## Observability
- log every tool call with input/output/latency
- flag any step that exceeds timeout
