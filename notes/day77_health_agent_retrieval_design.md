# Day 77 — Health Agent Retrieval Design

## 1. 为什么 Health Agent 的 retrieval 必须重新设计

普通 RAG 的默认思路通常是：
- 文档切块
- 向量检索
- top-k 返回

这在很多场景里已经够用。

但在医疗场景里，经常不够。

因为用户问的问题可能是：
- 当前药物有哪些？
- 哪些实验室指标最近变差了？
- 某药物和某疾病之间是什么关系？
- 从 1 月到 3 月病情发生了什么变化？

这些问题分别依赖：
- 语义相关性
- 时间顺序
- 实体关系

所以 Day 77 的核心结论是：

> **Health Agent 的 retrieval 不能只靠一条 dense retrieval 路径。**

---

## 2. 三类 retrieval 为什么都需要

### 1）Dense retrieval
适合：
- 语义相似问答
- 文本摘要
- 说明性信息查询

### 2）Graph retrieval
适合：
- 药物—疾病—检查项等关系查询
- 实体间连接
- 结构化知识关系

### 3）Timeline retrieval
适合：
- 指标变化趋势
- 多次就诊对比
- 时间线总结

这三类 retrieval 分别解决不同维度的问题。

所以 Day 77 的重点是：

> **retrieval 应该跟问题结构匹配，而不是只跟技术栈匹配。**

---

## 3. 为什么医疗 query 天然是多结构问题

医疗问题很少只是“找一段相关文字”。

它往往同时包含：
- 时间
- 实体
- 数值
- 关系
- 证据

比如：
> 最近 HbA1c 为什么下降了？和药物调整有没有关系？

这个问题里就同时涉及：
- 时间变化
- 化验指标
- 药物实体
- 因果/相关关系

这说明 Health Agent retrieval design 的本质，不是把检索做得更花，而是：

> **让检索形式更贴合问题结构。**

---

## 4. 为什么 retrieval fusion 很重要

既然有三条 retrieval 路径，系统最终就必须回答：
- 多条路径怎么合并？
- 哪条信号优先？
- 是否需要 rerank？

这时 fusion 就变得很重要。

因为如果只是简单拼在一起，可能会导致：
- 冗余证据很多
- 不同路径冲突
- prompt 过长

所以 Day 77 其实还在引出一个更高级问题：

> **多路 retrieval 的真正难点，不只是召回，而是融合。**

---

## 5. 为什么 retrieval design 会决定后面 eval 的难度

如果 retrieval 设计太单一，系统会：
- 时间类问题经常失败
- 关系类问题经常失败
- 指标趋势类问题经常失败

反过来，如果 retrieval 设计按问题结构来做，后面的 eval set 才有意义。

所以 Day 77 和 Day 79 是强相关的：
- Day 77 定义 retrieval 维度
- Day 79 用 eval 去验证这些维度是否真的有效

---

## 6. 今天最该记住的 5 句话

1. **Health Agent 的 retrieval 不能只靠单一路径 dense search。**
2. **dense、graph、timeline retrieval 分别服务于不同问题结构。**
3. **医疗 query 天然同时包含时间、实体和关系维度。**
4. **多路 retrieval 的难点不只是召回，而是融合。**
5. **Day 77 的 retrieval design 会直接决定后续 eval 的意义。**

---

## 7. 今日任务

### 必做
1. 给 3 类 retrieval 各写 2 个代表性问题
2. 画出多路 retrieval + fusion 的结构图
3. 写一句：为什么医疗问题不适合只靠 dense retrieval
4. 思考 fusion 时最容易出现的 2 个问题

### 你要能回答的问题
1. 为什么 Health Agent 要重新设计 retrieval？
2. dense / graph / timeline retrieval 分别适合什么？
3. 为什么医疗 query 是多结构问题？
4. fusion 为什么重要？
5. Day 77 和 Day 79 的关系是什么？

---

## 8. 一句话总结

> Health Agent Retrieval Design 的本质，是根据医疗问题天然包含的语义、关系与时间结构，设计一套 dense + graph + timeline 的多路检索体系，并通过融合机制把它们转化为更可靠的证据基础。 
