# WordPiece Tokenization

Used by models like BERT. WordPiece selects the best subword splits using likelihood models rather than just frequency. :contentReference[oaicite:12]{index=12}

## How It Works

1. Start with entire words
2. Break into subwords where appropriate
3. Choose subword parts based on vocabulary and probability

Example:
"hugs"
→ ["hug", "##s"]

## Key Differences from BPE

- WordPiece uses probabilistic decisions
- Only stores final vocabulary, not merge rules :contentReference[oaicite:13]{index=13}
