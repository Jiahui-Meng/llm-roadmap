# Full Daily Plan (84 Days)

This plan assumes ~5–6 focused hours per workday.

Daily structure:
- 1.5h reading / theory
- 2h coding / implementation
- 1.5h engineering / project work
- 0.5–1h notes / recap / commit

---

## Week 1 — Attention Foundations

### Day 1
- Read: *Attention Is All You Need* (Abstract, Intro, Figure 1)  
  https://arxiv.org/abs/1706.03762
- Read: Jay Alammar, *The Illustrated Transformer*  
  https://jalammar.github.io/illustrated-transformer/
- Write note: why Transformer replaced RNN-style sequence modeling
- Create repo note template and daily note format
- Output: `notes/day01_why_transformer.md`

### Day 2
- Read: HF tokenizer/embedding basics  
  https://huggingface.co/learn/nlp-course/
- Implement: PyTorch embedding demo
- Write note: token → id → embedding, one-hot vs learned embeddings
- Output: `code/transformer_basics/embedding_demo.py`

### Day 3
- Read: attention intuition blog / explainer
- Hand-work a toy attention example
- Write note: Query / Key / Value intuition
- Draw attention flow diagram
- Output: `notes/day03_attention_intuition.md`

### Day 4
- Read: AIAYN Section 3.2.1  
  https://arxiv.org/abs/1706.03762
- Read: Annotated Transformer  
  https://nlp.seas.harvard.edu/2018/04/03/attention.html
- Implement: scaled dot-product attention from scratch
- Test on tiny tensors and print scores/weights
- Write note: why divide by sqrt(d_k)
- Output: `code/transformer_basics/scaled_dot_product_attention.py`

### Day 5
- Implement self-attention layer using linear Q/K/V projections
- Run toy examples and inspect attention maps
- Write note: self-attention vs cross-attention vs RNN
- Output: `code/transformer_basics/self_attention_demo.py`

### Day 6
- Read: multi-head attention section in AIAYN
- Implement `MultiHeadAttention`
- Document tensor shapes carefully
- Output: `code/transformer_basics/multi_head_attention.py`

### Day 7
- Review all Week 1 code and notes
- Write summary note
- Record or rehearse a 10-minute explanation of attention
- Clean code comments and commit
- Output: `notes/week1_summary.md`

---

## Week 2 — Transformer Block and Model Families

### Day 8
- Read: positional encoding section in AIAYN / Annotated Transformer  
  https://arxiv.org/abs/1706.03762  
  https://nlp.seas.harvard.edu/2018/04/03/attention.html
- Implement sinusoidal positional encoding
- Visualize several positions
- Output: `code/transformer_basics/positional_encoding.py`

### Day 9
- Read: FFN explanations in Annotated Transformer
- Implement a basic FFN module
- Write note: attention handles token-token interaction, FFN handles token-wise transformation
- Output: `code/transformer_basics/feed_forward.py`

### Day 10
- Read: residual connection and LayerNorm explainers
- Implement residual + layernorm helpers
- Write note: why these stabilize deep networks
- Output: `code/transformer_basics/residual_layernorm.py`

### Day 11
- Implement a full Transformer block
- Run a forward pass with random tensors
- Draw block architecture
- Output: `code/transformer_basics/transformer_block.py`

### Day 12
- Read: causal masking / decoder masking explainers
- Implement padding mask and causal mask
- Visualize upper-triangular mask
- Output: `code/transformer_basics/masks.py`

### Day 13
- Read: BERT intro  
  https://arxiv.org/abs/1810.04805
- Read: T5 overview  
  https://arxiv.org/abs/1910.10683
- Read: Hugging Face course / GPT-style decoder overview  
  https://huggingface.co/learn/nlp-course/
- Make comparison table: encoder-only vs decoder-only vs encoder-decoder
- Output: `notes/day13_model_families.md`

