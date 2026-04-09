candidates = [
    ('doc-a', 0.62, 'Transformers and attention basics'),
    ('doc-b', 0.59, 'RAG pipeline overview'),
    ('doc-c', 0.55, 'Fine-tuning with LoRA'),
]
query = 'attention basics'
reranked = sorted(candidates, key=lambda x: (query in x[2].lower(), x[1]), reverse=True)
for item in reranked:
    print(item)
