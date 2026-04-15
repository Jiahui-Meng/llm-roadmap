# Day 34 — RAG Chunking Strategies

## 1. 为什么 chunking 是 RAG 里最容易被低估的一步

很多人第一次做 RAG，会以为 chunking 只是：
- 把文档切小一点
- 好塞进向量库
- 好塞进 prompt

但真正做过系统后就会发现：

> **chunking 不是简单切文本，而是在决定知识以什么粒度被检索和消费。**

chunk 过大：
- 噪声高
- token 浪费
- 检索精度下降

chunk 过小：
- 语义断裂
- 证据不完整
- 需要更多 chunk 才能回答问题

所以 Day 34 的重点是：

> **chunking 是 retrieval quality 的核心设计参数。**

---

## 2. chunk 到底在解决什么问题

RAG 不能总是直接把整篇文档拿来做 embedding 和 retrieval，因为：
- 文档太长
- 一个 query 通常只需要其中一小部分
- 长文本向量会稀释主题焦点
- prompt 上下文预算有限

所以 chunking 的任务是：

> 把文档拆成既保留语义、又适合检索的小单位。

这是一个非常微妙的平衡问题。

---

## 3. 最常见的 chunking 方法

### 1）Fixed-size chunking
按固定字符数 / token 数切，比如：
- 300 tokens 一块
- 500 tokens 一块

优点：
- 实现简单
- 稳定
- 易批处理

缺点：
- 可能把一句完整语义切断
- 不理解文档结构

---

### 2）Overlap chunking
在 fixed-size 基础上增加重叠，比如：
- chunk size = 500
- overlap = 100

优点：
- 减少边界切断问题
- 相邻语义更容易保留

缺点：
- 索引冗余增加
- 检索结果更容易重复

---

### 3）Paragraph-based chunking
按自然段切。

优点：
- 语义边界自然
- 阅读性更强

缺点：
- 段落长度不均匀
- 有时太短，有时太长

---

### 4）Heading-aware chunking
结合标题 / 小节结构切。

优点：
- 更符合人类文档组织方式
- chunk 与主题边界更一致

缺点：
- 依赖 ingestion 质量
- 对结构化文档更有效，对脏文本不一定适用

---

## 4. 为什么 chunk size 没有统一答案

很多人喜欢问：

> chunk 多大最合适？

没有统一答案，因为它取决于：
- 文档类型
- 查询类型
- embedding 模型
- 上下文窗口
- reranking 是否存在
- 你最终要回答的问题粒度

举例：

### FAQ / 短问答
更适合小 chunk

### 技术文档 / 长报告
可能需要中等 chunk + overlap

### 医疗 / 法律 / 合规文档
经常需要结构化 chunk + metadata + citations

所以 chunk size 不是固定超参数，而是：

> **任务与文档共同决定的设计选择。**

---

## 5. chunking 和 retrieval 之间的强耦合

chunking 决定了：
- 检索单元是什么
- embedding 的输入是什么
- prompt assembly 时上下文会长什么样

这意味着：

### chunk 切得太粗
retrieval 可能召回“相关但太杂”的内容

### chunk 切得太细
retrieval 可能只能召回碎片，无法支撑完整回答

所以 Day 34 最关键的一点是：

> **retrieval 错，很多时候不是 embedding 错，而是 chunking 错。**

---

## 6. overlap 什么时候重要

overlap 的意义在于保护边界。

因为语义往往不会刚好停在固定切分点上。

例如：
- 一个定义在段尾开始
- 解释在下一段继续
- fixed split 会把它们切开

overlap 可以缓解这个问题。

但 overlap 不是越大越好，因为：
- 索引体积会变大
- 重复内容更多
- prompt 里更容易塞入高度相似 chunk

所以 overlap 的本质也是 trade-off。

---

## 7. chunking 和 citation grounding 的关系

如果你后面要做 citation，chunking 更关键。

因为 citation 要求：
- 证据边界清楚
- 来源可定位
- 单个 chunk 尽量表达完整证据

如果 chunk 切得非常随意：
- 引用会不清楚
- 一个答案可能跨很多碎片
- 用户难验证

所以 chunking 不只是 retrieval 问题，也是：

> **grounding 和可解释性问题。**

---

## 8. 最好的 chunking 是实验出来的，不是想出来的

工程上一个很重要的认知是：

> **chunking 必须做实验。**

你应该比较：
- 300 vs 500 vs 800 tokens
- overlap 0 / 50 / 100
- paragraph-based vs heading-aware
- 不同文档类型下的命中率

然后看：
- retrieval hit rate
- answer correctness
- citation quality
- prompt token cost

这就是为什么 chunking 最终会进入 eval / ablation。

---

## 9. 今天最该记住的 5 句话

1. **chunking 决定知识以什么粒度被检索。**
2. **chunk 太大和太小都会伤害 RAG 效果。**
3. **fixed-size、overlap、paragraph、heading-aware 各有适用场景。**
4. **chunking 和 retrieval、citation、prompt cost 强耦合。**
5. **最优 chunking 需要靠实验和评估决定。**

---

## 10. 今日任务

### 必做
1. 比较至少 3 种 chunking 策略
2. 选一篇文档，手动切出 3 组不同粒度的 chunk
3. 思考哪种 chunk 更适合：FAQ / 技术文档 / 长报告
4. 写出 chunking 对 retrieval 和 citation 的影响

### 你要能回答的问题
1. 为什么 chunking 不是简单切文本？
2. fixed-size 和 paragraph-based 的区别是什么？
3. overlap 为什么有用？
4. chunk 太大 / 太小会分别带来什么问题？
5. 为什么 chunking 最终要靠实验确定？

---

## 11. 一句话总结

> RAG chunking 的本质，是为检索和生成找到一个合适的知识粒度平衡点：既不能大到噪声过重，也不能小到语义碎裂，而这件事最终必须通过系统评估来验证。
