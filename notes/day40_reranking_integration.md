# Day 40 — Reranking Integration

## 1. 为什么 retrieval 之后还需要 reranking

即使你已经做了 hybrid retrieval，系统返回的 top-k 候选也不一定就是最适合回答问题的上下文。

因为初检索通常追求的是：

> **尽量不要漏掉相关内容。**

这意味着它偏向 recall，而不是最优排序。

所以 Day 40 引入 reranking 的原因非常自然：

> **先广泛召回，再认真排序。**

---

## 2. reranker 真正在补什么

初检索常常会遇到这些问题：
- 候选都差不多相关，但顺序不理想
- 真正最关键的 chunk 不在最前面
- 噪声候选混进 top-k
- prompt assembly 时上下文密度不够高

reranker 的工作就是：

> 在较小候选集内，用更强的相关性判断重新排顺序。

所以 reranker 补的是：
- precision
- prompt context quality
- final answer grounding quality

---

## 3. 为什么不能一开始就用 reranker 检索全库

这是一个很重要的工程问题。

reranker 通常比初检索更贵，因为它需要：
- 更细粒度比较 query 与候选
- 往往用 cross-encoder 或更重的模型

所以它不适合直接对全库做搜索。

这就是为什么合理的两阶段结构通常是：

```text
large corpus
-> fast retrieval
-> top N candidates
-> reranker
-> top k final contexts
```

也就是说：

> retrieval 负责从大海里捞鱼，reranker 负责从桶里挑最好的几条。

---

## 4. reranking integration 的真正意义

Day 40 的重点不仅是“加一个模型”，而是：

> **把 RAG 从单阶段检索系统，升级成两阶段检索系统。**

这非常关键，因为两阶段系统通常更接近真实产品。

它意味着你开始关注：
- recall 和 precision 分层处理
- latency 和质量之间的 trade-off
- top-N / top-k 超参数选择

所以 reranking integration 是一个非常典型的工程升级点。

---

## 5. reranker 为什么对最终答案影响很大

因为 LLM 最终读到的上下文是有限的。

如果你给它的 top-k 里：
- 排在最前面的 chunk 不够关键
- 噪声比重太高
- 最有用的信息排得太后

那模型的回答质量会明显下降。

所以 reranker 影响的不是单纯排序，而是：

> **LLM 最终能看到什么样的证据。**

---

## 6. reranker 的代价是什么

reranking 当然不是免费午餐。

它的代价主要在：
- 增加一次模型计算
- 增加延迟
- 增加系统复杂度

所以你必须权衡：
- 候选数 N 选多大
- 最终送入 prompt 的 k 选多大
- 质量提升值不值得这部分 latency

这也是 Day 40 很工程的一点：

> **你在做的不是“理论提升”，而是“质量-成本平衡”。**

---

## 7. Day 40 和 Day 39 / Day 41 的关系

这三天可以连起来看：

### Day 39
- 让召回更稳（hybrid retrieval）

### Day 40
- 让排序更准（reranking）

### Day 41
- 让 query 更适合检索（query rewrite）

这三步组合起来，就构成了 RAG v2 里典型的 retrieval enhancement stack。

---

## 8. 今天最该记住的 5 句话

1. **retrieval 负责召回，reranker 负责精排。**
2. **reranker 的核心价值是提高 prompt 中证据的质量密度。**
3. **reranker 不适合检索全库，只适合处理候选集。**
4. **它把 RAG 从单阶段检索升级成两阶段检索系统。**
5. **reranking integration 本质上是在做质量与延迟的工程权衡。**

---

## 9. 今日任务

### 必做
1. 画出 retrieval-only 与 retrieval + rerank 两条流程
2. 写出 reranker 最适合处理的输入规模（为什么不是全库）
3. 思考：如果 top-20 候选里只有 3 个真正相关，reranker 能起什么作用？
4. 写一句：为什么 reranker 最终会影响答案质量

### 你要能回答的问题
1. reranker 和 retrieval 的核心区别是什么？
2. 为什么 reranker 不应该直接检索全库？
3. reranking integration 为什么是产品级 RAG 的常见升级？
4. reranker 对 prompt quality 的影响是什么？
5. 它的主要代价是什么？

---

## 10. 一句话总结

> Reranking integration 的本质，是在初检索召回候选之后，用更强但更贵的相关性模型做第二阶段精排，从而提升送入 LLM 的上下文质量密度，并把 RAG 从“能检索”升级到“检索更准”。
