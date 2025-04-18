from src.positional_encoding import PositionalEncoding

def print_positional_encoding(pe_matrix):
    for i, row in enumerate(pe_matrix):
        print(f"Position {i}: {['{:.4f}'.format(val) for val in row]}")

def test_positional_encoding():
    seq_len = 10
    dim = 8
    pe = PositionalEncoding(max_len=seq_len, embedding_dim=dim)
    pe_matrix = pe.get_encoding()

    print("Positional Encoding Matrix:")
    print_positional_encoding(pe_matrix)

if __name__ == "__main__":
    test_positional_encoding()
