import math

class PositionalEncoding:
    def __init__(self, max_len, embedding_dim):
        # Initialize the parameters for max_len and embedding_dim
        self.max_len = max_len
        self.embedding_dim = embedding_dim
        self.encoding = self.generate_positional_encoding()

    def generate_positional_encoding(self):
        # Create a positional encoding matrix with shape (max_len, embedding_dim)
        encoding = []
        for pos in range(self.max_len):
            pos_enc = []
            for i in range(self.embedding_dim):  # Fixed: changed self.dim -> self.embedding_dim
                if i % 2 == 0:
                    pos_enc.append(math.sin(pos / (10000 ** (i / self.embedding_dim))))
                else:
                    pos_enc.append(math.cos(pos / (10000 ** ((i - 1) / self.embedding_dim))))
            encoding.append(pos_enc)
        return encoding
    
    def get_encoding(self):
        return self.encoding
    
    def add_positional_encoding(self, token_embeddings):
        """
        Add positional encoding to the token embeddings.
        token_embeddings: List of token embeddings for a sentence (list of lists).
        """
        # Ensure the input token_embeddings has shape (max_len, embedding_dim)
        assert len(token_embeddings) == self.max_len
        assert len(token_embeddings[0]) == self.embedding_dim

        # Add positional encoding to each token's embedding
        for i in range(self.max_len):
            for j in range(self.embedding_dim):
                token_embeddings[i][j] += self.encoding[i][j]
        
        return token_embeddings


# Example of usage:
max_len = 10  # Sequence length
embedding_dim = 8  # Dimensionality of the embedding

# Create the positional encoding object
pos_encoder = PositionalEncoding(max_len, embedding_dim)

# Let's assume we have token embeddings (randomly generated for demonstration)
token_embeddings = [[1.0] * embedding_dim for _ in range(max_len)]  # Example of token embeddings

# Add positional encoding to the token embeddings
output_with_pos_encoding = pos_encoder.add_positional_encoding(token_embeddings)

# Print the result
print("Token embeddings with positional encoding:")
for i in range(max_len):
    print(f"Token {i}: {output_with_pos_encoding[i]}")
