# Day 6 — Multi-Head Attention

## 1. 为什么需要 Multi-Head Attention

你刚完成了 Day 5 的 Self-Attention，现在有个自然的问题：

> 一个 Attention Head 就够了吗？

答案是：**不够**。

### 问题 1：单个 Head 的局限

Day 5 的 Self-Attention 有一个 Q、K、V 投影对，整个序列通过一个 Attention 计算：

```
x -> W_q -> Q
  -> W_k -> K
  -> W_v -> V
  -> Attention(Q, K, V)
  -> output
```

这个 Head 只能学**一种**关注方式。比如，它可能学会：

- "关注距离近的 token" 或 "关注距离远的 token"
- "关注语法关键词" 或 "关注语义关键词"
- "前向关注" 或 "后向关注"

但它**不能同时做多个**。

### 问题 2：语言的多维性

实际上，语言理解需要多个不同的"视角"：

- **语法角度**：关注主语、动词、宾语
- **语义角度**：关注同义词和相关概念
- **实体角度**：关注人名、地名、机构名
- **短语角度**：关注短语边界和结构
- **长距离角度**：关注远处的指代词、递归结构

单个 Attention Head 无法同时捕捉所有这些维度。就像用一台黑白摄像机只能拍黑白照片，用彩色摄像机也只能拍一种色彩的信息。我们需要**多台摄像机，每台关注不同的颜色通道**。

### 问题 3：表达能力的瓶颈

从参数的角度看，\(W_q, W_k, W_v\) 都是 \((d_{model}, d_{model})\) 的矩阵。

这限制了 attention 的表达能力。单个 Head 的投影空间是固定的，模型想要多个不同的"投影视角"，只能要么：
1. **增大 d_model**（参数爆炸）
2. **用多个 Head**（参数高效）

Multi-Head 就是选择方案 2。

---

## 2. Multi-Head Attention 的核心思想

**一句话**：不用一个大的 Attention，改成 h 个小的 Attention，每个学不同的东西。

### 具体流程

给定输入 \(x \in \mathbb{R}^{(batch, seq\_len, d\_model)}\)，假设 \(h = 8\) 个 head：

#### 第一步：投影到 h 个较小的空间

定义 \(d_k = d_v = d_{model} / h\)（每个 head 的维度）。

对每个 head \(i = 1, 2, ..., h\)，执行投影：

\[
Q_i = x \cdot W_q^{(i)}, \quad K_i = x \cdot W_k^{(i)}, \quad V_i = x \cdot W_v^{(i)}
\]

其中 \(W_q^{(i)}, W_k^{(i)}, W_v^{(i)} \in \mathbb{R}^{(d_{model}, d_k)}\)。

投影后：
- \(Q_i, K_i, V_i \in \mathbb{R}^{(batch, seq\_len, d_k)}\)
- 每个 head 的维度都**变小了**（从 d_model 到 d_k）

#### 第二步：在每个 head 上做 Day 5 的 Attention

对每个 head \(i\)，计算 Self-Attention（就是 Day 5 的那个公式）：

\[
head_i = Attention(Q_i, K_i, V_i) = softmax\left(\frac{Q_i K_i^T}{\sqrt{d_k}}\right) V_i
\]

输出：
- \(head_i \in \mathbb{R}^{(batch, seq\_len, d_k)}\)

#### 第三步：拼接所有 head

把 h 个 head 的输出拼接在一起：

\[
concat = [head_1; head_2; ...; head_h]
\]

维度：\(concat \in \mathbb{R}^{(batch, seq\_len, h \cdot d_k)} = \mathbb{R}^{(batch, seq\_len, d_{model})}\)

**注意**：拼接后维度回到了原来的 d_model！

#### 第四步：最后的线性投影

通过一个大的投影矩阵 \(W_o\)（输出投影）：

\[
MultiHeadOutput = concat \cdot W_o
\]

其中 \(W_o \in \mathbb{R}^{(d_{model}, d_{model})}\)。