### Day 14
- Build a tiny mini-transformer (decoder-only is enough)
- Run a toy forward pass
- Write Week 2 summary
- Output: `code/transformer_basics/mini_transformer.py`

---

## Week 3 — Modern LLM Building Blocks

### Day 15
- Read: HF tokenizer course section  
  https://huggingface.co/learn/nlp-course/
- Compare tokenization across Chinese and English examples
- Output: `experiments/tokenization/tokenizer_demo.ipynb`

### Day 16
- Read: causal LM / next-token prediction explainer
- Write note: teacher forcing, train vs inference
- Create diagram of shifted labels
- Output: `notes/day16_causal_lm.md`

### Day 17
- Read: long-context / lost-in-the-middle blog(s)
- Write note: why context window is costly and limited
- Output: `notes/day17_context_window.md`

### Day 18
- Read: RoPE explainer  
  https://huggingface.co/blog/RDTvlokip/when-ai-finally-learns-where-it-is
- Write note: relative position intuition and why modern LLMs prefer RoPE
- Output: `notes/day18_rope.md`

### Day 19
- Read: LLaMA-style architecture explainer
- Write note: RMSNorm and SwiGLU vs classic LayerNorm/ReLU FFN
- Output: `notes/day19_modern_llm_block.md`

### Day 20
- Read: KV cache explainer + HF cache docs  
  https://huggingface.co/docs/transformers/main/cache_explanation
- Write note: why autoregressive decoding benefits from KV cache
- Output: `notes/day20_kv_cache.md`

### Day 21
- Read: FlashAttention summary, MQA/GQA explainer
- Write short concept cards for each
- Output: `notes/day21_flashattention_gqa_mqa.md`

---

## Week 4 — Bridge to LLM Engineering

### Day 22
- Read: RAG paper (Intro + Method)  
  https://arxiv.org/abs/2005.11401
- Read: LangChain RAG tutorial  
  https://python.langchain.com/docs/tutorials/rag/
- Write bridge note: Transformer limitations → RAG
- Output: `bridges/transformer_to_rag.md`

### Day 23
- Read: chunking strategy blogs
- Implement fixed-size, overlap, paragraph chunking on a long article
- Output: `experiments/retrieval/chunking_demo.ipynb`

### Day 24
- Read: embedding model overviews + FAISS basics
- Implement a tiny semantic retrieval demo with 2 embedding models
- Output: `code/retrieval/basic_retrieval_demo.py`

### Day 25
- Read: reranking explainer, bi-encoder vs cross-encoder
- Add note on reranking and where it fits in RAG
- If time: run a reranker demo
- Output: `notes/day25_reranker.md`

### Day 26
- Read: LoRA paper (Abstract, Intro, Method figure)  
  https://arxiv.org/abs/2106.09685
- Read: PEFT docs  
  https://huggingface.co/docs/peft/index
- Write bridge note: Transformer linear layers → LoRA injection points
- Output: `bridges/transformer_to_lora.md`

### Day 27
- Read: vLLM overview + paged attention explainer  
  https://docs.vllm.ai/  
  https://github.com/vllm-project/vllm
- Write bridge note: KV cache → serving → vLLM
- Output: `bridges/transformer_to_vllm.md`

### Day 28
- Read: ReAct intro  
  https://arxiv.org/abs/2210.03629
- Read: LangGraph intro  
  https://langchain-ai.github.io/langgraph/
- Read: SGLang intro  
  https://docs.sglang.ai/
- Write bridge note: model vs system orchestration
- Output: `bridges/transformer_to_agent.md`

---

## Week 5 — Minimal RAG Prototype

### Day 29
- Design a minimal RAG pipeline diagram
- Pick a small corpus (blogs, model cards, dataset cards)
- Output: `notes/day29_rag_architecture.md`

### Day 30
- Implement ingestion pipeline for a small text corpus
- Normalize and store documents with metadata
- Output: `code/rag_pipeline/ingest_demo.py`

