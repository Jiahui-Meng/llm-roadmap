from collections import Counter
from math import log

docs = [
    "transformers use self attention to model token relationships",
    "rag combines retrieval with generation",
    "lora is a parameter efficient fine tuning method",
]
query = "attention in transformers"

def tokenize(text):
    return text.lower().split()

def bm25_score(query_tokens, doc_tokens, avgdl, N, df, k1=1.5, b=0.75):
    score = 0.0
    counts = Counter(doc_tokens)
    dl = len(doc_tokens)
    for t in query_tokens:
        if t not in counts:
            continue
        idf = log((N - df.get(t,0) + 0.5) / (df.get(t,0) + 0.5) + 1)
        tf = counts[t]
        denom = tf + k1 * (1 - b + b * dl / avgdl)
        score += idf * tf * (k1 + 1) / denom
    return score

corpus = [tokenize(d) for d in docs]
df = Counter({})
for doc in corpus:
    for t in set(doc):
        df[t] += 1
avgdl = sum(len(d) for d in corpus) / len(corpus)
q = tokenize(query)
scored = sorted(((bm25_score(q, d, avgdl, len(corpus), df), i) for i,d in enumerate(corpus)), reverse=True)
for score, idx in scored:
    print(round(score, 4), docs[idx])
