import unittest
import numpy as np
from src.matrix import Matrix
from src.multi_head_attention import MultiHeadAttention  # Adjust the import path as needed

class TestMultiHeadAttention(unittest.TestCase):
    def test_multi_head_attention(self):
        # Step 1: Create a dummy input matrix (batch_size=1, seq_len=3, d_model=32 for simplicity)
        batch_size = 1
        seq_len = 3
        d_model = 32  # 32 dimensions

        # Random dummy data (you can replace this with any data)
        input_data = np.random.randn(batch_size, seq_len, d_model)

        # Step 2: Initialize the MultiHeadAttention object
        multi_head_attention = MultiHeadAttention(input_data, num_heads=16, d_model=d_model)

        # Step 3: Apply the MultiHeadAttention
        output, attention_weights = multi_head_attention.forward(input_data)

        # Step 4: Print the results
        print("Attention Output:")
        print(output)

        print("Attention Weights:")
        print(attention_weights)

        # Assertions to check the correctness of the output
        # Ensure output has the same shape as the input (after attention processing)
        self.assertEqual(output.shape[0], batch_size)
        self.assertEqual(output.shape[1], seq_len)
        self.assertEqual(output.shape[2], d_model)

        # Ensure attention weights are valid probabilities (between 0 and 1)
        for i in range(attention_weights.shape[0]):
            for j in range(attention_weights.shape[1]):
                for k in range(attention_weights.shape[2]):
                    self.assertGreaterEqual(attention_weights[i][j][k], 0)
                    self.assertLessEqual(attention_weights[i][j][k], 1)

        # Ensure each row of attention weights sums to 1 (softmax property)
        for i in range(attention_weights.shape[0]):
            for j in range(attention_weights.shape[1]):
                row_sum = np.sum(attention_weights[i][j])
                self.assertAlmostEqual(row_sum, 1.0, places=3)

if __name__ == '__main__':
    unittest.main()
