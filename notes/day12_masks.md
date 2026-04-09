# Day 12 — Masks

## 1. 为什么 Transformer 需要 mask

到现在你已经知道，attention 允许每个 token 看整个序列。

但现实中并不是所有位置都应该被看到。

比如：
- padding token 不应该影响有效 token
- decoder 预测下一个词时，不应该偷看未来 token

所以 attention 里需要一种机制告诉模型：

> **哪些位置能看，哪些位置不能看。**

这个机制就是 **mask**。

---

## 2. mask 的本质

mask 的本质是：

> 在 attention 分数矩阵里，把不允许看到的位置强行屏蔽掉。

回忆 attention：
\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

mask 一般加在 softmax 之前：
\[
softmax\left(\frac{QK^T}{\sqrt{d_k}} + mask\right)
\]

其中被屏蔽的位置通常会加上一个非常大的负数，比如：
- `-1e9`
- `-inf`

这样 softmax 之后，这些位置的权重几乎就是 0。

---

## 3. 两类最重要的 mask

Transformer 里最重要的两类 mask 是：

1. **Padding mask**
2. **Causal mask（look-ahead mask）**

---

## 4. Padding mask

### 什么问题
一个 batch 里的句子长度通常不同，所以需要 padding：

```text
["I love NLP", "Transformers are powerful"]
```

可能会 pad 成相同长度：

```text
[I, love, NLP, PAD]
[Transformers, are, powerful, today]
```

这里 `PAD` 不是实际内容，只是凑长度。

### 为什么必须 mask 掉 PAD
如果不 mask：
- 模型会把 PAD 当成真实 token
- attention 会错误分配权重给 PAD
- 污染表示学习

### 作用
padding mask 的目标是：

> **让真实 token 不去关注 padding 位置。**

---

## 5. Causal mask

### 什么问题
在 decoder-only 模型里，比如 GPT，模型在预测第 t 个 token 时，不能看到未来 token。

例如句子：

```text
I love machine learning
```

当模型预测 `love` 时，它不能看到 `machine` 和 `learning`。

否则训练就变成作弊。

### causal mask 的作用
causal mask 保证：

> 第 i 个位置只能看自己和自己之前的位置，不能看未来位置。

---

## 6. causal mask 的形状直觉

假设序列长度是 4，causal mask 通常是一个上三角屏蔽结构：

```text
[[1, 0, 0, 0],
 [1, 1, 0, 0],
 [1, 1, 1, 0],
 [1, 1, 1, 1]]
```

或者从“被屏蔽”角度看：

```text
[[0, -inf, -inf, -inf],
 [0,    0, -inf, -inf],
 [0,    0,    0, -inf],
 [0,    0,    0,    0]]
```

含义是：
- 位置 0 只能看自己
- 位置 1 可以看 0 和 1
- 位置 2 可以看 0、1、2
- 不能看未来

---

## 7. 为什么 causal mask 对 autoregressive 模型至关重要

GPT 这类模型本质上做的是：

> 根据前文，预测下一个 token。

如果没有 causal mask：
- 模型训练时会直接看到答案
- 损失函数失去意义
- 推理时和训练时行为不一致

所以 causal mask 是 decoder-only 训练目标成立的前提。

---

## 8. encoder 和 decoder 对 mask 的需求不同

### Encoder
通常使用：
- padding mask

因为 encoder 允许看完整输入序列，不需要屏蔽未来。

### Decoder
通常使用：
- padding mask（若有 padding）
- causal mask

因为 decoder 必须保持自回归约束。

---

## 9. mask 在代码里通常怎么实现

最常见做法：

### 第一步
先算 attention scores：
```python
scores = Q @ K.transpose(-2, -1) / sqrt(d_k)
```

### 第二步
对不允许的位置填充负无穷：
```python
scores = scores.masked_fill(mask == 0, -1e9)
```

### 第三步
再做 softmax：
```python
weights = softmax(scores, dim=-1)
```

这样被屏蔽位置的注意力权重就几乎为 0。

---

## 10. mask 为什么加在 softmax 之前

因为 softmax 会把数值转成概率分布。

如果你提前在 softmax 之前把非法位置变成极小值，那么：
- 它们在 softmax 后自然变成接近 0 的概率
- 不需要额外手工归一化

这是一种非常自然且稳定的实现方式。

---

## 11. mask 和 positional encoding 的区别

这两个东西很容易混。

### positional encoding
作用是：
- 告诉模型位置在哪里
- 提供顺序信息

### mask
作用是：
- 告诉模型哪些位置允许访问
- 提供可见性约束

一句话区分：
- positional encoding = **告诉你“位置是什么”**
- mask = **告诉你“哪些位置能看”**

---

## 12. 为什么 mask 是后面很多主题的基础

后面你学到的：
- Causal LM
- decoder-only 模型
- KV cache
- 生成推理

都离不开 mask 的理解。

特别是如果你不理解 causal mask，就很难真正理解：
- 为什么 GPT 是单向的
- 为什么训练和推理都遵循 autoregressive 逻辑

---

## 13. 今天最该记住的 5 句话

1. **mask 用来限制 attention 的可见范围。**
2. **padding mask 用来屏蔽 PAD。**
3. **causal mask 用来阻止模型偷看未来。**
4. **mask 通常在 softmax 前把非法位置置为负无穷。**
5. **没有 causal mask，就没有真正的 autoregressive 训练。**

---

## 14. 今日任务

### 必做
1. 阅读 Hugging Face / PyTorch 关于 causal mask 的说明
2. 运行：
   - `code/transformer_basics/masks.py`
3. 画出一个 4x4 causal mask
4. 自己解释一次 decoder-only 为什么不能看未来 token

### 你要能回答的问题
1. 为什么 attention 需要 mask？
2. padding mask 和 causal mask 的区别是什么？
3. 为什么 causal mask 对 GPT 类模型很关键？
4. mask 为什么通常加在 softmax 前？
5. mask 和 positional encoding 的作用区别是什么？

---

## 15. 一句话总结

> Mask 是 attention 里的可见性控制机制，它确保模型只关注合法位置：padding 不污染表示，decoder 也不能偷看未来，从而保证训练目标和推理逻辑成立。
