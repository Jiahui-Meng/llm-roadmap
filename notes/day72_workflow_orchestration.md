# Day 72 — Workflow Orchestration

## 1. 为什么有了工具还不够

即使你已经有了：
- search tool
- scrape tool
- retrieve tool
- summarize tool

系统仍然不等于 agent。

因为真正难的地方不是“有没有工具”，而是：

> **这些工具如何在多步任务里被正确、稳定、可控地组织起来。**

这就是 Day 72 的主题：workflow orchestration。

---

## 2. orchestration 在解决什么问题

多步任务最大的挑战是：
- 步骤有顺序
- 中间结果要传递
- 某一步失败要决定怎么处理
- 不同步骤对上下文依赖不同

如果没有 orchestration，工具就只是孤立函数。

orchestration 的作用就是：

> **把离散能力组织成可重复执行的任务流程。**

---

## 3. 为什么 shared state 很关键

多步 workflow 的核心之一是 shared state。

因为系统在执行中会不断产生中间结果：
- 原始问题
- 改写 query
- search results
- scraped content
- retrieved chunks
- final summary

如果这些信息没有统一状态容器，就会导致：
- 数据传递混乱
- debug 困难
- 重试代价高

所以 Day 72 的关键认识之一是：

> **workflow 的核心不是步骤列表，而是状态流。**

---

## 4. workflow orchestration 和单次 prompt 的根本区别

单次 prompt 的特点是：
- 输入一次
- 输出一次
- 中间过程不显式建模

workflow orchestration 的特点是：
- 明确分步
- 显式状态
- 可插入工具调用
- 可加错误处理
- 可记录轨迹

这意味着你已经从“prompt 设计”走向：

> **任务执行设计。**

---

## 5. 为什么 workflow-first 更适合真实系统

完全自治 agent 听起来很强，但现实里很容易带来：
- 行为不可预测
- debug 困难
- 成本难控
- 安全边界模糊

而 workflow-first 的优势是：
- 步骤可控
- 故障更易定位
- 更容易测试
- 更容易做 observability

所以 Day 72 强调的不是幻想中的“完全自主”，而是：

> **把任务流程明确建模。**

---

## 6. orchestration 为什么是 Agent 系统的真正骨架

工具像器官，LLM 像大脑，而 orchestration 更像神经系统和骨架。

它决定：
- 什么时候调用什么
- 调用后结果放哪
- 失败后怎么处理
- 下一步如何继续

所以没有 orchestration，就很难说你真的有一个完整 agent system。

---

## 7. 今天最该记住的 5 句话

1. **有工具不等于有 agent，关键在 orchestration。**
2. **workflow orchestration 的核心是把能力组织成多步流程。**
3. **shared state 是多步任务的核心基础设施。**
4. **workflow-first 比完全自治更适合真实工程系统。**
5. **orchestration 是 agent 系统真正的骨架。**

---

## 8. 今日任务

### 必做
1. 设计一个 shared state 结构
2. 画出 research agent 的状态流图
3. 为每个步骤定义输入、输出和失败处理
4. 写一句：为什么 workflow 比单次 prompt 更适合多步任务

### 你要能回答的问题
1. 为什么有工具还不够？
2. orchestration 在解决什么问题？
3. shared state 为什么关键？
4. workflow-first 为什么更适合真实系统？
5. 为什么说 orchestration 是 agent 的骨架？

---

## 9. 一句话总结

> Workflow orchestration 的本质，是把多个工具能力、模型推理和中间状态组织成一条可重复执行、可调试、可观察的任务流程，从而让 agent 真正具备稳定完成多步工作的系统能力。
