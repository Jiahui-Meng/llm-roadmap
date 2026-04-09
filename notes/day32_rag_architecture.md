# Day 32 — RAG Architecture

## 1. 什么是 RAG architecture

RAG（Retrieval-Augmented Generation）不是单一模型，而是一条系统流水线。

它通常包含：
1. ingestion
2. chunking
3. embedding / indexing
4. retrieval
5. reranking
6. prompt assembly
7. grounded generation
8. evaluation

所以 Day 32 的重点不是“RAG 是什么”，而是：

> **一个能工作的 RAG 系统到底由哪些层组成。**

---

## 2. 为什么 RAG 是系统，不是功能按钮

很多人把 RAG 想成：
- 先搜一下
- 再喂给 LLM

这太粗糙了。

真正的 RAG 效果取决于整条链：
- 文档怎么切
- embedding 模型怎么选
- 检索怎么做
- 是否 rerank
- prompt 怎么拼
- 是否要求 citation
- 如何评估答案质量

所以 RAG 不只是“加检索”，而是：

> **从数据到答案的一整套知识增强生成架构。**

---

## 3. ingestion 层

ingestion 负责把原始知识源接入系统，例如：
- PDF
- HTML
- Markdown
- wiki
- 数据库
- 企业文档

这一步的核心问题是：
- 数据从哪里来
- 如何清洗
- 如何标准化
- 如何保留 metadata

metadata 很关键，例如：
- 标题
- 来源
- 时间
- 文档 id
- section 信息

因为后面 retrieval 和 citation 都依赖它。

---

## 4. chunking 层

文档不能总是整篇塞进向量库和 prompt，所以需要切块。

chunking 的目标是平衡：
- 语义完整性
- 检索粒度
- token 成本

常见方式：
- fixed-size chunk
- overlap chunk
- paragraph chunk
- heading-aware chunk

chunking 是 RAG 里最容易被低估、但非常影响结果的一层。

---

## 5. embedding / indexing 层

切好块之后，需要把 chunk 编码成可检索表示。

这里通常会：
- 生成 embedding
- 存进向量数据库 / index

常见 index 形式：
- FAISS
- pgvector
- Milvus / Weaviate / Pinecone 等

这一层决定了：
- 能否高效召回相关 chunk
- 检索延迟怎样
- 向量质量怎样

---

## 6. retrieval 层

retrieval 层负责根据 query 找相关 chunk。

常见检索方式：
- lexical retrieval（如 BM25）
- dense retrieval（embedding similarity）
- hybrid retrieval

它的核心目标是：

> 在大文档库里快速找出可能最相关的上下文候选。

注意这里只是“候选”，还不一定是最终最优答案上下文。

---

## 7. reranking 层

很多系统会在 retrieval 后再做 rerank。

原因是：
- 初检索更注重召回
- reranker 更注重排序精度

这一步能显著提升：
- top-k 质量
- prompt 中上下文密度
- 最终答案相关性

---

## 8. prompt assembly 层

拿到检索结果后，还不能直接粗暴拼接。

需要决定：
- 放多少 chunk
- 按什么顺序放
- 是否压缩 / 摘要
- 是否保留 metadata / citation 标记
- 如何和系统提示词结合

prompt assembly 本质上决定了：

> 检索到的信息，最后是如何被模型消费的。

---

## 9. generation 层

generation 层由 LLM 完成：
- 读取用户问题
- 读取拼好的上下文
- 生成 grounded answer

好的 RAG generation 不只是“看过上下文就回答”，还应该尽量做到：
- 不乱编
- 能引用来源
- 不超出证据范围

---

## 10. evaluation 层

RAG 不评估就很难优化。

至少应该观察：
- retrieval hit rate
- answer correctness
- citation correctness
- hallucination rate
- latency

这就是为什么 Day 43–44 会引入 testset 和 ablation。

---

## 11. Day 32 的核心理解

你今天要形成的不是某个模块知识，而是一张系统图：

```text
raw docs
-> ingestion
-> chunking
-> indexing
-> retrieval
-> reranking
-> prompt assembly
-> generation
-> evaluation
```

如果这张图能在你脑子里稳定存在，后面的 Day 33–45 就会顺很多。

---

## 12. 今天最该记住的 5 句话

1. **RAG 是一条系统流水线，不是单个模型功能。**
2. **ingestion 和 chunking 决定了知识如何进入系统。**
3. **retrieval 负责召回，reranking 负责精排。**
4. **prompt assembly 决定检索结果如何真正进入 LLM。**
5. **evaluation 决定 RAG 是否能被持续优化。**

---

## 13. 一句话总结

> RAG architecture 的本质，是把“外部知识获取”与“LLM 生成能力”组织成一条可迭代优化的系统流水线，从原始文档一直贯通到 grounded answer 与评估闭环。
