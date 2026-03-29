# Day 5 — Self-Attention

## 1. 什么是 Self-Attention

Self-Attention 是对 Day 4 Scaled Dot-Product Attention 的进一步具体化。

它的核心思想是：

> 不是"给定 Q、K、V，怎么算 attention"，
> 而是"**从输入 x 出发，怎么生成 Q、K、V，再做 attention 计算**"。

换句话说，self-attention 承担了两个职责：
1. **投影**：把输入映射成 Query、Key、Value
2. **聚合**：用 Day 4 的 attention 公式聚合信息

---

## 2. Self-Attention vs Scaled Dot-Product Attention

### Day 4：Scaled Dot-Product Attention
你已经有 Q、K、V，直接问：

> 当前 Query 应该关注谁，关注多少，最后拿什么？

答案通过公式给出：

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

### Day 5：Self-Attention
现在没有现成的 Q、K、V，需要先生成它们：

\[
Q = xW_q, \quad K = xW_k, \quad V = xW_v
\]

然后再接上 Day 4 的公式：

\[
output = Attention(Q,K,V)
\]

所以整个流程是：

```text
input x
  ↓
W_q projection
  ↓ Q
  ↓
scaled dot-product attention  ← (同时使用 K、V)
  ↓
output
```

---

## 3. 为什么要有三个线性层（W_q、W_k、W_v）

这是 self-attention 最重要的设计之一。

你可能会问：**为什么不直接用 x 作为 Q、K、V？**

答案有三点：

### 原因 1：角色不同
- **Q**：当前 token 想找什么信息
- **K**：其他 token 提供什么信息特征
- **V**：其他 token 实际给出什么内容

这三个角色虽然都来自同一个输入，但它们的职责不同。  
如果不分开投影，模型就无法区分这些角色。

### 原因 2：可学习的表示变换
- \(W_q\)、\(W_k\)、\(W_v\) 都是可学习参数
- 模型在训练时会学到：
  - 怎样的 Q 投影能匹配相关的 K
  - 怎样的 V 投影能携带重要信息

这比固定投影灵活得多。

### 原因 3：特征空间的适应
不同的 token 对不同的上下文有不同的需求。  
通过分开投影，模型可以学到针对不同任务、不同角色的最优特征表示。

---

## 4. Self-Attention 的流程详解

假设输入 \(x\) 的 shape 是 \((batch, seq\_len, d\_model)\)。

### 第一步：生成 Q、K、V

```python
Q = x @ W_q      # shape: (batch, seq_len, d_model)
K = x @ W_k      # shape: (batch, seq_len, d_model)
V = x @ W_v      # shape: (batch, seq_len, d_model)
```

注意：**Q、K、V 的形状都和 x 一样**。

这意味着：
- 序列中的每个 token 都有对应的 Q、K、V
- 序列长度没有改变

### 第二步：计算相关性分数

```python
scores = Q @ K.T / sqrt(d_k)    # shape: (batch, seq_len, seq_len)
```

这一步后，我们得到一个"相关性矩阵"：
- 行：每个 query token
- 列：每个 key token
- 值：两者的相关性分数

### 第三步：转成注意力权重

```python
weights = softmax(scores, dim=-1)    # shape: (batch, seq_len, seq_len)
```

softmax 后：
- 每一行的权重加起来 = 1
- 权重都在 0 到 1 之间
- 代表每个 query token 应该关注其他 token 的程度

### 第四步：加权聚合 Value

```python
output = weights @ V    # shape: (batch, seq_len, d_model)
```

关键点：**输出 shape 和输入 shape 完全相同**。

这意味着：
- 每个 token 都被更新成一个新的表示
- 新表示融合了整个序列的信息
- 但还是有 seq_len 个 token

---

## 5. Self-Attention 和 RNN 的根本差别

### RNN 的方式
- 一个 token 一个 token 顺序处理
- 前面的信息通过隐藏状态逐步传到后面
- 距离太远的信息容易衰减
- 不能并行计算

### Self-Attention 的方式
- 所有 token 同时处理
- 每个 token 可以直接和所有 token 交互
- 距离不影响信息流动（只受 softmax 的影响）
- 天然可以并行计算

因此，self-attention 在**捕捉长距离依赖**和**计算效率**上都优于 RNN。

---

## 6. Self-Attention 输出代表什么

输出中的每个 token 都是：

> 当前 token 融合了整个序列信息后的新表示。

具体来说，假设输出是 \(output[i]\)，那么：

\[
output[i] = \sum_{j=0}^{n-1} weights[i, j] \cdot V[j]
\]

其中 \(weights[i,j]\) 表示第 i 个 token 对第 j 个 token 的关注程度。

这说明：
- 如果 \(weights[i, j]\) 很大，说明第 i 个 token 很在乎第 j 个 token
- 第 j 个 token 的 Value 会被大量纳入第 i 个 token 的新表示
- 如果 \(weights[i, j]\) 很小，第 j 个 token 的影响就微乎其微

---

## 7. 一个具体例子

假设句子是：

> The cat sat on the mat

