# Day 26 — RAG Ingestion and Chunking

## 1. 为什么 Day 26 是 RAG 的真正起点

很多人一提到 RAG，第一反应是：
- embedding
- 向量数据库
- semantic search

但真正的 RAG 系统起点往往更早。

因为在你检索之前，你必须先回答：
- 文档从哪里来？
- 以什么形式进入系统？
- 怎么清洗？
- 怎么切成适合检索的单元？

这就是 Day 26 的重点：

> **ingestion 和 chunking 是 RAG 能否工作得好的底层前提。**

---

## 2. ingestion 在解决什么问题

ingestion 可以理解成：

> 把外部原始资料，转成系统内部可继续处理的知识对象。

原始资料可能来自：
- PDF
- HTML 网页
- Markdown / wiki
- Word / docx
- 数据库记录
- 笔记或内部文档

它们的问题是：
- 格式不统一
- 噪声很多
- 结构信息可能混乱
- metadata 经常缺失或分散

所以 ingestion 的任务是：
- 抽取正文
- 清理噪声
- 保留来源信息
- 做统一结构化表示

这一步如果做差了，后面再强的 retrieval 也会受影响。

---

## 3. 为什么 chunking 不是“随便切一下”

很多初学者会把 chunking 理解成：
- 文本太长
- 切小一点就行

但真正工程上，chunking 决定的是：

> **系统以什么粒度理解和检索知识。**

chunk 太大：
- 噪声多
- 主题稀释
- token 浪费

chunk 太小：
- 语义碎裂
- 证据不完整
- retrieval 命中后仍然难回答

所以 chunking 的本质不是长度切割，而是：

> **知识粒度设计。**

---

## 4. ingestion 和 chunking 为什么必须一起看

这两个步骤很容易被分开理解，但其实它们高度耦合。

### ingestion 决定
- 文档结构是否被保留
- heading / section 是否还在
- metadata 是否完整

### chunking 决定
- 保留下来的结构如何被切成检索单元

如果 ingestion 已经把结构弄丢了，chunking 再聪明也很难补回来。

比如：
- PDF 页眉页脚没清理
- 网页导航混进正文
- heading 边界消失

这些都会直接影响 chunk 质量。

所以 Day 26 最重要的认知之一是：

> **chunking 上限受 ingestion 质量强约束。**

---

## 5. 为什么 metadata 在这一天就要重视

很多人前几天只盯着正文文本，但 RAG 真正成熟起来后，你会发现 metadata 极其重要。

常见 metadata 包括：
- title
- source
- URL
- author
- date
- page / section
- document id

它们的价值在于：
- retrieval filter
- citation grounding
- 时间排序
- 权限控制
- debug / trace

所以 Day 26 要建立的意识是：

> **知识进入系统时，不只是正文有价值，来源和结构信息同样有价值。**

---

## 6. 常见 chunking 策略为什么都只是权衡

你后面还会详细学 chunking，但 Day 26 先建立直觉：

### fixed-size
- 简单稳定
- 但容易切断语义

### overlap
- 减少边界割裂
- 但会增加冗余

### paragraph / heading-aware
- 语义更自然
- 但依赖 ingestion 结构质量

也就是说，没有“永远最优”的 chunking。

你最终需要的是：
- 对文档类型敏感
- 对 query 类型敏感
- 对 token 成本敏感

这就是工程上的 trade-off。

---

## 7. 为什么 Day 26 是 retrieval 之前最关键的工程日之一

很多 retrieval 问题，最后追根溯源并不在 embedding，而在更前面的数据准备：
- 文本脏
- chunk 切坏
- metadata 丢失

所以 Day 26 的价值在于提醒你：

> **RAG 并不是从“检索函数”开始，而是从“知识准备”开始。**

这是非常核心的系统思维。

---

## 8. 今天最该记住的 5 句话

1. **RAG 的真正起点不是检索，而是 ingestion。**
2. **chunking 决定知识以什么粒度被检索。**
3. **ingestion 和 chunking 是强耦合关系。**
4. **metadata 从 Day 26 开始就应该被认真保留。**
5. **很多 retrieval 问题，根源其实在数据进入系统的方式。**

---

## 9. 今日任务

### 必做
1. 列出 3 类你未来可能 ingest 的文档源
2. 写出每类文档最常见的噪声问题
3. 比较 fixed-size 和 paragraph-based chunking 的区别
4. 设计一个最小的 document object（content + metadata）

### 你要能回答的问题
1. ingestion 在 RAG 中到底解决什么问题？
2. chunking 为什么不是随便切文本？
3. ingestion 和 chunking 为什么必须一起看？
4. metadata 为什么从一开始就重要？
5. 为什么 Day 26 是 retrieval 之前最关键的工程日之一？

---

## 10. 一句话总结

> RAG ingestion and chunking 的本质，是把格式混乱的外部原始资料转成结构清晰、粒度合适、附带来源信息的知识单元，从而为后续 retrieval、grounding 和 generation 提供可靠底座。
