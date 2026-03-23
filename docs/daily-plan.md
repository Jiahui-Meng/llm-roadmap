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
- Read: HF tokenizer / embedding basics  
  https://huggingface.co/learn/nlp-course/
- Read: PyTorch embedding docs  
  https://pytorch.org/docs/stable/generated/torch.nn.Embedding.html
- Implement: PyTorch embedding demo
- Write note: token → id → embedding, one-hot vs learned embeddings
- Output: `code/transformer_basics/embedding_demo.py`

### Day 3
- Read: Lilian Weng attention explainer index  
  https://lilianweng.github.io/
- Read: Illustrated Transformer attention section  
  https://jalammar.github.io/illustrated-transformer/
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
- Write note: why divide by `sqrt(d_k)`
- Output: `code/transformer_basics/scaled_dot_product_attention.py`

### Day 5
- Read: Annotated Transformer attention code  
  https://nlp.seas.harvard.edu/2018/04/03/attention.html
- Read: PyTorch scaled dot-product attention docs  
  https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
- Implement self-attention layer using linear Q/K/V projections
- Run toy examples and inspect attention maps
- Write note: self-attention vs cross-attention vs RNN
- Output: `code/transformer_basics/self_attention_demo.py`

### Day 6
- Read: multi-head attention section in AIAYN  
  https://arxiv.org/abs/1706.03762
- Read: Illustrated Transformer multi-head section  
  https://jalammar.github.io/illustrated-transformer/
- Implement `MultiHeadAttention`
- Document tensor shapes carefully
- Output: `code/transformer_basics/multi_head_attention.py`

### Day 7
- Review all Week 1 code and notes
- Optional reread: Annotated Transformer overview  
  https://nlp.seas.harvard.edu/2018/04/03/attention.html
- Write summary note
- Record or rehearse a 10-minute explanation of attention
- Clean code comments and commit
- Output: `notes/week1_summary.md`

---

## Week 2 — Transformer Block and Model Families

### Day 8
- Read: positional encoding section in AIAYN  
  https://arxiv.org/abs/1706.03762
- Read: Annotated Transformer positional encoding section  
  https://nlp.seas.harvard.edu/2018/04/03/attention.html
- Implement sinusoidal positional encoding
- Visualize several positions
- Output: `code/transformer_basics/positional_encoding.py`

### Day 9
- Read: Annotated Transformer FFN explanation  
  https://nlp.seas.harvard.edu/2018/04/03/attention.html
- Read: PyTorch linear layer docs  
  https://pytorch.org/docs/stable/generated/torch.nn.Linear.html
- Implement a basic FFN module
- Write note: attention handles token-token interaction, FFN handles token-wise transformation
- Output: `code/transformer_basics/feed_forward.py`

### Day 10
- Read: PyTorch LayerNorm docs  
  https://pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html
- Read: Residual networks intuition (short explainer)  
  https://theaisummer.com/skip-connections/
- Implement residual + layernorm helpers
- Write note: why these stabilize deep networks
- Output: `code/transformer_basics/residual_layernorm.py`

### Day 11
- Read: Annotated Transformer block walkthrough  
  https://nlp.seas.harvard.edu/2018/04/03/attention.html
- Read: PyTorch `TransformerEncoderLayer` docs  
  https://pytorch.org/docs/stable/generated/torch.nn.TransformerEncoderLayer.html
- Implement a full Transformer block
- Run a forward pass with random tensors
- Draw block architecture
- Output: `code/transformer_basics/transformer_block.py`

### Day 12
- Read: causal masking explainer in HF course  
  https://huggingface.co/learn/nlp-course/
- Read: PyTorch Transformer docs (mask arguments)  
  https://pytorch.org/docs/stable/generated/torch.nn.Transformer.html
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
- Read: minGPT repo for minimal architecture inspiration  
  https://github.com/karpathy/minGPT
- Build a tiny mini-transformer (decoder-only is enough)
- Run a toy forward pass
- Write Week 2 summary
- Output: `code/transformer_basics/mini_transformer.py`

---

## Week 3 — Modern LLM Building Blocks

### Day 15
- Read: HF tokenizer course section  
  https://huggingface.co/learn/nlp-course/
- Read: Tokenizers docs  
  https://huggingface.co/docs/tokenizers/index
- Compare tokenization across Chinese and English examples
- Output: `experiments/tokenization/tokenizer_demo.ipynb`

### Day 16
- Read: HF language modeling task guide  
  https://huggingface.co/docs/transformers/tasks/language_modeling
- Read: generation basics  
  https://huggingface.co/docs/transformers/main/en/generation_strategies
- Write note: teacher forcing, train vs inference
- Create diagram of shifted labels
- Output: `notes/day16_causal_lm.md`

### Day 17
- Read: Lost in the Middle  
  https://arxiv.org/abs/2307.03172
