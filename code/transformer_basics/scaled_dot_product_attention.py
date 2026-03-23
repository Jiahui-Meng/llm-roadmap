import math
import torch


def scaled_dot_product_attention(q, k, v, mask=None):
    scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(q.size(-1))

    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))

    weights = torch.softmax(scores, dim=-1)
    output = torch.matmul(weights, v)
    return output, weights


def main():
    q = torch.tensor([[[1.0, 0.0], [0.0, 1.0]]])
    k = torch.tensor([[[1.0, 0.0], [0.0, 1.0]]])
    v = torch.tensor([[[1.0, 2.0], [3.0, 4.0]]])

    output, weights = scaled_dot_product_attention(q, k, v)
    print('weights:', weights)
    print('output:', output)


if __name__ == '__main__':
    main()
