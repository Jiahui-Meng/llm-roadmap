# Day 49 — Single-User Benchmark

## 1. 为什么 benchmark 要先从 single-user 开始

一提到 benchmark，很多人会立刻想到：
- 高并发
- 压测
- 吞吐曲线
- P95 延迟

但如果你连单用户基线都没有，后面所有并发数据都很难解释。

所以 Day 49 的任务是：

> **先建立一个干净、可重复的单用户性能基线。**

这非常重要，因为 single-user benchmark 是后面并发测试的参照系。

---

## 2. single-user benchmark 在测什么

它测的不是“模型聪不聪明”，而是：
- 单个请求下的延迟
- 首 token 速度
- 持续生成速度
- 内存占用
- prompt 长度变化时的表现

常见指标包括：
- TTFT（time to first token）
- tokens/sec
- total latency
- peak memory

所以 Day 49 的重点是：

> **把“感觉快不快”变成可量化指标。**

---

## 3. 为什么 TTFT 很重要

很多人只看总延迟，但在交互式产品里，TTFT 往往更重要。

因为对用户来说：
- 看到第一个 token 出来时，会觉得系统“开始工作了”
- 如果一直没反应，体验会很差

所以 single-user benchmark 不只是测“多久结束”，还要测：

> **多久开始。**

这对 chat / assistant / coding agent 场景都非常关键。

---

## 4. 为什么要分 prompt 长短和 generation 长短

如果只测一种固定输入，很容易得出误导性结论。

更合理的 single-user benchmark 至少要覆盖：
- 短 prompt + 短输出
- 长 prompt + 短输出
- 短 prompt + 长输出
- 长 prompt + 长输出

因为这些场景压力点不同：
- 长 prompt 更考验 prefill
- 长输出更考验 decode

Day 49 的关键意识之一就是：

> **LLM latency 不是单一数字，而是场景相关的。**

---

## 5. single-user benchmark 为什么是后续优化的地基

你后面还会继续遇到：
- concurrency benchmark
- quantization
- serving runtime 对比
- 模型替换

如果没有 single-user baseline，你很难知道：
- 现在的瓶颈主要在 prefill 还是 decode
- 新优化到底提升了哪一部分
- latency 变化是不是异常

所以 Day 49 不是可有可无的准备工作，而是：

> **所有 serving 优化实验的基准坐标。**

---

## 6. single-user benchmark 常见误区

### 1）只测一次
一次结果很容易受偶然因素影响。

### 2）不控制 prompt / output 长度
导致结果无法比较。

### 3）只看总时间
忽略 TTFT 和 decode speed。

### 4）不记录硬件环境
导致结果不可复现。

这说明 benchmark 不是“随便跑一下”，而是实验设计问题。

---

## 7. 今天最该记住的 5 句话

1. **single-user benchmark 是所有 serving 测试的基线。**
2. **TTFT、tokens/sec、total latency、peak memory 都值得关注。**
3. **单一场景 benchmark 无法代表真实使用表现。**
4. **prompt 长度和输出长度会影响不同性能阶段。**
5. **Day 49 的价值是把性能感觉转成可量化基准。**

---

## 8. 今日任务

### 必做
1. 设计 4 种单用户 benchmark 场景
2. 为每种场景记录 TTFT / total latency / tokens/sec
3. 补充硬件环境说明
4. 写一句：当前 serving 性能的主要压力点是什么

### 你要能回答的问题
1. 为什么要先做 single-user benchmark？
2. TTFT 为什么重要？
3. 为什么 prompt 长度和 generation 长度要分开测？
4. single-user benchmark 对后续优化有什么价值？
5. benchmark 最常见误区有哪些？

---

## 9. 一句话总结

> Single-user benchmark 的本质，是为模型 serving 建立一个干净、可重复、可量化的性能基线，让你后续对并发、量化和运行时优化的讨论都建立在可信参考坐标之上。
