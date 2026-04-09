# Day 20 — KV Cache

## 1. 为什么需要 KV cache

在 decoder-only 模型推理时，生成是逐 token 进行的：
- 先生成一个 token
- 再接着生成下一个
- 每一步都继续往后扩展

问题是：

> 如果每次生成一个新 token，都重新把整个历史序列完整算一遍 attention，会非常浪费。

这就是 KV cache 要解决的问题。

---

## 2. KV cache 的核心思想

在 attention 中，每一步都要用到：
- Query（当前 token）
- Key / Value（历史 token）

对于已经生成过的历史 token：
- 它们的 K 和 V 是不会变的

所以我们可以把历史 token 的 K/V 存起来：

> **下次生成新 token 时，不需要重新计算旧 token 的 K/V，只要追加新 token 的 K/V 即可。**

这就是 KV cache。

---

## 3. 为什么 cache 的是 K 和 V，不是 Q

因为在自回归生成里：
- Query 只和“当前正在生成的位置”有关
- 历史 Query 已经完成使命，不需要重复用
- Key / Value 会被未来所有 token 反复访问

所以缓存最有价值的是：
- K
- V

不是 Q。

---

## 4. KV cache 如何减少计算

没有 cache：
- 每生成一步，都重新算整个前缀的 attention 相关张量

有 cache：
- 旧 token 的 K/V 直接复用
- 只为新 token 计算新的 Q/K/V
- 然后和历史 cache 拼接起来做 attention

因此带来的好处是：
- 延迟下降
- 重复计算减少
- 长生成时收益非常明显

---

## 5. KV cache 的代价

KV cache 不是白送的，它用空间换时间。

也就是说：
- 你减少了重复计算
- 但要占用更多显存 / 内存存历史 K/V

所以 context 越长、batch 越大、层数越多时：
- cache 会越来越大
- 内存压力会非常明显

---

## 6. 为什么 KV cache 对 serving 特别重要

如果没有 KV cache：
- 长对话推理会越来越慢
- 每一步都重复算历史，成本太高

而服务系统（serving）最在意的是：
- latency
- throughput
- GPU memory

所以 KV cache 是几乎所有高效 LLM serving 系统的基础能力。

这也是你后面学 vLLM 时的前置知识。

---

## 7. KV cache 和 context window 的关系

context 越长，历史 token 越多，cache 就越大。

因此 KV cache 和这些问题高度相关：
- 长上下文成本
- 显存占用
- 批处理策略
- attention serving 优化

所以你可以把 KV cache 理解为：

> 自回归模型在长序列推理里的关键状态管理机制。

---

## 8. KV cache 为什么是“推理优化”而不是“训练优化”

训练时通常：
- 整个序列已知
- teacher forcing
- 并行计算整个序列 loss

这时不会像推理那样一步一步扩展历史，因此 KV cache 主要不是训练中的核心优化。

推理时才是：
- 单步生成
- 历史不断增长
- 重复使用旧上下文

所以 KV cache 主要服务于 inference / serving。

---

## 9. 今天最该记住的 5 句话

1. **KV cache 用来避免在生成时重复计算历史 token 的 K/V。**
2. **缓存的是 Key 和 Value，而不是 Query。**
3. **它本质上是用内存换时间。**
4. **上下文越长，KV cache 越重要，也越占资源。**
5. **KV cache 是现代 LLM serving 的基础能力之一。**

---

## 10. 今日任务

1. 阅读 HF cache explanation
2. 阅读 generation with cache docs
3. 写清楚：为什么生成时可以缓存 K/V
4. 思考：KV cache 如何影响推理延迟和显存使用

---

## 11. 一句话总结

> KV cache 通过复用历史 token 的 Key 和 Value，避免了自回归生成过程中对旧上下文的重复计算，是现代 LLM 推理与 serving 系统实现低延迟的重要基础机制。
