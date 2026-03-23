import torch
import torch.nn as nn


def main():
    vocab_size = 10
    dim = 8
    token_ids = torch.tensor([[1, 2, 3], [4, 5, 6]])

    embedding = nn.Embedding(vocab_size, dim)
    out = embedding(token_ids)

    print('token_ids shape:', token_ids.shape)
    print('embedding output shape:', out.shape)
    print(out)


if __name__ == '__main__':
    main()
