# Day 30 — Transformer to vLLM Bridge

## 1. 为什么会从 Transformer 走向 vLLM

前面你已经学了很多模型内部知识：
- self-attention
- KV cache
- FlashAttention / GQA / MQA
- context window
- modern LLM block

这些知识让你理解了：

> **模型为什么强。**

但工程世界马上会问另一个问题：

> **模型怎么才能高效地服务出去？**

一个模型“会推理”，和一个模型“能被大量用户稳定、便宜、快速地调用”，这中间隔着一整层系统工程。

这层系统工程，正是 Day 30 要引出的 vLLM。

---

## 2. Transformer 为什么天然会带来 serving 难题

Transformer 很强，但它也有几个非常不友好的 serving 特性：

### 1）自回归生成是串行的
decoder-only 模型生成时：
- 先出一个 token
- 再接着生成下一个
- 无法像训练时那样把未来一步并行出来

这意味着延迟天然存在。

### 2）上下文越长，成本越高
你已经学过 context window 和 attention 成本。
长 prompt 会带来：
- 更高显存占用
- 更长 prefill 时间
- 更重的 KV cache 压力

### 3）多请求一起服务很复杂
生产环境不是“一个 prompt 跑到底”，而是：
- 很多用户同时发请求
- 请求长度不一致
- 输出长度不一致
- batch 很不规整

这会让 GPU 很难始终高效利用。

---

## 3. 为什么普通“跑模型”不等于“做 serving”

很多人第一次接触 LLM 时，会觉得：
- 我已经能在 transformers 里加载模型
- 我已经能跑 `generate()`
- 那不就能上线了吗？

其实差很远。

### 本地 generate
更像：
- 单人实验
- 原型验证
- 功能测试

### 生产 serving
更关注：
- 吞吐量
- 并发
- 显存管理
- 调度
- 稳定性
- 成本

所以 Day 30 最重要的认知转变是：

> **从“模型能跑”升级到“模型如何被高效服务”。**

---

## 4. vLLM 在补什么问题

vLLM 并不是一个新模型，也不是新的训练框架。

它补的是：

> **LLM inference / serving runtime 这一层。**

它想解决的问题包括：
- KV cache 怎么更高效地存
- 请求怎么更好地调度
- 显存怎么少浪费
- 多用户并发怎么提高吞吐

换句话说，vLLM 在做的不是“让模型更聪明”，而是：

> **让同一个模型被服务得更好。**

---

## 5. Transformer 到 vLLM 的桥梁逻辑

这一桥接的真正逻辑是：

```text
Transformer 是生成模型
-> 生成是自回归串行的
-> 串行生成带来 KV cache 与调度问题
-> 长上下文加重内存压力
-> 多用户并发让 batch 更不规则
-> 需要专门的 serving runtime
-> vLLM 出现
```

所以 vLLM 不是平地起楼，而是：

> Transformer 推理代价和服务约束，天然催生出来的系统层解决方案。

---

## 6. 为什么 Day 20 的 KV cache 是 Day 30 的前置知识

如果你不理解 KV cache，很难真正理解 vLLM 为什么重要。

因为 vLLM 的许多核心优化，最终都绕不开：
- cache 怎么存
- cache 怎么复用
- cache 怎么避免碎片
- 多请求时 cache 怎么调度

也就是说：

### Day 20 教你的是“现象层原理”
- 为什么缓存 K/V 能提升推理效率

### Day 30 开始引你进入“系统层实现”
- 怎么把这些 cache 真正管好，变成高吞吐 serving

---

## 7. 为什么大模型越大，vLLM 这类系统越重要

如果模型很小，随便跑一跑也许问题不大。

但当模型变成：
- 7B
- 14B
- 70B
- 更长上下文
- 更高并发

问题就会一下子爆发：
- 显存不够
- batch 难调
- latency 难控
- GPU 利用率不稳定

这时系统工程的重要性甚至会接近模型本身。

所以在真实 LLM 工程中，很多性能瓶颈不在模型架构，而在 serving runtime。

---

## 8. 为什么这一天是“系统意识切换日”

Day 30 很像一个分界线。

### 之前你主要关注：
- 模型结构
- 表达能力
- block / attention / cache 原理

### 从 Day 30 开始，你开始关注：
- 服务能力
- latency
- throughput
- memory efficiency
- deployment constraints

这意味着你开始从“模型学习者”往“LLM 工程师”切换。

---

## 9. 今天最该记住的 5 句话

1. **Transformer 很强，但 serving 并不天然高效。**
2. **自回归生成、长上下文和多并发会把 serving 问题放大。**
3. **vLLM 是 serving runtime，不是新模型。**
4. **它补的是 KV cache、调度、显存效率和吞吐问题。**
5. **从 Transformer 到 vLLM，是从模型机制走向推理系统机制。**

---

## 10. 今日任务

### 必做
1. 回顾 KV cache 和 context window 的工程含义
2. 阅读 vLLM overview / quickstart
3. 用自己的话写出：为什么普通 `generate()` 不等于生产 serving
4. 画出“Transformer → KV cache → serving runtime → vLLM”的逻辑链

### 你要能回答的问题
1. 为什么 Transformer 会带来复杂的 serving 问题？
2. 为什么长上下文会让 serving 更难？
3. vLLM 解决的是哪一层问题？
4. 为什么 KV cache 是理解 vLLM 的前置知识？
5. 为什么 Day 30 是一个系统意识切换点？

---

## 11. 一句话总结

> 从 Transformer 走向 vLLM，本质上是从“理解大模型为什么会生成”进一步走到“如何把这种生成高效、稳定、可扩展地服务给真实用户”，而 vLLM 正是这一层推理系统工程的代表性答案。
