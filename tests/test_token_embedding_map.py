import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import numpy as np
from src.tokenizer import Tokenizer
from src.embedding import CustomEmbedding

def test_token_embedding_map():
    sentence = "I feel awesome today and I am happy"
    tokenizer = Tokenizer()
    tokenizer.build_vocab([sentence])

    # Tokenize and encode
    token_ids = tokenizer.encode(sentence, max_len=10)
    tokens = tokenizer.tokenize(sentence)

    # Map tokens to their IDs
    print("🔹 Token to ID mapping:")
    for token in tokens:
        print(f"'{token}': {tokenizer.vocab.get(token)}")
    
    print("\n🔹 Token IDs (padded):", token_ids)

    # Create embedding and get vectors
    embedding_dim = 8
    embedding = CustomEmbedding(vocab_size=len(tokenizer.vocab), embedding_dim=embedding_dim)
    token_ids_np = np.array([token_ids])
    embedded_output = embedding(token_ids_np)  # Shape: (1, seq_len, embedding_dim)

    print("\n🔹 Embeddings:")
    for i, token in enumerate(tokens):
        emb = embedded_output[0][i]
        print(f"Token: '{token}' | Embedding: {np.round(emb, 4)}")

if __name__ == "__main__":
    test_token_embedding_map()
