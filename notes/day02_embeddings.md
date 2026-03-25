# Day 2 — Embeddings

## 1. 什么是 token
在自然语言处理中，模型不能直接处理原始文本字符串，因此需要先把文本切分成更小的基本单位，这些单位就叫 **token**。  

token 不一定总是完整单词，它可以是：
- 一个词（word）
- 一个子词（subword）
- 一个字符（character）
- 一个标点符号或特殊符号
- 特殊标记（如 `[CLS]`、`[SEP]`、`<bos>`、`<eos>`）

不同 tokenizer 的切分方式不同，因此同一句话在不同模型里可能会被分成不同的 token 序列。

---

## 2. 什么是 token id
tokenizer 会把每个 token 映射到词表（vocabulary）中的一个整数编号，这个编号就是 **token id**。  

token id 的本质是：
- 一个整数索引
- 用来在词表中定位 token
- 本身不携带真正的语义信息

例如：
- `"hello"` 可能对应 id `15496`
- `"world"` 可能对应 id `995`

这里的数字只是编号，不代表 `hello` 和 `world` 的语义关系。

---

## 3. 什么是 embedding
embedding 是把离散的 token id 映射成连续向量表示的过程。  
换句话说，embedding 层会把一个整数 id 转换为一个可学习的向量（vector）。

例如：
- token id `15496` → 一个长度为 `d_model` 的向量
- token id `995` → 另一个长度为 `d_model` 的向量

这个向量就是模型真正处理的输入表示。  
后续的 attention、feed-forward、Transformer block 处理的都不是原始文字，也不是 token id，而是这些 embedding 向量。

---

## 4. 为什么需要 embedding
神经网络不能直接处理字符串，也不能很好地仅靠离散整数编号来学习语义关系。  
因此，模型需要一种**连续、可训练、适合数值计算的表示方式**，embedding 就承担了这个角色。

embedding 的意义在于：
- 把离散符号映射到连续向量空间
- 让模型可以进行矩阵运算和梯度优化
- 让相似 token 在训练后往往能拥有更接近的表示

因此，embedding 是自然语言进入神经网络的第一层表示转换。

---

## 5. one-hot 和 embedding 的区别

### 5.1 one-hot 表示
one-hot 向量的特点是：
- 维度等于词表大小
- 只有一个位置是 1，其余位置全是 0
- 是高维、稀疏表示

问题在于：
- 不同 token 之间几乎没有结构信息
- 无法自然表达“相似词更接近”
- 维度高，不够高效

### 5.2 embedding 表示
embedding 的特点是：
- 是低维、稠密向量
- 每个 token 都有一个可学习的连续表示
- 更适合神经网络计算与训练

训练之后，语义相近或上下文相似的 token，往往会在向量空间中更接近。

### 5.3 核心区别
因此，one-hot 和 embedding 的核心区别在于：

- one-hot 是离散、稀疏、无语义结构的表示
- embedding 是连续、稠密、可学习的表示

---

## 6. embedding matrix 的本质
embedding 层本质上对应一个可训练参数矩阵，通常形状为：

> `vocab_size × d_model`

其中：
- `vocab_size`：词表大小
- `d_model`：向量维度（embedding dimension）

这个矩阵中的每一行都对应一个 token 的向量表示。  
当输入一个 token id 时，本质上就是到这个矩阵中取出对应的那一行。

因此，embedding lookup 可以理解为：
- 输入：token id
- 输出：该 token 在 embedding matrix 中对应的向量

---

## 7. 为什么模型处理 embedding，而不是原始文本或 token id
模型不直接处理原始文本，是因为：
- 字符串无法直接用于神经网络数值计算

模型也不直接把 token id 当作语义表示，是因为：
- token id 只是索引编号
- 相邻 id 不代表语义相近
- id 本身没有连续空间结构

embedding 的作用就是：
- 把离散符号转换成连续向量
- 让模型可以在向量空间中学习表示和关系
- 为后续 attention 和 Transformer block 提供输入基础

所以，Transformer 真正处理的是 embedding 向量，而不是文本本身。

---

## 8. 一个简单流程总结
自然语言输入到 Transformer 的前几步可以概括为：

1. 原始文本  
2. tokenizer 切分成 token  
3. token 映射成 token id  
4. token id 经过 embedding 层映射为向量  
5. Transformer 后续模块处理这些向量表示

也就是说：

> 文本 → token → token id → embedding vector → Transformer

---

## 9. 今天的核心理解
今天最重要的结论是：

- token 是文本切分后的基本单位
- token id 是 token 在词表中的编号
- embedding 是 token 的可学习向量表示
- Transformer 处理的是 embedding，而不是原始文本或离散编号

---

## 10. 一句话总结
embedding 是把离散 token id 映射成连续、可学习的稠密向量表示，使神经网络能够在向量空间中处理语言信息，这也是 Transformer 输入表示的基础。
