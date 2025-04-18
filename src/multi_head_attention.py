import math
import numpy as np
from src.matrix import Matrix

class MultiHeadAttention:
    def __init__(self, input_matrix, num_heads=16, d_model=32, dropout_rate=0.1):
        self.num_heads = num_heads
        self.d_model = d_model
        self.d_head = d_model // num_heads  # Dimension per head
        
        # Initialize weights for Q, K, V (Query, Key, Value matrices)
        self.Wq = self._initialize_weights(d_model, d_model)
        self.Wk = self._initialize_weights(d_model, d_model)
        self.Wv = self._initialize_weights(d_model, d_model)
        
        # Output projection matrix
        self.Wo = self._initialize_weights(d_model, d_model)
        
        # Dropout
        self.dropout_rate = dropout_rate

    def _initialize_weights(self, in_dim, out_dim):
        # Default weight initialization (random)
        return np.random.randn(in_dim, out_dim) * 0.01  # Using small random values

    def _split_into_heads(self, matrix):
        """Split the input matrix into `num_heads` smaller matrices (one per attention head)."""
        # matrix is of shape (batch_size, seq_len, d_model)
        batch_size, seq_len, _ = matrix.shape
        # Split into num_heads heads (shape: batch_size, seq_len, num_heads, d_head)
        return matrix.reshape(batch_size, seq_len, self.num_heads, self.d_head)

    def scaled_dot_product_attention(self, Q, K, V):
        """Calculate scaled dot-product attention."""
        # Step 1: Calculate Q.K^T (dot product of Q and K)
        K_T = K.transpose(0, 1, 3, 2)  # Transpose to match Q shape for dot product
        matmul_qk = np.matmul(Q, K_T)  # Shape: (batch_size, seq_len, num_heads, seq_len)
        
        # Step 2: Scale by sqrt(d_k)
        dk = float(K.shape[-1])  # Dimension of key (d_k)
        scaled_attention_logits = matmul_qk / math.sqrt(dk)
        
        # Step 3: Apply softmax to get attention weights
        attention_weights = self.softmax(scaled_attention_logits)
        
        # Step 4: Multiply attention weights by V
        output = np.matmul(attention_weights, V)
        return output, attention_weights

    def softmax(self, logits):
        """Softmax function to convert logits to probabilities."""
        exp_values = np.exp(logits - np.max(logits, axis=-1, keepdims=True))
        return exp_values / np.sum(exp_values, axis=-1, keepdims=True)

    def forward(self, input_matrix):
        """Apply MultiHead Attention."""
        # Step 1: Apply weight matrices to input (Q, K, V)
        Q = np.matmul(input_matrix, self.Wq)
        K = np.matmul(input_matrix, self.Wk)
        V = np.matmul(input_matrix, self.Wv)

        # Step 2: Split Q, K, V into multiple heads
        Q = self._split_into_heads(Q)
        K = self._split_into_heads(K)
        V = self._split_into_heads(V)

        # Step 3: Apply scaled dot-product attention to each head
        output, attention_weights = self.scaled_dot_product_attention(Q, K, V)
        
        # Step 4: Combine the heads back into a single matrix
        output = output.reshape(output.shape[0], output.shape[1], self.d_model)  # Flatten heads back into d_model

        # Step 5: Apply output projection (Wo)
        output = np.matmul(output, self.Wo)
        
        # Step 6: Apply ReLU activation
        output = np.maximum(output, 0)  # ReLU activation

        # Step 7: Apply dropout (if specified)
        if self.dropout_rate > 0:
            output = self.apply_dropout(output)

        return output, attention_weights

    def apply_dropout(self, output):
        """Apply dropout regularization."""
        mask = (np.random.rand(*output.shape) > self.dropout_rate).astype(np.float32)
        return output * mask

