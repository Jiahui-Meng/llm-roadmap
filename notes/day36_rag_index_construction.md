# Day 36 — RAG Index Construction

## 1. 为什么 index construction 不是“把向量存进去”这么简单

当你完成了：
- ingestion
- chunking
- embedding

下一步就是 index construction。

很多人直觉上会把这一步理解成：
- 算出向量
- 存起来
- 检索时拿出来比相似度

但真正工程上，index construction 远不只是存储，它决定了：
- 检索速度
- 扩展性
- 存储成本
- 增量更新难度
- metadata filter 能力

所以 Day 36 的核心是：

> **索引不是被动存储层，而是 retrieval 系统的一部分。**

---

## 2. index 到底在解决什么问题

如果文档库很小，也许你可以暴力比对所有向量。

但一旦规模上来：
- 几万 chunks
- 几十万 chunks
- 几百万 chunks

全量暴力搜索就会变得越来越贵。

index 的任务就是：

> **让系统在大规模向量空间中更快地找到近似最相关的候选。**

也就是说，index 负责的是：
- speed
n- scalability
- retrieval practicality

---

## 3. 常见 index 方案

### 1）FAISS
最常见的向量检索库之一。
优点：
- 成熟
- 快
- 本地实验方便

适合：
- 原型系统
- 本地 benchmark
- 中小规模 RAG

### 2）pgvector
把向量能力放进 PostgreSQL。
优点：
- 和现有数据库结合方便
- metadata filter 很自然
- 工程整合简单

适合：
- 已经强依赖 Postgres 的产品系统

### 3）专门向量数据库
如 Milvus / Weaviate / Pinecone 等。
优点：
- 专门做向量检索
- 可扩展性更强
- 常带过滤、集群、管理能力

适合：
- 较大规模或更正式的产品化系统

---

## 4. 为什么 metadata filter 会影响 index 选择

真实 RAG 检索经常不只是“语义最近”。

还会带条件，例如：
- 只看最近 30 天文档
- 只看某个知识库
- 只看某种类别
- 只看某个用户权限范围内的数据

这意味着索引系统不仅要支持向量近邻搜索，还要支持：
- metadata filter
- hybrid retrieval
- 权限约束

因此 index construction 不是孤立选择，而是：

> **和你的产品约束一起决定的架构选择。**

---

## 5. index construction 和 ingestion / chunking / embedding 的关系

这一天其实是在把前几天的内容接起来：

- ingestion 决定知识怎么进来
- chunking 决定检索单位
- embedding 决定语义空间
- index 决定如何高效搜索这个空间

所以 index construction 不是独立模块，而是 retrieval pipeline 的第四层。

如果前面做得差：
- chunk 乱
- metadata 缺
- embedding 不适配

index 再高级，也救不回来太多。

---

## 6. build index 时常被忽略的问题

### 1）增量更新
新文档不断进来时，怎么加到索引里？

### 2）删除与重建
原文更新后，旧 chunk 怎么删？新 chunk 怎么替换？

### 3）版本一致性
索引里到底是哪一版文档？和源文档版本是否一致？

### 4）metadata 同步
chunk 内容、metadata、向量三者要不要一起更新？

所以 index construction 不是“一次构建完就结束”，而是一个长期维护问题。

---

## 7. ANN（近似最近邻）为什么是现实工程核心

大多数大规模向量检索系统并不是做精确全量搜索，而是做：

> Approximate Nearest Neighbor（ANN）

因为在工程里更重要的是：
- 够快
- 够好
- 可扩展

而不是每次都数学上最精确。

所以 index construction 的本质 trade-off 是：
- recall
- latency
- memory
- scale

---

## 8. Day 36 的工程意识转变

Day 36 很重要，因为它会让你意识到：

> RAG 的 retrieval 不是单个函数调用，而是一个存储 + 搜索 + 更新 + 过滤的系统设计问题。

这会让你开始以更系统的方式思考 RAG，而不是只把它当作 embedding 检索 demo。

---

## 9. 今天最该记住的 5 句话

1. **index 不是简单存储层，而是 retrieval 系统的一部分。**
2. **index construction 决定检索速度、扩展性和工程可维护性。**
3. **FAISS、pgvector、向量数据库各有适用场景。**
4. **metadata filter 和权限约束会反过来影响 index 选择。**
5. **index construction 是一个长期更新与维护问题，不是一次性动作。**

---

## 10. 今日任务

### 必做
1. 比较 FAISS、pgvector、向量数据库的优劣
2. 写出你未来系统最可能需要哪些 metadata filter
3. 设计一个 index object 至少包含哪些字段
4. 思考：如果文档更新了，索引应该如何同步更新？

### 你要能回答的问题
1. index construction 解决的核心问题是什么？
2. 为什么索引选择会受产品需求影响？
3. ANN 为什么在工程里这么重要？
4. metadata filter 为什么会反向影响索引架构？
5. 为什么 index construction 不是一次性工作？

---

## 11. 一句话总结

> RAG index construction 的本质，是把 embedding 后的知识对象组织成一个既能高效搜索、又能支持过滤、更新和扩展的检索系统层，而这一步决定了你的 retrieval 是否真正具备工程可用性。
