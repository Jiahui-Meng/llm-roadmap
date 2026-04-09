# Day 24 — MoE Systems Implications

## 1. 为什么 MoE 是系统问题

如果只从论文公式看，MoE 好像很诱人：
- 参数更多
- 每 token 激活更少
- 好像能更高效扩展

但一到真实系统里，问题马上变复杂：
- token 要被路由到不同 experts
- experts 可能分布在不同设备上
- 通信成本会增加
- batch 会变得不规则

所以 MoE 不只是模型设计问题，更是：

> **系统设计问题。**

---

## 2. token dispatch / gather 的代价

在 dense 模型中：
- 所有 token 走同一条路径
- 数据流比较规整

在 MoE 中：
- token 先被分组
- 按 expert 分发
- 处理后再收集回来

这会引入：
- dispatch 开销
- gather 开销
- 数据重排开销

也就是说，MoE 的额外成本很多时候不是算子本身，而是：

> **token 路由带来的数据搬运。**

---

## 3. 通信成本为什么会成为瓶颈

如果 experts 分布在不同 GPU / 节点上，就会出现：
- token 要跨设备发送
- expert 输出还要跨设备收回

这样一来：
- 计算并不是唯一成本
- 通信可能成为真正瓶颈

所以 MoE 的难点之一是：

> 如何让“更多参数”的优势不被“更多通信”抵消。

---

## 4. batching 会变得更复杂

dense 模型下，一个 batch 通常较整齐。

MoE 下则会出现：
- 不同 token 被送到不同 experts
- 每个 expert 收到的 token 数不一样
- 计算负载不均匀

于是 GPU 利用率、kernel 效率、并行调度都会变得更难做。

所以 MoE 常常不是“理论 FLOPs 低就真的更快”。

---

## 5. latency 和 throughput 的权衡

MoE 可能在某些场景下：
- 提高模型容量
- 改善质量

但系统上你还必须问：
- latency 会不会更高？
- throughput 会不会受通信限制？
- 高并发下路由会不会更糟？

也就是说，MoE 是否值得，不是只看 loss 或 benchmark，而要看：

> **端到端系统表现。**

---

## 6. 为什么 observability 很重要

MoE 系统里，很多问题如果不观察就看不出来：
- 哪些 experts 长期过热
- 哪些 experts 常年空闲
- routing 是否失衡
- 某些 GPU 是否成为热点

所以 MoE 系统更需要细粒度 observability：
- token per expert
- expert utilization
- dispatch latency
- overflow / dropped tokens

---

## 7. MoE 的服务难点

在 serving 场景里，MoE 会面临：
- 动态 batch
- 不同请求长度
- 不同 token 分布
- KV cache 与 routing 叠加

这使得部署复杂度往往高于 dense decoder-only 模型。

所以即使 MoE 理论上有优势，也不代表它一定是最省心的产品方案。

---

## 8. Day 24 的核心理解

你今天最重要的理解不是公式，而是：

> MoE 把问题从“模型是不是更大”转成了“系统能不能承受动态稀疏路由”。

这一步非常关键，因为它会让你对后面所有“模型很强”的宣传保持更工程化的判断。

---

## 9. 今天最该记住的 5 句话

1. **MoE 的挑战很多来自系统，而不只是算法。**
2. **token dispatch / gather 会引入显著额外开销。**
3. **跨设备通信可能成为 MoE 的主要瓶颈。**
4. **MoE 的理论效率不一定直接转化成实际吞吐优势。**
5. **没有细粒度 observability，很难把 MoE 系统调好。**

---

## 10. 今日任务

1. 阅读 HF MoE blog 里 systems trade-offs 部分
2. 看 vLLM docs 里的 serving 视角说明
3. 写出：为什么 MoE 是系统问题，不只是模型问题
4. 列出你认为 MoE serving 最难的 3 个点

---

## 11. 一句话总结

> MoE 通过稀疏激活换来更大模型容量，但它把原本规整的 dense 计算变成了带有路由、通信、负载均衡和观测难题的系统工程问题，因此是否划算必须从端到端服务表现来判断。
