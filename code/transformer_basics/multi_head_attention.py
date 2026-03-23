import torch
import torch.nn as nn
from scaled_dot_product_attention import scaled_dot_product_attention


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=16, num_heads=4):
        super().__init__()
        assert d_model % num_heads == 0
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_head = d_model // num_heads

        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)

    def split_heads(self, x):
        batch, seq_len, _ = x.shape
        x = x.view(batch, seq_len, self.num_heads, self.d_head)
        return x.transpose(1, 2)

    def combine_heads(self, x):
        batch, heads, seq_len, d_head = x.shape
        x = x.transpose(1, 2).contiguous()
        return x.view(batch, seq_len, heads * d_head)

    def forward(self, x, mask=None):
        q = self.split_heads(self.w_q(x))
        k = self.split_heads(self.w_k(x))
        v = self.split_heads(self.w_v(x))

        out, weights = scaled_dot_product_attention(q, k, v, mask)
        out = self.combine_heads(out)
        out = self.w_o(out)
        return out, weights


if __name__ == '__main__':
    x = torch.randn(2, 5, 16)
    mha = MultiHeadAttention()
    out, weights = mha(x)
    print('out shape:', out.shape)
    print('weights shape:', weights.shape)