最终输出：\(MultiHeadOutput \in \mathbb{R}^{(batch, seq\_len, d_{model})}\)

---

## 3. Multi-Head Attention 的完整公式

通常写成：

\[
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W_o
\]

其中：

\[
head_i = Attention(Q W_q^{(i)}, K W_k^{(i)}, V W_v^{(i)})
\]

或者更紧凑的形式：

\[
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W_o
\]

\[
head_i = softmax\left(\frac{(x W_q^{(i)})(x W_k^{(i)})^T}{\sqrt{d_k}}\right) (x W_v^{(i)})
\]

---

## 4. 一个具体的数值例子

假设：
- d_model = 512
- h = 8（8 个 head）
- 所以 d_k = 512 / 8 = 64

### 前向过程

#### 输入
- x: (batch=2, seq_len=10, d_model=512)

#### 第一步：投影
对每个 head i：
- \(W_q^{(i)}\): (512, 64)
- \(W_k^{(i)}\): (512, 64)
- \(W_v^{(i)}\): (512, 64)

计算：
- \(Q_i = x \cdot W_q^{(i)}\): (2, 10, 64)
- \(K_i = x \cdot W_k^{(i)}\): (2, 10, 64)
- \(V_i = x \cdot W_v^{(i)}\): (2, 10, 64)

#### 第二步：Attention
对每个 head i：

\[
scores_i = Q_i \cdot K_i^T / \sqrt{64}
\]

形状：(2, 10, 10)（每个 query 和每个 key 的相关性）

\[
weights_i = softmax(scores_i, dim=-1)
\]

形状：(2, 10, 10)（归一化的权重）

\[
head_i = weights_i \cdot V_i
\]

形状：(2, 10, 64)（加权后的值）

#### 第三步：拼接
```
concat = [head_1; head_2; ...; head_8]
```

形状：(2, 10, 8*64) = (2, 10, 512)

#### 第四步：输出投影
```
W_o: (512, 512)
output = concat @ W_o
```

形状：(2, 10, 512)

**结果**：输入和输出形状完全一样！

---

## 5. Multi-Head 背后的直觉

### 比喻：多个专家视角

想象你要理解一个复杂的事件。单靠一个人的视角不行，需要多个专家：

- **语言学家**：关注语法结构
- **心理学家**：关注人物关系
- **经济学家**：关注财务细节
- **政治家**：关注权力关系

每个专家用自己的 Head 做 Attention，各自关注不同的维度，最后综合所有视角得到更完整的理解。

### 参数的视角

**单 Head 情况**（Day 5）：
```
参数：3 * (512 * 512) = 786K
一个 Head 的投影空间是固定的 (512, 512)
```

**8 Head 情况**（Day 6）：
```
参数：8 * 3 * (512 * 64) + (512 * 512)
    = 8 * 3 * 32768 + 262144
    = 786432 + 262144
    ≈ 1.05M
```

虽然多了一点点参数（大概 33% 增加），但**表达能力提升了很多倍**。

### 学习多个不同的模式

因为每个 Head 的 \(W_q^{(i)}, W_k^{(i)}, W_v^{(i)}\) 都不同，梯度更新会让它们学到不同的模式：

- Head 1：可能学到"关注临近 token"
- Head 2：可能学到"关注同类词汇"
- Head 3：可能学到"关注远处 token"
- ...以此类推

---

## 6. 为什么要维度缩小？（从 d_model 缩到 d_k = d_model / h）

这是个很好的问题。为什么不让每个 head 都用完整的 d_model 维度？

### 原因 1：计算效率

- 单 Head 的 Attention 复杂度：\(O(seq\_len^2 \cdot d_{model})\)
- h Heads 的总复杂度：\(O(h \cdot seq\_len^2 \cdot d_k) = O(seq\_len^2 \cdot d_{model})\)

**总复杂度没变，但分散到 h 个小 head 上，可以更好地并行化！**

