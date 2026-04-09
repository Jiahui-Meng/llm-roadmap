# Day 11 — Transformer Block

## 1. 今天学什么

前面几天你已经分别学了：
- Multi-Head Attention
- Positional Encoding
- FFN
- Residual + LayerNorm

Day 11 的目标就是把这些零件真正拼起来，形成一个完整的 **Transformer block**。

这是一个非常关键的节点，因为从今天开始，你不再只是理解“模块”，而是开始理解：

> **Transformer 真正重复堆叠的基本单元是什么。**

---

## 2. 什么是 Transformer block

Transformer block 可以理解成：

> 一层标准的信息处理单元，它会先让 token 彼此交互，再让每个 token 独立加工，最后把输出传给下一层。

在原始 Transformer encoder block 中，结构通常是：

```text
input
-> Multi-Head Self-Attention
-> Add & Norm
-> Feed Forward Network
-> Add & Norm
-> output
```

这个 block 可以反复堆叠很多层，形成完整模型。

---

## 3. 为什么 block 才是 Transformer 的真正单位

很多人以为 Transformer 的核心是 attention 公式。其实更准确地说：

- attention 是核心计算机制
- **block 才是核心结构单位**

原因是：
- 真正被重复堆叠的是 block
- 每层 block 都做一次“交互 + 加工”
- 多层 block 叠加后，模型表达能力才逐步增强

所以 Day 11 的理解非常重要：

> 你必须开始把 Transformer 想成“由许多重复 block 组成的深层系统”。

---

## 4. block 里的第一部分：Multi-Head Attention

### 作用
让每个 token 看整个序列，和其他 token 交互。

### 它解决的问题
- 谁和谁相关
- 当前 token 应该从哪些 token 吸收信息
- 局部依赖、长距离依赖、结构关系如何建模

### 输出是什么
输出依然是：
```python
(batch, seq_len, d_model)
```

但每个 token 的表示，已经不再是原始 embedding，而是：

> 融合了上下文后的表示。

---

## 5. block 里的第二部分：Add & Norm（第一次）

attention 完成之后，不能直接把结果裸着送进下一层。

需要先做：

\[
out_1 = LayerNorm(x + Attention(x))
\]

### 为什么这样做
- `x + Attention(x)`：保留原输入并叠加新信息
- `LayerNorm(...)`：稳定数值分布

这一步的意义是：

> 在保留主干信息的基础上，把 attention 的更新安全注入表示里。

---

## 6. block 里的第三部分：FFN

现在 token 已经有了上下文信息，但还需要进一步加工。

于是接下来：

\[
FFN(out_1)
\]

FFN 的作用不是再和别的 token 交互，而是：

> 对每个 token 独立做一次强非线性变换。

它让 token 在吸收了上下文之后，进一步提炼内部表示。

---

## 7. block 里的第四部分：Add & Norm（第二次）

FFN 之后，再做一次残差和归一化：

\[
out_2 = LayerNorm(out_1 + FFN(out_1))
\]

这一步和前面的逻辑一样：
- 保留上一阶段表示
- 加上 FFN 新学到的修正
- 再稳定一下分布

最终得到本层 block 的输出。

---

## 8. 完整公式视角

一个标准 Transformer block 可以简写为：

### Step 1
\[
h = LayerNorm(x + MHA(x))
\]

### Step 2
\[
out = LayerNorm(h + FFN(h))
\]

这就是最经典的 block 结构。

如果是现代 pre-norm 版本，顺序会略有调整，但逻辑不变：
- attention 子层
- FFN 子层
- 每个子层周围都有 residual + norm

---

## 9. block 内部的信息流

你可以把 block 理解成两阶段流水线：

### 阶段 1：信息交互
Multi-Head Attention 回答：

> 当前 token 该从哪里拿上下文？

### 阶段 2：信息加工
FFN 回答：

> 当前 token 拿到上下文之后，怎样把它变成更有用的内部表示？

所以 block 的本质就是：

> **先交流，再加工。**

---

## 10. shape 如何流动

假设输入：
```python
x.shape = (batch, seq_len, d_model)
```

### 经过 MHA
```python
mha_out.shape = (batch, seq_len, d_model)
```

### Add & Norm 后
```python
h.shape = (batch, seq_len, d_model)
```

### 经过 FFN
```python
ffn_out.shape = (batch, seq_len, d_model)
```

### 第二次 Add & Norm 后
```python
out.shape = (batch, seq_len, d_model)
```

重要结论：

> 一个 block 的输入输出 shape 保持不变。

这正是 block 可以堆叠的原因。

---

## 11. 为什么 block 可以反复堆叠

因为每层 block：
- 输入 shape 不变
- 输出 shape 不变
- 表示逐层变得更丰富

所以可以这样：

```text
embeddings + positions
-> block 1
-> block 2
-> block 3
-> ...
-> block N
```

每往上一层，token 表示都会融入更多抽象结构。

---

## 12. Encoder block vs Decoder block

### Encoder block
通常只有 self-attention + FFN。

### Decoder block
除了 self-attention + FFN，通常还会额外有：
- causal mask
- 在 encoder-decoder 模型中还会有 cross-attention

所以 Day 11 你先重点掌握的是：

> **最基本的 Transformer block 结构。**

---

## 13. block 为什么是现代 LLM 的祖先结构

虽然现代 LLM（LLaMA、GPT 等）做了很多改动，比如：
- RoPE
- RMSNorm
- SwiGLU
- pre-norm

但本质上依旧是在做：

```text
attention 子层
+ 残差/归一化
+ FFN 子层
+ 残差/归一化
```

所以 Day 11 学的 block，不是“过时结构”，而是：

> 所有现代 LLM block 的原型。

---

## 14. 今天最该记住的 5 句话

1. **Transformer 真正被重复堆叠的单位是 block。**
2. **block 的核心是：先 attention，再 FFN。**
3. **attention 负责 token 间交互，FFN 负责 token 内加工。**
4. **每个子层周围都有 residual + normalization。**
5. **block 输入输出 shape 不变，所以可以反复堆叠。**

---

## 15. 今日任务

### 必做
1. 阅读 Annotated Transformer 中 block walkthrough
2. 阅读 PyTorch `TransformerEncoderLayer` 文档
3. 运行：
   - `code/transformer_basics/transformer_block.py`
4. 自己画出 block 结构图

### 你要能回答的问题
1. 为什么 block 才是 Transformer 的真正结构单位？
2. attention 和 FFN 在 block 中各负责什么？
3. 为什么 block 的输入输出 shape 必须一样？
4. Add & Norm 为什么要出现两次？
5. block 和现代 LLM block 的关系是什么？

---

## 16. 一句话总结

> Transformer block 是由 attention 子层、FFN 子层以及残差归一化结构组成的可重复堆叠单元，它是整个 Transformer 乃至现代 LLM 架构的基础骨架。
