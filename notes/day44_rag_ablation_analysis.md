# Day 44 — RAG Ablation Analysis

## 1. 为什么要做 ablation

当你的 RAG v2 里开始出现越来越多组件：
- hybrid retrieval
- reranker
- query rewrite
- citation grounding
- 不同 chunking / embedding 方案

你迟早会遇到一个问题：

> **到底是哪一个组件真的带来了提升？**

如果不做 ablation，你只能看到一个混合后的最终效果，却不知道：
- 哪个组件最值钱
- 哪个组件只是增加复杂度
- 哪个组件在拖慢系统

这就是 Day 44 的意义。

---

## 2. ablation analysis 的本质

ablation 不是为了炫技，而是为了回答：

> **拆掉某个模块后，系统会损失多少能力？**

例如比较：
- dense only
- hybrid retrieval
- hybrid + rerank
- hybrid + rerank + rewrite
- hybrid + rerank + rewrite + citation

这样你才能知道每一步增强到底值不值。

---

## 3. 为什么 ablation 比单次对比更有信息量

如果你只比较：
- baseline
- final system

你只知道“总共好了多少”，但你不知道：
- 提升主要来自哪一层
- 哪些模块只是锦上添花
- 哪些模块收益很小但代价很高

ablation 的价值就在于把复杂系统拆开看。

也就是说：

> **ablation 是系统因果分析的近似方法。**

---

## 4. RAG ablation 应该看哪些指标

不能只看一个指标。

至少应看：
- retrieval hit rate
- answer correctness
- citation correctness
- latency
- token cost / prompt size

因为现实中很常见的情况是：
- 某个组件让答案更准
- 但 latency 大幅上升
- 或 citation 更稳，但 token 更贵

所以 Day 44 的核心不是“找最高分”，而是：

> **理解质量与成本之间的边际贡献。**

---

## 5. 为什么 ablation 对工程决策很重要

产品系统不是论文榜单。

你最终要回答的是：
- 这个组件是否值得上线？
- 它提升了多少？
- 值不值得付出额外延迟和维护复杂度？

这意味着 ablation 的目标是支持决策，而不只是生成图表。

所以一个好的 ablation 结果，应该能帮助你说出：
- “reranker 提升明显，值得保留”
- “query rewrite 对这类 query 有帮助，但不是默认必开”
- “citation 对高风险场景必须保留，即便有成本”

---

## 6. Day 44 和 Day 43 的关系

没有 Day 43 的 evaluation set，Day 44 几乎没法做。

因为 ablation 需要在同一批题上做稳定比较。

所以：
- Day 43 提供测量尺
- Day 44 用这把尺拆解系统贡献

这两天本质上是一组。

---

## 7. 常见错误：把 ablation 做成故事会

工程上最常见的问题是：
- 只挑几个看起来好的案例
- 不做系统对比
- 最后只写主观感受

这样不叫 ablation。

真正的 ablation 要求：
- 同一数据集
- 同一评估条件
- 明确只改变一个或一组变量
- 记录结果表格

换句话说：

> **ablation 的价值在于控制变量。**

---

## 8. 今天最该记住的 5 句话

1. **ablation 的目标是搞清楚每个模块的真实贡献。**
2. **只看 baseline vs final system，信息量不够。**
3. **RAG ablation 必须同时看质量和成本指标。**
4. **ablation 的本质是支持工程决策，而不是只做展示。**
5. **控制变量是 ablation 有意义的前提。**

---

## 9. 今日任务

### 必做
1. 设计 4–5 个系统变体用于比较
2. 为每个变体记录至少 3 个指标
3. 写一张结果表
4. 写一句每个组件的“是否值得保留”结论

### 你要能回答的问题
1. 为什么要做 ablation？
2. 为什么 baseline vs final system 不够？
3. RAG ablation 至少要看哪些指标？
4. 为什么 ablation 对产品决策重要？
5. 控制变量为什么是关键？

---

## 10. 一句话总结

> RAG ablation analysis 的本质，是用控制变量的方式拆解复杂系统中每个增强模块的边际贡献，从而帮助你判断哪些改进真正提升了效果，哪些只是增加了复杂度和成本。
