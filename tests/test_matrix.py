import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from src.matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_add(self):
        A = Matrix(2, 2)
        B = Matrix(2, 2)
        A.fill(1)
        B.fill(2)
        result = A.add(B)
        expected = [[3, 3], [3, 3]]
        self.assertEqual(result.data, expected)

    def test_multiply(self):
        A = Matrix(2, 3)
        B = Matrix(3, 2)
        A.fill_dummy()  # fills with 1 to 6
        B.fill(1)      # fills all with 1
        result = A.multiply(B)
        expected = [[6, 6], [15, 15]]
        self.assertEqual(result.data, expected)

    def test_transpose(self):
        A = Matrix(2, 3)
        A.fill_dummy()
        result = A.transpose()
        expected = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(result.data, expected)

    def test_scalar_multiply(self):
        A = Matrix(2, 2)
        A.fill(3)
        result = A.scalar_multiply(2)
        expected = [[6, 6], [6, 6]]
        self.assertEqual(result.data, expected)

    def test_dot_product(self):
        A = Matrix(1, 3)
        B = Matrix(1, 3)
        A.set(0, 0, 1)
        A.set(0, 1, 2)
        A.set(0, 2, 3)
        B.set(0, 0, 4)
        B.set(0, 1, 5)
        B.set(0, 2, 6)
        result = A.dot_product(B)
        self.assertEqual(result, 32)  # 1*4 + 2*5 + 3*6

if __name__ == '__main__':
    unittest.main()
