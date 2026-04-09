# Day 13 — Model Families

## 1. 为什么要学 model families

到 Day 12 为止，你学到的是 Transformer 的核心结构。

但 Transformer 不是只有一种形态。根据任务目标不同，它可以被组织成不同家族：

1. **Encoder-only**
2. **Decoder-only**
3. **Encoder-decoder**

这三类模型家族决定了：
- 输入输出形式
- attention 使用方式
- 适合做什么任务
- 为什么 GPT 成为主流生成式 LLM

所以 Day 13 的重点是：

> **结构选择如何影响任务适配和产品设计。**

---

## 2. Encoder-only

### 代表模型
- BERT
- RoBERTa
- DeBERTa

### 核心特点
Encoder-only 模型使用的是 **双向 self-attention**：
- 每个 token 可以看左边和右边所有 token
- 更适合理解整个输入序列

### 强项任务
- 文本分类
- 情感分析
- 命名实体识别
- 语义匹配
- 检索 embedding / reranking（很多时候）

### 为什么适合理解任务
因为它可以看到完整上下文，适合做：

> “给定一段输入，理解它是什么意思。”

### 局限
它不天然适合 autoregressive 文本生成。

---

## 3. Decoder-only

### 代表模型
- GPT 系列
- LLaMA 系列
- Mistral
- Qwen（大部分生成式版本）

### 核心特点
Decoder-only 模型使用 **causal self-attention**：
- 当前位置只能看自己和前文
- 不能看未来 token

### 强项任务
- 文本生成
- 对话
- 代码生成
- instruction following
- 通用生成式任务

### 为什么它成为主流 LLM 形态
因为很多今天的大模型产品，本质上都可以写成：

> 给定 prompt，继续往后生成。

这和 decoder-only 的 autoregressive 目标完全一致。

### 一句话总结
> Decoder-only 是最自然的生成式大模型架构。

---

## 4. Encoder-decoder

### 代表模型
- T5
- BART
- FLAN-T5

### 核心特点
它有两个部分：
- encoder：先理解输入
- decoder：再基于 encoder 输出生成结果

decoder 中除了 self-attention，还会做 **cross-attention** 去看 encoder 的表示。

### 强项任务
- 翻译
- 摘要
- 问答
- 输入到输出格式转换

### 为什么它适合 sequence-to-sequence
因为它天然把流程拆成：

```text
输入理解
-> 条件生成输出
```

这很适合“给一段输入，生成另一段输出”的任务。

---

## 5. 三大家族最核心的区别

| 家族 | attention 可见性 | 典型任务 | 代表模型 |
|------|------------------|----------|----------|
| Encoder-only | 双向 | 理解、分类、匹配 | BERT |
| Decoder-only | 单向（causal） | 生成、对话、代码 | GPT / LLaMA |
| Encoder-decoder | encoder 双向 + decoder 单向 + cross-attention | 翻译、摘要、seq2seq | T5 / BART |

---

## 6. BERT 为什么强在理解，不强在生成

BERT 在训练时通常做的是：
- Masked Language Modeling
- 让模型同时利用左右文恢复被遮住的 token

这让它非常擅长：
- 建模完整句子语义
- 提取上下文表示

但问题是：
- 它不是按“从左到右”训练的
- 训练目标和 autoregressive generation 不一致

所以 BERT 虽然很强，但它不是今天生成式产品的主流骨架。

---

## 7. GPT 为什么主导生成式 LLM

GPT 类模型做的事情非常直接：

> 给定前文，预测下一个 token。

这和实际产品场景几乎完美对齐：
- 聊天
- 写文章
- 写代码
- 续写
- 调用工具并输出文本

而且 decoder-only 结构：
- 简洁
- 易扩展
- 易做大规模预训练
- 非常适合大规模 next-token prediction

所以今天绝大多数通用生成式 LLM，都是 decoder-only。

---

## 8. T5 / encoder-decoder 为什么仍然重要

虽然通用对话领域 decoder-only 最主流，但 encoder-decoder 仍然非常重要，尤其是在：
- 翻译
- 摘要
- 文本重写
- 输入输出映射清晰的任务

它的优点是：
- 输入理解和输出生成职责清楚
- 对 seq2seq 任务很自然
- 某些任务上更高效

所以它不是过时，而是：

> 更偏“任务导向型生成”，而不是“通用续写型生成”。

---

## 9. 结构选择如何影响产品设计

这部分很重要，因为 Day 13 不只是模型课，也是工程课。

### 如果你做分类器 / reranker / embedding
更可能会用：
- encoder-only

### 如果你做聊天机器人 / 通用助手 / 代码生成
更可能会用：
- decoder-only

### 如果你做翻译 / 摘要 / 改写系统
可能更适合：
- encoder-decoder

所以 architecture choice 不只是论文问题，而是：

> 和你的任务、接口、延迟、训练目标直接相关。

---

## 10. Day 13 和后面 roadmap 的关系

你后面学的：
- causal LM
- KV cache
- vLLM
- LoRA
- Agent

几乎都主要围绕 **decoder-only LLM** 展开。

所以 Day 13 要特别记住：

> 为什么今天主流大模型大多是 decoder-only。

这是后续现代 LLM 学习的入口。

---

## 11. 今天最该记住的 5 句话

1. **Encoder-only 更偏理解任务。**
2. **Decoder-only 更偏生成任务。**
3. **Encoder-decoder 更偏输入到输出的 seq2seq 任务。**
4. **GPT 成为主流，是因为 autoregressive 目标和生成式产品高度一致。**
5. **模型家族选择会直接影响任务适配、训练方式和系统设计。**

---

## 12. 今日任务

### 必做
1. 读 BERT intro
2. 读 T5 overview
3. 结合 GPT / decoder-only 资料做一张比较表
4. 写出：为什么 GPT 主导生成式 LLM

### 你要能回答的问题
1. encoder-only、decoder-only、encoder-decoder 的核心区别是什么？
2. 为什么 BERT 强在理解？
3. 为什么 GPT 强在生成？
4. T5 适合什么任务？
5. 架构选择为什么会影响产品设计？

---

## 13. 一句话总结

> Transformer 的三大模型家族分别面向不同任务：encoder-only 擅长理解，decoder-only 擅长生成，encoder-decoder 擅长输入到输出的映射，而今天通用生成式 LLM 之所以以 GPT 类为主，是因为 decoder-only 与 next-token generation 天然匹配。
