# src/embedding.py

import numpy as np

class CustomEmbedding:
    def __init__(self, vocab_size, embedding_dim):
        self.embedding_dim = embedding_dim
        self.vocab_size = vocab_size
        self.embeddings = np.random.randn(vocab_size, embedding_dim) * 0.01

    def forward(self, input_ids):
        return np.array([[self.embeddings[token] for token in sentence] for sentence in input_ids])

    def __call__(self, input_ids):
        return self.forward(input_ids)
