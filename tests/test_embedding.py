# tests/test_embedding.py

import numpy as np
from src.tokenizer import Tokenizer
from src.embedding import CustomEmbedding

def test_embedding():
    data = [
        ("I am so happy today!", "happy"),
        ("This is the worst day ever.", "sad"),
        ("I feel great and excited!", "happy"),
        ("I'm angry and frustrated.", "angry"),
        ("Feeling very low and depressed.", "sad"),
    ]

    texts = [x[0] for x in data]
    tokenizer = Tokenizer()
    tokenizer.build_vocab(texts)

    encoded_inputs = [tokenizer.encode(text, max_len=10) for text in texts]
    encoded_inputs = np.array(encoded_inputs)

    embedding_dim = 16
    embedding = CustomEmbedding(vocab_size=len(tokenizer.vocab), embedding_dim=embedding_dim)
    embedded_output = embedding(encoded_inputs)

    assert embedded_output.shape == (len(texts), 10, embedding_dim)
    print("✅ Embedding test passed. Output shape:", embedded_output.shape)

if __name__ == "__main__":
    test_embedding()
