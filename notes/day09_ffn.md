# Day 9 — Feed Forward Network (FFN)

## 1. 为什么 attention 之后还需要 FFN

很多人学 Transformer 时会有一个误解：

> attention 已经这么强了，为什么还要 FFN？

这是一个很关键的问题。

attention 的作用是：
- 建立 token 和 token 之间的关系
- 让每个 token 从别的 token 那里取信息

但 attention 做完之后，还有一个问题：

> 每个 token 自己拿到上下文后，如何进一步加工、变换、提升表达能力？

这个工作，就是 FFN 做的。

---

## 2. FFN 的核心作用

FFN（Feed Forward Network）可以理解成：

> **对每个 token 单独做一次非线性特征变换。**

注意：
- attention 负责 **token-token interaction**
- FFN 负责 **token-wise transformation**

也就是说：
- attention 让 token 彼此交流
- FFN 让每个 token 在拿到上下文后，自己再做一次深加工

---

## 3. Transformer 中的标准 FFN 公式

原始 Transformer 中，一个 FFN 通常写成：

\[
FFN(x) = max(0, xW_1 + b_1)W_2 + b_2
\]

或者更直观地说：

1. 先线性升维
2. 再过激活函数
3. 再线性降维

典型结构：
- 输入维度：`d_model`
- 中间维度：`d_ff`
- 输出维度：`d_model`

通常：
\[
d_{ff} \gg d_{model}
\]

例如：
- `d_model = 512`
- `d_ff = 2048`

---

## 4. 为什么要先升维再降维

这是 FFN 设计里很重要的一点。

### 升维的意义
把表示投到更高维空间，可以让模型：
- 容纳更多特征组合
- 提升非线性表达能力
- 对每个 token 做更复杂的内部变换

### 降维的意义
再映射回 `d_model`，这样：
- 能和残差连接兼容
- 可以继续送入下一个 Transformer block

所以 FFN 可以看成：

> 输入 token 表示的“扩展加工车间”

---

## 5. attention 和 FFN 的职责分工

这是 Day 9 最重要的理解。

### attention 负责什么？
attention 回答的是：

> 当前 token 应该从其他 token 那里拿什么信息？

### FFN 负责什么？
FFN 回答的是：

> 当前 token 在已经拿到上下文之后，怎样把这些信息重新加工成更有用的内部表示？

### 一句话区分
- attention：**交流**
- FFN：**加工**

---

## 6. FFN 是逐 token 独立作用的

这是 FFN 非常重要的特性。

假设输入 shape：
```python
x.shape = (batch, seq_len, d_model)
```

FFN 处理时并不会让 token 之间再交互，而是：
- 对每个位置上的向量独立应用同一个两层 MLP

所以：
- token A 用 FFN
- token B 也用同一个 FFN
- 参数共享，但计算互不影响

这就是为什么它叫 **position-wise feed-forward network**。

---

## 7. 一个简单例子

假设某个 token 在 attention 之后的表示已经融合了上下文：

```text
"bank" + 附近上下文 -> 更偏向“河岸”或“银行”
```

这时 FFN 的作用就是：
- 对这个上下文化表示做更复杂的特征变换
- 把有用模式突出
- 把不重要模式压下去

也就是说，attention 把上下文拿来了，FFN 再把这些上下文信息“揉一揉、提纯一下”。

---

## 8. 为什么激活函数很重要

如果 FFN 只是两层线性层，中间没有非线性激活，那么：
- 两层线性映射可以合并成一层线性映射
- 表达能力不会真正提升多少

所以必须加入非线性，例如：
- ReLU
- GELU
- SwiGLU（现代 LLM 常见）

### 原始 Transformer
使用的是 ReLU：
\[
max(0, x)
\]

### 现代 LLM
很多模型更常用：
- GELU
- SwiGLU

Day 19 会专门讲现代 LLM block 中 FFN 的升级版。

---

## 9. FFN 与残差结构的关系

在 Transformer block 中，FFN 不是单独裸跑的，而是通常这样出现：

```text
x
-> attention
-> add & norm
-> FFN
-> add & norm
```

所以 FFN 的输入，不是原始 embedding，而是：
- 已经经过 attention
- 已经融合了上下文信息
- 已经过第一次 add & norm 的表示

也就是说：

> FFN 是对“上下文化后的 token 表示”做进一步加工。

---

## 10. shape 如何变化

假设：
- `x.shape = (batch, seq_len, d_model)`
- `d_model = 512`
- `d_ff = 2048`

### 第一步：升维
```python
x @ W1
```
shape：
```python
(batch, seq_len, 2048)
```

### 第二步：激活
shape 不变：
```python
(batch, seq_len, 2048)
```

### 第三步：降维
```python
... @ W2
```
shape：
```python
(batch, seq_len, 512)
```

所以 FFN 的输入输出维度一致，中间会临时变大。

---

## 11. 为什么每个 Transformer block 都需要 FFN

如果一个 block 只有 attention：
- token 可以交流
- 但每个 token 的内部非线性加工能力不足

如果一个 block 只有 FFN：
- 每个 token 只能自己变换
- 无法和其他 token 交互

所以必须两者结合：

> attention 负责“看别人”，FFN 负责“改自己”。

这是 Transformer block 的核心分工。

---

## 12. 与现代 LLM 的关系

原始 Transformer 用的是：
- 2 层线性层 + ReLU

现代 LLM 常见升级：
- GELU
- SwiGLU
- 更高效的 gating 结构

但不管名字怎么变，本质没变：

> 它们仍然是在做 token-wise 的非线性特征变换。

---

## 13. 今天最该记住的 5 句话

1. **attention 负责 token 间交互。**
2. **FFN 负责每个 token 的独立非线性变换。**
3. **FFN 通常是两层线性层，中间带激活。**
4. **FFN 常见结构是先升维再降维。**
5. **Transformer block 需要 attention + FFN 两种能力结合。**

---

## 14. 今日任务

### 必做
1. 阅读 Annotated Transformer 里 FFN 对应部分
2. 阅读 PyTorch `Linear` 文档
3. 运行：
   - `code/transformer_basics/feed_forward.py`
4. 观察输入输出 shape

### 你要能回答的问题
1. FFN 和 attention 的职责区别是什么？
2. 为什么 FFN 要逐 token 独立计算？
3. 为什么 FFN 需要非线性激活？
4. 为什么先升维再降维？
5. 为什么 Transformer block 同时需要 attention 和 FFN？

---

## 15. 一句话总结

> FFN 是 Transformer block 中负责“逐 token 深加工”的模块，它在 attention 完成上下文交互之后，对每个 token 表示再做一次强非线性变换，从而提升模型表达能力。
