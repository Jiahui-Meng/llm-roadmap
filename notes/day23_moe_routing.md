# Day 23 — MoE Routing and Load Balancing

## 1. 为什么 routing 是 MoE 的核心

Day 22 你已经知道：
- MoE 有很多 experts
- 每个 token 不会经过所有 experts
- 而是只走其中一部分

那最关键的问题就是：

> **谁决定 token 应该去哪个 expert？**

这个问题的答案就是：router。

所以 MoE 真正难的地方，不只是“有很多专家”，而是：

> **如何把 token 合理、高效、稳定地分配给专家。**

---

## 2. router 在做什么

router 可以理解成一个打分器。

给定某个 token 表示，router 会输出：
- 这个 token 对每个 expert 的匹配分数

然后系统根据分数决定：
- top-1 expert
- 或 top-2 experts
- 或其他 routing 策略

也就是说，router 的本质是：

> 根据 token 内容，决定它走哪条专家路径。

---

## 3. top-k routing

MoE 里最常见的路由方法之一是 **top-k routing**。

### top-1
- 每个 token 只分给 1 个 expert
- 计算最省
- 但稳定性和表达能力可能受限

### top-2
- 每个 token 送到 2 个 experts
- 表达能力更强
- 稳定性往往更好
- 但计算成本更高

所以 top-k routing 本质是一个 trade-off：
- k 越小，越省
- k 越大，越灵活

---

## 4. 为什么 load balancing 很重要

理想情况是：
- 所有 experts 都差不多有活干

但现实中 router 很可能会偏心：
- 有几个 expert 很受欢迎
- 大量 token 都涌向它们
- 其他 experts 几乎闲置

这会导致：
1. 专家利用不均衡
2. 计算热点严重
3. 模型容量被浪费
4. 训练不稳定

所以 MoE 不只是“路由对不对”，还要“分布均不均”。

---

## 5. capacity constraint 是什么

为了防止某个 expert 被塞爆，很多 MoE 系统会给每个 expert 设置容量上限（capacity）。

意思是：
- 某个 batch 中
- 一个 expert 最多接收多少 token

如果超了怎么办？
- token 可能被丢弃
- 或被路由到备选 expert
- 或延后处理（取决于实现）

这说明 routing 不只是数学问题，还是调度问题。

---

## 6. expert utilization 为什么重要

MoE 理论上有很多参数，但如果只有少数 experts 经常被用到，那就会出现：
- 总参数很多
- 真正有效工作的参数却不多

这就是 expert utilization 问题。

如果 utilization 差：
- 模型容量优势会被打折
- 有些 expert 学不到东西
- 整个系统效率变差

---

## 7. 为什么 routing 会影响训练稳定性

如果 token 分配波动太大：
- 某些 experts 梯度极强
- 某些 experts 梯度极弱
- 训练会变得不均匀

所以实际系统里经常要加入：
- auxiliary loss
- load-balancing loss
- routing regularization

目的就是鼓励 token 分布更平衡。

---

## 8. routing 的系统视角

从工程角度看，routing 会带来额外开销：
- token dispatch
- token gather
- expert 间通信
- 不同设备之间的数据搬运

所以 MoE 不是只看 FLOPs，还要看：
- 通信代价
- 调度复杂度
- GPU 利用率
- batch 结构是否友好

这也是为什么 MoE 系统实现难度明显高于 dense 模型。

---

## 9. 今天最该记住的 5 句话

1. **MoE 的关键不只是专家多，而是路由是否合理。**
2. **router 根据 token 内容决定它走哪些 experts。**
3. **top-k routing 是表达能力与成本的折中。**
4. **load balancing 决定 experts 是否被均匀利用。**
5. **routing 一旦做不好，MoE 的容量优势会被系统问题吞掉。**

---

## 10. 今日任务

1. 阅读 Expert Choice Routing 论文摘要 / intro
2. 阅读 Sebastian Raschka 的相关说明
3. 写出：top-1 和 top-2 routing 的区别
4. 写出：为什么 load balancing 对 MoE 很关键

---

## 11. 一句话总结

> MoE routing 的本质，是根据 token 内容把计算动态分配给少量专家；而 load balancing、capacity 和 utilization 则决定了这种条件计算在训练和系统层面能否真正高效工作。
