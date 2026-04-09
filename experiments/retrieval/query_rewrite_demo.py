query = 'how does rag work'
rewrites = [
    'retrieval augmented generation architecture',
    'rag pipeline ingestion retrieval generation',
    'how retrieval augments llm generation'
]
print('Original:', query)
print('Rewrites:')
for r in rewrites:
    print('-', r)
