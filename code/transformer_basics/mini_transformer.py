import torch
import torch.nn as nn
from transformer_block import TransformerBlock
from positional_encoding import positional_encoding


class MiniTransformer(nn.Module):
    def __init__(self, vocab_size=100, d_model=32, num_heads=4, d_ff=64, num_layers=2, max_len=64):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.layers = nn.ModuleList([
            TransformerBlock(d_model=d_model, num_heads=num_heads, d_ff=d_ff)
            for _ in range(num_layers)
        ])
        self.output = nn.Linear(d_model, vocab_size)
        self.register_buffer('pe', positional_encoding(max_len, d_model))

    def forward(self, token_ids, mask=None):
        x = self.embedding(token_ids)
        x = x + self.pe[: x.size(1)].unsqueeze(0)
        for layer in self.layers:
            x, _ = layer(x, mask)
        return self.output(x)


if __name__ == '__main__':
    model = MiniTransformer()
    token_ids = torch.randint(0, 100, (2, 10))
    logits = model(token_ids)
    print('logits shape:', logits.shape)
