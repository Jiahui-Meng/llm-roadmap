# Day 3 — Attention Intuition

## 1. 什么是 Attention

Attention 的核心思想是：

> 当模型处理当前 token 时，它不必只依赖固定窗口或按顺序传递的信息，而是可以主动去“看”整个序列中哪些 token 和自己最相关，并把这些相关信息汇总过来。

换句话说，attention 机制让每个 token 都能动态决定：
- 我现在应该关注谁？
- 我应该从谁那里拿信息？
- 每个人的信息该占多大权重？

这和传统按顺序一步步传递信息的方式不同。
在 attention 里，一个 token 可以直接与其他所有 token 建立联系，因此更容易捕捉长距离依赖关系。

---

## 2. 为什么需要 Attention

在自然语言中，一个词的含义往往依赖上下文。

例如这句话：

> The animal didn’t cross the street because **it** was too tired.

这里的 **it** 指代的是 **the animal**，而不是 street。
模型如果只看局部位置，可能很难准确理解这种依赖关系。

Attention 的作用就是：
- 让当前 token 能查看整个句子
- 自动判断哪些 token 更重要
- 根据重要性聚合信息，形成更好的表示

因此，attention 解决的不是简单的“看前后几个词”，而是**让模型在全局范围内有选择地获取信息**。

---

## 3. Query / Key / Value 的直觉

Attention 中最重要的三个概念是：

- **Query（Q）**
- **Key（K）**
- **Value（V）**

它们不是三种完全不同来源的数据，而是**由输入表示经过不同线性变换得到的三组向量**。

在 **self-attention** 里：
- Q、K、V 都来自同一份输入
- 只是它们各自承担的角色不同

可以这样直观理解：

### 3.1 Query：我现在想找什么
Query 表示当前 token 的“查询需求”。

它像是在问：

> 我现在需要什么信息？
> 谁和我最相关？

所以 Q 可以理解成当前 token 发出的“搜索请求”。

---

### 3.2 Key：我这里有什么特征可供匹配
Key 表示每个 token 暴露出来的“索引标签”或“特征标签”。

它像是在说：

> 我这里有这些信息，你可以拿你的 Query 来和我匹配。

所以 K 像数据库里的“检索键”。

---

### 3.3 Value：如果你关注我，我真正给你的内容是什么
Value 表示每个 token 真正携带、可被聚合的信息。

它像是在说：

> 如果你的 Query 认为我很重要，那你最终拿走的是我的 Value。

所以：
- **Q 决定你想找什么**
- **K 决定谁和你匹配**
- **V 决定你最终拿到什么内容**

---

## 4. Attention Score 是什么

Attention score 的作用是衡量：

> 当前 token 对其他 token 应该关注多少。

通常做法是用当前 token 的 Query 去和所有 token 的 Key 做匹配。
匹配得越好，分数越高，说明这两个 token 的相关性越强。

可以把它理解为：

- score 高：说明“你对我很重要”
- score 低：说明“你和我关系不大”

因此，attention score 本质上是一个**相关性分数**。

---

## 5. 为什么不是只找关系，而是要做加权汇总

这点非常重要。

Attention 并不是只为了知道“谁和谁有关”，而是为了：

> 根据这种相关性，把其他 token 的信息聚合到当前 token 上。

流程可以理解成两步：

### 第一步：决定该关注谁
通过 Q 和 K 的匹配，得到每个 token 的 attention score。

### 第二步：把有用的信息收集过来
再利用这些分数，对所有 token 的 Value 做加权求和。

结果就是：

> 当前 token 的新表示，不再只包含它自己原来的信息，
> 而是融合了整个序列中与它最相关的上下文信息。

所以 attention 的真正价值在于：

- **先判断重要性**
- **再按重要性整合信息**

这也是 Transformer 强大的原因之一。

---

## 6. Self-Attention 的本质

Self-attention 指的是：

> 序列中的每个 token 都用自己生成的 Query，去和同一序列中所有 token 的 Key 做匹配，再对这些 token 的 Value 做加权汇总。

因为 Q、K、V 都来自同一个输入序列，所以叫 **self-attention**。