### 原因 2：参数数量

- 单 Head（d_model）：3 * d_model²
- h Heads（每个 d_k）：h * 3 * d_k² = h * 3 * (d_model/h)² = 3 * d_model² / h

**参数反而减少了！**（如果 h > 1）

### 原因 3：正则化效果

每个 Head 的维度更小，意味着每个 Head 的投影空间更受限。这有一种"正则化"的效果，避免了某个 Head 过度复杂。

### 原因 4：信息的多样性

如果维度太大，某个 Head 可能会"贪心"地学到所有重要特征，导致其他 Head 学不到东西（这叫 Head Collapse）。维度缩小后，每个 Head 被迫学不同的东西。

---

## 7. 多 Head 的注意力分布

### 观察：不同 Head 学到不同的模式

在实际的 Transformer 中（比如 BERT、GPT），如果你可视化不同 Head 的注意力权重矩阵，你会看到：

- **Head 1**：关注当前词和前一个词（局部模式）
- **Head 2**：关注特殊 token（比如 [CLS] 或 [SEP]）
- **Head 3**：均匀分散（所有 token 等权重）
- **Head 4**：关注某类词汇（比如形容词）
- ...

这说明 Multi-Head 确实让不同的头学到了**不同的关注模式**。

### 为什么会这样？

在训练过程中，梯度下降会自动让每个 Head 学到不同的东西，因为：

1. 如果两个 Head 学的完全一样，梯度就会指向不同的方向，推动它们分化
2. 损失函数对"多样性"有隐式的激励（每个 Head 都对最终结果有贡献）
3. 初始化的随机性也会让不同的 Head 往不同的方向演化

---

## 8. 计算 √d_k 缩放因子的作用

在 Day 4，我们讲过：

\[
Attention = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right) V
\]

分母是 \(\sqrt{d_k}\)，不是 1。为什么？

### 问题：梯度衰退

如果 d_k 很大（比如 512），那么 \(QK^T\) 中的每个元素的量级也会很大。

假设 Q 和 K 都是随机初始化的标准正态分布：
```
E[Q[i,j] * K[j,i]] = 0
E[(Q*K[i,i])^2] ≈ d_k
```

所以 \(QK^T\) 的方差约是 \(d_k\)。

当你用 softmax 时，如果输入的方差很大，softmax 会变得很"尖锐"（一个值接近 1，其他接近 0），导致：

1. **梯度饱和**：softmax 的导数会非常小
2. **信息瓶颈**：权重集中在一个 token 上，其他信息丢失

### 解决：用 √d_k 缩放

通过除以 \(\sqrt{d_k}\)，我们把方差标准化回 1：

\[
E\left[\left(\frac{QK^T}{\sqrt{d_k}}\right)^2\right] \approx 1
\]

这样 softmax 的输入方差就是正常的，梯度也不会饱和。

### 在 Multi-Head 中

因为每个 Head 的维度是 d_k（不是 d_model），所以缩放因子用的是 \(\sqrt{d_k}\)，而不是 \(\sqrt{d_{model}}\)。

---

## 9. Multi-Head Attention 的代码实现

### 最简单的实现

