# filename: examples/tokenize_hf.py

from transformers import AutoTokenizer

def tokenize_text(model_name, text):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # Encode returns token IDs
    encoding = tokenizer(text, return_tensors="pt")
    tokens = tokenizer.convert_ids_to_tokens(encoding["input_ids"][0])
    token_ids = encoding["input_ids"][0].tolist()

    print("Model:", model_name)
    print("Input Text:", text)
    print("Tokens:", tokens)
    print("Token IDs:", token_ids)

if __name__ == "__main__":
    sample_text = "Hello LLMs from Pune!"
    tokenize_text("gpt2", sample_text)          # GPT-2 style BPE tokenizer
    tokenize_text("bert-base-uncased", sample_text)  # WordPiece tokenizer
