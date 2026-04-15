# Day 41 — Query Rewrite

## 1. 为什么要做 query rewrite

RAG 系统面对的不是“完美检索 query”，而是用户随手打出来的问题。

用户 query 很常见的问题包括：
- 太短
- 太口语化
- 信息不完整
- 缺少关键术语
- 问法不适合检索系统

于是就出现了一个关键问题：

> **用户说的话，未必是检索系统最容易理解的话。**

Day 41 的 query rewrite，就是在解决这个问题。

---

## 2. query rewrite 的本质是什么

query rewrite 不是改写答案，而是改写检索输入。

它的目标是：
- 补充缺失关键词
- 明确检索意图
- 标准化表达
- 生成更适合搜索的 query 形式

一句话说：

> **query rewrite 是把“用户语言”翻译成“检索语言”。**

---

## 3. 为什么 rewrite 可能显著改善 retrieval

举个例子：

用户问：
> 这个系统怎么更靠谱一点？

对人来说你可能能猜到它在问：
- grounding
- citation
- retrieval quality
- hallucination reduction

但对检索系统而言，这个 query 太模糊了。

如果改写成：
> methods to improve grounding and citation quality in retrieval augmented generation

检索质量通常会提升很多。

这说明 query rewrite 的核心收益是：

> **让原本模糊的 query 变成更容易命中正确文档的 query。**

---

## 4. query rewrite 常见做法

### 1）关键词扩展
补充缺失术语。

### 2）术语标准化
比如把口语说法转成正式术语。

### 3）生成多个 query 变体
即 multi-query retrieval。

### 4）去掉无关噪声
把不影响检索的口语废话剔掉。

这些方法的共同点是：
- 不改用户问题本质
- 只提升检索可用性

---

## 5. query rewrite 的风险是什么

query rewrite 很有用，但也有风险。

最大的风险是：

> **rewrite 可能偏离原意。**

也就是说，系统可能把用户问题“理解过头”了。

比如用户本来问的是：
- 如何让系统更稳定

系统却改写成：
- 如何降低 hallucination

这两者可能重叠，但不完全一样。

所以 query rewrite 必须在“增强检索”与“保持原意”之间平衡。

---

## 6. query rewrite 和 reranker 的区别

Day 40 和 Day 41 容易混。

### Reranker
在候选结果出来以后，重排候选。

### Query rewrite
在检索开始之前，改写 query 本身。

所以：
- query rewrite 影响的是输入
- reranker 影响的是输出排序

两者可以同时存在，而且经常一起用。

---

## 7. 为什么 Day 41 是 retrieval engineering 的高级增强点

Day 39–41 这三天本质上是在逐步增强检索：
- Day 39：增强召回信号
- Day 40：增强候选排序
- Day 41：增强检索输入本身

这说明你已经从“RAG 可以跑”进化到：

> **RAG 的 query path 可以被工程化优化。**

这就是更成熟的 retrieval engineering 思维。

---

## 8. 今天最该记住的 5 句话

1. **用户语言不一定等于检索语言。**
2. **query rewrite 的目标是提升检索可用性，而不是改变问题本身。**
3. **它可以通过扩词、标准化、multi-query 等方式改善 retrieval。**
4. **最大风险是改写偏离原意。**
5. **query rewrite 是 retrieval engineering 的输入侧增强。**

---

## 9. 今日任务

### 必做
1. 找 3 个模糊用户 query，手动把它们改写成更适合检索的 query
2. 比较 rewrite 前后各自可能命中的文档差异
3. 写出 query rewrite 的一个好处和一个风险
4. 思考 multi-query retrieval 为什么会有用

### 你要能回答的问题
1. query rewrite 到底在改什么？
2. 为什么用户语言不一定适合 retrieval？
3. query rewrite 最常见的几种方式是什么？
4. 它和 reranker 的区别是什么？
5. query rewrite 最大的风险是什么？

---

## 10. 一句话总结

> Query rewrite 的本质，是把用户自然语言问题转换成更适合检索系统理解和召回的查询表达，从而提升 retrieval 命中率，但同时必须小心不要在改写过程中偏离原始意图。