它的结果是：
- 每个 token 都能“看”整个序列
- 每个 token 都能根据自己的需求，动态选择关注对象
- 最终每个 token 都会得到一个融合上下文后的新表示

---

## 7. Self-Attention 和 RNN 的差别

传统 RNN 的信息传递方式是：
- 按顺序一个 token 一个 token 处理
- 前面的信息通过隐藏状态逐步传到后面
- 距离太远时，信息容易衰减

而 self-attention 的方式是：
- 每个 token 都可以直接和所有 token 交互
- 不需要经过很长的传递路径
- 更容易捕捉远距离依赖
- 也更适合并行计算

所以两者最大的区别可以概括为：

- **RNN：顺序传递信息**
- **Self-attention：全局直接交互信息**

---

## 8. 一个简单例子：Attention 在做什么

假设句子是：

> The cat sat on the mat

当模型处理 **sat** 时，它可能会关注：
- **cat**：谁坐下了
- **on**：动作和介词结构的关系
- **mat**：坐在什么上面

也就是说，当前 token 不只是机械地处理自己，而是在问：

> 和我最相关的是哪些词？
> 我应该从它们那里拿到什么信息？

最后，**sat** 的表示会融合这些相关词的信息，从而更准确地表达其上下文含义。

---

## 9. Toy Attention 的直觉版理解

可以把 attention 想象成开会时做信息筛选：

- **Query**：我现在想知道什么
- **Key**：每个人身上的标签，告诉别人我擅长什么
- **Value**：每个人真正能提供的内容
- **Score**：我觉得谁最值得听
- **Weighted Sum**：把大家的内容按重要程度汇总成我的最终结论

所以 attention 并不是“只看谁存在”，而是：

> 主动检索、筛选、加权、整合信息的过程。

---

## 10. 为什么说 Attention 是动态的

Attention 不是固定规则，比如“永远看前一个词”或者“永远看相邻词”。

它是动态的，因为：
- 不同 token 的 Query 不同
- 同一个 token 在不同上下文中的关注对象也会不同
- 模型会根据当前输入内容决定注意力分配

因此，attention 是一种**内容驱动的选择机制**，而不是死板的位置规则。

---

## 11. 今天的核心理解

今天最重要的理解有四点：

### 1）Q / K / V 的角色不同，但来源可以相同
在 self-attention 中，它们通常都由同一份输入经过不同线性变换得到。

### 2）Attention score 表示相关性
当前 token 用自己的 Query 去和其他 token 的 Key 做匹配，分数越高，说明越值得关注。

### 3）Attention 不只是找关系，更是整合信息
模型会根据分数对 Value 做加权汇总，把相关上下文注入当前 token 的表示中。

### 4）Self-attention 让每个 token 都能看到整个序列
这使得模型更容易捕捉长距离依赖，也比 RNN 更适合并行计算。

---

## 12. 一句话总结

> Self-attention 的本质，就是让每个 token 用自己的 Query 去匹配所有 token 的 Key，再把对应的 Value 按相关性加权汇总，从而得到融合上下文信息的新表示。

---

## 13. 可补充的手推例子说明

如果你想把内容再写得更扎实，可以加一个 3-token 的 toy example：

假设句子里有 3 个 token：
- token A
- token B
- token C

当处理 token A 时：
1. 用 A 的 Query 分别去和 A、B、C 的 Key 计算相关性
2. 得到三个分数
3. 分数归一化后得到权重
4. 用这些权重对 A、B、C 的 Value 加权求和
5. 得到 A 的新表示

这说明：
- A 虽然是当前 token
- 但它的新表示不只来自 A 自己
- 而是来自整个序列中与 A 相关的信息组合

---

## 14. Attention Flow Diagram 可以怎么画

你可以画成下面这种逻辑：

1. 输入 token embeddings
2. 线性变换得到 Q / K / V
3. 当前 token 的 Q 与所有 token 的 K 计算 score
4. score 经过 softmax 变成权重
5. 权重与 V 相乘并加权求和
6. 得到当前 token 的 contextualized representation

你也可以用一句话标注图的含义：

> 每个 token 都会从整个序列中选择性地收集与自己最相关的信息。
