# Day 30 — Transformer to vLLM

## 1. 为什么会从 Transformer 走向 vLLM

当模型从“能训练”走向“要上线服务”时，你会遇到新的问题：
- 自回归生成很慢
- KV cache 很占显存
- 多请求并发调度复杂
- GPU 利用率不高

这时候问题已经不再是模型结构，而是：

> **如何高效服务 Transformer / LLM。**

这就是从 Transformer 到 vLLM 的桥梁。

---

## 2. Transformer 的哪些特性导致 serving 难

几个关键点：
1. **自回归生成是串行的**
2. **KV cache 会不断增长**
3. **上下文长度直接影响显存和延迟**
4. **多请求会产生不规则 batch**

这些特性会让标准 serving 方案变得很低效。

---

## 3. vLLM 在解决什么

vLLM 是一个 LLM serving 系统，重点解决：
- 高效管理 KV cache
- 提高吞吐
- 降低显存浪费
- 改善并发服务表现

所以它不是在发明新的 Transformer，而是在问：

> 已经有了 Transformer / LLM，怎样把它服务得更高效？

---

## 4. 这条桥的核心逻辑

Transformer 给了我们强大的生成模型，
但真正部署时，瓶颈来自：
- memory management
- batching
- scheduling
- serving kernel efficiency

因此从 Transformer 走向 vLLM，本质上是：

> 从模型机制走向推理系统机制。

---

## 5. 今天最该记住的 5 句话

1. **Transformer 适合生成，但生成式 serving 很难做高效。**
2. **自回归推理和 KV cache 是 serving 难点的核心来源。**
3. **vLLM 是服务层优化，不是模型结构替代。**
4. **它重点解决显存管理、吞吐和并发问题。**
5. **理解 vLLM 的前提，是先理解 Transformer 推理为什么贵。**

---

## 6. 一句话总结

> 从 Transformer 走向 vLLM，意味着你开始把注意力从“模型怎么工作”转向“模型如何被高效部署与服务”，而这正是现代 LLM 工程能力的重要分水岭。
