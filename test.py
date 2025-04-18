import unittest
from src.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        vocab = {"<PAD>": 0, "<UNK>": 1, "hello": 2, "world": 3}
        self.tokenizer = Tokenizer(vocab)

    def test_tokenize(self):
        text = "hello world"
        expected = ['hello', 'world']
        result = self.tokenizer.tokenize(text)
        self.assertEqual(result, expected)

    def test_tokenize_and_convert_to_ids(self):
        text = "hello world"
        expected = [2, 3]  # Assuming the vocab is correct
        result = self.tokenizer.encode(text)
        self.assertEqual(result, expected)

    def test_decode(self):
        token_ids = [2, 3]
        expected = "hello world"
        result = self.tokenizer.decode(token_ids)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
