# Transformer To Rag

## Bridge question
This note explains how Transformer limitations around parametric memory, context limits, and freshness naturally motivate RAG systems.

## From foundations to systems
Start from the Transformer mechanics you already know:
- token embeddings
- self-attention and multi-head attention
- context window limits
- autoregressive decoding

Then ask: what breaks or becomes expensive in production? The answer creates demand for a new system layer.

## Main bridge
- **Model-only approach**: simple but limited by context, freshness, or cost.
- **System-augmented approach**: adds retrieval / adapters / serving optimization / tools.
- **Engineering implication**: new observability, evaluation, and failure modes appear.

## What to remember
A bridge note should connect a model primitive to an engineering system, not just define a buzzword.
