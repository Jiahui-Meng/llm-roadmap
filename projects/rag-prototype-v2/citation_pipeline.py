from dataclasses import dataclass

@dataclass
class Citation:
    doc_id: str
    quote: str
    reason: str

citations = [
    Citation('doc1', 'Transformers use multi-head attention.', 'supports the model-mechanism explanation'),
    Citation('doc2', 'RAG adds retrieval to generation workflows.', 'supports the system bridge'),
]
for c in citations:
    print(f'[{c.doc_id}] {c.quote} -> {c.reason}')
