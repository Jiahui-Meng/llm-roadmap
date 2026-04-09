# Day 25 — Transformer to RAG

## 1. 为什么会从 Transformer 走向 RAG

你已经学了很多 Transformer / LLM 内部机制：
- attention
- context window
- causal LM
- RoPE
- KV cache

但当模型进入真实产品时，会遇到几个根本限制：

1. **参数知识不是实时更新的**
2. **context window 再长也有限**
3. **模型会幻觉**
4. **企业私有数据不能全塞进预训练参数**

这些限制共同推动出一个系统层方案：

> **RAG（Retrieval-Augmented Generation）**

---

## 2. Transformer 的限制是什么

Transformer / LLM 本质上是参数化模型。

它知道的知识主要来自：
- 预训练数据
- 微调数据
- prompt 给它的上下文

问题在于：
- 参数里的知识不容易实时改
- 模型不能天然“主动查资料”
- 长文档全塞进 prompt 成本高

所以模型虽然会生成，但不天然擅长：
- 动态查新信息
- 精准引用外部证据
- 面向企业知识库回答问题

---

## 3. RAG 在补什么

RAG 的核心思想是：

> 不只靠模型参数记忆，而是先检索外部知识，再把相关上下文喂给模型生成。

也就是说：

```text
question
-> retrieve relevant docs/chunks
-> attach retrieved context
-> LLM generates grounded answer
```

这样做的好处是：
- 知识更可更新
- 答案更可解释
- 可以连接企业文档 / 私有数据
- 减少纯参数幻觉

---

## 4. 为什么不是长上下文就够了

你在 Day 17 学过：
- 长上下文昂贵
- Lost in the Middle 存在
- 能塞进去不等于用得好

所以即使模型上下文很长，RAG 仍然重要，因为：
- 检索可以先筛选真正相关内容
- 提高上下文密度
- 降低无关噪声
- 降低 token 成本

---

## 5. Transformer 到 RAG 的真正桥梁

这条桥梁的逻辑可以概括为：

### 模型本体很强
- 会理解 prompt
- 会整合上下文
- 会生成自然语言答案

### 但模型本体不够
- 不会自己可靠地查外部知识
- 不擅长保证来源可追踪
- 对动态知识维护成本高

### 所以需要系统补层
- ingestion
- chunking
- embedding / indexing
- retrieval
- reranking
- grounded generation

这就是 RAG。

---

## 6. 今天最该记住的 5 句话

1. **Transformer 很强，但它的知识主要在参数里。**
2. **参数知识不适合高频更新和精确引用。**
3. **RAG 用检索系统给 LLM 提供外部上下文。**
4. **长上下文不能替代检索。**
5. **RAG 是从“模型能力”走向“系统能力”的第一座桥。**

---

## 7. 一句话总结

> 从 Transformer 走向 RAG，本质上是承认模型参数化知识有边界，然后用检索系统把外部、可更新、可引用的知识接入生成流程，从而把“会生成”升级成“更会基于真实资料生成”。