```python
import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # 投影层：注意这里一次性投影到 d_model，然后再分成 h 个 head
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
    
    def split_heads(self, x):
        """
        x: (batch, seq_len, d_model)
        -> (batch, num_heads, seq_len, d_k)
        """
        batch_size, seq_len, d_model = x.size()
        x = x.view(batch_size, seq_len, self.num_heads, self.d_k)
        return x.transpose(1, 2)  # (batch, num_heads, seq_len, d_k)
    
    def forward(self, x):
        # x: (batch, seq_len, d_model)
        batch_size = x.size(0)
        
        # 投影
        Q = self.W_q(x)  # (batch, seq_len, d_model)
        K = self.W_k(x)  # (batch, seq_len, d_model)
        V = self.W_v(x)  # (batch, seq_len, d_model)
        
        # 分割成多个 head
        Q = self.split_heads(Q)  # (batch, num_heads, seq_len, d_k)
        K = self.split_heads(K)  # (batch, num_heads, seq_len, d_k)
        V = self.split_heads(V)  # (batch, num_heads, seq_len, d_k)
        
        # Attention 计算（对每个 head）
        scores = Q @ K.transpose(-2, -1) / (self.d_k ** 0.5)
        # scores: (batch, num_heads, seq_len, seq_len)
        
        weights = torch.softmax(scores, dim=-1)
        # weights: (batch, num_heads, seq_len, seq_len)
        
        context = weights @ V
        # context: (batch, num_heads, seq_len, d_k)
        
        # 拼接所有 head
        context = context.transpose(1, 2)  # (batch, seq_len, num_heads, d_k)
        context = context.contiguous().view(batch_size, -1, self.d_model)
        # context: (batch, seq_len, d_model)
        
        # 输出投影
        output = self.W_o(context)  # (batch, seq_len, d_model)
        
        return output


# 使用例子
d_model = 512
num_heads = 8
batch_size = 2
seq_len = 10

x = torch.randn(batch_size, seq_len, d_model)

mha = MultiHeadAttention(d_model, num_heads)
output = mha(x)

print(f"Input shape: {x.shape}")
print(f"Output shape: {output.shape}")
# Input shape: torch.Size([2, 10, 512])
# Output shape: torch.Size([2, 10, 512])
```

### 理解关键步骤

#### 1) `split_heads`：将 (batch, seq_len, d_model) 变成 (batch, num_heads, seq_len, d_k)

原始：
```
(2, 10, 512)
```

投影后仍然是：
```
(2, 10, 512)
```

然后重塑成：
```
(2, 10, 8, 64)
```

再交换维度：
```
(2, 8, 10, 64)
```

现在第二个维度代表"Head 编号"，后面可以并行计算所有 head。

#### 2) `@` 矩阵乘法：自动对批量和 head 进行广播

```python
scores = Q @ K.transpose(-2, -1)
# Q: (batch, num_heads, seq_len, d_k)
# K.T: (batch, num_heads, d_k, seq_len)
# scores: (batch, num_heads, seq_len, seq_len)
```

PyTorch 的 `@` 对最后两个维度做矩阵乘，对前面的维度自动广播，非常高效。

#### 3) softmax 和加权

```python
weights = torch.softmax(scores, dim=-1)
# 对最后一个维度（seq_len）做 softmax
# 这样每一行的权重加起来 = 1

context = weights @ V
# weights: (batch, num_heads, seq_len, seq_len)
# V: (batch, num_heads, seq_len, d_k)
# context: (batch, num_heads, seq_len, d_k)
```

#### 4) 拼接和重塑

```python
context = context.transpose(1, 2)  
# (batch, num_heads, seq_len, d_k)
# -> (batch, seq_len, num_heads, d_k)

context = context.contiguous().view(batch_size, -1, self.d_model)
# (batch, seq_len, num_heads, d_k)
# -> (batch, seq_len, num_heads * d_k)
# = (batch, seq_len, d_model)
```

最后的 `contiguous()` 是因为 `transpose` 改变了内存布局，需要重新连续化才能 view。

### 一行一行执行的完整演示

```python
# 假设：
d_model = 512
num_heads = 8
d_k = 64
batch_size = 2
seq_len = 10

x = torch.randn(2, 10, 512)

# Step 1: 投影
Q_proj = torch.randn(512, 512)  # W_q
Q = x @ Q_proj  # (2, 10, 512)

# Step 2: 分割成 8 个 head
Q = Q.view(2, 10, 8, 64)  # (2, 10, 8, 64)
Q = Q.transpose(1, 2)     # (2, 8, 10, 64)

K = ...  # 同样处理
V = ...  # 同样处理

# Step 3: Attention
scores = Q @ K.transpose(-2, -1) / 8  # (2, 8, 10, 10)
weights = torch.softmax(scores, dim=-1)
context = weights @ V  # (2, 8, 10, 64)

# Step 4: 拼接
context = context.transpose(1, 2)  # (2, 10, 8, 64)
context = context.view(2, 10, 512)  # (2, 10, 512)

# Step 5: 输出投影
output = context @ W_o  # (2, 10, 512)
```

