from pathlib import Path
import json

query = 'attention generation'
index = json.loads(Path('artifacts/index.json').read_text(encoding='utf-8'))
q = set(query.split())
scored = []
for doc_id, bow in index.items():
    score = sum(bow.get(tok, 0) for tok in q)
    scored.append((score, doc_id))
for score, doc_id in sorted(scored, reverse=True):
    print(score, doc_id)
