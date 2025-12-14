# Tokenizer Components

Tokenizers aren’t monolithic — they have **distinct parts**:

## 1) Pre-Tokenizer
Initial splitting of text using simple rules:
- whitespace
- punctuation
- regex
This prepares text for deeper segmentation. :contentReference[oaicite:7]{index=7}

## 2) Vocabulary
A list of known tokens and their numeric IDs:
{"hello": 1312, "world": 312, "##ing": 65, ...}


Vocabulary size is a key hyperparameter in training tokenizers. :contentReference[oaicite:8]{index=8}

## 3) Encoder
Maps each token to its numeric ID:
"hello" → 1312


## 4) Decoder
Converts IDs back to tokens for output generation.

## 5) Special Tokens
Models also use tokens like:
- `[UNK]` (unknown)
- `[PAD]` (padding)
- `[CLS]` / `[SEP]`
These help with structure and control. :contentReference[oaicite:9]{index=9}


