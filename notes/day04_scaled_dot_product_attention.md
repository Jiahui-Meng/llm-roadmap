# Day 4 — Scaled Dot-Product Attention

## 1. 什么是 Scaled Dot-Product Attention

Scaled Dot-Product Attention 是 Transformer 中最核心的 attention 计算方式之一。
它的作用是：

> 用当前 token 的 Query 去和所有 token 的 Key 计算相关性分数，再根据这些分数对 Value 做加权汇总，得到当前 token 的新表示。

它的标准公式是：

\[
Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

其中：
- \(Q\)：Query
- \(K\)：Key
- \(V\)：Value
- \(d_k\)：Key 向量的维度

这个公式虽然不长，但实际上完整表达了 attention 的核心流程：
1. 先算相关性
2. 再做缩放
3. 然后转成权重
4. 最后加权聚合信息

---

## 2. 整体流程在做什么

Scaled Dot-Product Attention 可以拆成四步理解：

### 第一步：计算分数 \(QK^T\)
当前 token 的 Query 会和所有 token 的 Key 做点积，得到一个分数矩阵。

这个分数表示：

> 当前 token 与其他 token 的匹配程度有多高。

点积越大，通常说明两个向量越相似、越相关。

---

### 第二步：除以 \(\sqrt{d_k}\)
得到分数后，不是直接进入 softmax，而是先除以 \(\sqrt{d_k}\)。

这一步叫 **scaled（缩放）**。

它的作用是：

> 防止点积结果随着维度增大而变得过大，导致 softmax 输出过于极端。

这也是为什么这个 attention 叫 **scaled dot-product attention**，而不只是 dot-product attention。

---

### 第三步：做 softmax
缩放后的分数会经过 softmax，变成一组权重。

softmax 的作用是：
- 把分数转换成非负值
- 让所有权重加起来等于 1
- 让模型能够表达“更关注谁、少关注谁”

所以这一步相当于：

> 把相关性分数变成真正可用于加权汇总的信息分配比例。

---

### 第四步：对 Value 做加权求和
有了权重之后，就可以对所有 token 的 Value 做加权求和，得到输出。

这一步意味着：

> 当前 token 会从所有 token 中，按重要程度收集信息，并整合成新的表示。

因此，attention 的最终目标不是只算分数，而是通过这些分数完成信息聚合。

---

## 3. 为什么点积可以表示相关性

在 attention 里，Query 和 Key 的点积被用来衡量匹配程度。

直觉上可以这样理解：

- Query 表示“我现在想找什么信息”
- Key 表示“我这里具有什么信息特征”

当 Query 和某个 Key 的方向越接近时，点积通常越大。
这就意味着：

> 当前 token 的需求，与那个 token 的特征越匹配。

所以，点积可以作为一种“相似度”或“相关性”的近似度量。

---

## 4. 为什么要除以 \(\sqrt{d_k}\)

这是 Day 4 最关键的理解点之一。

如果 Key 的维度 \(d_k\) 很大，那么 Query 和 Key 的点积结果也可能会变得很大。
而 softmax 对数值大小非常敏感：

- 如果输入值差异太大
- softmax 输出会变得非常尖锐
- 某一个位置的权重会特别接近 1
- 其余位置会特别接近 0

这样会带来两个问题：
1. 模型过早地“只盯住一个 token”
2. 梯度可能变小，训练不稳定

因此要除以 \(\sqrt{d_k}\)，让分数的尺度更稳定。

可以把这一步理解为：

> 给相关性分数做一个标准化处理，防止数值过大，把 softmax 推得太极端。

所以，缩放的目的不是改变 attention 的本质，而是让训练更稳定、数值更合理。

---

## 5. 为什么需要 softmax

如果只有原始分数 \(QK^T\)，模型只能知道：
- 谁更相关
- 谁没那么相关

但这些分数还不能直接作为“信息汇总比例”来使用。

softmax 的作用是把这些分数转换成权重分布：

- 所有权重都是非负的
- 所有权重加起来等于 1
- 更大的分数对应更大的权重

这就使得模型可以明确表示：

> 当前 token 应该从哪些 token 那里拿多少信息。

因此，softmax 是 attention 从“打分机制”变成“加权聚合机制”的关键一步。

---

## 6. 一个简单的直觉例子

假设当前 token 的 Query 和三个 Key 计算出来的分数是：

- 2.0
- 1.0
- 0.1

经过 softmax 后，可能变成：

- 0.65
- 0.25
- 0.10

这说明：
- 第一个 token 最值得关注
- 第二个 token 也有一定价值
- 第三个 token 影响较小

接着，模型会用这三个权重去加权对应的 Value：

\[
output = 0.65V_1 + 0.25V_2 + 0.10V_3
\]

因此，attention 输出不是某一个 token 的 Value，
而是多个 token 信息的加权组合。

---

## 7. Scaled Dot-Product Attention 的本质

它的本质可以总结为：

> 用 Query 和 Key 计算“该关注谁”，再用这个关注分布去聚合 Value 中真正的信息。

所以 attention 其实做了两件事：

1. **信息检索**：找出哪些 token 更相关
2. **信息聚合**：把相关 token 的内容收集回来

这也是 attention 特别强的地方。
它不是死板地按位置取信息，而是根据内容动态选择信息来源。

---

## 8. 和 Day 3 的关系

Day 3 更偏直觉理解，重点是：
- 什么是 Q / K / V
- self-attention 在做什么
- token 为什么可以“看”整个序列

Day 4 则更进一步，开始理解 attention 的具体数学实现：

- 为什么用点积计算相关性
- 为什么要做缩放
- 为什么要过 softmax
- 为什么最后还要乘 \(V\)

所以可以说：

> Day 3 解决“attention 在干嘛”  
> Day 4 解决“attention 是怎么算出来的”

---

## 9. 代码实现时要注意什么

在自己实现 scaled dot-product attention 时，通常会有下面几个核心步骤：

1. 计算 score：
```python
scores = Q @ K.T
```

2. 做缩放：
```python
scores = scores / math.sqrt(d_k)
```

3. 过 softmax：
```python
weights = softmax(scores)
```

4. 加权汇总 Value：
```python
output = weights @ V
```

因此，一个最小实现通常会返回：
- `output`
- `attention_weights`

如果想更方便调试，也可以额外返回：
- `raw_scores`
- `scaled_scores`

这样可以更清楚地观察 attention 在每一步到底算出了什么。

---

## 10. Toy Tensor 测试记录

为了更直观地理解 attention，我使用了一个非常小的 toy example。

### 输入
```python
q = torch.tensor([[[1.0, 0.0]]])
k = torch.tensor([[[1.0, 0.0],
                   [0.0, 1.0],
                   [1.0, 1.0]]])
v = torch.tensor([[[1.0, 0.0],
                   [0.0, 2.0],
                   [3.0, 3.0]]])
```

### 计算逻辑
- 先算 \(QK^T\)
- 再除以 \(\sqrt{d_k}\)
- 再做 softmax 得到 attention weights
- 最后用 weights 对 V 做加权求和

### 观察重点
- 第一个 query 会更偏向与自己方向更接近的 key
- softmax 后的权重能直观看出“模型更关注谁”
- 最终 output 是多个 value 的加权组合，而不是单一 value 的复制

这个 toy test 很适合拿来验证：
- 数学公式是不是实现对了
- tensor shape 是否正确
- attention weights 是否符合直觉

---

## 11. 今天的核心理解

今天最重要的结论有四点：

### 1）\(QK^T\) 用来计算相关性
Query 和 Key 的点积可以衡量当前 token 与其他 token 的匹配程度。

### 2）除以 \(\sqrt{d_k}\) 是为了稳定数值
如果不缩放，分数可能过大，导致 softmax 过于尖锐，影响训练稳定性。

### 3）softmax 把分数变成权重
这一步让 attention 从“打分”变成“分配注意力”。

### 4）最终输出是对 Value 的加权和
attention 的目标不是只找相关 token，而是把相关信息整合成新的表示。

---

## 12. 一句话总结

> Scaled Dot-Product Attention 的本质，就是先用 Query 和 Key 的点积计算相关性，再通过缩放和 softmax 得到注意力权重，最后对 Value 做加权求和，生成融合上下文的新表示。

---

## 13. 今天的复盘

今天我真正理解的是：

- attention 不是一个抽象概念，而是一个明确的数学计算流程
- `QK^T` 决定关注程度
- `softmax` 决定关注比例
- `V` 才是真正被聚合的信息
- `sqrt(d_k)` 的存在是为了数值稳定，而不是随便加上的技巧

这使我第一次把“attention 的直觉”和“attention 的公式”真正连接起来。
