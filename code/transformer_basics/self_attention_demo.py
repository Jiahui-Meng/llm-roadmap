import torch
import torch.nn as nn
import math


def scaled_dot_product_attention(Q, K, V, mask=None):
    """
    Compute scaled dot-product attention.

    Args:
        Q: Query tensor of shape (..., seq_len, d_k)
        K: Key tensor of shape (..., seq_len, d_k)
        V: Value tensor of shape (..., seq_len, d_v)
        mask: Optional mask broadcastable to (..., seq_len, seq_len)

    Returns:
        output: Attention output tensor
        weights: Attention weights after softmax
    """
    d_k = Q.size(-1)

    scores = torch.matmul(Q, K.transpose(-1, -2)) / math.sqrt(d_k)

    if mask is not None:
        scores = scores.masked_fill(mask == 0, float("-inf"))

    weights = torch.softmax(scores, dim=-1)
    output = torch.matmul(weights, V)

    return output, weights


class SelfAttention(nn.Module):
    """
    Single-head self-attention layer.

    This is the building block for multi-head attention.
    It projects the input into Q, K, V and computes scaled dot-product attention.
    """

    def __init__(self, d_model):
        """
        Args:
            d_model: Dimension of the model (embedding dimension)
        """
        super().__init__()
        self.d_model = d_model

        # Linear projections for Q, K, V
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        """
        Args:
            x: Input tensor of shape (batch, seq_len, d_model)
            mask: Optional mask

        Returns:
            output: Attention output of shape (batch, seq_len, d_model)
            weights: Attention weights of shape (batch, seq_len, seq_len)
        """
        Q = self.W_q(x)
        K = self.W_k(x)
        V = self.W_v(x)

        output, weights = scaled_dot_product_attention(Q, K, V, mask)

        return output, weights


def toy_example_1():
    """Minimal 1-token example to understand the flow."""
    print("=" * 60)
    print("Toy Example 1: Single Query Token")
    print("=" * 60)

    d_model = 4
    batch_size = 1
    seq_len = 3

    # Create a self-attention layer
    sa = SelfAttention(d_model)

    # Input: 1 batch, 3 tokens, 4-dim embeddings
    x = torch.tensor(
        [
            [[1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0], [1.0, 1.0, 0.0, 0.0]],
        ]
    )

    print(f"\nInput shape: {x.shape}")
    print("Input (x):")
    print(x)

    output, weights = sa(x)

    print(f"\nOutput shape: {output.shape}")
    print("Output (x_new - each token updated with context):")
    print(output)

    print(f"\nAttention weights shape: {weights.shape}")
    print("Attention weights (how much each token looks at others):")
    print(weights)

    print("\n--- Analysis ---")
    print("Notice that:")
    print("1. Input shape == Output shape (both are (batch, seq_len, d_model))")
    print(
        "2. Each row in weights sums to 1.0 (softmax normalization)"
    )
    print("3. The model learned to attend to certain tokens more than others")
    print()


def toy_example_2():
    """Slightly more interesting example with batch."""
    print("=" * 60)
    print("Toy Example 2: Batch of 2 Sequences")
    print("=" * 60)

    d_model = 8
    batch_size = 2
    seq_len = 4

    sa = SelfAttention(d_model)

    # Create random batch input
    x = torch.randn(batch_size, seq_len, d_model)

    print(f"\nInput shape: {x.shape}")

    output, weights = sa(x)

    print(f"Output shape: {output.shape}")
    print(f"Attention weights shape: {weights.shape}")

    # Let's look at attention for the first sequence, all queries
    print("\n--- Attention weights for first sequence ---")
    print("(What does each token look at?)")
    print(weights[0])

    print("\n--- Understanding attention distribution ---")
    for i in range(seq_len):
        max_weight_idx = weights[0, i].argmax().item()
        max_weight_val = weights[0, i].max().item()
        print(
            f"Token {i} attends most to token {max_weight_idx} (weight={max_weight_val:.4f})"
        )

    print()


def toy_example_3():
    """Example showing how self-attention differs across tokens."""
    print("=" * 60)
    print("Toy Example 3: Comparing attention patterns")
    print("=" * 60)

    d_model = 6
    batch_size = 1
    seq_len = 3

    sa = SelfAttention(d_model)

    # More interesting input with some structure
    x = torch.tensor(
        [
            [
                [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # Token 0: mostly first dim
                [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],  # Token 1: mostly second dim
                [0.0, 0.0, 1.0, 1.0, 0.0, 0.0],  # Token 2: mixed
            ]
        ]
    )

    output, weights = sa(x)

    print("\nInput tokens (each row is a token):")
    for i, token in enumerate(x[0]):
        print(f"Token {i}: {token}")

    print("\nAttention pattern (what each query attends to):")
    for i in range(seq_len):
        print(f"Query {i} attention weights: {weights[0, i].detach().numpy()}")

    print("\nKey insight:")
    print("- Each query vector creates a unique attention pattern")
    print("- The model learned to look at different parts of the sequence")
    print("- This is data-dependent (not fixed position-based)")

    print()


if __name__ == "__main__":
    torch.manual_seed(42)
    torch.set_printoptions(precision=4, sci_mode=False)

    toy_example_1()
    toy_example_2()
    toy_example_3()
