import math
from src.matrix import Matrix

class SelfAttention:
    def __init__(self, input_matrix):
        self.input = input_matrix
        self.Q = self.input
        self.K = self.input
        self.V = self.input

    def scaled_dot_product_attention(self, Q, K, V):
        # Step 1: Q · K^T
        K_T = K.transpose()
        matmul_qk = Q.dot(K_T)

        print("Dot product (Q · K^T):")
        matmul_qk.print()

        # Step 2: scale by √dk
        dk = Q.cols
        scale_factor = 1 / math.sqrt(dk)
        scaled_attention_logits = matmul_qk.scalar_multiply(scale_factor)

        print(f"\nScaled logits (divided by √{dk:.2f}):")
        scaled_attention_logits.print()

        # Step 3: softmax
        attention_weights = self.softmax(scaled_attention_logits)

        print("\nSoftmax (attention weights):")
        attention_weights.print()

        # Step 4: weighted sum with V
        output = attention_weights.dot(V)

        print("\nFinal Output (Attention result):")
        output.print()

        return output, attention_weights

    def softmax(self, logits):
        result = Matrix(logits.rows, logits.cols)
        for i in range(logits.rows):
            row_max = max(logits.data[i])  # Stability trick
            exp_vals = [math.exp(x - row_max) for x in logits.data[i]]
            row_sum = sum(exp_vals)
            for j in range(logits.cols):
                result.data[i][j] = exp_vals[j] / row_sum
        return result
