# Day 69 — Agent Workflows

## 1. 什么是 agent workflow

到目前为止，你学过的系统（RAG、serving、structured generation）基本都是：
- 一次请求、一次返回
- 或者最多是"检索 + 生成"的两步

但真实任务经常需要：
- 多步执行
- 中间调工具
- 根据结果决定下一步
- 可能会失败需要重试

这就需要 **agent workflow** —— 一种让 LLM 在多步任务里持续工作的框架。

---

## 2. workflow vs autonomous agent

### workflow
- 步骤相对确定
- 流程有结构
- 每步有明确输入输出
- 更可控、更可测试

### autonomous agent
- 步骤不预设
- LLM 自己决定做什么
- 更灵活、但更难预测

Day 69 的建议是：

> **先从 workflow 入手，再逐步走向更自主的 agent。**

---

## 3. ReAct 模式

ReAct 是最经典的 agent 交互模式之一：
- Reasoning：先想
- Acting：再做
- Observation：看结果
- 循环直到完成

这种模式适合：
- 工具调用
- 多步问答
- 研究型任务

---

## 4. 为什么 agent 需要 tool calling

单纯靠 LLM 生成文字不够，agent 需要：
- 搜索
- 读文件
- 调 API
- 查数据库
- 执行代码

这些都通过 tool calling 实现。

tool calling 是 agent 从"会说话"到"能做事"的关键。

---

## 5. 今天最该记住的 5 句话

1. **agent workflow 让 LLM 在多步任务里持续工作。**
2. **workflow 更可控，autonomous agent 更灵活。**
3. **ReAct 是经典的 reasoning + acting 循环模式。**
4. **tool calling 是 agent 连接外部世界的核心机制。**
5. **先掌握 workflow，再走向更自主的 agent。**

---

## 6. 一句话总结

> Agent workflow 把 LLM 从单次生成扩展为多步执行系统，通过 tool calling 和状态管理让模型不只"会说"，还"能做"，而 ReAct 等模式为这种循环交互提供了可复用的框架。