---

## 10. Multi-Head Attention 和 Day 5 的关系

### 如果你忘记了 Day 5

Day 5 的 Self-Attention 是：

```
x -> W_q, W_k, W_v -> Q, K, V -> Attention(Q,K,V) -> output
```

其中 Attention 就是：

```
softmax(Q @ K.T / sqrt(d_k)) @ V
```

### Multi-Head 就是这个的"并行版"

Multi-Head 是：

```
x -> 8对(W_q, W_k, W_v) -> 8对(Q,K,V) -> 8个Attention -> concat -> W_o -> output
```

每对投影的维度更小（512 变成 64），但数量增加了（1 变成 8）。

**总参数量基本不变，但表达能力大幅提升。**

---

## 11. Multi-Head Attention 的优势总结

| 优势 | 解释 |
|------|------|
| **多角度学习** | 每个 head 学不同的关注模式 |
| **参数高效** | 虽然 head 数增加，但总参数量不增加（甚至减少） |
| **可并行化** | h 个 head 可以独立计算，天然支持 GPU 并行 |
| **表达能力强** | 组合 h 个 head 的输出能表达更复杂的关注模式 |
| **梯度健康** | 小维度的 d_k 让梯度不会饱和 |
| **易于实现** | 代码简单直接，PyTorch 原生支持 |

---

## 12. 常见 Head 数和 d_model 的配搭

实践中常见的配置：

| d_model | num_heads | d_k | 用途 |
|---------|-----------|-----|------|
| 512 | 8 | 64 | BERT-base 的设置 |
| 768 | 12 | 64 | BERT-large 的设置 |
| 1024 | 16 | 64 | 一般中等模型 |
| 2048 | 32 | 64 | 较大的模型 |
| 4096 | 64 | 64 | 很大的模型（如部分 LLaMA） |

**规律**：d_k 通常固定在 64（或 32/128），然后根据模型大小调整 num_heads。

为什么 d_k = 64 这么常见？
- 64 是个"舒适"的大小：
  - 不太小（太小了维度约束太强）
  - 不太大（太大了单个 head 计算量太大）
- 历史原因：Attention is All You Need 论文用的就是这个

---

## 13. Multi-Head Attention 的失败案例：Head Collapse

### 什么是 Head Collapse

在某些模型训练中，你会发现：

- 大部分 head 的注意力分布都很相似
- 只有 1-2 个 head 学到了真正不同的模式
- 其他 head 被"浪费"了

### 原因

1. **参数初始化太相似**：所有 head 初始时都差不多
2. **优化困难**：某个 head 抢先学到了重要特征，其他 head 跟不上
3. **缺乏多样性正则化**：没有显式的约束让 head 多样化

### 解决方案

1. **参数初始化**：用更好的初始化方法（比如 Kaiming 初始化）
2. **多样性正则化**：加一个 loss 项，惩罚 head 之间的相似性
3. **Head 独立性**：确保每个 head 有不同的学习率或训练策略
4. **监测和调试**：定期检查 head 的多样性

---

## 14. 一个具体例子（翻译任务）

假设用 Multi-Head Attention 翻译这句话：

**英文**：The cat sat on the mat

**法文**：Le chat s'est assis sur le tapis

### 每个 Head 可能学到的不同模式

**Head 1 - 局部依赖**：
- sat → cat（直接依赖，距离近）
- on → mat（短语内依赖）

**Head 2 - 远程引用**：
- The → cat（主语引用）
- on → the（冠词关系）

**Head 3 - 词序和语法**：
- sat → on（动词和前置词组合）
- The → mat（整体短语）

