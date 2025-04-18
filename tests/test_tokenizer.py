import json
import os
import sys

# Add src to Python path so we can import Tokenizer
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from tokenizer import Tokenizer

# Load data.json from the same directory
with open(os.path.join(os.path.dirname(__file__), "data.json"), "r") as f:
    data = json.load(f)

texts = data["texts"]

# Create tokenizer and build vocab
tokenizer = Tokenizer()
tokenizer.build_vocab(texts)

# Test encoding and decoding
for text in texts:
    encoded = tokenizer.encode(text, max_len=10)
    decoded = tokenizer.decode(encoded)
    
    print(f"Original : {text}")
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decoded}")
    print("-" * 40)
