import json

sample = {
    "title": "Multi-head attention",
    "summary": "Parallel attention heads learn different interaction patterns.",
    "key_terms": ["attention", "head", "projection", "concat", "W_o"]
}
print(json.dumps(sample, ensure_ascii=False, indent=2))
