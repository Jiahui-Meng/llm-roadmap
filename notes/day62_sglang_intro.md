# Day 62 — SGLang Intro

## 1. SGLang 在哪个位置

你已经学了：
- vLLM：高效 LLM serving
- structured generation（概念）

SGLang 在这个生态里的位置是：

> **一个面向 LLM 程序化交互的运行时与语言框架。**

它不是替代 vLLM，而是在 serving 之上提供更高层的编程接口，特别适合：
- 多轮结构化交互
- 约束输出
- 复杂 prompt 编排

---

## 2. 为什么需要 SGLang

直接调 LLM API 当然可以工作，但如果任务变得复杂——比如：
- 先生成 JSON
- 再用 JSON 调工具
- 再根据工具结果续写

那裸 API 调用就会变得非常繁琐。

SGLang 的价值是：

> 让复杂 LLM 交互逻辑变得更可编程、更可控、更高效。

---

## 3. SGLang vs vLLM

### vLLM
- 偏底层 serving
- 聚焦吞吐、显存、调度

### SGLang
- 偏上层编程接口
- 聚焦结构化交互和 prompt 编排
- 可以跑在 vLLM 等 backend 之上

所以它们更像互补关系，不是竞争关系。

---

## 4. 你今天要抓住的核心

1. SGLang 是 LLM 程序化交互的框架
2. 它在 serving 层之上
3. 它对 structured output 和 multi-step prompting 特别有帮助

---

## 5. 一句话总结

> SGLang 是面向结构化、可编程 LLM 交互的运行时框架，它在 vLLM 等 serving 引擎之上提供更高层的编排能力，让复杂 LLM 工作流变得更可控。
