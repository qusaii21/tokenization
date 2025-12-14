# filename: examples/tokenize_batch.py

from transformers import AutoTokenizer

def batch_tokenize(model_name, texts):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    encodings = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    
    for i, txt in enumerate(texts):
        tokens = tokenizer.convert_ids_to_tokens(encodings["input_ids"][i])
        print(f"\nText: {txt}")
        print("Tokens:", tokens)

if __name__ == "__main__":
    sentences = [
        "Tokenization is fun!",
        "Batch processing with Transformers."
    ]
    batch_tokenize("bert-base-uncased", sentences)
