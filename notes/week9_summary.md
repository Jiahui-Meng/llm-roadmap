# Week 9 Summary — SGLang and Structured Generation

## What we covered
- SGLang as a programmable LLM interaction runtime
- JSON output generation
- Schema-constrained extraction
- Free-form vs structured output comparison
- Reusable structured generation module

## Key takeaways
1. Structured generation makes LLM output more reliable for downstream consumption
2. SGLang sits above serving engines and provides higher-level orchestration
3. Schema validation catches format errors before they propagate
4. The trade-off is between output flexibility and format reliability

## Connection to roadmap
Structured generation is the bridge between "LLM can generate text" and "LLM output can be consumed by code." This is essential for agent tool calling, data extraction, and any pipeline where downstream systems expect predictable formats.
