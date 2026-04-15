# Day 29 — Transformer to LoRA Bridge

## 1. 为什么会从 Transformer 走到 LoRA

你前面已经把 Transformer 的基本骨架学得很清楚了：
- attention
- FFN
- residual / norm
- block 堆叠

如果只停留在“模型怎么工作”，你就只学到了模型内部。

但当模型真正进入工程实践时，一个非常现实的问题马上出现：

> **如果我已经有一个大模型，想让它适应新任务，难道每次都要全量微调吗？**

这个问题，正是 Day 29 要解决的桥梁问题。

LoRA 的出现，不是凭空来的，而是因为 Transformer 的参数结构天然使它成为一个非常适合参数高效微调（PEFT）的模型家族。

---

## 2. Transformer 为什么让“微调成本”变得很高

Transformer 的强大来自大规模参数，尤其是：
- attention projection 矩阵
- FFN 里的大线性层
- 多层 block 堆叠后的整体参数量

当模型从：
- 几千万参数
- 上升到几十亿、上百亿参数

全量微调会变得非常昂贵：
- 显存需求高
- 训练时间长
- 存储多个任务版本成本极高
- 每个新任务都要维护一份完整模型副本

所以问题不是“能不能微调”，而是：

> **有没有更便宜的方法，让模型学会新任务，而不是每次重训整套参数。**

---

## 3. LoRA 在补什么问题

LoRA（Low-Rank Adaptation）要解决的问题非常工程化：

### 它不是要替代 Transformer
它并不改 Transformer 的主干骨架。

### 它也不是让模型变小
底座模型依然在那里。

LoRA 真正做的是：

> **在不改动大部分原始参数的前提下，只训练一小部分增量参数，让模型完成任务适配。**

所以从 Transformer 到 LoRA，这条桥的核心逻辑是：

```text
Transformer 很强
-> 参数很多
-> 全量微调太贵
-> 需要 PEFT
-> LoRA 成为最自然的方案之一
```

---

## 4. 为什么 Transformer 特别适合 LoRA

这是 Day 29 最重要的理解点之一。

Transformer 里有大量线性变换：
- `W_q`
- `W_k`
- `W_v`
- `W_o`
- FFN 的线性层

而 LoRA 本质上就是：

> **对这些线性层的参数更新，做低秩近似。**

也就是说，LoRA 并不是随便贴在模型上，而是非常自然地长在 Transformer 的线性代数结构上。

这就是为什么：
- CNN 上可以做别的方法
- 但在 LLM / Transformer 生态里，LoRA 特别自然、特别流行

因为它和模型结构是高度匹配的。

---

## 5. LoRA 的核心直觉是什么

LoRA 背后的核心直觉可以用一句话说：

> **任务适配所需的参数变化，不一定需要一整个满秩大矩阵来表达。**

也就是说：
- 原模型大矩阵很大
- 但针对一个具体任务，真正需要学习的“偏移量”可能并没有那么复杂
- 于是可以用低秩分解去近似这种变化

这就带来一个非常重要的结果：

- 主模型参数可以冻结
- 只训练小型低秩矩阵
- 成本大幅下降

所以 LoRA 的魅力不只是“能训练”，而是：

> **能以远低于全量微调的成本训练。**

---

## 6. 从 Prompting 到 Fine-tuning，中间为什么需要 LoRA

很多人学到这里会问：

> 既然有 prompt engineering，为什么还要 LoRA？

因为 prompting 和 fine-tuning 解决的问题不完全一样。

### Prompting
适合：
- 临时任务
- 零样本 / 少样本引导
- 不需要改变模型内部行为的情况

### Full fine-tuning
适合：
- 任务很重
- 需要深度改造模型行为
- 资源非常充足

### LoRA
正好卡在中间：
- 比 prompting 更能稳定改变模型行为
- 比 full fine-tuning 成本低很多

所以 LoRA 很像一个现实世界中最常见的工程折中：

> **比 prompt 更强，比 full fine-tune 更省。**

---

## 7. 为什么 Day 29 是一个“桥接日”

Day 29 不是正式讲 LoRA 数学细节的日子，而是一个桥接日。

桥接日的意义在于：

### 前面你学的是模型结构
- Transformer block
- modern LLM block
- context / KV cache / serving

### 从这里开始，你要进入模型适配
- LoRA
- QLoRA
- 数据格式
- 微调实验
- before/after evaluation

所以 Day 29 要完成的，不是背公式，而是建立一个心智转变：

> **从“模型如何工作”走向“模型如何被任务化地改造”。**

---

## 8. LoRA 为什么对今天的大模型工程这么重要

如果没有 LoRA，很多团队会遇到这些问题：
- 没法在有限 GPU 上做微调
- 多任务适配成本太高
- 模型版本管理很重
- 很难快速做领域定制

LoRA 的现实意义是：

> 让大模型定制化，从“大公司专属能力”，变成更多团队可负担的工程手段。

这就是为什么 LoRA 几乎成了 LLM 工程里必学内容。

---

## 9. 今天最该记住的 5 句话

1. **Transformer 的大规模线性层结构，使它天然适合 LoRA。**
2. **LoRA 的动机是：全量微调太贵。**
3. **LoRA 不改主干模型，而是在关键线性层上学习低秩增量。**
4. **LoRA 是 prompting 和 full fine-tuning 之间的重要工程折中。**
5. **从 Transformer 到 LoRA，是从“理解模型”走向“高效改造模型”。**

---

## 10. 今日任务

### 必做
1. 重新回看 Transformer 里有哪些主要线性层
2. 阅读 LoRA paper intro + HF PEFT 概览
3. 写一句自己的理解：为什么 Transformer 特别适合 LoRA
4. 比较：prompting / LoRA / full fine-tuning 的区别

### 你要能回答的问题
1. 为什么全量微调在大模型时代代价很高？
2. 为什么 Transformer 的结构让 LoRA 很自然？
3. LoRA 在工程上补的是什么问题？
4. LoRA 和 prompting 的差别是什么？
5. 为什么 Day 29 是进入微调路线的重要桥梁？

---

## 11. 一句话总结

> 从 Transformer 走向 LoRA，本质上是从“理解大模型内部的大规模线性结构”进一步走到“如何以更低成本对这些结构做任务适配”，而 LoRA 正是大模型参数高效微调最自然、最实用的工程答案之一。
