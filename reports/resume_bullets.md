# Resume Bullets

## Transformer Foundations
- Built a mini Transformer from scratch covering embedding, positional encoding, multi-head attention, FFN, residual connections, and layer normalization
- Implemented scaled dot-product attention, self-attention, and multi-head attention with comprehensive test suites

## RAG System
- Designed and built an end-to-end RAG pipeline with ingestion, chunking, hybrid retrieval (dense + BM25), reranking, and grounded generation
- Implemented citation grounding to make every generated claim traceable to source documents
- Built evaluation framework with testset and ablation analysis across retrieval variants

## vLLM / Serving
- Evaluated LLM serving performance including single-user and concurrency benchmarks
- Analyzed KV cache management, PagedAttention, and quantization trade-offs (AWQ, GPTQ, GGUF)

## LoRA / QLoRA Fine-tuning
- Designed and executed a LoRA/QLoRA fine-tuning pipeline: task selection, data preparation, instruction formatting, training, and evaluation
- Compared before/after model behavior with structured eval report

## Structured Generation
- Built schema-constrained output modules with JSON validation for downstream system consumption
- Evaluated free-form vs structured generation on format stability and usability

## Agent Workflow
- Designed a multi-step research agent with search, scrape, retrieve, and summarize tools
- Implemented workflow orchestration with retry/fallback, trace logging, and citation support

## Health Agent 2.0 (Flagship)
- Architected a healthcare LLM system with hybrid retrieval (dense + graph + timeline), evidence grounding, and observability
- Designed evaluation set covering entity extraction, summarization, timeline, and relationship queries
- Built evidence panel for citation traceability in safety-critical healthcare context

---

## 中文版

### Transformer 基础
- 从零实现 mini Transformer，覆盖 embedding、位置编码、多头注意力、FFN、残差连接和层归一化
- 实现了缩放点积注意力、自注意力和多头注意力，并编写完整测试

### RAG 系统
- 设计并构建端到端 RAG 流水线：数据摄入、分块、混合检索（稠密 + BM25）、精排和基于证据的生成
- 实现引用溯源机制，使每条生成内容均可追溯到源文档
- 构建评估框架，包含测试集和多变量消融分析

### vLLM / 服务化
- 评估 LLM 服务性能，包括单用户和并发基准测试
- 分析 KV cache 管理、PagedAttention 和量化方案（AWQ、GPTQ、GGUF）

### LoRA / QLoRA 微调
- 设计并执行 LoRA/QLoRA 微调流程：任务选择、数据准备、指令格式化、训练和评估
- 对比微调前后模型行为，编写结构化评估报告

### 结构化生成
- 构建 schema 约束输出模块，支持 JSON 验证以供下游系统消费
- 比较自由文本与结构化生成在格式稳定性和可用性上的差异

### Agent 工作流
- 设计多步研究型 Agent，集成搜索、抓取、检索和摘要工具
- 实现工作流编排，支持重试/降级、追踪日志和引用

### Health Agent 2.0（旗舰项目）
- 设计医疗 LLM 系统架构：混合检索（稠密 + 图谱 + 时间线）、证据溯源和可观测性
- 构建多类型评估集：实体提取、摘要、时间线和关系查询
- 设计证据面板，在安全关键的医疗场景中实现引用可追溯
