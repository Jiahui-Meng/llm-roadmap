# Day 7 — Week 1 Review

## 1. 今天的任务是什么

Day 7 不是新知识点日，而是 **把 Day 1 到 Day 6 串成一个完整系统**。

如果前 6 天你学的是：
- Why Transformer
- Embeddings
- Attention intuition
- Scaled dot-product attention
- Self-attention
- Multi-head attention

那么 Day 7 要完成的事情就是：

> 不再把这些当成 6 个孤立知识点，而是把它们变成一条完整的 Transformer 理解链路。

---

## 2. Week 1 的总图景

Transformer 的核心不是某一个公式，而是一整套从输入到上下文建模的流程：

```text
text
-> tokenization
-> token ids
-> embeddings
-> Q / K / V projections
-> scaled dot-product attention
-> self-attention
-> multi-head attention
-> richer contextual representation
```

这一周你真正学的是：

1. 为什么旧方法（RNN/LSTM）不够好
2. Transformer 的输入表示是什么
3. attention 到底在算什么
4. self-attention 怎样让 token 彼此交互
5. multi-head attention 怎样增强表达能力

---

## 3. Day 1 — Why Transformer

### 核心问题
为什么 Transformer 会替代传统 RNN / LSTM？

### RNN 的主要限制
1. **顺序计算**
   - 一个 token 必须等前一个 token 处理完
   - 很难高效并行

2. **长距离依赖困难**
   - 信息需要通过很多步隐藏状态传递
   - 距离远时容易衰减

3. **训练效率问题**
   - 序列长时训练慢
   - GPU 并行利用率差

### Transformer 的关键突破
Transformer 用 attention 替代递归传播，允许：
- 每个 token 直接看全序列
- 更容易建模长距离依赖
- 大规模并行训练

### 一句话总结
> Transformer 的强大之处，在于让 token 之间进行直接、全局、并行的信息交互。

---

## 4. Day 2 — Embeddings

### 为什么需要 embedding
模型不能直接理解离散 token，例如：
- `cat`
- `dog`
- `attention`

这些只是符号，不是可计算的连续表示。

所以需要：

```text
token -> token id -> embedding vector
```

### embedding 的作用
Embedding 把离散符号映射成连续向量空间，使模型可以：
- 比较相似性
- 学习语义模式
- 在向量空间上做线性代数运算

### one-hot 的问题
- 维度高
- 稀疏
- 不能表达语义相似性

### learned embedding 的优势
- 稠密
- 可训练
- 能逐渐学出有意义的结构

### 一句话总结
> Embedding 是 Transformer 的输入语言，把词变成模型能处理的向量。

---

## 5. Day 3 — Attention intuition

### attention 的直觉
attention 不是平均看所有 token，而是：

> 当前 token 根据任务需求，动态决定更该关注谁。

### Q / K / V 的角色
- **Q（Query）**：我在找什么信息？
- **K（Key）**：我身上有哪些可匹配的特征？
- **V（Value）**：如果你关注我，我能提供什么内容？

### 举例
句子：
> The cat sat on the mat.

如果当前 token 是 `sat`：
- Query 会去找与动作相关的上下文
- 可能更关注 `cat`（谁坐）
- 也会关注 `mat`（坐在哪里）

### 一句话总结
> attention 是一种“按相关性动态取信息”的机制。

---

## 6. Day 4 — Scaled Dot-Product Attention