**Head 4 - 功能词关注**：
- on、the、sat（功能词的分布）

**Head 5 - 语义相关性**：
- cat ↔ mat（同一场景的概念）

**Head 6 - 句子结构**：
- 监测 SVO（主-谓-宾）顺序

**Head 7 - 对齐信息**：
- English → French（翻译对齐）

**Head 8 - 特殊模式**：
- 其他你想象不到的复杂模式

通过这 8 个 head 的综合，模型能更准确地进行翻译。

---

## 15. 与 Day 5 Self-Attention 的关键对比

| 维度 | Day 5 (Self-Attention) | Day 6 (Multi-Head) |
|------|------------------------|-------------------|
| Head 数 | 1 | h（通常 8-64） |
| Q/K/V 维度 | d_model（512） | d_k（64） |
| 投影矩阵数 | 3 个（W_q, W_k, W_v） | 3h 个 |
| 总参数量 | 3 × d_model² | ~3 × d_model² + d_model²（基本不变） |
| 表达能力 | 单一视角 | 多个视角组合 |
| 并行度 | 低 | 高（h 个 head 可并行） |
| 学习模式 | 一种 attention 模式 | h 种不同模式 |

---

## 16. 代码复盘：从 Day 5 到 Day 6

### Day 5 的代码

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
        
        scores = Q @ K.T / (d_model ** 0.5)
        weights = torch.softmax(scores, dim=-1)
        output = weights @ V
        
        return output
```

### Day 6 的改进

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # 现在有 h 倍的投影层
        self.W_q = nn.Linear(d_model, d_model)  # 投到 h 个小 head
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)  # 拼接后的投影
    
    def forward(self, x):
        # 投影 + 分割成 h 个 head
        Q = self.split_heads(self.W_q(x))  # (batch, h, seq, d_k)
        K = self.split_heads(self.W_k(x))
        V = self.split_heads(self.W_v(x))
        
        # 对每个 head 计算 attention（自动广播）
        scores = Q @ K.transpose(-2, -1) / (self.d_k ** 0.5)
        weights = torch.softmax(scores, dim=-1)
        
        # 加权聚合（对所有 head）
        output = self.merge_heads(weights @ V)  # 拼接回去
        
        # 最后的线性投影
        output = self.W_o(output)
        
        return output
```

**核心改变**：
1. 加了 `num_heads` 参数
2. 改了投影维度从 d_model 到 d_model（但内部分成 h 个 d_k）
3. 加了 `W_o` 输出投影
4. 加了 `split_heads` 和 `merge_heads` 来处理多个 head

---

## 17. 深度思考：为什么这个设计这么有效？

### 从信息论的角度

一个 Attention Head 相当于一个**信息通道**：

- 单通道（Day 5）：信息必须通过一个瓶颈（一个特定的关注模式）
- 多通道（Day 6）：信息可以通过多个并行的通道

**多通道允许更多信息流动**。这符合信息论中的"通道容量"概念。

### 从学习论的角度

训练深度神经网络的关键是**梯度多样性**：

- 如果只有一个 head，梯度方向单一，学习不够灵活
- 多个 head 的梯度来自不同的"任务视角"，学习更灵活

### 从生物视角

人类的视觉系统也是"多头"的：

- 不同的神经回路处理颜色、运动、形状、深度等
- 大脑最后综合所有这些信息做出决策

Multi-Head Attention 某种程度模拟了这个多路径处理的方式。

---

## 18. 常见错误和陷阱

### 错误 1：认为 Multi-Head 就是多层

**错误想法**：Multi-Head Attention 和堆多层 Transformer 是一样的？

**真相**：不一样。
- Multi-Head：同一层内的并行处理
- 多层：不同深度的序列处理

两者都重要，但作用不同。

### 错误 2：Head 数越多越好

**错误想法**：如果 8 个 head 好，那 128 个 head 应该更好？

