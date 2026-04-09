# Week 1 Summary — Transformer Foundations

## What I learned
Week 1 built the core mental model of the Transformer stack: embeddings turn tokens into vectors, attention computes token-token relevance, self-attention generates Q/K/V from the same sequence, and multi-head attention lets the model learn multiple interaction patterns in parallel.

## Day-by-day recap
- **Day 1 — Why Transformer**: Transformer replaces recurrent hidden-state passing with direct token-token interaction and much better parallelism.
- **Day 2 — Embeddings**: tokens become dense vectors that can carry semantic similarity.
- **Day 3 — Attention intuition**: Q asks, K advertises, V provides content.
- **Day 4 — Scaled dot-product attention**: score, scale, normalize, aggregate.
- **Day 5 — Self-attention**: Q/K/V are learned projections from the same input sequence.
- **Day 6 — Multi-head attention**: multiple smaller attention heads learn different patterns in different subspaces.

## Core formulas
### Scaled dot-product attention
\[
Attention(Q,K,V)=softmax\left(rac{QK^T}{\sqrt{d_k}}ight)V
\]

### Self-attention projections
\[
Q=xW_q, \quad K=xW_k, \quad V=xW_v
\]

### Multi-head attention
\[
MultiHead(Q,K,V)=Concat(head_1,\dots,head_h)W_o
\]

## Key comparisons
### RNN vs Transformer
- RNN processes sequentially; Transformer processes tokens in parallel.
- RNN struggles with long-range dependencies; Transformer directly attends across the sequence.
- Transformer is more hardware-friendly and scales better.

### Attention vs Self-attention
- Attention assumes Q/K/V are already given.
- Self-attention learns Q/K/V from the same input sequence.

### Self-attention vs Multi-head attention
- Self-attention uses one projection set and one attention pattern.
- Multi-head attention uses several smaller heads to learn multiple patterns.

## Engineering takeaways
- Shape tracking matters as much as formulas.
- `sqrt(d_k)` scaling stabilizes softmax and gradients.
- The output projection `W_o` is needed to fuse information after concatenating heads.

## What still needs reinforcement
- positional encoding and masks
- how the full Transformer block combines MHA + residual + norm + FFN
- how these ideas evolve into modern LLM variants like RoPE, RMSNorm, and KV cache
