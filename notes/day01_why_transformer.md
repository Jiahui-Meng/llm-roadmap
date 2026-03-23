# Day 1 — Why Transformer

## Questions
- Why were RNN/LSTM-based approaches limiting at scale?
- Why does parallelism matter?
- What changed when attention became the primary mechanism?

## Key Points
- RNNs process tokens sequentially, which limits parallelism.
- Long-range dependencies are harder to preserve across many recurrent steps.
- Attention lets each token interact with other tokens directly.
- Transformer made large-scale sequence modeling much more hardware-friendly.

## Engineering Relevance
- Parallelism and scalable training made large language models practical.
- Attention-centric architectures also shape inference cost and context handling later.
