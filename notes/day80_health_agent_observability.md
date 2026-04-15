# Day 80 — Health Agent Observability

## 1. 为什么 Health Agent 特别需要 observability

Health Agent 2.0 已经不是单一模型调用，而是一个复杂系统：
- 多路 retrieval
- evidence grounding
- 可能的 reranking
- 结构化输出
- 最终生成

这样的系统如果没有 observability，很快就会变成黑盒。

而在医疗场景里，黑盒尤其危险，因为你不仅要关心：
- 系统有没有返回答案

还要关心：
- 系统到底怎么得出这个答案
- 哪一步最慢
- 哪一路 retrieval 最常失败
- token 成本是否失控

所以 Day 80 的重点是：

> **把 Health Agent 从“复杂功能集合”变成“可测量、可监控、可诊断”的系统。**

---

## 2. observability 在这里到底包括什么

最少可以分成三层：

### 1）Latency / Performance
- 总延迟
- retrieval 各路径耗时
- generation 耗时
- reranking 耗时

### 2）Behavior / Decision
- 选择了哪些 retrieval path
- top-k 是什么
- citation 数量多少
- prompt 大小多少

### 3）Quality Signals
- unsupported claim rate（离线或半在线）
- 用户反馈
- 某类 query 的失败率

也就是说，Health Agent 的 observability 不只是看“服务活着没”，而是：

> **看它到底怎么工作、工作得是否稳定、哪部分在退化。**

---

## 3. 为什么 token usage 在 Health Agent 里很重要

多路 retrieval + grounding 往往意味着更长上下文。

如果不观察 token usage，很容易出现：
- prompt 膨胀
- 延迟上升
- 成本上升
- citation 很多但真正有用证据比例不高

所以 Day 80 特别值得关注：
- prompt token size
- completion token size
- 每类 query 的 token 分布

因为 token 其实是：

> **系统成本和复杂度的直接代理指标。**

---

## 4. 为什么工具/路径选择也要被观测

Health Agent 不是固定一条 retrieval 路径。

你前面设计了：
- dense
- graph
- timeline

如果系统一直只用 dense，说明：
- graph/timeline 没真正发挥作用
- 或 routing / query understanding 设计有问题

所以 observability 还必须回答：
- 各 retrieval path 使用频率如何
- 哪种 query 实际触发了哪条路径
- 哪条路径效果最好 / 最差

这就是为什么 Day 80 是设计验证的一部分，而不是单纯运维工作。

---

## 5. 为什么 observability 对医疗系统尤其是信任基础设施

在医疗场景里，可观测性不只是工程便利，而是信任基础设施。

因为如果用户、开发者或评估者问：
- 为什么它这次回答慢？
- 为什么这次没给出证据？
- 为什么 timeline 问题回答得差？

系统必须有办法回溯。

所以 Day 80 的意义也在于：

> **让 Health Agent 的行为具备可回溯性。**

---

## 6. 今天最该记住的 5 句话

1. **Health Agent 没有 observability，就很容易成为危险黑盒。**
2. **可观测性至少要覆盖性能、行为和质量信号三层。**
3. **token usage 是成本与复杂度的重要代理指标。**
4. **多路 retrieval 的选择行为本身必须被观测。**
5. **在医疗场景里，observability 也是信任基础设施。**

---

## 7. 今日任务

### 必做
1. 列出 Health Agent 至少应记录的 10 个观测字段
2. 区分性能指标、行为指标和质量指标
3. 设计一份 request-level 日志 schema
4. 写一句：为什么 observability 对医疗系统尤其重要

### 你要能回答的问题
1. 为什么 Health Agent 特别需要 observability？
2. observability 在这里至少包括哪三层？
3. token usage 为什么重要？
4. 为什么 retrieval path 选择也要被观测？
5. Day 80 为什么不仅是运维问题？

---

## 8. 一句话总结

> Health Agent Observability 的本质，是让一个多路检索、证据驱动、代价敏感的医疗 LLM 系统具备可测量、可回溯、可诊断的能力，从而同时服务于性能优化、质量监控和信任建立。
