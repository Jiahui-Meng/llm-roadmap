# Day 35 — RAG Embedding Selection

## 1. 为什么 embedding selection 是 RAG 的关键决策

RAG 的 dense retrieval 很大程度上取决于一个东西：

> **你的 embedding 模型，到底把文本表示成了什么样的向量。**

很多人把 embedding 当成“默认组件”，随便选一个就往前走。

但实际上，embedding 模型几乎决定了：
- 语义相似性能否被正确编码
- query 和文档是否能对齐
- 检索召回的上限
- 多语言、代码、专业领域的适配能力

所以 Day 35 的重点是：

> **embedding 不是辅助件，而是 dense retrieval 的核心引擎。**

---

## 2. embedding 模型在 RAG 中到底做什么

在 RAG 里，embedding 模型同时处理两类对象：
- user query
- document chunks

然后把它们映射到同一个向量空间里。

如果这个空间学得好：
- 相似语义会靠近
- 相关 query 和 chunk 会对齐

如果这个空间学得不好：
- 真相关的东西可能离得很远
- 表面相似但语义不对的东西反而更近

所以 embedding selection 的本质是：

> **你选的不是一个模型名字，而是一个语义空间。**

---

## 3. 选择 embedding 时最常见的维度

### 1）通用能力
模型是否对常见英文 / 中文 / 技术文本都有不错表现。

### 2）领域适配
如果你做的是：
- 医疗
- 法律
- 金融
- 代码

就要考虑通用 embedding 是否足够。

### 3）多语言能力
如果 query 和文档语言不完全一致，多语言 embedding 很重要。

### 4）向量维度
维度越高不一定越好。
- 高维可能表达更丰富
- 但索引成本更高
- 检索和存储更贵

### 5）推理成本
embedding 计算本身也有成本，特别是大规模 ingestion 时。

---

## 4. 为什么“好模型”不一定适合你的 RAG

一个常见误区是：

> leaderboard 上高分 = 我的系统一定更好

不一定。

因为 RAG embedding selection 要看具体任务：
- 文档是长文本还是短文本？
- query 是自然问句还是关键词？
- 需要跨语言吗？
- 是否需要代码检索？
- 是否有强领域术语？

举例：
- 一个通用 embedding 在开放问答很好
- 但在半导体术语检索里可能一般

所以 embedding 选择不能只看排行榜，而要看：

> **任务分布与语料分布。**

---

## 5. query-document 对齐为什么重要

RAG 检索不是“文档找文档”，而是“query 找文档”。

所以一个 embedding 模型必须擅长：
- 把用户提问映射到语义空间
- 再和文档 chunk 建立相关性

如果模型只擅长句子相似度，不擅长 query-to-passage retrieval，效果就未必好。

因此在选择 embedding 时，要意识到：

> **不是所有 embedding 都同样适合检索任务。**

---

## 6. embedding selection 和 chunking 的关系

Day 34 和 Day 35 是紧密相连的。

因为 embedding 吃进去的是 chunk。

这意味着：
- chunk 太大，embedding 可能把主题平均化
- chunk 太小，embedding 可能缺少足够语义上下文

所以 embedding selection 不是孤立选择，而是和 chunking 联动的。

也就是说：

> **你最终检索效果，是 chunking 和 embedding 的组合结果。**

---

## 7. 如何评估 embedding 模型

最靠谱的方法不是猜，而是做实验。

至少应比较：
- hit@k
- recall@k
- MRR / nDCG（如果你有标注集）
- 最终答案正确率
- token / latency / storage 成本

你甚至可以发现这种情况：
- embedding A 检索分略高
- 但 embedding B 最终回答质量更好

因为 retrieval quality 并不完全等于 final answer quality。

---

## 8. open-source vs API embedding

实际工程中通常也会在两类方案中选：

### API embedding
优点：
- 上手快
- 质量常较强
- 运维简单

缺点：
- 成本持续发生
- 数据外发问题
- 可控性较弱

### open-source embedding
优点：
- 可私有部署
- 可控性高
- 长期成本可能更低

缺点：
- 需要自己部署
- 需要自己 benchmark

所以 embedding selection 也是：

> **能力、成本、隐私、可控性之间的工程权衡。**

---

## 9. 今天最该记住的 5 句话

1. **embedding 模型决定 dense retrieval 的语义空间。**
2. **选 embedding，本质上是在选 query 和文档如何对齐。**
3. **好的排行榜成绩不一定适合你的具体语料和任务。**
4. **embedding 效果和 chunking 强耦合。**
5. **embedding selection 最终必须靠实验和评估决定。**

---

## 10. 今日任务

### 必做
1. 比较至少两种 embedding 模型的优缺点
2. 写出你的 RAG 任务属于哪类语料（通用 / 领域 / 多语言）
3. 思考：如果 query 很短、文档很长，embedding 选择会有什么影响？
4. 列出你会用来评估 embedding 的 3 个指标

### 你要能回答的问题
1. embedding 模型在 RAG 中到底负责什么？
2. 为什么 embedding 选择不能只看排行榜？
3. query-document 对齐是什么意思？
4. embedding 和 chunking 有什么关系？
5. API embedding 和开源 embedding 的工程取舍是什么？

---

## 11. 一句话总结

> RAG embedding selection 的本质，是为你的 query 与文档 chunk 选择一个最合适的语义对齐空间，而这个选择不仅影响检索上限，也直接决定系统的成本、隐私与部署策略。
