from pathlib import Path
import json

RAW_DOCS = [
    {"id": "doc1", "text": "Transformers use multi-head attention."},
    {"id": "doc2", "text": "RAG adds retrieval to generation workflows."},
]

out = Path('artifacts/ingested_docs.json')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(RAW_DOCS, indent=2), encoding='utf-8')
print(f"Wrote {out}")
