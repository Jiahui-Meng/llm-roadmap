# Day 14 — Mini Transformer

## 1. 为什么要做 mini Transformer

到 Day 14，你已经学完了：
- embeddings
- positional encoding
- self-attention / multi-head attention
- FFN
- residual + layernorm
- masks
- model families

如果你还停留在“每个模块都懂一点”，那说明你只掌握了零件，还没有掌握系统。

所以 Day 14 的目标很明确：

> **把前面所有零件组装成一个最小可运行的 Transformer。**

这一步特别重要，因为它会让你第一次真正形成“模型整体感”。

---

## 2. mini Transformer 的意义

Mini Transformer 不是为了追求性能，而是为了验证：

1. 你是否真的理解各模块如何连接
2. 你是否能追踪输入到输出的 shape 流
3. 你是否知道一个完整模型最少需要哪些组件

所以 Day 14 本质上是：

> **Week 2 的系统集成课。**

---

## 3. 一个最小 Transformer 通常包含什么

如果是一个最小 decoder-only Transformer，通常包括：

1. token embedding
2. positional encoding
3. 一个或多个 Transformer block
4. 最终输出层（映射到 vocab logits）

结构图可以写成：

```text
token ids
-> token embedding
-> positional encoding
-> transformer block x N
-> final hidden states
-> linear head
-> logits over vocabulary
```

---

## 4. 从输入到输出的完整流程

### Step 1：输入 token ids
例如：
```python
x_ids.shape = (batch, seq_len)
```

### Step 2：embedding
```python
x = embedding(x_ids)
```
得到：
```python
(batch, seq_len, d_model)
```

### Step 3：加位置编码
```python
x = x + pos_encoding
```
shape 不变：
```python
(batch, seq_len, d_model)
```

### Step 4：经过 block 堆叠
```python
x = block1(x)
x = block2(x)
...
```
每层输出 shape 仍然不变。

### Step 5：输出到词表维度
```python
logits = lm_head(x)
```
得到：
```python
(batch, seq_len, vocab_size)
```

这就是一个语言模型最基础的输出形式。

---

## 5. logits 是什么

logits 表示：

> 对每个位置，下一个 token 属于词表中每个词的未归一化分数。

例如：
- batch = 2
- seq_len = 10
- vocab_size = 50000

那么 logits shape 是：
```python
(2, 10, 50000)
```

这意味着：
- 第 1 个 batch
- 第 3 个 token 位置
- 对所有 50000 个词
都有一个分数。

softmax 后就得到概率分布。

---

## 6. 为什么 Day 14 很重要

因为从这一天开始，你不再只是知道：
- attention 是什么
- FFN 是什么
- residual 是什么

而是能回答：

> 一个 LLM 的 forward pass 到底是怎么跑下来的？

这是从“概念理解”跨到“模型工程理解”的关键一步。

---

## 7. mini Transformer 和真实大模型的关系

当然，真实大模型会更复杂，比如：
- 更多层
- 更大 hidden size
- 更复杂位置编码（RoPE）
- 更现代的 norm / FFN 设计
- KV cache
- 量化 / serving 优化

但它们的核心骨架并没有变：

```text
embedding
+ positional information
+ repeated blocks
+ output projection
```

所以 mini Transformer 的价值在于：

> 先把骨架彻底搞懂，后面所有现代变体都只是这个骨架上的升级。

---

## 8. mini Transformer 中最容易卡住的点

### 1）shape 不清楚
最常见问题就是：
- embedding 后 shape 是什么
- block 前后 shape 是否变化
- logits 为什么是 `(batch, seq_len, vocab_size)`

### 2）忘了位置编码
如果不加 position，模型顺序感会缺失。

### 3）不理解 block 堆叠
模型不是一个 attention 就结束了，而是多层 block 逐步提取更复杂表示。

### 4）不知道 lm head 的意义
最后一层线性投影不是“装饰”，而是把隐藏表示投到词表空间，生成下一个 token 的打分。

---

## 9. mini Transformer 和 model families 的关系

### 如果你做的是 decoder-only mini Transformer
那它更接近 GPT 风格。

### 如果你做的是 encoder stack
那它更接近 BERT 风格。

### 如果你搭 encoder-decoder
那它更接近 T5 / translation 风格。

通常在学习阶段，最推荐先做：

> **decoder-only mini Transformer**

因为它和后面现代 LLM 路线最接近。

---

## 10. Day 14 和后续 roadmap 的关系

Day 14 是一个非常关键的分界线。

在 Day 14 之前，你学的是：
- Transformer 基础模块

在 Day 15 之后，你开始学：
- tokenization
- causal LM
- context window
- RoPE
- KV cache
- FlashAttention

也就是说：

> Day 14 是“经典 Transformer 基础”到“现代 LLM 工程”的桥梁。

---

## 11. 今天最该记住的 5 句话

1. **Mini Transformer 是对前面所有模块的系统集成。**
2. **一个最小模型至少要有 embedding、position、blocks、output head。**
3. **block 可以反复堆叠，因为输入输出 shape 一致。**
4. **最终 logits 是对词表的打分。**
5. **理解 mini Transformer 的 forward pass，是走向现代 LLM 工程的关键一步。**

---

## 12. 今日任务

### 必做
1. 运行：
   - `code/transformer_basics/mini_transformer.py`
2. 观察：
   - embedding 输出 shape
   - block 输出 shape
   - logits shape
3. 自己画一个 mini Transformer 结构图
4. 用一段话解释从 token ids 到 logits 的全过程

### 你要能回答的问题
1. mini Transformer 最少由哪些模块组成？
2. 为什么必须加 positional encoding？
3. 为什么 block 可以堆很多层？
4. logits 的含义是什么？
5. 为什么 Day 14 是连接现代 LLM 学习的重要桥梁？

---

## 13. 一句话总结

> Mini Transformer 的意义，不是做出一个强模型，而是让你第一次把 embedding、position、attention、FFN、block 和输出层真正连成一个完整的可运行系统，从而为后续现代 LLM 学习建立整体框架。
