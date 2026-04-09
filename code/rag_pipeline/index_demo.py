from pathlib import Path
import json
from collections import Counter

docs = json.loads(Path('artifacts/ingested_docs.json').read_text(encoding='utf-8'))
index = {d['id']: Counter(d['text'].lower().split()) for d in docs}
out = Path('artifacts/index.json')
out.write_text(json.dumps({k: dict(v) for k,v in index.items()}, indent=2), encoding='utf-8')
print(f"Indexed {len(index)} docs")
