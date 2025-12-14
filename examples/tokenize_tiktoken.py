# filename: examples/tokenize_tiktoken.py

import tiktoken

def tokenize_with_tiktoken(text):
    # choose one encoding — often model-specific
    enc = tiktoken.get_encoding("gpt2")
    token_ids = enc.encode(text)
    tokens = [enc.decode([i]) for i in token_ids]

    print("Input text:", text)
    print("Tokens:", tokens)
    print("Token IDs:", token_ids)

if __name__ == "__main__":
    sample_text = "Tokenize with tiktoken!"
    tokenize_with_tiktoken(sample_text)
