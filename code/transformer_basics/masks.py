import torch


def causal_mask(seq_len):
    return torch.tril(torch.ones(seq_len, seq_len)).unsqueeze(0).unsqueeze(0)


if __name__ == '__main__':
    print(causal_mask(5))
