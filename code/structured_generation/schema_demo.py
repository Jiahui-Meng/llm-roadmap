import json

schema = {
  "type": "object",
  "properties": {
    "topic": {"type": "string"},
    "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]},
    "takeaways": {"type": "array", "items": {"type": "string"}}
  },
  "required": ["topic", "difficulty", "takeaways"]
}
example = {"topic": "RoPE", "difficulty": "medium", "takeaways": ["encodes relative position", "works well for decoder LLMs"]}
print('Schema:')
print(json.dumps(schema, indent=2))
print('
Example structured output:')
print(json.dumps(example, ensure_ascii=False, indent=2))