- Read: long-context overview blog  
  https://www.pinecone.io/learn/chunking-strategies/
- Write note: why context window is costly and limited
- Output: `notes/day17_context_window.md`

### Day 18
- Read: RoPE explainer  
  https://huggingface.co/blog/RDTvlokip/when-ai-finally-learns-where-it-is
- Read: RoFormer paper abstract / intro  
  https://arxiv.org/abs/2104.09864
- Write note: relative position intuition and why modern LLMs prefer RoPE
- Output: `notes/day18_rope.md`

### Day 19
- Read: LLaMA architecture explainer  
  https://magazine.sebastianraschka.com/p/understanding-and-coding-self-attention
- Read: RMSNorm paper  
  https://arxiv.org/abs/1910.07467
- Write note: RMSNorm and SwiGLU vs classic LayerNorm/ReLU FFN
- Output: `notes/day19_modern_llm_block.md`

### Day 20
- Read: KV cache explainer + HF cache docs  
  https://huggingface.co/docs/transformers/main/cache_explanation
- Read: generation with cache docs  
  https://huggingface.co/docs/transformers/main/en/kv_cache
- Write note: why autoregressive decoding benefits from KV cache
- Output: `notes/day20_kv_cache.md`

### Day 21
- Read: FlashAttention paper  
  https://arxiv.org/abs/2205.14135
- Read: grouped-query attention overview  
  https://sebastianraschka.com/llms-from-scratch/ch04/04_gqa
- Write short concept cards for FlashAttention / MQA / GQA
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
- Read: chunking strategies  
  https://www.pinecone.io/learn/chunking-strategies/
- Read: LlamaIndex text splitting concepts  
  https://docs.llamaindex.ai/
- Implement fixed-size, overlap, paragraph chunking on a long article
- Output: `experiments/retrieval/chunking_demo.ipynb`

### Day 24
- Read: sentence-transformers docs  
  https://www.sbert.net/
- Read: FAISS getting started  
  https://github.com/facebookresearch/faiss/wiki/Getting-started
- Implement a tiny semantic retrieval demo with 2 embedding models
- Output: `code/retrieval/basic_retrieval_demo.py`

### Day 25
- Read: reranking overview  
  https://www.pinecone.io/learn/series/rag/rerankers/
- Read: BGE reranker model card  
  https://huggingface.co/BAAI/bge-reranker-base
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
- Read: vLLM overview + docs  
  https://docs.vllm.ai/
- Read: vLLM GitHub  
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
- Read: RAG pipeline overview (LangChain)  
  https://python.langchain.com/docs/tutorials/rag/
- Read: LlamaIndex starter docs  
  https://docs.llamaindex.ai/
- Design a minimal RAG pipeline diagram
- Pick a small corpus (blogs, model cards, dataset cards)
- Output: `notes/day29_rag_architecture.md`

### Day 30
- Read: trafilatura docs for web text extraction  
  https://trafilatura.readthedocs.io/
- Read: Beautiful Soup docs  
  https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Implement ingestion pipeline for a small text corpus
- Normalize and store documents with metadata
- Output: `code/rag_pipeline/ingest_demo.py`

### Day 31
- Read: FAISS getting started  
  https://github.com/facebookresearch/faiss/wiki/Getting-started
- Read: pgvector docs  
  https://github.com/pgvector/pgvector
- Implement embedding + indexing (FAISS or pgvector)
- Output: `code/rag_pipeline/index_demo.py`

### Day 32
- Read: sentence-transformers semantic search examples  
  https://www.sbert.net/examples/applications/semantic-search/README.html
- Implement retrieval and top-k inspection tool
- Output: `code/rag_pipeline/retrieve_demo.py`

### Day 33
- Read: prompt engineering guide for grounded QA  
  https://www.promptingguide.ai/
- Read: HF generation docs  
  https://huggingface.co/docs/transformers/main/en/generation_strategies
- Implement generation step with retrieved context
- Use a simple model or API for now
- Output: `code/rag_pipeline/generate_demo.py`

### Day 34
- Read: Streamlit docs or FastAPI docs  
  https://streamlit.io/  
  https://fastapi.tiangolo.com/
- Combine steps into a minimal CLI or notebook RAG prototype
- Output: `projects/rag-prototype-v1/`

### Day 35
- Read: good README examples (choose one favorite OSS repo)
- Write README and failure cases for prototype v1
- Output: `projects/rag-prototype-v1/README.md`

---

## Week 6 — Advanced RAG and Evaluation

### Day 36
- Read: hybrid retrieval overview  
  https://www.pinecone.io/learn/series/rag/hybrid-search/
- Read: rank-bm25 repo  
  https://github.com/dorianbrown/rank_bm25
- Add BM25 or lexical retrieval baseline
- Output: `experiments/retrieval/hybrid_search_demo.py`

