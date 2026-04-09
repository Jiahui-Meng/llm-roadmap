# Day 31 — Transformer to Agent

## 1. 为什么会从 Transformer 走向 Agent

Transformer / LLM 本质上是序列建模器：
- 给输入
- 生成输出

但真实任务往往不只是“一次生成就结束”，而是需要：
- 查资料
- 调工具
- 分步规划
- 读中间结果
- 再继续行动

于是就有了从模型到 agent 的延伸。

---

## 2. LLM 本身的边界

仅靠一个纯文本生成模型，通常会遇到这些限制：
- 不能可靠访问实时外部系统
- 不能天然维护复杂状态流
- 不能稳定完成多步任务执行
- 难以把推理过程和工具调用编排成稳定工作流

所以从 Transformer 到 Agent，不是因为模型没用了，而是因为：

> **模型需要被放入一个更大的任务执行框架。**

---

## 3. Agent 在补什么

Agent 系统一般补的是：
- tool calling
- workflow orchestration
- memory / state management
- retry / fallback
- trace / observability

也就是说，Agent 不是只让模型“会说”，而是让它：

> **能和外部世界交互，并在多步任务里持续工作。**

---

## 4. Transformer 为什么是 Agent 的核心脑子

虽然 Agent 是系统层概念，但其核心 reasoning / planning / language interface 往往仍然由 LLM 提供。

也就是说：
- Transformer 提供语言理解与生成能力
- Agent 系统提供工具、状态和执行框架

所以 Agent 不是替代 Transformer，而是：

> 在 Transformer 外面搭一个可行动的系统壳。

---

## 5. 这条桥的真正意义

从 Transformer 到 Agent，代表了一次抽象层升级：
- 从 token-level generation
- 到 task-level orchestration

你不再只关心：
- 下一个 token 是什么

而开始关心：
- 下一步动作是什么
- 该不该调用搜索
- 结果是否可信
- 失败后如何恢复

---

## 6. 今天最该记住的 5 句话

1. **Transformer 是语言与推理核心，不是完整任务系统。**
2. **Agent 补的是工具、状态、流程和可靠性。**
3. **Agent 不是替代 LLM，而是把 LLM 放进更大执行框架。**
4. **从 Transformer 到 Agent，是从生成模型走向任务系统。**
5. **后面的 tool calling、workflow、observability 都建立在这条桥上。**

---

## 7. 一句话总结

> 从 Transformer 走向 Agent，本质上是把一个强大的语言生成核心，扩展成一个能调用工具、维护状态、执行多步流程并具备可观测性的任务系统，这标志着从模型理解到产品化系统设计的重要跃迁。
