"""Day 64 — Schema-constrained output demo."""
import json

SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "summary": {"type": "string", "maxLength": 200},
        "tags": {"type": "array", "items": {"type": "string"}, "maxItems": 5}
    },
    "required": ["title", "summary", "tags"]
}

# Simulated constrained output
output = {
    "title": "KV Cache in LLM Inference",
    "summary": "KV cache stores historical key and value tensors to avoid redundant computation during autoregressive generation, trading memory for speed.",
    "tags": ["kv-cache", "inference", "serving", "transformer"]
}

print("Schema:")
print(json.dumps(SCHEMA, indent=2))
print("\nOutput:")
print(json.dumps(output, indent=2))

# Basic validation
for field in SCHEMA["required"]:
    assert field in output, f"Missing required field: {field}"
assert len(output["summary"]) <= 200
assert len(output["tags"]) <= 5
print("\nSchema validation passed.")
