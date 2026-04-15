# Day 63 — JSON Output Demo

## 1. 为什么 structured generation 第一站是 JSON output

当 LLM 只用来聊天时，输出是自由文本也没关系。

但一旦你想让模型输出被程序直接消费，问题就变了。

程序不是人在读，它需要：
- 可解析
- 可验证
- 字段稳定
- 格式一致

所以 structured generation 的第一步，最自然的切入就是 JSON。

因为 JSON 同时满足：
- 机器可读
- 结构清晰
- 易验证
- 易下游处理

这就是 Day 63 的意义。

---

## 2. JSON output demo 在解决什么问题

自由文本输出常见问题包括：
- 字段顺序乱
- 格式不稳定
- 缺少必要字段
- 多余解释性废话
- 解析困难

JSON output demo 的本质是：

> **验证模型能否按指定结构返回结果，而不是只返回“像答案的文字”。**

这一步非常关键，因为后面：
- schema-constrained generation
- tool calling
- extraction
- workflow automation

都建立在“输出能被代码可靠消费”这个前提上。

---

## 3. 为什么 Day 63 是从“文本生成”走向“系统生成”的分界点

在普通聊天中，LLM 输出一段好看的文字就够了。

但在系统里，你更关心：
- 这个结果能不能 parse？
- 这个字段有没有缺？
- 这个数组是不是合法？
- 下游程序会不会因为格式错直接崩掉？

这说明 JSON output demo 的真正价值在于：

> **把生成结果从“给人看”转向“给系统用”。**

---

## 4. JSON 输出最常见的问题

### 1）额外废话
模型会在 JSON 前后加解释。

### 2）字段缺失
少了关键字段，下游无法处理。

### 3）类型不一致
本来应该是数组，结果输出成字符串。

### 4）格式非法
括号、逗号、引号错了，导致解析失败。

这也是为什么 Day 63 不只是看“看起来像 JSON”，而是要真的 parse 一次。

---

## 5. 为什么 parse success rate 很重要

在 structured generation 场景里，一个最基础的指标就是：

> **输出到底能不能被稳定解析。**

如果 parse success rate 不高，那么即使模型“内容很聪明”，在工程上也很难用。

这和普通聊天完全不同。

所以 Day 63 的重点不是内容多精彩，而是：

> **输出是否稳定且可消费。**

---

## 6. Day 63 和后面几天的关系

Day 63 是最基础的 structured generation 验证。

后面会继续升级：
- Day 64：schema 约束
- Day 65：和自由文本比较稳定性
- Day 66：封装模块
- Day 67：形成项目文档

所以 Day 63 是整个 structured generation mini-module 的起点。

---

## 7. 今天最该记住的 5 句话

1. **JSON output 是 structured generation 最自然的起点。**
2. **它的目标是让模型输出可被程序直接消费。**
3. **“像 JSON”不够，必须真的能 parse。**
4. **parse success rate 是关键基础指标。**
5. **Day 63 标志着从自由文本生成走向系统可消费生成。**

---

## 8. 今日任务

### 必做
1. 设计一个简单 JSON 输出任务
2. 实测模型输出能否稳定 parse
3. 记录至少 3 种常见格式错误
4. 写一句：为什么 JSON output 对下游系统重要

### 你要能回答的问题
1. 为什么 structured generation 要先从 JSON 开始？
2. JSON output demo 在解决什么问题？
3. 为什么 parse success rate 很关键？
4. JSON 输出最常见的失败点是什么？
5. Day 63 为什么是系统生成的分界点？

---

## 9. 一句话总结

> JSON output demo 的本质，是验证模型是否能够从“生成自然语言答案”进一步迈向“生成程序可直接消费的结构化结果”，这是 structured generation 和 agent 系统的基础前提之一。