### 公式
\[
Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

### 拆解理解
#### 第一步：打分
\[
QK^T
\]
表示 query 与所有 key 的匹配程度。

#### 第二步：缩放
\[
\frac{QK^T}{\sqrt{d_k}}
\]
避免当维度较大时，点积值过大导致 softmax 过于尖锐。

#### 第三步：归一化
\[
softmax(...)
\]
把分数变成注意力分布。

#### 第四步：加权聚合
\[
weights \cdot V
\]
根据注意力分布，从所有 value 中加权取信息。

### 为什么除以 `sqrt(d_k)`
如果不缩放：
- 点积会随着维度增大而增大
- softmax 输出过于极端
- 梯度会不稳定

### 一句话总结
> scaled dot-product attention 就是：先打分，再归一化，再用权重聚合 value。

---

## 7. Day 5 — Self-Attention

### 核心变化
Day 4 假设 Q/K/V 已经给你了。

Day 5 的 self-attention 则是：

\[
Q=xW_q,\quad K=xW_k,\quad V=xW_v
\]

也就是说：

> Q/K/V 不是外部给的，而是从输入序列自己投影出来的。

### 为什么需要三个投影矩阵
因为三个角色不同：
- Query：提问者
- Key：被匹配者
- Value：信息提供者

如果直接 `Q=K=V=x`：
- 角色混在一起
- 模型表达能力下降
- 学不到高质量的注意力模式

### self-attention 的本质
每个 token：
- 保留自己的位置
- 对所有 token 打分
- 聚合相关上下文
- 得到新的上下文表示

### 一句话总结
> Self-attention = 从输入中生成 Q/K/V，再在同一序列内部做 attention。

---

## 8. Day 6 — Multi-Head Attention

### 为什么单头不够
单个 attention head 只能学一种关注模式。可语言理解往往同时需要：
- 语法模式
- 语义模式
- 局部依赖
- 长距离依赖
- 实体关系

### 核心公式
\[
MultiHead(Q,K,V)=Concat(head_1,...,head_h)W_o
\]

每个 head：
\[
head_i = softmax\left(\frac{Q_iK_i^T}{\sqrt{d_k}}\right)V_i
\]

### 直觉理解
可以把多头看成多个专家并行分析：
- 一个看语法
- 一个看语义
- 一个看远距离依赖
- 一个看局部词组

最后把这些结果拼接起来，再统一融合。

### shape 变化
假设：
- `d_model = 512`
- `num_heads = 8`
- `d_k = 64`

那么：
- 输入：`(batch, seq_len, 512)`
- 拆头后：`(batch, 8, seq_len, 64)`
- attention 分数：`(batch, 8, seq_len, seq_len)`
- 聚合后：`(batch, 8, seq_len, 64)`
- 合并后：`(batch, seq_len, 512)`

### 为什么最后要 `W_o`
因为 head 们只是并行提取了不同视角的信息，`Concat` 后还需要一次统一投影融合，形成最终表示。

### 一句话总结
> Multi-head attention 让模型能从多个子空间、多个视角同时理解序列。

---

## 9. Week 1 三个最重要的公式

### 公式 1：Scaled Dot-Product Attention
\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

### 公式 2：Self-Attention Q/K/V 投影
\[
Q=xW_q,\quad K=xW_k,\quad V=xW_v
\]

### 公式 3：Multi-Head Attention
\[
MultiHead(Q,K,V)=Concat(head_1,...,head_h)W_o
\]

---

## 10. Week 1 的几个核心对比

### RNN vs Transformer
- RNN：顺序处理，长距离依赖弱
- Transformer：全局交互，并行计算强

### Attention vs Self-Attention
- Attention：Q/K/V 已给定
- Self-Attention：Q/K/V 由输入投影得到

### Self-Attention vs Multi-Head Attention
- Self-Attention：一个 head
- Multi-Head：多个并行 head + 拼接融合

---

## 11. 本周最关键的工程理解

1. **shape 比背公式更重要**
   - 公式背错一小步还好
   - shape 不懂会直接不会实现

2. **attention 是 Transformer 的核心计算模式**
   - 后面所有现代 LLM 改进几乎都围绕它展开

3. **Week 1 不是概念堆砌，而是层层递进**
   - embedding 提供输入表示
   - attention 提供交互机制
   - self-attention 把交互放到序列内部
   - multi-head 提高表达能力

---

## 12. 你现在应该能回答的问题

1. 为什么 Transformer 能替代 RNN？
2. embedding 的作用是什么？
3. Q/K/V 各自代表什么？
4. 为什么要除以 `sqrt(d_k)`？
5. self-attention 和普通 attention 的差别是什么？
6. 为什么一个 head 不够？
7. `W_o` 在 multi-head 里做什么？

如果这些你能顺着讲出来，说明 Week 1 已经真正打底成功。

---

## 13. 下一步预告

Week 2 开始，你会学：
- positional encoding
- FFN
- residual + layernorm
- transformer block
- masks

也就是说，Week 2 要把目前这些“attention 核心”拼成一个完整的 Transformer block。

### 一句话收尾
> Week 1 解决的是“Transformer 如何让 token 和 token 交互”；Week 2 解决的是“如何把这种交互稳定地堆成完整模型”。
