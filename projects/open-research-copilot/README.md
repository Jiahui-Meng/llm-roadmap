# Open Research Copilot

## What is this
A structured research agent that accepts a question, searches for sources, retrieves local knowledge, and produces a cited research brief.

## Architecture
```
question → rewrite → search → scrape → retrieve → merge → summarize → brief
```

## Components
- `design.md` — system design and goals
- `tools/` — tool definitions (search, scrape, retrieve, summarize)
- `workflow/` — step-by-step orchestration
- `trace/` — intermediate step logging
- `reliability.md` — retry, fallback, and citation design

## Status
Scaffolded. Ready for implementation with real tool backends.

## Future
- plug in real search API
- connect to RAG index
- add evaluation set
- deploy as CLI or API
