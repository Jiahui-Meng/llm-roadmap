# Interview Notes — LLM Engineering

## Transformer

### Q: 为什么 Transformer 取代了 RNN？
RNN 串行处理导致难以并行化，长序列梯度消失/爆炸严重。Transformer 用 attention 一次看全部位置，可以高效并行训练，且天然支持长距离依赖。

### Q: Q/K/V 分别是什么？
Query 是"我在找什么"，Key 是"我有什么"，Value 是"我能给什么"。Q 和 K 算相关性分数，分数作为权重对 V 加权求和。

### Q: 为什么要除以 sqrt(d_k)？
防止点积值过大导致 softmax 输出接近 one-hot，梯度几乎为零。除以 sqrt(d_k) 让分布更平滑。

### Q: Multi-head attention 的意义？
不同 head 学习不同子空间的注意力模式，提升表达能力。

### Q: Pre-norm vs Post-norm？
Pre-norm 梯度流更好，训练更稳定，现代大模型大多采用 pre-norm。

---

## RAG

### Q: RAG 解决什么问题？
模型参数知识不实时、不可更新、易幻觉。RAG 通过检索外部知识注入上下文，减少幻觉并支持动态知识。

### Q: 长上下文能否替代 RAG？
不能。长上下文贵、利用不均（Lost in the Middle）、不适合大规模知识库。检索提高相关性密度。

### Q: Hybrid retrieval 为什么比纯 dense 好？
Lexical 擅长精确匹配，dense 擅长语义匹配，结合两者减少各自盲区。

### Q: Reranker 的作用？
初检索注重召回，reranker 注重精度。Cross-encoder reranker 能提升 top-k 质量。

---

## vLLM / Serving

### Q: KV cache 是什么？
缓存历史 token 的 K/V，避免自回归生成时重复计算。用内存换时间。

### Q: PagedAttention 的直觉？
像 OS 虚拟内存分页管理 KV cache，减少碎片和浪费。

### Q: 量化的核心 trade-off？
精度 vs 资源。INT8/INT4 省显存省带宽，但可能损失质量。AWQ 考虑激活分布更精细。

---

## LoRA

### Q: LoRA 的核心思想？
任务适配不需要更新全部参数。冻结主模型，只训练低秩增量矩阵。

### Q: QLoRA 和 LoRA 的区别？
QLoRA 在量化的底座上跑 LoRA，进一步降低微调资源门槛。

### Q: LoRA rank 怎么选？
rank 越高表达能力越强但成本越高。通常 8-64 之间，根据任务复杂度和资源决定。

---

## SGLang / Structured Generation

### Q: SGLang 和 vLLM 的关系？
vLLM 偏底层 serving，SGLang 偏上层编程接口。SGLang 可以跑在 vLLM 之上。

### Q: 结构化生成为什么重要？
让 LLM 输出能被代码直接消费，减少格式错误，是 agent tool calling 和数据提取的基础。

---

## Agent

### Q: Workflow vs autonomous agent？
Workflow 步骤确定，更可控可测试。Autonomous agent 自主决策，更灵活但更难预测。生产中优先 workflow。

### Q: ReAct 模式是什么？
Reasoning + Acting + Observation 循环。先想、再做、看结果、继续。

### Q: Tool calling 为什么重要？
让 LLM 从"会说"到"能做"。搜索、读文件、调 API 都通过 tool calling。
