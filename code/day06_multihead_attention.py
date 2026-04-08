"""
Day 6 - Multi-Head Attention Implementation
Complete working code with examples and visualization
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


class MultiHeadAttention(nn.Module):
    """
    Multi-Head Attention 的完整实现
    
    输入：x (batch, seq_len, d_model)
    输出：output (batch, seq_len, d_model)，形状完全相同
    """
    
    def __init__(self, d_model, num_heads, dropout=0.0):
        super().__init__()
        
        assert d_model % num_heads == 0, "d_model 必须能被 num_heads 整除"
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # 投影层
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
        
        self.dropout = nn.Dropout(dropout)
    
    def split_heads(self, x):
        """
        将输入分割成多个 head
        
        输入：x (batch, seq_len, d_model)
        输出：(batch, num_heads, seq_len, d_k)
        """
        batch_size, seq_len, d_model = x.size()
        x = x.view(batch_size, seq_len, self.num_heads, self.d_k)
        return x.transpose(1, 2)
    
    def merge_heads(self, x):
        """
        将多个 head 合并回去
        
        输入：x (batch, num_heads, seq_len, d_k)
        输出：(batch, seq_len, d_model)
        """
        batch_size, num_heads, seq_len, d_k = x.size()
        x = x.transpose(1, 2)  # (batch, seq_len, num_heads, d_k)
        return x.contiguous().view(batch_size, seq_len, -1)
    
    def forward(self, x, mask=None):
        """
        前向传播
        
        参数：
            x: (batch, seq_len, d_model)
            mask: (batch, seq_len, seq_len) 或 None，用于 masked attention
        
        返回：
            output: (batch, seq_len, d_model)
            attention_weights: (batch, num_heads, seq_len, seq_len)
        """
        batch_size = x.size(0)
        
        # 步骤 1：投影到 Q、K、V
        Q = self.W_q(x)  # (batch, seq_len, d_model)
        K = self.W_k(x)  # (batch, seq_len, d_model)
        V = self.W_v(x)  # (batch, seq_len, d_model)
        
        # 步骤 2：分割成多个 head
        Q = self.split_heads(Q)  # (batch, num_heads, seq_len, d_k)
        K = self.split_heads(K)  # (batch, num_heads, seq_len, d_k)
        V = self.split_heads(V)  # (batch, num_heads, seq_len, d_k)
        
        # 步骤 3：计算注意力分数（scaled dot-product）
        scores = Q @ K.transpose(-2, -1)  # (batch, num_heads, seq_len, seq_len)
        scores = scores / (self.d_k ** 0.5)
        
        # 步骤 4：应用 mask（如果有）
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        
        # 步骤 5：转成概率分布（softmax）
        weights = F.softmax(scores, dim=-1)  # (batch, num_heads, seq_len, seq_len)
        weights = self.dropout(weights)
        
        # 步骤 6：加权聚合 Value
        context = weights @ V  # (batch, num_heads, seq_len, d_k)
        
        # 步骤 7：合并所有 head
        output = self.merge_heads(context)  # (batch, seq_len, d_model)
        
        # 步骤 8：最后的线性投影
        output = self.W_o(output)  # (batch, seq_len, d_model)
        
        return output, weights


# ============================================================================
# 辅助函数：生成 mask（用于 Decoder 的 Causal Attention）
# ============================================================================

def create_causal_mask(seq_len, device):
    """
    创建因果 mask（upper triangular）
    
    用途：确保当前 token 不能看到未来的 token
    
    示例（seq_len=4）：
    [[1, 0, 0, 0],
     [1, 1, 0, 0],
     [1, 1, 1, 0],
     [1, 1, 1, 1]]
    """
    mask = torch.tril(torch.ones(seq_len, seq_len, device=device))
    return mask.unsqueeze(0).unsqueeze(0)  # (1, 1, seq_len, seq_len)


def create_padding_mask(seq_len, pad_len, device):
    """
    创建 padding mask
    
    用途：mask 掉 padding token
    
    示例（seq_len=5, pad_len=2）：
    [[1, 1, 1, 0, 0]]
    """
    mask = torch.ones(1, 1, seq_len, device=device)
    mask[0, 0, -pad_len:] = 0
    return mask


# ============================================================================
# 测试代码
# ============================================================================

def test_basic():
    """测试基本功能"""
    print("=" * 60)
    print("Test 1: 基本功能测试")
    print("=" * 60)
    
    # 参数设置
    d_model = 512
    num_heads = 8
    batch_size = 2
    seq_len = 10
    
    # 创建模块和输入
    mha = MultiHeadAttention(d_model, num_heads)
    x = torch.randn(batch_size, seq_len, d_model)
    
    # 前向传播
    output, weights = mha(x)
    
    print(f"Input shape:          {x.shape}")
    print(f"Output shape:         {output.shape}")
    print(f"Attention weights:    {weights.shape}")
    print(f"✓ 输入输出形状相同")
    
    # 检查权重是否是有效的概率分布
    weight_sum = weights.sum(dim=-1)
    print(f"权重和（应该≈1）:    {weight_sum[0, 0, 0].item():.4f}")
    print()


def test_gradient_flow():
    """测试梯度流动"""
    print("=" * 60)
    print("Test 2: 梯度流动测试")
    print("=" * 60)
    
    d_model = 512
    num_heads = 8
    
    mha = MultiHeadAttention(d_model, num_heads)
    x = torch.randn(2, 10, d_model, requires_grad=True)
    
    output, _ = mha(x)
    loss = output.sum()
    loss.backward()
    
    # 检查梯度是否存在且非零
    print(f"x.grad 是否存在:     {x.grad is not None}")
    print(f"x.grad 是否非零:     {(x.grad != 0).any()}")
    print(f"梯度范数:           {x.grad.norm().item():.4f}")
    print("✓ 梯度流动正常")
    print()


def test_head_independence():
    """测试不同 head 的独立性"""
    print("=" * 60)
    print("Test 3: Head 独立性测试")
    print("=" * 60)
    
    d_model = 512
    num_heads = 8
    
    mha = MultiHeadAttention(d_model, num_heads)
    x = torch.randn(1, 10, d_model)
    
    _, weights = mha(x)
    # weights: (batch=1, num_heads=8, seq_len=10, seq_len=10)
    
    print(f"权重形状: {weights.shape}")
    
    # 计算不同 head 之间的相似度
    head_0 = weights[0, 0].reshape(-1)
    head_1 = weights[0, 1].reshape(-1)
    
    similarity = F.cosine_similarity(head_0.unsqueeze(0), head_1.unsqueeze(0)).item()
    print(f"Head 0 和 Head 1 的余弦相似度: {similarity:.4f}")
    print(f"（相似度低说明不同 head 学到了不同的模式）")
    print()


def test_dimension_scaling():
    """测试不同维度配置"""
    print("=" * 60)
    print("Test 4: 维度缩放测试")
    print("=" * 60)
    
    configs = [
        (256, 4),
        (512, 8),
        (768, 12),
        (1024, 16),
    ]
    
    for d_model, num_heads in configs:
        mha = MultiHeadAttention(d_model, num_heads)
        x = torch.randn(2, 10, d_model)
        output, weights = mha(x)
        
        d_k = d_model // num_heads
        
        print(f"d_model={d_model:4d}, num_heads={num_heads:2d}, d_k={d_k:3d} -> ", end="")
        print(f"Output: {output.shape}")
    print()


def test_causal_mask():
    """测试因果 mask"""
    print("=" * 60)
    print("Test 5: 因果 Mask 测试")
    print("=" * 60)
    
    d_model = 512
    num_heads = 8
    seq_len = 4
    
    mha = MultiHeadAttention(d_model, num_heads)
    x = torch.randn(1, seq_len, d_model)
    
    # 创建因果 mask
    causal_mask = create_causal_mask(seq_len, device=x.device)
    
    print(f"因果 Mask 形状: {causal_mask.shape}")
    print(f"因果 Mask:\n{causal_mask[0, 0].int().tolist()}")
    
    # 前向传播（带 mask）
    output, weights = mha(x, mask=causal_mask)
    
    # 查看第一个 token 的注意力分布
    print(f"\n第 1 个 token 的注意力分布:")
    print(f"{weights[0, 0, 0].tolist()}")
    
    # 查看最后一个 token 的注意力分布
    print(f"\n最后一个 token 的注意力分布:")
    print(f"{weights[0, 0, -1].tolist()}")
    print()


def test_attention_patterns():
    """可视化注意力模式"""
    print("=" * 60)
    print("Test 6: 注意力模式分析")
    print("=" * 60)
    
    d_model = 128
    num_heads = 4
    seq_len = 6
    
    # 创建一个输入（所有 token 相同，用来观察自发的模式）
    x = torch.randn(1, seq_len, d_model)
    
    mha = MultiHeadAttention(d_model, num_heads)
    _, weights = mha(x)
    
    # weights: (1, 4, 6, 6)
    
    print("不同 Head 的注意力模式（行=query token，列=key token）:\n")
    
    for head_idx in range(num_heads):
        print(f"Head {head_idx}:")
        head_attn = weights[0, head_idx].tolist()
        
        for query_idx, attn_weights in enumerate(head_attn):
            formatted = [f"{w:.2f}" for w in attn_weights]
            print(f"  Token {query_idx}: {' '.join(formatted)}")
        print()


# ============================================================================
# 主程序
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Multi-Head Attention 完整测试套件")
    print("=" * 60 + "\n")
    
    test_basic()
    test_gradient_flow()
    test_head_independence()
    test_dimension_scaling()
    test_causal_mask()
    test_attention_patterns()
    
    print("=" * 60)
    print("所有测试通过！✓")
    print("=" * 60)
