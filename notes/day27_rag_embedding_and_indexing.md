# Day 27 — RAG Embedding and Indexing

## 1. 为什么 Day 27 是 RAG 真正进入“检索工程”的一天

前一天你已经完成了：
- ingestion
- chunking
- metadata 保留

从 Day 27 开始，RAG 才真正进入 retrieval engine 的核心部分：
- embedding
- indexing

也就是说，到了今天，问题变成了：

> **如何把这些切好的知识单元映射到一个可搜索的空间里。**

这是从“准备知识”走向“搜索知识”的关键一步。

---

## 2. embedding 在 RAG 中到底做什么

embedding 的任务是把：
- query
- document chunks

映射到同一个向量空间里。

如果这个空间设计得好：
- 语义接近的问题和文档会靠近
- 用词不同但意思相近的内容也可能互相命中

所以 embedding 的本质不是“把文本变成数字”，而是：

> **把文本放进一个可做语义检索的表示空间。**

这一步决定了 dense retrieval 的上限。

---

## 3. 为什么 query 和 chunk 的对齐这么重要

RAG 检索不是做“文档相似度”研究，而是做：

> **用户问题能否找到真正有帮助的证据。**

这意味着 embedding 模型必须能处理：
- 用户自然语言问题
- 文档 chunk 的表达方式
- 两者在同一空间中的对齐

如果模型只擅长句子相似度，但不擅长 query-to-passage retrieval，效果就未必好。

所以 Day 27 的一个关键认识是：

> **embedding 选型本质上是在选 query 和知识如何对齐。**

---

## 4. indexing 在补什么问题

假设你已经有了所有 chunk 的 embedding。

如果知识库只有几十条，也许还能暴力搜索。

但只要规模一上来：
- 几万
- 几十万
- 几百万 chunks

你就必须面对一个工程问题：

> **如何在大规模向量空间里高效搜索。**

这就是 indexing 的作用。

它补的不是语义质量，而是：
- 搜索效率
- 可扩展性
- 大规模检索可行性

---

## 5. 为什么 embedding 和 indexing 必须一起学

很多人会把这两个主题拆开理解，但在 RAG 工程里它们本来就是同一链条的上下游：

### embedding 决定
- 语义空间是否有意义

### indexing 决定
- 这个空间是否能被高效搜索

如果 embedding 很好但 index 很差：
- 检索太慢
- 无法扩展

如果 index 很强但 embedding 不适合：
- 仍然找不到对的东西

所以 Day 27 的主线其实是：

> **retrieval quality = 语义空间质量 × 搜索系统质量。**

---

## 6. 为什么 metadata 在 indexing 里继续重要

indexing 不是只存向量。

真实系统中你通常还要保留：
- doc id
- source
- date
- title
- section
- category

因为检索时常常还需要：
- filter
- rerank 特征
- citation 输出
- 时间限制
- 权限控制

这说明从 Day 26 到 Day 27，有一个很重要的连续性：

> **你不是在建一个“纯向量机器”，而是在建一个知识检索系统。**

---

## 7. 为什么 Day 27 是 RAG 工程感最强的一天之一

Day 25 是桥接日，Day 26 是知识准备日，Day 27 开始真正碰到 retrieval engineering 的核心：
- 表示
- 搜索
- 规模
- 速度
- filter

也就是说，从这一天开始，你已经不只是在“做一个会回答的系统”，而是在：

> **设计一个可扩展的知识搜索层。**

这就是 RAG 和普通 prompt engineering 最大的不同之一。

---

## 8. 今天最该记住的 5 句话

1. **embedding 负责把 query 和 chunk 放进可语义对齐的空间。**
2. **indexing 负责让这个空间可被高效搜索。**
3. **embedding 和 indexing 必须一起考虑，缺一不可。**
4. **RAG 的索引不是只存向量，还要保留 metadata。**
5. **Day 27 标志着你真正进入 retrieval engineering。**

---

## 9. 今日任务

### 必做
1. 写出 embedding 和 indexing 各自解决的问题
2. 解释为什么 query-to-passage 对齐很重要
3. 列出一个 index object 至少应包含哪些字段
4. 写一句：为什么 Day 27 是 retrieval engineering 的起点

### 你要能回答的问题
1. embedding 在 RAG 中到底做什么？
2. indexing 在补什么问题？
3. 为什么 embedding 和 indexing 必须一起学？
4. metadata 为什么在索引阶段仍然重要？
5. Day 27 为什么代表从知识准备走向知识搜索？

---

## 10. 一句话总结

> RAG embedding and indexing 的本质，是先把 query 与 chunk 放进一个可语义对齐的向量空间，再把这个空间组织成可扩展、可过滤、可高效搜索的检索层，从而真正让系统具备“从问题找到知识”的能力。
