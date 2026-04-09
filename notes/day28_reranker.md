# Day 28 — Reranker

## 1. 为什么检索之后还要 rerank

RAG 里，第一阶段检索通常追求的是：

> 快速从大文档库里捞出一批“可能相关”的候选块。

但“可能相关”不等于“最相关”。

因此很多系统会在初检索之后，再加一层 reranker：

> 用更强但更贵的模型，对少量候选结果重新排序。

---

## 2. retrieval 和 reranking 的职责区别

### retrieval
- 面向大规模文档库
- 追求召回
- 要求快
- 常用 embedding search / BM25 / hybrid

### reranking
- 面向少量候选结果
- 追求精度
- 可以更慢一些
- 常用 cross-encoder 或更精细的相关性模型

一句话：
- retrieval = 先广泛捞
- reranker = 再认真挑

---

## 3. 为什么 reranker 很有价值

因为很多 query：
- 在 embedding 空间里“差不多都相关”
- 但真正最适合回答问题的 chunk 只有少数几个

reranker 能改善：
- top-k 质量
- 上下文相关性密度
- 最终生成准确率
- 引用质量

---

## 4. bi-encoder vs cross-encoder

### bi-encoder retrieval
- query 和文档分别编码
- 速度快
- 适合大规模检索

### cross-encoder reranker
- query 和候选文档一起看
- 理解更细
- 排序更准
- 但更慢

所以常见架构是：
- 先用 bi-encoder 检索
- 再用 cross-encoder rerank

---

## 5. reranker 的工程意义

reranker 不是必须，但往往是从“能用的 RAG”到“效果不错的 RAG”的重要一步。

它的代价是：
- 增加一次模型调用
- 增加延迟

它的收益是：
- 更高 precision
- 更少无关 chunk
- 更稳定的 grounded generation

---

## 6. 今天最该记住的 5 句话

1. **retrieval 解决召回，reranker 解决排序精度。**
2. **reranker 通常在少量候选上工作，而不是全库检索。**
3. **cross-encoder reranker 往往更准，但也更贵。**
4. **reranking 能提升 RAG 上下文质量和最终答案质量。**
5. **它是高级 RAG pipeline 的常见增强层。**

---

## 7. 一句话总结

> Reranker 是 RAG 中位于“初检索”和“最终生成”之间的精排层，它牺牲一部分延迟来换更高的检索精度，从而提升最终答案的相关性和引用质量。
