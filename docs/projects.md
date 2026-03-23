# Project Plans

## Project 1 — Open Research Copilot
A multi-source research and retrieval assistant that ingests web pages, model cards, dataset cards, PDFs, and technical notes.

### Core Features
- web/document ingestion
- metadata extraction
- hybrid retrieval
- reranking
- grounded answers with citations
- structured research report generation
- evaluation set and retrieval benchmark

### Suggested Data Sources
- Hugging Face model cards
- Hugging Face dataset cards
- Kaggle dataset descriptions
- arXiv abstracts / intros
- technical blogs / docs pages

### Stack
- Python
- FastAPI
- FAISS / pgvector
- sentence-transformers
- reranker model
- React / Next.js / Streamlit

## Project 2 — Health Agent 2.0
Upgrade an existing health-focused AI agent into a flagship LLM system.

### Core Features
- graph-aware retrieval
- note retrieval + timeline retrieval + relation retrieval
- tool calling
- evidence display panel
- structured summaries
- evaluation suite
- observability metrics

### Key Selling Points
- domain grounding
- safety-oriented context control
- graph + text hybrid retrieval
- engineering-grade system thinking

## Project 3 — Serving + LoRA Lab
A technical depth project to show inference and lightweight adaptation capabilities.

### Core Features
- vLLM serving benchmarks
- OpenAI-compatible endpoint
- latency / throughput report
- LoRA / QLoRA mini-fine-tuning task
- before/after evaluation
- optional SGLang structured generation demo

### Suggested Fine-tuning Tasks
1. JD skill extraction
2. evidence summarization
3. structured report generation
4. clinical-style structured summaries (with suitable public data)

## Project Standards
Every project should have:
- README
- architecture diagram
- reproducible setup instructions
- screenshots / logs / outputs
- evaluation or benchmark report
- failure case analysis
- clear resume-ready summary bullets
