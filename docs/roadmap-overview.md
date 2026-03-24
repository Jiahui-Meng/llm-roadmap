# 12-Week Roadmap Overview

## Phase 1 — Foundations (Weeks 1-4)
Build a deep, practical understanding of Transformer and modern LLM fundamentals.

### Week 1
- Why Transformer
- Embeddings
- Attention intuition
- Scaled dot-product attention
- Self-attention
- Multi-head attention

### Week 2
- Positional encoding
- FFN
- Residual + LayerNorm
- Transformer block
- Masks
- Encoder vs decoder vs encoder-decoder
- Mini Transformer implementation

### Week 3
- Tokenization
- Causal LM
- Context window and long-context limitations
- RoPE
- RMSNorm
- SwiGLU
- KV cache
- FlashAttention / MQA / GQA concepts

### Week 3.5 — MoE Mini Module
- What Mixture of Experts is
- Dense vs sparse activation
- Router / expert / top-k routing
- Why MoE scales model capacity
- Load balancing and expert utilization
- Serving and systems implications of MoE

### Week 4
- Transformer → RAG bridge
- Transformer → LoRA bridge
- Transformer → vLLM bridge
- Transformer → Agent / SGLang bridge
- First small retrieval prototype

## Phase 2 — Core LLM Engineering (Weeks 5-8)
Focus on the systems that actually matter for applied LLM roles.

### Week 5
- RAG architecture
- Embeddings
- FAISS / pgvector basics
- Chunking
- Minimal RAG prototype

### Week 6
- Reranking
- Hybrid search
- Query rewrite
- Citation grounding
- RAG evaluation
- Advanced RAG prototype

### Week 7
- vLLM overview
- Serving open-source models
- Benchmarking latency / throughput
- Self-hosted RAG generation backend

### Week 7.5 — Quantization Mini Module
- Quantization basics: FP16 / BF16 / INT8 / INT4
- Weight-only vs activation quantization
- AWQ / GPTQ / GGUF / bitsandbytes overview
- Quality / latency / memory trade-offs
- Deployment implications for local and self-hosted models

### Week 8
- LoRA fundamentals
- QLoRA basics
- Instruction data formatting
- Small fine-tuning project
- Before/after evaluation

## Phase 3 — System Design & Productization (Weeks 9-12)
Turn knowledge into engineering-grade projects.

### Week 9
- SGLang basics
- Structured generation
- Constrained output design
- Structured generation lab

### Week 10
- Agent workflows
- ReAct
- Tool calling
- LangGraph / stateful orchestration
- Research agent prototype

### Week 11
- Upgrade Health Agent 2.0
- Hybrid retrieval
- Graph-aware context routing
- Evaluation and observability

### Week 12
- Finalize portfolio assets
- Clean repos
- Add READMEs, diagrams, screenshots
- Resume-ready bullets and interview notes

## Expected Final Outputs
- Transformer foundations notes + code
- Minimal and advanced RAG prototypes
- vLLM benchmark report
- LoRA / QLoRA mini-project
- Structured generation / SGLang lab
- Research Agent workflow prototype
- Health Agent 2.0 project upgrade
