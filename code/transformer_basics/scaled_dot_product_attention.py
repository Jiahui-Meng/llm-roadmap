import math
import torch


def scaled_dot_product_attention(q, k, v, mask=None):
    """
    Compute scaled dot-product attention.

    Args:
        q: Query tensor of shape (..., seq_len_q, d_k)
        k: Key tensor of shape (..., seq_len_k, d_k)
        v: Value tensor of shape (..., seq_len_k, d_v)
        mask: Optional mask broadcastable to (..., seq_len_q, seq_len_k)

    Returns:
        output: attention output tensor
        weights: attention weights after softmax
        raw_scores: unscaled QK^T scores
        scaled_scores: scaled scores before softmax
    """
    d_k = q.size(-1)

    raw_scores = torch.matmul(q, k.transpose(-2, -1))
    scaled_scores = raw_scores / math.sqrt(d_k)

    if mask is not None:
        scaled_scores = scaled_scores.masked_fill(mask == 0, float("-inf"))

    weights = torch.softmax(scaled_scores, dim=-1)
    output = torch.matmul(weights, v)

    return output, weights, raw_scores, scaled_scores


def run_toy_example():
    """A minimal toy example for understanding the full attention flow."""
    q = torch.tensor([[[1.0, 0.0]]])
    k = torch.tensor([[[1.0, 0.0],
                       [0.0, 1.0],
                       [1.0, 1.0]]])
    v = torch.tensor([[[1.0, 0.0],
                       [0.0, 2.0],
                       [3.0, 3.0]]])

    output, weights, raw_scores, scaled_scores = scaled_dot_product_attention(q, k, v)

    print("=== Toy Example ===")
    print("Q shape:", tuple(q.shape))
    print("K shape:", tuple(k.shape))
    print("V shape:", tuple(v.shape))
    print()
    print("Q:")
    print(q)
    print("K:")
    print(k)
    print("V:")
    print(v)
    print()
    print("Raw scores (QK^T):")
    print(raw_scores)
    print("Scaled scores (QK^T / sqrt(d_k)):")
    print(scaled_scores)
    print("Attention weights after softmax:")
    print(weights)
    print("Final output (weights @ V):")
    print(output)
    print()


def run_multi_query_example():
    """A slightly richer example with two query positions."""
    q = torch.tensor([[[1.0, 0.0],
                       [0.0, 1.0]]])
    k = torch.tensor([[[1.0, 0.0],
                       [0.0, 1.0],
                       [1.0, 1.0]]])
    v = torch.tensor([[[1.0, 2.0],
                       [3.0, 4.0],
                       [5.0, 6.0]]])

    output, weights, raw_scores, scaled_scores = scaled_dot_product_attention(q, k, v)

    print("=== Multi-Query Example ===")
    print("Q shape:", tuple(q.shape))
    print("K shape:", tuple(k.shape))
    print("V shape:", tuple(v.shape))
    print()
    print("Raw scores (QK^T):")
    print(raw_scores)
    print("Scaled scores (QK^T / sqrt(d_k)):")
    print(scaled_scores)
    print("Attention weights after softmax:")
    print(weights)
    print("Final output (weights @ V):")
    print(output)
    print()


if __name__ == "__main__":
    torch.set_printoptions(precision=4, sci_mode=False)
    run_toy_example()
    run_multi_query_example()
