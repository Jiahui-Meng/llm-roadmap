# Day 30 — Transformer to vLLM Bridge

## 核心内容

从 Transformer 自回归推理特性出发，理解为什么 serving 很难做高效，以及 vLLM 如何通过更好的 KV cache 管理和调度解决这些问题。
