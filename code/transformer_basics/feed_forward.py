import torch
import torch.nn as nn


class FeedForward(nn.Module):
    def __init__(self, d_model=16, d_ff=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Linear(d_ff, d_model),
        )

    def forward(self, x):
        return self.net(x)


if __name__ == '__main__':
    x = torch.randn(2, 5, 16)
    ffn = FeedForward()
    out = ffn(x)
    print(out.shape)
