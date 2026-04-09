# Day 15 — Tokenization

## 1. 为什么 tokenization 是 LLM 的入口

大模型不能直接读取原始字符串，它看到的不是“句子”，而是：

> 一串 token id

所以 tokenization 是整个 LLM pipeline 的第一步：

```text
raw text -> tokenizer -> token ids -> embeddings -> model
```

如果这一步做得不好，后面所有模块都会受到影响，包括：
- 上下文长度
- 训练效率
- 多语言能力
- 生成质量
- 检索切分策略

---

## 2. tokenization 在解决什么问题

自然语言不是天然离散且固定长度的结构。模型需要把文本变成可处理的离散单元。

最直接的方法似乎是：
- 按单词切
- 每个词一个 id

但这会遇到很多问题：
- 未登录词（OOV）
- 词表太大
- 多语言适配差
- 词形变化太多

所以现代 LLM 通常不直接按“整词”切，而是使用：
- subword tokenization
- byte-level tokenization
- BPE / WordPiece / Unigram 等方法

---

## 3. 为什么 subword 很重要

subword 的核心思想是：

> 不一定把文本切成完整单词，而是切成更高频、更可复用的子词片段。

比如：
- `unbelievable` 可以拆成 `un + believ + able`
- `tokenization` 可以拆成 `token + ization`

优点：
1. 降低 OOV 问题
2. 控制词表大小
3. 提高组合能力
4. 对多语言更稳

---

## 4. 常见 tokenizer 方法

### BPE（Byte Pair Encoding）
- 从字符开始
- 反复合并高频相邻单元
- GPT 系列常见

### WordPiece
- 类似 subword merge 思路
- BERT 系列常见

### Unigram
- 从更大候选集出发
- 通过概率选择最优切分
- SentencePiece 常见

### Byte-level tokenizer
- 直接从 byte 层工作
- 对任意文本更鲁棒
- 常见于 GPT / LLaMA 系生态的一些实现

---

## 5. tokenization 为什么会影响上下文长度

模型的 context window 按 token 计，不按字符也不按单词计。

这意味着：
- 同一句话，不同 tokenizer 切出来 token 数可能不同
- token 数越多，越占上下文预算

例如：
- 英文可能切得较紧凑
- 中文、代码、特殊符号可能切得更碎

所以 tokenization 会直接影响：
- 推理成本
- prompt 预算
- RAG chunking 粒度

---

## 6. 中文和英文 tokenization 的差异

英文往往天然有空格边界，而中文没有显式空格。

这意味着 tokenizer 在中文上常常更依赖：
- subword 模式
- byte / character fallback

所以同样长度的文本：
- 中文 token 数未必少
- 有时反而可能更多

这就是为什么 Day 15 推荐你比较中英 tokenization 行为。

---

## 7. tokenization 和 embeddings 的关系

tokenizer 的输出是 token ids。

后面 embedding 层做的是：
\[
ids -> vectors
\]

所以 tokenization 决定了：
- vocabulary 是什么
- 每个 token id 对应哪个 embedding 向量
- 模型到底以什么粒度理解文本

一句话说：

> tokenizer 决定模型“看到什么单位”。

---

## 8. tokenization 的工程意义

你后面做这些时都要考虑 tokenization：
- prompt 设计
- RAG chunking
- 价格估算
- truncation 策略
- 长文本处理
- 多语言应用

很多实际问题，本质上是 token budget 问题，不是字符数问题。

---

## 9. 今天最该记住的 5 句话

1. **模型看到的是 token，不是原始文字。**
2. **tokenizer 决定模型理解文本的基本粒度。**
3. **subword tokenization 解决 OOV 和词表规模问题。**
4. **context window 按 token 计，不按字符计。**
5. **tokenization 会直接影响多语言表现、成本和系统设计。**

---

## 10. 今日任务

1. 打开 `experiments/tokenization/tokenizer_demo.ipynb`
2. 比较几组中英文句子的 token 数
3. 观察特殊词、长词、中文短句会怎么被切
4. 写下：tokenizer 对上下文长度和系统成本的影响

---

## 11. 一句话总结

> Tokenization 决定了文本如何被离散化成模型可处理的单元，它不仅是输入预处理步骤，更直接影响上下文预算、训练效率、多语言能力和整个 LLM 系统设计。
