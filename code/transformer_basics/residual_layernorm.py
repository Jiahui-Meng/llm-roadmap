import torch
import torch.nn as nn


class AddNorm(nn.Module):
    def __init__(self, d_model=16):
        super().__init__()
        self.norm = nn.LayerNorm(d_model)

    def forward(self, x, sublayer_out):
        return self.norm(x + sublayer_out)


if __name__ == '__main__':
    x = torch.randn(2, 5, 16)
    y = torch.randn(2, 5, 16)
    add_norm = AddNorm()
    out = add_norm(x, y)
    print(out.shape)
