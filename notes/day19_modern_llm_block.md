# Day 19 — Modern LLM Block

## 1. 为什么要学 modern LLM block

你在 Day 11 学的是经典 Transformer block：
- Multi-Head Attention
- Add & Norm
- FFN
- Add & Norm

但现代 LLM（如 LLaMA、Mistral 等）并不是原封不动照抄 2017 Transformer。

它们通常会做一些关键升级，例如：
- RoPE
- RMSNorm
- SwiGLU
- pre-norm

所以 Day 19 的重点是：

> **理解现代 LLM block 相比经典 Transformer block 改了什么，为什么要这样改。**

---

## 2. 经典 block vs 现代 block

### 经典 Transformer block
- absolute/sinusoidal positional encoding
- LayerNorm
- ReLU FFN
- 原始 Add & Norm 结构

### 现代 LLM block
常见变体：
- RoPE 取代 classic positional encoding 注入方式
- RMSNorm 替代 LayerNorm
- SwiGLU 替代简单 ReLU FFN
- pre-norm 更常见

这些改动的目标通常是：
- 训练更稳定
- 表达能力更强
- 推理更高效
- 更适配 decoder-only 生成模型

---

## 3. RMSNorm 是什么

RMSNorm（Root Mean Square Norm）可以理解成 LayerNorm 的轻量化变体。

它不像 LayerNorm 那样显式减去均值，而更关注：

> 把向量的整体尺度控制住。

直觉上：
- LayerNorm 更完整
- RMSNorm 更简单、更省一些计算

为什么现代 LLM 喜欢它：
- 效率更好
- 效果往往也足够强
- 在大模型实践中被证明可行

---

## 4. SwiGLU 是什么

Day 9 你学了原始 FFN：
- Linear
- ReLU
- Linear

现代 LLM 常把 FFN 换成更强的 gated 结构，比如 **SwiGLU**。

它的核心思想是：

> 不只是做简单非线性，还通过 gating 机制更灵活地控制信息流。

可以粗略理解成：
- 一路产生内容
- 一路产生门控
- 两者结合后再输出

这通常能提升表达能力。

---

## 5. pre-norm 为什么更常见

原始 Transformer 常写成 post-norm：
\[
LayerNorm(x + F(x))
\]

现代 LLM 更常见的是 pre-norm：
\[
out = x + F(Norm(x))
\]

为什么？
- 更深层模型训练更稳
- 梯度流动通常更好
- 工程实践中更适合大模型堆叠

所以 modern LLM block 往往会优先采用 pre-norm 风格。

---

## 6. RoPE 在 modern block 中的位置

RoPE 通常不是一个独立层直接加在输入上，而是：

> 在 attention 子层内部，对 Q/K 注入位置信息。

这使 modern block 在位置编码上和经典 Transformer 有很大差别。

---

## 7. 为什么 modern block 更像“面向生成优化的 Transformer”

现代 LLM block 的所有改动，几乎都在服务于一个事实：

> 今天主流大模型是大规模 decoder-only 生成模型。

所以 modern block 更关注：
- 自回归推理效率
- 长上下文适配
- 深层训练稳定性
- 更强 FFN 表达能力

这和 2017 年通用 Transformer 的目标略有不同。

---

## 8. Day 19 的核心理解

你今天不用把所有现代 block 细节背下来，但要建立这个框架：

### 经典 block 的骨架没变
仍然是：
- attention 子层
- FFN 子层
- residual / norm

### 现代 block 的改动点
主要是把：
- 位置机制
- 归一化方式
- FFN 激活结构
- 子层摆放方式

做了更适合 LLM 的升级。

---

## 9. 今天最该记住的 5 句话

1. **现代 LLM block 仍然继承经典 Transformer block 骨架。**
2. **RoPE、RMSNorm、SwiGLU、pre-norm 是常见升级点。**
3. **这些升级主要服务于 decoder-only 大模型训练和推理。**
4. **RMSNorm 更轻量，SwiGLU 更强表达，RoPE 更适合现代位置建模。**
5. **理解 modern block，就是理解经典 Transformer 如何演化成今天的 LLM。**

---

## 10. 今日任务

1. 阅读 LLaMA architecture explainer
2. 阅读 RMSNorm 论文摘要
3. 写出：经典 block vs modern block 的差别
4. 用自己的话解释：为什么这些升级适合大模型

---

## 11. 一句话总结

> Modern LLM block 本质上仍然是 Transformer block，但它通过 RoPE、RMSNorm、SwiGLU 和 pre-norm 等改造，更好地适应了大规模 decoder-only 语言模型在训练稳定性、长上下文和推理效率上的需求。
