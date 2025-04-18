# src/tokenizer.py

import re
import json
from collections import defaultdict

class Tokenizer:
    def __init__(self, vocab=None):
        self.vocab = vocab if vocab else {"<PAD>": 0, "<UNK>": 1}
        self.reverse_vocab = {v: k for k, v in self.vocab.items()}

    def clean_text(self, text):
        return re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())

    def tokenize(self, text):
        return self.clean_text(text).strip().split()

    def build_vocab(self, texts, min_freq=1):
        freq = defaultdict(int)
        for text in texts:
            for token in self.tokenize(text):
                freq[token] += 1

        idx = len(self.vocab)
        for word, count in freq.items():
            if count >= min_freq and word not in self.vocab:
                self.vocab[word] = idx
                idx += 1

        self.reverse_vocab = {v: k for k, v in self.vocab.items()}

    def encode(self, text, max_len=10):
        tokens = self.tokenize(text)
        token_ids = [self.vocab.get(t, self.vocab["<UNK>"]) for t in tokens]
        token_ids = token_ids[:max_len]
        token_ids += [self.vocab["<PAD>"]] * (max_len - len(token_ids))
        return token_ids

    def decode(self, token_ids):
        return ' '.join([self.reverse_vocab.get(i, "<UNK>") for i in token_ids])

    def save_vocab(self, filepath="vocab.json"):
        with open(filepath, "w") as f:
            json.dump(self.vocab, f)

    def load_vocab(self, filepath="vocab.json"):
        with open(filepath, "r") as f:
            self.vocab = json.load(f)
        self.reverse_vocab = {int(v): k for k, v in self.vocab.items()}
