import torch
import torch.nn as nn
from multi_head_attention import MultiHeadAttention
from feed_forward import FeedForward
from residual_layernorm import AddNorm


class TransformerBlock(nn.Module):
    def __init__(self, d_model=16, num_heads=4, d_ff=64):
        super().__init__()
        self.mha = MultiHeadAttention(d_model, num_heads)
        self.ffn = FeedForward(d_model, d_ff)
        self.add_norm1 = AddNorm(d_model)
        self.add_norm2 = AddNorm(d_model)

    def forward(self, x, mask=None):
        attn_out, weights = self.mha(x, mask)
        x = self.add_norm1(x, attn_out)
        ffn_out = self.ffn(x)
        x = self.add_norm2(x, ffn_out)
        return x, weights


if __name__ == '__main__':
    x = torch.randn(2, 5, 16)
    block = TransformerBlock()
    out, weights = block(x)
    print('out shape:', out.shape)
    print('weights shape:', weights.shape)
