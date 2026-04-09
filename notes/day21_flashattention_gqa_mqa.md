# Day 21 — FlashAttention / GQA / MQA

## 1. 为什么会出现这些注意力优化

到 Day 21，你已经知道几个事实：
- attention 很强
- 长上下文很贵
- KV cache 很重要

那么接下来最自然的问题就是：

> attention 能不能更快、更省显存？

FlashAttention、MQA、GQA，都是在回答这个问题。

它们不是改变 Transformer 的大方向，而是：

> **优化 attention 的计算与服务成本。**

---

## 2. FlashAttention 在解决什么问题

经典 attention 的一个大问题是：
- attention matrix 很大
- 中间张量读写代价高
- 显存 / 内存 IO 成本很重

FlashAttention 的核心思想不是近似 attention，而是：

> 在不改变数学结果的前提下，用更 IO-aware 的方式组织计算，减少显存读写开销。

简单理解就是：
- 不傻乎乎把大中间矩阵全展开再回写
- 尽量在更高效的内存层次上分块完成计算

所以它常常可以：
- 更快
- 更省显存
- 更适合长上下文训练 / 推理

---

## 3. MQA 是什么

MQA = **Multi-Query Attention**。

在普通 multi-head attention 里：
- 每个 head 都有自己的 Q/K/V

而 MQA 的关键改动是：
- 多个 query head 共享同一组 K/V

也就是说：
- Q 仍然是多头
- K/V 变成共享

这样做的主要好处是：
- KV cache 更小
- 推理更省内存
- serving 更高效

---

## 4. GQA 是什么

GQA = **Grouped-Query Attention**。

它可以理解成介于传统 multi-head attention 和 MQA 之间的折中方案：

- 不是所有 query head 都共享同一组 K/V（那是 MQA）
- 也不是每个 head 都独立拥有自己的 K/V（那是标准 MHA）
- 而是：

> 把多个 query head 分组，每组共享一组 K/V

这样做的好处是：
- 比 MHA 更省资源
- 比 MQA 更保留表达能力

所以 GQA 往往是一个很实用的工程折中。

---

## 5. 三者在解决什么层面的问题

### FlashAttention
优化的是：
- attention 计算实现
- IO / memory access pattern

### MQA / GQA
优化的是：
- K/V 表示结构
- KV cache 大小
- 推理内存与吞吐

所以它们不完全是同类问题：
- FlashAttention 更偏 kernel / implementation 优化
- MQA / GQA 更偏 architecture 级别优化

---

## 6. 为什么这些优化对 serving 特别关键

在真实服务系统里，主要压力来自：
- 长上下文
- 高并发
- KV cache 占用
- GPU memory bandwidth

所以如果没有这些优化：
- 延迟容易上升
- 吞吐容易下降
- 成本会非常高

因此你可以把 Day 21 看成：

> 从“会 attention”走向“能理解 attention 系统优化”的开始。

---

## 7. FlashAttention 不等于稀疏 attention

一个容易误解的点是：
- FlashAttention 不是“近似 attention”
- 也不是“稀疏 attention”

它的重点是：

> **同样的精确 attention，换一种更高效的执行方式。**

这点很重要。

---

## 8. MHA vs MQA vs GQA 的直觉比较

### 标准 MHA
- 表达能力强
- K/V 多
- cache 大
- 推理成本高

### MQA
- K/V 最省
- cache 最小
- 推理最省资源
- 但表达能力可能牺牲更多

### GQA
- 在表达能力和资源成本之间折中
- 是现代模型中很常见的实用方案

---

## 9. 今天最该记住的 5 句话

1. **FlashAttention 优化的是 attention 的执行方式，而不是目标函数。**
2. **MQA 让多个 query head 共享同一组 K/V。**
3. **GQA 是 MHA 和 MQA 之间的折中。**
4. **这些方法都强烈服务于长上下文和高效推理。**
5. **理解这些优化，是理解现代 LLM serving 的关键一步。**

---

## 10. 今日任务

1. 阅读 FlashAttention paper abstract / intro
2. 阅读 GQA / MQA explainer
3. 写三张 concept cards：
   - FlashAttention
   - MQA
   - GQA
4. 写清楚：它们分别优化了 attention 的哪一层问题

---

## 11. 一句话总结

> FlashAttention、MQA 和 GQA 都是在为现代 LLM 的长上下文和高效推理服务：前者优化 attention 的执行与 IO 成本，后两者优化 K/V 结构与 cache 开销，从而提升大模型 serving 的速度和资源效率。