### Day 37
- Read: rerankers article  
  https://www.pinecone.io/learn/series/rag/rerankers/
- Read: jina reranker models  
  https://huggingface.co/jinaai
- Add reranker stage
- Compare retrieval-only vs reranked results
- Output: `experiments/retrieval/rerank_demo.py`

### Day 38
- Read: query transformation concepts in LangChain  
  https://python.langchain.com/docs/tutorials/rag/
- Read: multi-query retrieval guide  
  https://python.langchain.com/docs/how_to/MultiQueryRetriever/
- Implement a simple query rewrite step
- Output: `experiments/retrieval/query_rewrite_demo.py`

### Day 39
- Read: citation / grounded QA ideas from RAGAS or TruLens docs  
  https://docs.ragas.io/  
  https://www.trulens.org/
- Add citation grounding to answers
- Output: `projects/rag-prototype-v2/citation_pipeline.py`

### Day 40
- Read: RAGAS docs  
  https://docs.ragas.io/
- Read: DeepEval docs  
  https://docs.confident-ai.com/
- Build a small evaluation set (30–50 questions)
- Output: `reports/rag_eval/testset_v1.json`

### Day 41
- Read: TruLens docs  
  https://www.trulens.org/
- Compare chunking / embedding / reranker variants
- Write result tables
- Output: `reports/rag_eval/ablation_results.md`

### Day 42
- Review all Week 6 experiments
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
- Read: vLLM quickstart  
  https://docs.vllm.ai/
- Read: model cards for one target model (Qwen / Llama / Mistral)  
  https://huggingface.co/Qwen  
  https://huggingface.co/meta-llama  
  https://huggingface.co/mistralai
- Set up vLLM locally/remotely and serve one open-source model
- Output: `experiments/serving/vllm_setup.md`

### Day 45
- Read: OpenAI-compatible server docs in vLLM  
  https://docs.vllm.ai/
- Read: FastAPI docs  
  https://fastapi.tiangolo.com/
- Test OpenAI-compatible API calls and streaming
- Output: `code/serving/vllm_client_demo.py`

### Day 46
- Read: basic benchmarking / latency measurement guide  
  https://docs.python.org/3/library/time.html
- Benchmark single-user latency and tokens/sec
- Output: `reports/serving/benchmark_single.md`

### Day 47
- Read: concurrency testing basics (locust or simple async load)  
  https://locust.io/
- Benchmark basic concurrency / throughput
- Output: `reports/serving/benchmark_concurrency.md`

### Day 48
- Read: quantization overview  
  https://huggingface.co/docs/transformers/main/en/quantization/bitsandbytes
- Read: llama.cpp quantization notes  
  https://github.com/ggerganov/llama.cpp
- Make comparison note, no deep dive needed yet
- Output: `notes/day48_quantization_basics.md`

### Day 49
- Review: vLLM docs and your RAG code
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
- Read: QLoRA paper  
  https://arxiv.org/abs/2305.14314
- Read: bitsandbytes docs  
  https://github.com/TimDettmers/bitsandbytes
- Write note: 4-bit / NF4 / memory savings at a practical level
- Output: `notes/day51_qlora.md`

### Day 52
- Browse: Kaggle datasets  
  https://www.kaggle.com/datasets
- Browse: Hugging Face datasets  
  https://huggingface.co/datasets
- Choose task and dataset
- Suggested tasks: JD skill extraction, evidence summarization, structured report generation
- Output: `projects/lora-lab/task_selection.md`

### Day 53
- Read: datasets library docs  
  https://huggingface.co/docs/datasets/index
- Read: Kaggle API docs  
  https://www.kaggle.com/docs/api
- Collect / clean dataset from Kaggle / Hugging Face / web sources
- Output: `projects/lora-lab/data/raw/`

### Day 54
- Read: instruction tuning format examples in HF docs  
  https://huggingface.co/docs/transformers/tasks/language_modeling
- Convert data to instruction format
- Output: `projects/lora-lab/data/processed/train.jsonl`

### Day 55
- Read: PEFT quicktour  
  https://huggingface.co/docs/peft/quicktour
- Read: Unsloth docs  
  https://docs.unsloth.ai/
- Run first LoRA/QLoRA fine-tuning experiment
- Output: `projects/lora-lab/training/run1/`

### Day 56
- Read: evaluation / comparison examples in PEFT ecosystem
- Compare before/after samples, write mini eval report
- Output: `reports/lora_eval/run1_report.md`

---

## Week 9 — SGLang and Structured Generation

### Day 57
- Read: SGLang intro docs  
  https://docs.sglang.ai/
- Read: SGLang GitHub  
  https://github.com/sgl-project/sglang
- Write note: where SGLang fits relative to vLLM and workflow frameworks
- Output: `notes/day57_sglang_intro.md`

