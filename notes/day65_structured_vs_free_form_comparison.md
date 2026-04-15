# Day 65 — Structured vs Free-form Comparison

## 1. 为什么要比较 structured generation 和 free-form generation

到了这一步，你已经学了：
- JSON output
- schema-constrained generation

如果只看 structured generation 的成功案例，很容易形成一种偏见：
- “结构化输出永远更好”

其实不一定。

因为在很多场景中：
- 自由文本更自然
- 更有表达力
- 更适合开放回答

而 structured generation 更适合：
- 可验证
- 可解析
- 可自动化消费

所以 Day 65 的重点是：

> **理解两种生成模式的边界，而不是盲目崇拜其中一种。**

---

## 2. free-form generation 强在哪里

自由文本最大的优势是：
- 自然流畅
- 表达空间大
- 对开放式任务更友好
- 不容易被格式约束限制

适合场景：
- 聊天
- 长摘要
- 创意写作
- 开放问答

也就是说，free-form 更偏向“给人读”。

---

## 3. structured generation 强在哪里

结构化生成最大的优势是：
- 格式稳定
- 易验证
- 易被程序直接消费
- 更适合工具调用和自动化流程

适合场景：
- 信息抽取
- JSON 输出
- tool arguments
- 状态更新
- 表单填充

也就是说，structured generation 更偏向“给系统用”。

---

## 4. 为什么要比较“稳定性”而不是只比“好不好看”

Day 65 的核心指标不是文采，而是：
- parse success rate
- schema success rate
- format consistency
- 下游消费成功率

因为在工程里，很多时候最重要的问题是：

> **这个结果能不能稳定地被后续流程处理。**

这和自由文本聊天的评价标准完全不一样。

---

## 5. structured generation 的代价是什么

结构化生成也不是免费午餐。

它的代价包括：
- prompt 更复杂
- 输出灵活性下降
- 某些任务表达力受限
- 如果约束设计不好，模型可能更容易出奇怪错误

所以真正的工程判断不是：
- structured 一定更高级

而是：
- **这个任务到底更需要表达自由，还是更需要格式可靠。**

---

## 6. Day 65 的核心工程意识

这一天真正要建立的是：

> **生成方式要服务于任务，不要让任务去迁就生成方式。**

如果任务是开放总结，你不一定要强行 JSON。
如果任务是抽取或工作流状态更新，自由文本通常就不够稳定。

这就是 Day 65 最关键的判断能力。

---

## 7. 为什么这一天对 Agent 很重要

后面做 agent 时，你会不断遇到这个问题：
- 有些地方应该让模型自由解释
- 有些地方必须强约束输出

所以 Day 65 的比较，不只是为了 structured generation 本身，而是在训练你形成：

> **什么时候该让模型自由说，什么时候必须让模型按协议说。**

---

## 8. 今天最该记住的 5 句话

1. **free-form 更适合给人读，structured 更适合给系统用。**
2. **工程里比较的核心指标是稳定性，不是文采。**
3. **structured generation 提升可靠性，但会牺牲一些表达自由。**
4. **生成方式应该由任务需求决定。**
5. **Day 65 是在训练“什么时候需要协议化输出”的判断力。**

---

## 9. 今日任务

### 必做
1. 用同一任务分别做 free-form 和 structured 输出
2. 比较 parse success、格式稳定性和表达自然度
3. 写出两种方案各自最适合的任务类型
4. 总结：你的系统中哪些环节必须 structured

### 你要能回答的问题
1. free-form 和 structured generation 各自强在哪？
2. 为什么 Day 65 更该关注稳定性而不是文采？
3. structured generation 的代价是什么？
4. 为什么生成方式必须由任务决定？
5. 这一天为什么对 Agent 学习重要？

---

## 10. 一句话总结

> Structured vs free-form comparison 的本质，是帮助你建立一种工程判断：什么时候需要自由表达，什么时候必须强约束输出，从而让 LLM 生成方式真正服务于任务和系统目标。
