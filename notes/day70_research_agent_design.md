# Day 70 — Research Agent Design

## 1. 为什么 Agent 设计第一步不是写工具代码

很多人一想到做 agent，会立刻想：
- 接搜索 API
- 写爬虫
- 连向量库
- 调 LLM

但如果没有先定义清楚 agent 到底要解决什么问题，这些工具很快就会变成一堆零散能力，最后拼不成系统。

所以 Day 70 的重点不是实现，而是设计：

> **先定义 agent 的任务边界、输入输出和工作流，再决定工具和实现。**

这和前面做 RAG / LoRA 时的原则一样：

> **先定义问题，再搭系统。**

---

## 2. research agent 在解决什么问题

research agent 不是“一个会搜网页的 LLM”，而是：

> **一个能够围绕研究问题，完成检索、阅读、筛选、整合和输出结构化结论的多步系统。**

也就是说，它要帮助用户完成的不是单次回答，而是一个研究过程：
- 理解问题
- 找资料
- 读资料
- 合并信息
- 形成引用清晰的研究摘要

这已经不是普通聊天的任务范畴了。

---

## 3. 为什么 use case 必须先定义清楚

agent 最容易做失败的地方之一，就是“想做所有事”。

比如：
- 能搜网页
- 能看论文
- 能写总结
- 能做报告
- 能推荐下一步
- 能持续跟踪

听起来很强，但如果没有清晰边界，项目很快会失控。

所以 Day 70 要先明确：
- 输入是什么（research question）
- 输出是什么（cited brief / structured report）
- 成功标准是什么（有用、可验证、能复现）

这就是为什么 design 先于 implementation。

---

## 4. workflow graph 为什么重要

research agent 通常不是一次 prompt 完成的，而是一个多步过程。

最典型的链路可能是：

```text
question
-> rewrite query
-> search
-> scrape / retrieve
-> summarize with citations
-> output research brief
```

workflow graph 的价值在于：
- 明确每一步做什么
- 明确每一步的输入输出
- 明确哪里可能失败
- 明确哪里适合插入重试或 fallback

也就是说：

> **workflow graph 是 agent 从“想法”变成“系统”的第一张蓝图。**

---

## 5. 为什么 research agent 特别适合 workflow-first

在 agent 领域，一个很常见误区是：
- 越自由越智能
- 越少限制越像 agent

但 research task 实际上非常适合 workflow-first：
- 步骤天然有顺序
- 用户对可解释性要求高
- citation 很重要
- 中间结果必须可回溯

所以比起完全自治，研究型 agent 更适合：

> **受控工作流 + 必要工具调用 + 明确状态转移。**

这也更符合工程可控性。

---

## 6. Day 70 的设计重点到底是什么

这一天最该聚焦的不是“工具有多强”，而是：

### 1）输入输出清晰
用户进来问什么？系统最后交付什么？

### 2）步骤边界清晰
每一步到底负责什么？

### 3）责任分工清晰
LLM 负责什么？工具负责什么？workflow 负责什么？

### 4）失败路径清晰
如果 search 挂了怎么办？如果 scrape 失败怎么办？

也就是说，Day 70 是 agent 的系统设计日，而不是功能堆砌日。

---

## 7. 今天最该记住的 5 句话

1. **Research agent 不是“会搜索的聊天机器人”，而是研究工作流系统。**
2. **设计要先于实现，先明确任务边界和输出目标。**
3. **workflow graph 是把 agent 从想法变成系统的第一张蓝图。**
4. **research task 特别适合 workflow-first，而不是完全自治。**
5. **Day 70 的核心是输入、步骤、责任和失败路径的设计。**

---

## 8. 今日任务

### 必做
1. 明确 research agent 的输入、输出和成功标准
2. 画一张 workflow graph
3. 列出系统至少需要的 4 个工具
4. 为每一步写一句职责说明

### 你要能回答的问题
1. 为什么 agent 设计第一步不是写工具？
2. research agent 和普通聊天助手的区别是什么？
3. workflow graph 为什么重要？
4. 为什么 research task 适合 workflow-first？
5. Day 70 真正要设计的核心维度是什么？

---

## 9. 一句话总结

> Research Agent Design 的本质，是先把“研究型问题解决流程”定义成一个输入清晰、步骤明确、职责分工合理、失败路径可控的多步系统蓝图，再基于这个蓝图决定具体工具和实现方式。
