# Research Copilot — Workflow

## Steps
1. receive question
2. rewrite query for search
3. call search_tool
4. call scrape_tool on top results
5. call retrieve_tool on local index
6. merge external + local evidence
7. call summarize_tool with citations
8. output final brief

## State
Each step reads from and writes to a shared state dict.

## Error handling
- search fails → fall back to local retrieve only
- scrape fails → skip that URL
- summarize fails → return raw evidence list
