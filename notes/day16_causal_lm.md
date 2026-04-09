# Day 16 — Causal Language Model

## 1. 什么是 causal LM

Causal language model（因果语言模型）做的事情很简单：

> 根据前面的 token，预测下一个 token。

也就是：

\[
P(x_t | x_1, x_2, ..., x_{t-1})
\]

整句联合概率可以写成：

\[
P(x_1, ..., x_n)=\prod_{t=1}^{n} P(x_t|x_{<t})
\]

这就是 GPT 类模型最核心的训练目标。

---

## 2. 为什么叫“causal”

因为第 t 个位置只能依赖前文，不能看到未来。

这和 Day 12 的 causal mask 完全对应：
- 训练时不允许偷看未来 token
- 推理时也只能根据已经生成的内容继续往后生成

所以“causal”不是哲学名词，而是：

> **单向、自回归、前文决定后文。**

---

## 3. 训练时怎么做 next-token prediction

假设序列是：

```text
I love machine learning
```

训练时会做成：

### 输入
```text
I love machine
```

### 标签
```text
love machine learning
```

也就是通常说的 **shifted labels**。

更一般地：
- 输入位置 t 的表示
- 负责预测位置 t+1 的 token

---

## 4. teacher forcing 是什么

训练 causal LM 时，通常使用 **teacher forcing**。

意思是：
- 在训练过程中
- 模型每一步都喂入真实前文 token
- 而不是喂自己刚刚生成出来的 token

这样有两个好处：
1. 训练更稳定
2. 可以并行计算整个序列的 loss

---

## 5. 为什么训练可以并行，推理却要串行

这是 causal LM 非常关键的点。

### 训练时
虽然目标是 next-token prediction，但真实前文全部已知。

所以可以一次性把整个序列送进去：
- 用 causal mask 保证每个位置不能看未来
- 同时计算所有位置的预测 loss

所以训练时可以并行。

### 推理时
未来 token 还不存在，只能：
1. 先生成第一个新 token
2. 把它接到上下文后面
3. 再生成下一个
4. 一步一步往后走

所以推理是串行的。

---

## 6. causal LM 为什么适合生成式 LLM

因为很多真实任务都可以写成：

> 给定前文，继续生成后文。

例如：
- 聊天
- 写代码
- 摘要（在 prompt 里条件化）
- 翻译（也可以 prompt 化）
- 工具调用输出

所以 decoder-only causal LM 成了今天最主流的生成式模型目标。

---

## 7. 和 masked LM 的区别

### Causal LM
- 单向
- 预测下一个 token
- 更适合生成

### Masked LM（如 BERT）
- 双向上下文
- 恢复被遮住的 token
- 更适合理解任务

这就是 Day 13 model families 的延续：
- BERT 更偏理解
- GPT 更偏生成

---

## 8. causal LM 的输出是什么

模型输出通常是：
\[
logits \in \mathbb{R}^{(batch, seq\_len, vocab\_size)}
\]

含义是：
- 对于每个位置
- 给整个词表每个 token 一个分数

训练时：
- 用 cross entropy 和 shifted labels 计算损失

推理时：
- 对最后一个位置的 logits 做采样 / greedy / beam 等决策

---

## 9. causal LM 的工程意义

你后面学的很多东西都建立在它上面：
- KV cache
- decoding strategy
- serving latency
- vLLM
- prompt budget
- speculative decoding

因为一切生成性能和成本问题，都和“自回归一步一步生成”有关。

---

## 10. 今天最该记住的 5 句话

1. **causal LM 的目标是根据前文预测下一个 token。**
2. **causal mask 保证训练时不能偷看未来。**
3. **teacher forcing 让训练可以稳定并行化。**
4. **训练可以并行，推理必须串行。**
5. **现代通用生成式 LLM 基本都建立在 causal LM 上。**

---

## 11. 今日任务

1. 阅读 HF language modeling guide
2. 阅读 generation basics
3. 画出 shifted labels 图
4. 写清楚训练 vs 推理的差异

---

## 12. 一句话总结

> Causal language modeling 是以“前文预测后文”为目标的单向自回归训练方式，它既解释了 GPT 类模型为什么适合生成，也解释了为什么训练能并行而推理必须逐 token 串行进行。
