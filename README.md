# Tokenization in Large Language Models (LLMs)

This repository explains **tokenization** — the foundational process that enables Large Language Models (LLMs) like GPT, BERT, and others to understand human text.

Tokenization:
1. **Breaks text into small pieces** called *tokens*.  
2. Converts tokens into numbers (token IDs) the model can process.  
3. Feeds those numeric sequences into the model for tasks like generation, classification, or embeddings. :contentReference[oaicite:1]{index=1}

---

## What you will Learn from this repository

- What tokenization is  
- Why it’s critical for LLMs  
- Tokenizer components  
- Processing pipeline  
- Subword tokenization methods (BPE, WordPiece, SentencePiece)  
- Practical examples  
- References

---

## Why Tokenization Matters

Raw text cannot be directly processed by LLMs because models operate on numeric data (vectors). Tokenization maps text to numeric IDs efficiently, aiding:

- **Memory efficiency**
- **Vocabulary coverage**
- **Handling rare/out-of-vocabulary words**

Modern LLMs use subword tokenization to strike a balance between vocabulary size and expressiveness. :contentReference[oaicite:2]{index=2}