### Day 58
- Read: structured output guides  
  https://www.promptingguide.ai/
- Run a simple structured generation demo
- Output: `code/structured_generation/json_output_demo.py`

### Day 59
- Read: JSON / schema validation basics  
  https://json-schema.org/understanding-json-schema/
- Build a schema-constrained summarization or extraction task
- Output: `code/structured_generation/schema_demo.py`

### Day 60
- Review: SGLang docs + your output logs
- Compare free-form prompting vs structured generation on stability
- Output: `reports/structured_generation/comparison.md`

### Day 61
- Read: SGLang examples  
  https://docs.sglang.ai/
- Wrap structured generation into a reusable module
- Output: `projects/structured-generation-lab/`

### Day 62
- Read: good OSS README examples
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
- Read: Anthropic tool use overview  
  https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
- Read: OpenAI function calling guide  
  https://platform.openai.com/docs/guides/function-calling
- Define a research-agent use case and workflow graph
- Output: `projects/open-research-copilot/design.md`

### Day 66
- Read: Beautiful Soup docs  
  https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Read: Tavily / SerpAPI docs if using external search  
  https://docs.tavily.com/  
  https://serpapi.com/search-api
- Implement tools: search, scrape, retrieve, summarize
- Output: `projects/open-research-copilot/tools/`

### Day 67
- Read: LangGraph state / graph concepts  
  https://langchain-ai.github.io/langgraph/
- Implement stateful workflow orchestration
- Output: `projects/open-research-copilot/workflow/`

### Day 68
- Read: tracing / observability ideas from LangSmith or OpenTelemetry  
  https://docs.smith.langchain.com/  
  https://opentelemetry.io/docs/
- Add trace logging and intermediate step capture
- Output: `projects/open-research-copilot/trace/`

### Day 69
- Read: retry / backoff basics  
  https://tenacity.readthedocs.io/
- Add retry / fallback / citation support
- Output: `projects/open-research-copilot/reliability.md`

### Day 70
- Review all Week 10 components
- Package Research Agent v1 with README
- Output: `projects/open-research-copilot/README.md`

---

## Week 11 — Health Agent 2.0 Upgrade

### Day 71
- Read: GraphRAG overview  
  https://microsoft.github.io/graphrag/
- Re-scope Health Agent as flagship LLM system
- Write architecture note
- Output: `projects/health-agent-2.0/architecture.md`

### Day 72
- Read: Graph retrieval / graph database concepts  
  https://neo4j.com/developer/
- Design hybrid retrieval: note retrieval + graph retrieval + timeline retrieval
- Output: `projects/health-agent-2.0/retrieval_design.md`

### Day 73
- Read: evidence-grounded UI inspirations from RAG tools / docs
- Implement evidence / citation panel plan
- Output: `projects/health-agent-2.0/evidence_panel.md`

### Day 74
- Read: RAGAS or DeepEval again for eval inspiration  
  https://docs.ragas.io/  
  https://docs.confident-ai.com/
- Create evaluation set for summary, timeline, meds, labs, relation queries
- Output: `projects/health-agent-2.0/eval/testset_v1.json`

### Day 75
- Read: OpenTelemetry docs  
  https://opentelemetry.io/docs/
- Add observability plan: latency, tool selection, prompt size, token usage
- Output: `projects/health-agent-2.0/observability.md`

### Day 76
- Review current Health Agent architecture and implement / prototype one upgraded retrieval path
- Output: `projects/health-agent-2.0/prototype/`

### Day 77
- Read: example benchmark / evaluation report formats from OSS repos
- Write README and benchmark ideas for Health Agent 2.0
- Output: `projects/health-agent-2.0/README.md`

---

## Week 12 — Portfolio Packaging

### Day 78
- Read: good monorepo structure examples from favorite OSS repos
- Clean all project directories and standardize structure
- Output: cleaned repo tree

### Day 79
- Read: Mermaid docs or draw.io usage  
  https://mermaid.js.org/  
  https://www.diagrams.net/
- Add diagrams and screenshots / logs to key projects
- Output: `assets/`

### Day 80
- Read: strong engineering resume bullet examples  
  https://www.levels.fyi/blog/applicant-tracking-system-resume.html
- Write resume bullets for each major project in English and Chinese
- Output: `reports/resume_bullets.md`

### Day 81
- Read: common ML / LLM interview question sets and your own notes
- Write interview Q&A notes for Transformer, RAG, vLLM, LoRA, SGLang, Agent
- Output: `reports/interview_notes.md`

### Day 82
- Read: great GitHub portfolio README examples
- Write portfolio-level overview README
- Output: `reports/portfolio_overview.md`

### Day 83
- Review gaps, list next-stage improvements
- Output: `reports/next_steps.md`

### Day 84
- Final polish, final commit, optional GitHub push prep
- Output: final local portfolio-ready repo
