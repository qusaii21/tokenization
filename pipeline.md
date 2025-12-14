# Tokenization Pipeline

Below is a typical pipeline for processing text into tokens for LLMs.

## 1) Input Text
User prompt or corpus text:
“Transformers are powerful”

## 2) Pre-Tokenization
Initial splitting (e.g., regex + punctuation):
["Transformers", "are", "powerful"]

## 3) Subword Segmentation
Using subword models (BPE/WordPiece/SentencePiece):
["Trans", "form", "ers", "are", "power", "ful"]


## 4) Token → ID Mapping
Each token gets a numeric ID via the vocabulary.

## 5) Model Input
The numeric tokens feed into the model for embedding and inference.

## 6) Decode
Model outputs token IDs → tokens → text.

## Glossary

- **Token**: A piece of text used by the model.
- **Vocabulary**: Set of all tokens a model can recognize.
- **Embedding**: Vector representation of a token.
