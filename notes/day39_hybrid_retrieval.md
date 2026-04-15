# Day 39 — Hybrid Retrieval

## 1. 为什么要做 hybrid retrieval

到 RAG v1 为止，你通常已经有一种主检索方式了，最常见的是 dense retrieval。

dense retrieval 很强，但它并不是万能的。

在真实 query 里，经常会出现：
- 专有名词
- 产品名
- 版本号
- 错误码
- 精确术语
- 缩写词

这些东西，单纯语义相似检索不一定最稳。

于是就出现了一个非常自然的问题：

> **能不能同时利用“词面匹配”和“语义匹配”的优势？**

答案就是 hybrid retrieval。

---

## 2. dense retrieval 和 lexical retrieval 各自强在哪

### Dense retrieval
强在：
- 语义相似
- 同义改写
- query 和文档用词不同但意思接近时仍能命中

弱在：
- 专有名词可能不稳
- 数字、版本号、代号有时不敏感

### Lexical retrieval（如 BM25）
强在：
- 关键词精确匹配
- 特定术语、实体名、数字更稳

弱在：
- 不擅长同义改写
- 只认字面，不认深层语义

所以两者其实是互补关系。

---

## 3. hybrid retrieval 的本质

hybrid retrieval 的核心思想就是：

> **不要把召回完全押在单一信号上。**

它会把：
- dense retrieval 的语义信号
- lexical retrieval 的词面信号

结合起来。

这可以减少这两类单独方案的盲区。

所以 hybrid retrieval 不是“更复杂一点的检索”，而是：

> **更稳健的检索。**

---

## 4. 为什么 hybrid retrieval 常常是产品默认方案

如果你真正做产品，你会遇到各种 query：
- 正常自然语言问题
- 关键词式搜索
- 实体查找
- 半结构化问题
- 拼写不稳定的问题

单一检索方法通常很难在所有 query 类型上都表现好。

而 hybrid retrieval 往往能提供一个更稳的默认底座。

所以很多成熟 RAG 系统，最终都会走向：

> dense + lexical 的组合。

---

## 5. hybrid retrieval 和 reranker 的关系

要注意：

### hybrid retrieval
解决的是：
- **初召回更稳**

### reranker
解决的是：
- **候选排序更准**

也就是说：
- hybrid retrieval 主要提升 recall
- reranker 主要提升 precision

这两步经常是串联关系，而不是替代关系。

---

## 6. 为什么 Day 39 是 RAG v2 的关键升级点

如果 Day 37–38 的 v1 是：
- 最小可运行系统

那么 Day 39 开始，你进入的是：
- 更真实的 retrieval engineering

Day 39 的价值在于，它会让你第一次意识到：

> RAG 的提升，往往不是靠模型更大，而是靠召回机制更合理。

---

## 7. hybrid retrieval 的工程权衡

好处：
- 更稳健
- 对 query 类型更鲁棒
- 对术语 / 代码 / 数字更友好

代价：
- 系统更复杂
- 需要维护两条检索路径
- 可能需要融合策略
- latency 和实现成本会上升

所以 hybrid retrieval 的本质不是“总是最好”，而是：

> **在更复杂工程代价下换更稳的召回。**

---

## 8. 今天最该记住的 5 句话

1. **dense retrieval 和 lexical retrieval 是互补关系。**
2. **hybrid retrieval 的核心目标是提升召回稳健性。**
3. **它特别适合处理专有名词、术语、数字和自然语言混合 query。**
4. **hybrid retrieval 提升 recall，reranker 提升 precision。**
5. **Day 39 标志着你开始进入更真实的 retrieval engineering。**

---

## 9. 今日任务

### 必做
1. 列出 3 类 dense retrieval 可能失败、BM25 更擅长的 query
2. 列出 3 类 BM25 可能失败、dense 更擅长的 query
3. 画出 hybrid retrieval 的召回流程图
4. 写一句：为什么 hybrid retrieval 往往更适合产品系统

### 你要能回答的问题
1. dense retrieval 和 lexical retrieval 各自强弱点是什么？
2. hybrid retrieval 的本质是什么？
3. 为什么 hybrid retrieval 往往比单一路径更稳？
4. 它和 reranker 的区别是什么？
5. 为什么 Day 39 是 RAG v2 的关键升级点？

---

## 10. 一句话总结

> Hybrid retrieval 的本质，是把语义匹配和词面匹配这两种不同信号结合起来，让 RAG 的初检索在更多类型的 query 上都更稳健，从而为后续 reranking 和 grounded generation 打下更可靠的候选基础。