### Day 31
- Implement embedding + indexing (FAISS or pgvector)
- Output: `code/rag_pipeline/index_demo.py`

### Day 32
- Implement retrieval and top-k inspection tool
- Output: `code/rag_pipeline/retrieve_demo.py`

### Day 33
- Implement generation step with retrieved context
- Use a simple model or API for now
- Output: `code/rag_pipeline/generate_demo.py`

### Day 34
- Combine steps into a minimal CLI or notebook RAG prototype
- Output: `projects/rag-prototype-v1/`

### Day 35
- Write README and failure cases for prototype v1
- Output: `projects/rag-prototype-v1/README.md`

---

## Week 6 — Advanced RAG and Evaluation

### Day 36
- Read: hybrid retrieval overview
- Add BM25 or lexical retrieval baseline
- Output: `experiments/retrieval/hybrid_search_demo.py`

### Day 37
- Add reranker stage
- Compare retrieval-only vs reranked results
- Output: `experiments/retrieval/rerank_demo.py`

### Day 38
- Read: query rewrite / multi-query retrieval blogs
- Implement a simple query rewrite step
- Output: `experiments/retrieval/query_rewrite_demo.py`

### Day 39
- Add citation grounding to answers
- Output: `projects/rag-prototype-v2/citation_pipeline.py`

### Day 40
- Build a small evaluation set (30–50 questions)
- Output: `reports/rag_eval/testset_v1.json`

### Day 41
- Compare chunking / embedding / reranker variants
- Write result tables
- Output: `reports/rag_eval/ablation_results.md`

### Day 42
- Package advanced RAG prototype v2 with evaluation report
- Output: `projects/rag-prototype-v2/`

---

## Week 7 — vLLM and Serving

### Day 43
- Read: vLLM official docs overview  
  https://docs.vllm.ai/
- Read: vLLM GitHub / examples  
  https://github.com/vllm-project/vllm
- Write note: serving problems vLLM solves
- Output: `notes/day43_vllm_overview.md`

### Day 44
- Set up vLLM locally/remotely and serve one open-source model
- Output: `experiments/serving/vllm_setup.md`

### Day 45
- Test OpenAI-compatible API calls and streaming
- Output: `code/serving/vllm_client_demo.py`

### Day 46
- Benchmark single-user latency and tokens/sec
- Output: `reports/serving/benchmark_single.md`

### Day 47
- Benchmark basic concurrency / throughput
- Output: `reports/serving/benchmark_concurrency.md`

### Day 48
- Read: quantization concepts (AWQ/GPTQ/GGUF overview)
- Make comparison note, no deep dive needed yet
- Output: `notes/day48_quantization_basics.md`

### Day 49
- Connect RAG prototype generation to the vLLM endpoint
- Output: `projects/rag-prototype-v2-selfhosted/`

---

## Week 8 — LoRA / QLoRA Mini Project

### Day 50
- Read: LoRA paper and HF PEFT intro  
  https://arxiv.org/abs/2106.09685  
  https://huggingface.co/docs/peft/index
- Write note: LoRA vs full fine-tuning vs prompting
- Output: `notes/day50_lora_intro.md`

### Day 51
- Read: QLoRA explainer  
  https://arxiv.org/abs/2305.14314
- Write note: 4-bit / NF4 / memory savings at a practical level
- Output: `notes/day51_qlora.md`

### Day 52
- Choose task and dataset
- Suggested tasks: JD skill extraction, evidence summarization, structured report generation
- Output: `projects/lora-lab/task_selection.md`

### Day 53
- Collect / clean dataset from Kaggle / Hugging Face / web sources
- Output: `projects/lora-lab/data/raw/`

### Day 54
- Convert data to instruction format
- Output: `projects/lora-lab/data/processed/train.jsonl`

### Day 55
- Run first LoRA/QLoRA fine-tuning experiment
- Output: `projects/lora-lab/training/run1/`

