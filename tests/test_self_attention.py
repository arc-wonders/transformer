import unittest
from src.matrix import Matrix
from src.self_attention import SelfAttention  # Assuming you have the SelfAttention class in self_attention.py

class TestSelfAttention(unittest.TestCase):
    def test_scaled_dot_product_attention(self):
        # Step 1: Create a dummy input matrix (3x3 for simplicity)
        matrix = Matrix(3, 3)
        matrix.data = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 1, 0]
        ]  # Filling the matrix with dummy values
        
        # Print the original matrix
        print("Original Matrix:")
        matrix.print()
        
        # Step 2: Initialize the SelfAttention object
        self_attention = SelfAttention(matrix)
        
        # Step 3: Perform scaled dot-product attention
        output, attention_weights = self_attention.scaled_dot_product_attention(matrix, matrix, matrix)
        
        # Step 4: Print the results
        print("Attention Output:")
        output.print()
        
        print("Attention Weights:")
        attention_weights.print()
        
        # Assertions to check the correctness of the output
        # Ensure the output is of the same shape as the input
        self.assertEqual(output.rows, matrix.rows)
        self.assertEqual(output.cols, matrix.cols)
        
        # Ensure the attention weights are probabilities (between 0 and 1)
        for i in range(attention_weights.rows):
            for j in range(attention_weights.cols):
                self.assertGreaterEqual(attention_weights.data[i][j], 0)
                self.assertLessEqual(attention_weights.data[i][j], 1)
        
        # Ensure the attention weights sum to 1 for each row (softmax property)
        for i in range(attention_weights.rows):
            row_sum = sum(attention_weights.data[i])
            self.assertAlmostEqual(row_sum, 1.0, places=3)  # Sum should be approximately 1

if __name__ == '__main__':
    unittest.main()
