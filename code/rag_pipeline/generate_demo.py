context = [
    'Transformers use multi-head attention.',
    'RAG combines retrieval with generation.'
]
question = 'How does RAG relate to transformers?'
answer = f"Question: {question}

Context used:
- " + "
- ".join(context) + "

Draft answer: RAG builds on transformer generation by injecting retrieved external knowledge into the prompt."
print(answer)
