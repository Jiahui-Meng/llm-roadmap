# Day 10 — Residual Connection + LayerNorm

## 1. 为什么需要 Residual 和 LayerNorm

当你把 Transformer 叠很多层时，会出现一个非常现实的问题：

> 模型越来越深，但训练越来越不稳定。

深层网络常见问题包括：
- 梯度消失
- 梯度爆炸
- 表示分布不断漂移
- 深层训练困难

Transformer 之所以能堆很多层，一个关键原因就是：

> **Residual Connection + LayerNorm**

这两个机制不是“锦上添花”，而是让深层 Transformer 真的能训起来的关键结构。

---

## 2. Residual Connection 是什么

Residual connection（残差连接）通常写成：

\[
out = x + F(x)
\]

其中：
- `x`：输入
- `F(x)`：某个复杂变换（比如 attention 或 FFN）

### 直觉理解
残差连接的含义是：

> 模型不用每一层都重新发明输入表示，而是在原表示基础上做“增量修正”。

也就是说，层学的不是整个新表示，而是：

> 我应该在输入基础上补充什么修正？

---

## 3. 为什么 residual 有用

### 原因 1：信息更容易流动
如果没有残差连接，信息每一层都必须穿过复杂变换。

有了残差连接后，即使 `F(x)` 学得不好，输入 `x` 也至少能直接传到后面。

### 原因 2：梯度更容易回传
反向传播时，梯度可以沿着 identity path 直接传递，减轻梯度消失问题。

### 原因 3：更容易优化
模型只需要学习“相对于输入的改进”，往往比从零学习一个全新表示更容易。

---

## 4. LayerNorm 是什么

LayerNorm（层归一化）是对每个样本、每个 token 的特征维度做归一化。

给定一个向量：
\[
x = [x_1, x_2, ..., x_d]
\]

LayerNorm 会在特征维度上计算：
- 均值
- 方差

然后做标准化：
\[
\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}}
\]

再乘以可学习参数：
\[
y = \gamma \hat{x} + \beta
\]

### 直觉理解
LayerNorm 的作用是：

> 把每层输出的数值分布拉回比较稳定的范围。

这样模型不会因为中间层数值漂移太厉害而变得很难训练。

---

## 5. 为什么 Transformer 里更适合 LayerNorm

你可能听过 BatchNorm，但 Transformer 更常用 LayerNorm。

### BatchNorm 的问题
BatchNorm 依赖 batch 维度统计量：
- 对序列任务不总是方便
- 对变长序列不够自然
- 对 autoregressive 解码不够理想

### LayerNorm 的优势
LayerNorm：
- 对每个 token 独立处理
- 不依赖 batch 的统计量
- 更适合 NLP 与序列模型

所以 Transformer 标准做法是 LayerNorm，而不是 BatchNorm。

---

## 6. Add & Norm 是什么

在 Transformer 论文图里，你会看到：

```text
Add & Norm
```

它的含义就是：
1. 先残差相加
2. 再做 LayerNorm

例如：
\[
out = LayerNorm(x + F(x))
\]

在原始 Transformer 中：
- attention 后有一次 Add & Norm
- FFN 后再有一次 Add & Norm

所以一个 block 会长这样：

```text
x
-> Multi-Head Attention
-> Add & Norm
-> Feed Forward
-> Add & Norm
```

---

## 7. 为什么 Add & Norm 这么重要

因为 Transformer 的两个核心模块：
- attention
- FFN

本身都会对表示做比较强的变换。

如果没有残差：
- 旧信息容易被覆盖掉
- 深层网络难训练

如果没有归一化：
- 数值分布层层漂移
- 训练不稳定

所以这两个模块的组合，实际上起到了：

> **稳住训练 + 保留信息主干 + 让深层网络可优化**

的作用。

---

## 8. pre-norm vs post-norm

这是一个很重要的延伸话题。

### 原始 Transformer（post-norm）
原论文常写成：
\[
LayerNorm(x + F(x))
\]

也就是：
- 先算子层
- 再残差相加
- 再 LayerNorm

### 现代 LLM 更常见（pre-norm）
很多现代模型更常用：
\[
out = x + F(LayerNorm(x))
\]

即：
- 先 LayerNorm
- 再进入 attention / FFN
- 最后做残差相加

### 为什么 modern LLM 喜欢 pre-norm
因为 pre-norm 在更深的网络里往往训练更稳定，梯度流动更好。

你现在先记住：
- **原始 Transformer：post-norm 常见**
- **现代大模型：pre-norm 更常见**

---

## 9. 一个简单例子

假设输入是某一层表示 `x`。

### attention 子层
```python
attn_out = Attention(x)
out1 = LayerNorm(x + attn_out)
```

### FFN 子层
```python
ffn_out = FFN(out1)
out2 = LayerNorm(out1 + ffn_out)
```

这样每个子层都：
- 保留原始路径
- 叠加当前新变换
- 再把表示规范化

---

## 10. shape 是否变化

这是一个容易忽略的点。

无论是 residual 还是 LayerNorm，它们都不会改变张量主 shape。

假设输入：
```python
(batch, seq_len, d_model)
```

那么：
- `F(x)` 输出也必须是 `(batch, seq_len, d_model)`
- `x + F(x)` 才能合法相加
- LayerNorm 输出 shape 仍然不变

所以：

> residual + layernorm 的作用是稳定表示，不是改变张量结构。

---

## 11. 为什么 Transformer block 里所有模块都要 shape 对齐

因为残差连接要求：
\[
x + F(x)
\]
必须维度一致。

这直接决定了：
- attention 输出维度要回到 `d_model`
- FFN 最终输出也要回到 `d_model`

这就是为什么：
- multi-head attention 最后需要 `W_o`
- FFN 要先升维再降维

本质上都是为了兼容残差路径。

---

## 12. 训练稳定性的核心逻辑

你可以把 Transformer 的训练稳定性理解成三层保护：

### 1）Residual path
给模型一条信息和梯度的高速公路。

### 2）LayerNorm
把数值分布拉回可控范围。

### 3）模块输出 shape 保持一致
使得每层都能安全堆叠。

这三者配合，才让 Transformer 可以堆很多层。

---

## 13. 今天最该记住的 5 句话

1. **Residual connection 让模型学习增量修正，而不是从零重建表示。**
2. **Residual 帮助信息和梯度跨层流动。**
3. **LayerNorm 稳定每层输出的数值分布。**
4. **Transformer 里的 Add & Norm = residual + layer normalization。**
5. **现代 LLM 常更偏好 pre-norm，因为更利于深层训练。**

---

## 14. 今日任务

### 必做
1. 阅读 PyTorch LayerNorm 文档
2. 阅读一篇 residual / skip connection 的解释文
3. 运行：
   - `code/transformer_basics/residual_layernorm.py`
4. 看清楚输入输出 shape 是否保持一致

### 你要能回答的问题
1. residual connection 为什么能缓解深层训练困难？
2. LayerNorm 和 BatchNorm 的区别是什么？
3. 为什么 Add & Norm 是 Transformer 的标准结构？
4. pre-norm 和 post-norm 有什么区别？
5. 为什么 attention 和 FFN 最终都必须回到 `d_model`？

---

## 15. 一句话总结

> Residual connection 负责让信息和梯度顺畅跨层流动，LayerNorm 负责稳定每层表示分布；两者结合，才让 Transformer 能被安全地堆叠成深层模型。
