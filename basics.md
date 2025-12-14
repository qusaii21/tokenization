# Tokenization Basics

## What is Tokenization?

Tokenization converts raw text into smaller units called **tokens** that the model can understand and process. These tokens may represent:

- **Words**
- **Subwords**
- **Characters**

LLMs then map tokens to **numerical IDs** via a lookup table (vocabulary). :contentReference[oaicite:3]{index=3}

Example:
Input: “Hello world!”
Tokens: ["Hello", "world", "!"]
IDs: [154, 26, 7] # (example)


## Types of Tokenization

### 1) Word Tokenization
Splits text into full words.
- Simple but large vocabulary
- Harder to handle rare words
- Works in languages with clear spaces :contentReference[oaicite:4]{index=4}

Example:
"The car"
→ ["The", "car"]


### 2) Character Tokenization
Splits text into individual characters.
- Small vocabulary
- Very long sequences
- Good for languages without clear spaces :contentReference[oaicite:5]{index=5}

Example:
### 2) Character Tokenization
Splits text into individual characters.
- Small vocabulary
- Very long sequences
- Good for languages without clear spaces :contentReference[oaicite:5]{index=5}

Example:
"Hi"
→ ["H", "i"]


### 3) Subword Tokenization
Breaks into pieces between full words and characters.
- Efficient vocabulary
- Handles unseen words
- Widely used in LLMs :contentReference[oaicite:6]{index=6}

Example:
"unhappy" → ["un", "happy"]


