# Day 8 — Positional Encoding

## 1. 为什么需要位置编码

到 Day 6 为止，你已经理解了 attention、自注意力和多头注意力。

但这里会出现一个很关键的问题：

> attention 本身知道 token 的“内容相关性”，但它并不知道 token 的“顺序”。

换句话说，如果你只给模型 embedding，而不给位置信息，那么：
- `I love you`
- `you love I`

从 bag-of-token 的角度看，词差不多一样，但语义明显不同。

Transformer 没有像 RNN 那样天然按时间顺序处理序列，因此：

> **位置信息必须显式加进去。**

---

## 2. attention 为什么天然不带位置信息

attention 做的是：
\[
softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

这里用到的是 token 的向量表示，以及它们之间的点积关系。

问题在于：
- 点积只关心向量内容是否匹配
- 并不关心 token 出现在第 1 个位置还是第 10 个位置

所以如果不额外加入位置表示，模型只能学到“谁和谁相关”，学不到“谁在谁前面、谁在谁后面”。

---

## 3. positional encoding 的核心思想

既然 attention 不知道顺序，我们就要主动告诉模型：

> 每个 token 除了有自己的 embedding，还要叠加一个“位置向量”。

也就是：
\[
input = token\_embedding + positional\_encoding
\]

于是序列输入从：
```text
token embedding only
```
变成：
```text
token embedding + position information
```

这样模型就能同时知道：
- 这个 token 是什么
- 这个 token 出现在什么位置

---

## 4. sinusoidal positional encoding

Transformer 原论文使用的是 **sinusoidal positional encoding**（正弦/余弦位置编码）。

定义如下：

\[
PE(pos, 2i)=sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)
\]

\[
PE(pos, 2i+1)=cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
\]

其中：
- `pos`：位置编号
- `i`：维度索引
- `d_model`：模型维度

### 直觉理解
不同维度用不同频率的正弦/余弦波来编码位置。

结果是：
- 每个位置都会有一个唯一的向量模式
- 相邻位置的向量会有连续变化
- 不同距离关系可以通过线性结构体现出来

---

## 5. 为什么用 sin 和 cos

这个设计很巧妙，主要有几个原因。

### 原因 1：连续且平滑
sin/cos 会随着位置平滑变化，模型更容易学习位置变化规律。

### 原因 2：不同频率覆盖不同尺度
高频维度更关注局部位置变化，低频维度更关注更长距离的位置关系。

### 原因 3：相对位置信息可被推导
sin/cos 的组合有助于模型学习“相对距离”而不仅仅是绝对位置。

### 原因 4：可泛化到更长序列
因为是公式生成，而不是查表 learned embedding，所以理论上可以生成比训练时更长的位置编码。

---

## 6. learned positional embedding vs sinusoidal encoding

### learned positional embedding
做法：
- 给每个位置一个可学习向量
- 和 token embedding 一样，训练中更新

优点：
- 灵活
- 对训练分布适应性强

缺点：
- 长度受训练位置上限限制
- 泛化到超长序列时通常较差

### sinusoidal positional encoding
优点：
- 无需训练
- 任意位置可直接计算
- 有更好的长度外推潜力

缺点：
- 固定形式，不够灵活
- 不一定是最适合所有任务的编码方案

---

## 7. 位置编码如何加到输入上

最常见方式：
\[
X = Embedding(tokens) + PE(positions)
\]

其中：
- `Embedding(tokens)` shape = `(batch, seq_len, d_model)`
- `PE(positions)` shape = `(seq_len, d_model)` 或 broadcast 成 `(batch, seq_len, d_model)`

加完后：
- 形状不变
- 但每个 token 向量都同时带有语义和位置信息

---

## 8. 一个小例子

假设：
- `d_model = 4`
- 序列有 3 个位置：0, 1, 2

那位置编码可能长这样（示意）：

```text
pos 0 -> [sin(0), cos(0), sin(0), cos(0)]
pos 1 -> [sin(a), cos(a), sin(b), cos(b)]
pos 2 -> [sin(2a), cos(2a), sin(2b), cos(2b)]
```

你会发现：
- 每个位置都有不同向量
- 相邻位置变化平滑
- 模型可以从这些模式中推断顺序关系

---

## 9. positional encoding 在 Transformer 中的位置

完整输入流程是：

```text
tokens
-> token ids
-> token embeddings
-> add positional encoding
-> send into Transformer block
```

所以位置编码是在 **进入 attention 之前** 加进去的。

这样 Q/K/V 的生成就会基于“内容 + 位置”的联合表示。

---

## 10. positional encoding 的局限

虽然它解决了“位置缺失”的问题，但也有局限：

1. 它是较早期的方案
2. 在现代 decoder-only LLM 中，很多模型更喜欢 **RoPE**
3. 对超长上下文来说，经典位置编码未必最稳

所以你可以把 sinusoidal PE 看成：

> Transformer 早期的标准答案，也是理解现代位置编码方法的起点。

---

## 11. 与后续内容的关系

### 和 RoPE 的关系
Day 18 你会学到 RoPE，它本质上也是一种位置编码思想的升级版本。

### 和 masks 的关系
位置编码告诉模型“位置是什么”，mask 则告诉模型“哪些位置可以看，哪些不可以看”。

### 和 full Transformer block 的关系
没有 position，attention 只能知道相关性；有了 position，attention 才能知道顺序结构。

---

## 12. 今天最该记住的 5 句话

1. **attention 本身不感知顺序。**
2. **Transformer 需要显式加入位置信息。**
3. **位置编码通常和 token embedding 直接相加。**
4. **sinusoidal encoding 用不同频率的 sin/cos 表示位置。**
5. **它是理解 RoPE 等现代位置方案的起点。**

---

## 13. 今日任务

### 必做
1. 读原论文 positional encoding 那一节
2. 读 Annotated Transformer 的对应部分
3. 跑：
   - `code/transformer_basics/positional_encoding.py`
4. 看几个位置的编码值怎么变化

### 你要能回答的问题
1. 为什么 attention 本身不知道顺序？
2. 为什么可以直接把位置编码加到 embedding 上？
3. sinusoidal encoding 为什么用 sin/cos？
4. learned positional embedding 和 sinusoidal encoding 有什么差别？
5. positional encoding 和 RoPE 的关系是什么？

---

## 14. 一句话总结

> Positional encoding 的作用，是把“位置信息”显式注入到 token 表示中，让 Transformer 在没有递归结构的前提下仍然能理解序列顺序。
