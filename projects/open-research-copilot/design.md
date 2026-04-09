# Open Research Copilot — Design

## Goal
Build a research agent that can:
1. Accept a research question
2. Search for relevant sources
3. Scrape and extract key content
4. Retrieve from local knowledge base
5. Summarize findings with citations
6. Present a structured research brief

## Architecture
```
user question
-> query rewrite
-> search tool (web / local)
-> scrape / retrieve
-> summarize with citations
-> output structured brief
```

## Tools needed
- search (web search API or local index)
- scrape (BeautifulSoup / readability)
- retrieve (local RAG index)
- summarize (LLM with citation prompt)

## Workflow type
Structured workflow with defined steps, not fully autonomous agent.

## Success criteria
- produces a useful research brief
- citations are traceable
- can be run end-to-end in one command
