# Day 68 — Week 9 Summary

## 1. Week 9 学了什么

Week 9 的主题是：

> **SGLang 与 Structured Generation**

这一周表面上看像是在学“输出格式”，但实际上，你学到的是一层非常关键的系统能力：

> **如何让 LLM 的输出从“给人看”变成“给系统用”。**

这件事的重要性非常高，因为从这一周开始，你不再只把 LLM 当成一个聊天模型，而是开始把它当成：
- 工作流节点
- 自动化系统的一部分
- tool calling 的上游
- 结构化数据生产器

这就是 Week 9 的真正价值。

---

## 2. 这一周的主线是什么

如果把 Week 9 串起来，其实是一条非常清晰的能力升级路线：

```text
LLM 可以生成文本
-> LLM 可以输出 JSON
-> LLM 可以被 schema 约束
-> 结构化输出比自由输出更稳定
-> 结构化能力可被封装成模块
-> 模块可进入更复杂的 workflow / agent 系统
```

所以这一周的主线不是“学几个格式技巧”，而是：

> **把生成能力协议化、模块化、系统化。**

---

## 3. Day 62：SGLang 的定位

这一周从 SGLang 开始，是因为它代表了一种重要思路：

> LLM 不只是被动接收 prompt，而是可以被编排成更可控的程序化交互系统。

SGLang 的意义不在于“它是某个框架”，而在于它提醒你：
- serving 不等于 workflow
- 模型接口不等于程序接口
- 结构化交互需要更高层的运行时抽象

所以 Day 62 给你建立的不是工具知识，而是世界观：

> **LLM 可以被程序化地组织起来。**

---

## 4. Day 63–64：从 JSON 到 Schema

这两天构成了 structured generation 的核心起点。

### Day 63
你先确认：
- LLM 输出不仅能是文字，也能是 JSON
- JSON 输出要真正可 parse，而不是“看起来像 JSON”

### Day 64
你进一步学到：
- JSON 只是格式
- schema 才是真正约束
- 程序真正需要的是可验证输出，不只是结构化外观

这两天最重要的认知升级是：

> **自由文本不再是默认唯一输出形式。**

---

## 5. Day 65：为什么一定要比较 free-form vs structured

这一点非常关键。

如果你不做比较，很容易出现两种错误：
- 觉得 structured generation 永远更高级
- 或者觉得自由文本已经足够，不需要额外约束

Day 65 的真正价值，是建立判断力：

### Free-form 更适合
- 给人读
- 开放回答
- 高表达自由度场景

### Structured 更适合
- 给系统用
- 自动化消费
- 工具调用参数
- 状态更新
- 信息抽取

所以这一周不是在“替代自由文本”，而是在学：

> **什么时候该自由，什么时候必须协议化。**

---

## 6. Day 66–67：从 demo 到 module，再到 project

如果前几天只是 demo，Week 9 的价值会很有限。

Day 66–67 让你做了两件非常工程化的事：

### Day 66：模块化
把 JSON output / schema validation 抽象成：
- 可复用
- 可验证
- 可被 workflow 调用

### Day 67：文档化
把结构化输出能力从“几个文件”整理成：
- 清晰目标
- 清晰边界
- 清晰用途
- 可展示的小项目

这意味着 Week 9 最终不是“学了点 structured generation”，而是：

> **你已经开始把结构化生成能力做成工程组件。**

---

## 7. 为什么 Week 9 对后面的 Agent 很关键

Week 10 要学 Agent Workflows。

如果没有 Week 9，你做 agent 时会经常卡在这些地方：
- tool arguments 输出不稳定
- 状态对象格式漂移
- 中间结果难验证
- workflow 很脆弱

而有了 Week 9 的基础，你会更自然地意识到：
- 哪些节点必须结构化
- 哪些输出必须可验证
- 哪些地方要用 schema
- 哪些地方可以允许自由文本

所以 Week 9 其实是在给 Agent 铺路。

这也是为什么它在 roadmap 里放在 Agent 前面，而不是后面。

---

## 8. Week 9 的核心收获

如果压缩成几个最重要的收获，这一周你应该带走的是：

1. **LLM 输出可以不只是自然语言，还可以是结构化协议。**
2. **JSON 只是开始，schema 才是真正的系统约束。**
3. **结构化输出的价值核心在于稳定性和可消费性。**
4. **structured generation 应该被模块化，而不是散落成 demo。**
5. **这一周的能力会直接进入后面的 tool calling / agent workflow。**

---

## 9. 你现在应该能回答的问题

1. 为什么 structured generation 对系统集成很重要？
2. JSON 和 schema 的区别是什么？
3. free-form 和 structured generation 各自适合什么任务？
4. 为什么 structured generation 需要模块化？
5. 为什么 Week 9 是 Agent 学习的前置能力？

如果这些问题你能清楚回答，说明 Week 9 你就不是“看过概念”，而是真的建立了系统理解。

---

## 10. 一句话总结

> Week 9 的真正价值，不是学会让模型输出 JSON，而是学会如何把 LLM 输出变成一种可解析、可验证、可复用、可进入 workflow 和 agent 系统的工程能力。