### Day 56
- Compare before/after samples, write mini eval report
- Output: `reports/lora_eval/run1_report.md`

---

## Week 9 — SGLang and Structured Generation

### Day 57
- Read: SGLang intro docs  
  https://docs.sglang.ai/
- Write note: where SGLang fits relative to vLLM and workflow frameworks
- Output: `notes/day57_sglang_intro.md`

### Day 58
- Run a simple structured generation demo
- Output: `code/structured_generation/json_output_demo.py`

### Day 59
- Build a schema-constrained summarization or extraction task
- Output: `code/structured_generation/schema_demo.py`

### Day 60
- Compare free-form prompting vs structured generation on stability
- Output: `reports/structured_generation/comparison.md`

### Day 61
- Wrap structured generation into a reusable module
- Output: `projects/structured-generation-lab/`

### Day 62
- Add README, usage examples, screenshots or logs
- Output: `projects/structured-generation-lab/README.md`

### Day 63
- Review and summarize SGLang learnings
- Output: `notes/week9_summary.md`

---

## Week 10 — Agent Workflows

### Day 64
- Read: ReAct paper intro + LangGraph quickstart  
  https://arxiv.org/abs/2210.03629  
  https://langchain-ai.github.io/langgraph/
- Write note: workflow vs autonomous agent
- Output: `notes/day64_agent_workflows.md`

### Day 65
- Define a research-agent use case and workflow graph
- Output: `projects/open-research-copilot/design.md`

### Day 66
- Implement tools: search, scrape, retrieve, summarize
- Output: `projects/open-research-copilot/tools/`

### Day 67
- Implement stateful workflow orchestration
- Output: `projects/open-research-copilot/workflow/`

### Day 68
- Add trace logging and intermediate step capture
- Output: `projects/open-research-copilot/trace/`

### Day 69
- Add retry / fallback / citation support
- Output: `projects/open-research-copilot/reliability.md`

### Day 70
- Package Research Agent v1 with README
- Output: `projects/open-research-copilot/README.md`

---

## Week 11 — Health Agent 2.0 Upgrade

### Day 71
- Re-scope Health Agent as flagship LLM system
- Write architecture note
- Output: `projects/health-agent-2.0/architecture.md`

### Day 72
- Design hybrid retrieval: note retrieval + graph retrieval + timeline retrieval
- Output: `projects/health-agent-2.0/retrieval_design.md`

### Day 73
- Implement evidence / citation panel plan
- Output: `projects/health-agent-2.0/evidence_panel.md`

### Day 74
- Create evaluation set for summary, timeline, meds, labs, relation queries
- Output: `projects/health-agent-2.0/eval/testset_v1.json`

### Day 75
- Add observability plan: latency, tool selection, prompt size, token usage
- Output: `projects/health-agent-2.0/observability.md`

### Day 76
- Implement / prototype one upgraded retrieval path
- Output: `projects/health-agent-2.0/prototype/`

### Day 77
- Write README and benchmark ideas for Health Agent 2.0
- Output: `projects/health-agent-2.0/README.md`

---

## Week 12 — Portfolio Packaging

### Day 78
- Clean all project directories and standardize structure
- Output: cleaned repo tree

### Day 79
- Add diagrams and screenshots / logs to key projects
- Output: `assets/`

### Day 80
- Write resume bullets for each major project in English and Chinese
- Output: `reports/resume_bullets.md`

### Day 81
- Write interview Q&A notes for Transformer, RAG, vLLM, LoRA, SGLang, Agent
- Output: `reports/interview_notes.md`

### Day 82
- Write portfolio-level overview README
- Output: `reports/portfolio_overview.md`

### Day 83
- Review gaps, list next-stage improvements
- Output: `reports/next_steps.md`

### Day 84
- Final polish, final commit, optional GitHub push prep
- Output: final local portfolio-ready repo