**真相**：不一定。原因：
- Head 数太多，每个 head 的维度太小（d_k 变成 4），丧失表达能力
- 计算开销会线性增加
- Head Collapse 更容易发生

通常 8-12 个 head 对大多数任务最优。

### 错误 3：忽视 √d_k 缩放

**错误想法**：缩放因子不重要，可以去掉？

**真相**：缩放因子非常关键。
- 没有缩放：softmax 梯度消失
- 有缩放：梯度流动正常

### 错误 4：认为每个 Head 学到的都有用

**错误想法**：8 个 head 就能学到 8 种完全不同的模式？

**真相**：可能有 2-3 个 head 学到有用的模式，其他 head 冗余或没用。这很正常。

---

## 19. 今天的复盘建议

学完 Day 6，你可以问自己：

1. **Multi-Head Attention 和 Self-Attention 的核心区别是什么？**
2. **为什么要把 d_model 分成 h 个 d_k？**
3. **√d_k 缩放因子起什么作用？**
4. **如果有 8 个 head，每个 head 一定学到不同的模式吗？**
5. **代码中 `split_heads` 和 `merge_heads` 分别做什么？**
6. **写出 Multi-Head Attention 的完整 forward pass。**

如果你能流畅地回答这些问题，并能手写代码实现，就说明 Day 6 真的理解透了。

---

## 20. 快速参考表

### 公式速查

单个 Head：
\[
head_i = softmax\left(\frac{Q_i K_i^T}{\sqrt{d_k}}\right) V_i
\]

所有 Heads 拼接：
\[
concat = [head_1; head_2; ...; head_h]
\]

Multi-Head 最终输出：
\[
MultiHead(x) = Concat W_o
\]

### 维度速查

| 对象 | 输入维度 | 输出维度 |
|------|---------|---------|
| x | (batch, seq_len, d_model) | - |
| Q_i | - | (batch, seq_len, d_k) |
| K_i | - | (batch, seq_len, d_k) |
| V_i | - | (batch, seq_len, d_k) |
| scores_i | - | (batch, seq_len, seq_len) |
| head_i | - | (batch, seq_len, d_k) |
| concat | - | (batch, seq_len, d_model) |
| output | - | (batch, seq_len, d_model) |

### 参数速查

```
W_q: (d_model, d_model) -> 投到所有 head
W_k: (d_model, d_model)
W_v: (d_model, d_model)
W_o: (d_model, d_model) -> 拼接后投影

总参数：~4 * d_model^2 (对多 head 没有额外成本)
```

---

## 21. 一句话总结

> Multi-Head Attention 通过让 h 个并行的 head，每个在更小的维度空间（d_k）上独立学习，使模型能从多个角度同时理解数据，在参数几乎不增加的情况下大幅提升表达能力。

---

## 22. 下一步（Day 7 Preview）

现在你已经理解了 Attention 的核心（Day 4-5）和多头设计（Day 6）。

下一步会讲：
- **Positional Encoding**（Day 8）：为什么需要告诉模型 token 的位置
- **Residual Connection & LayerNorm**（Day 10）：为什么需要残差和归一化
- **完整 Transformer Block**（Day 11）：把所有部分组合起来

但在此之前，Day 7 是"复习周"（Week 1 复习）。

预计会做：
- 回顾 Day 1-6 的核心概念
- 整理一份概念地图
- 用代码综合实现一个"迷你 Transformer"，包含多个 Multi-Head Attention 块

---

## 附录：通俗解释

如果用最通俗的语言，Multi-Head Attention 就是：

> 你翻译一篇文章时，不是一个人翻译，而是 8 个翻译官各自关注不同的层面：
> - 翻译官 1 关注句子语法
> - 翻译官 2 关注词汇意思
> - 翻译官 3 关注文化背景
> - 翻译官 4 关注专业术语
> - ...
> 
> 最后把 8 个翻译官的意见综合起来，得到最终的、最准确的翻译。
> 
> 这就是 Multi-Head Attention。