当计算 **sat** 的新表示时：

1. **生成 Q、K、V**
   - sat 的 Q：表示"sat 这个 token 想找什么"
   - 所有 token 的 K：表示"我分别代表什么特征"
   - 所有 token 的 V：表示"我分别提供什么内容"

2. **计算注意力**
   - sat 的 Q 和每个 token 的 K 计算匹配度
   - 可能的结果：
     - cat 匹配度高（因为 cat 是主语）
     - on 匹配度次高（因为 on 是介词）
     - mat 也匹配度不错（因为 on the mat 是短语）

3. **聚合信息**
   - sat 的新表示 = 0.4 * cat_V + 0.3 * on_V + 0.2 * mat_V + ...
   - 结果是对主语、介词、地点等信息的融合

所以最终，**sat** 的表示就从"坐"这个词的意思，变成了"谁坐在哪里"这个更丰富的上下文理解。

---

## 8. Self-Attention 在 Transformer 中的位置

Self-Attention 是 Transformer 中最核心的模块，但不是全部。

完整的 Transformer block 包括：

```text
input x
  ↓
[Self-Attention]
  ↓ (融合上下文的 x')
  ↓
[Add & Norm] (残差连接)
  ↓
[Feed-Forward Network]
  ↓ (逐 token 的特征变换)
  ↓
[Add & Norm] (残差连接)
  ↓
output
```

Day 5 我们只关心 Self-Attention 这一块。  
后面的日子会逐步补齐其他部分。

---

## 9. Self-Attention 的计算复杂度

这是一个重要的实际考量。

### 时间复杂度
- 计算相关性分数：\(O(n^2 \cdot d)\)，其中 n 是序列长度，d 是维度
- **这意味着序列越长，计算量越大**

### 空间复杂度
- 存储注意力权重矩阵：\(O(n^2)\)

### 实际影响
- 对于短序列（几百 token）：非常快
- 对于长序列（几千 token）：开始变慢
- 对于超长序列（几万 token）：可能内存爆炸

这也是后续会出现 Sparse Attention、FlashAttention 等优化技术的原因。

---

## 10. Self-Attention 的关键参数

当你写 `SelfAttention(d_model)` 时，关键参数只有：

- **d_model**：输入/输出的维度
  - \(W_q\)、\(W_k\)、\(W_v\) 的输入维度都是 d_model
  - 输出维度也是 d_model

没有其他超参数。

---

## 11. 今天的核心理解

今天最重要的四个理解是：

### 1）Self-Attention = 投影 + Day 4 的 Attention
```
x -> W_q/W_k/W_v -> Q/K/V -> Day 4 的公式 -> output
```

### 2）为什么需要三个线性层
每个层承担不同角色：Q 是查询，K 是索引，V 是值。

### 3）输入输出的 shape 完全相同
\((batch, seq\_len, d\_model)\)  
这说明每个 token 都被原地更新了。

### 4）每个 token 的新表示是序列中所有 token 信息的加权组合
权重由模型动态学出，不是固定的。

---

## 12. 一句话总结

> Self-Attention 通过学习 Q、K、V 的投影，让每个 token 都能根据内容动态决定关注谁、关注多少，从而融合上下文信息得到新表示。

---

## 13. 代码实现复盘

当你写下面这个代码时：

```python
class SelfAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)

    def forward(self, x):
        Q = self.W_q(x)
        K = self.W_k(x)
        V = self.W_v(x)
        output, weights = scaled_dot_product_attention(Q, K, V)
        return output, weights
```

你其实在实现这样的思路：

1. 学习 3 个投影矩阵，把输入映射成 3 个不同的"视角"
2. 用这 3 个"视角"通过 attention 公式进行信息交互
3. 得到一个新的、融合了上下文的表示

这就是 Transformer 强大的秘密。

---

## 14. 常见问题

### Q：为什么输出 shape 和输入 shape 一样？
A：因为我们对每个 token 都进行了 attention 计算。输出的每个位置都是融合信息后的结果，不减少、不增加 token 数量。

### Q：权重矩阵在哪里？
A：就是 \(W_q\)、\(W_k\)、\(W_v\)。这三个 \((d\_model, d\_model)\) 的矩阵就是模型学习的全部参数。

### Q：为什么一定要 softmax？
A：softmax 确保权重分布在 0 到 1 之间，且和为 1。这样才能代表"注意力分配比例"。

### Q：能不能用其他权重生成方式代替 softmax？
A：理论上可以，但 softmax 结合 QK^T 的点积这个选择被证实非常有效。

---

## 15. 今天的复盘建议

学完 Day 5，你可以问自己：

1. **Self-Attention 和 Scaled Dot-Product Attention 的差别是什么？**
2. **为什么需要三个线性层 W_q、W_k、W_v？**
3. **Self-Attention 输出 shape 为什么不变？**
4. **如果我把 W_q、W_k、W_v 全部设成相同的矩阵会怎样？**
5. **Self-Attention 相比 RNN 最大的优势是什么？**

如果你能流畅地回答这些问题，就说明 Day 5 真的理解透了。
