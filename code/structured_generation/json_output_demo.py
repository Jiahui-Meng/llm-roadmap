"""Day 63 — JSON output demo for structured generation."""
import json

SYSTEM = "You are a helpful assistant. Always respond in valid JSON."
USER = "List 3 benefits of RAG in a JSON array."

# Simulated structured output
response = json.dumps({
    "benefits": [
        "Reduces hallucination by grounding answers in retrieved evidence",
        "Enables dynamic knowledge updates without retraining",
        "Improves citation and traceability of answers"
    ]
}, indent=2)

print("Prompt:", USER)
print("Structured output:")
print(response)

# Validate
parsed = json.loads(response)
assert isinstance(parsed["benefits"], list)
print(f"\nValidation passed: {len(parsed['benefits'])} items")
