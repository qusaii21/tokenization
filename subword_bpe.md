# Byte Pair Encoding (BPE)

BPE is a subword segmentation method that builds a vocabulary by merging the most frequent pairs of characters into larger units. :contentReference[oaicite:10]{index=10}

## How BPE Works

1. Start with every character as a token.
2. Count adjacent pairs.
3. Merge the most frequent pair into a new token.
4. Repeat until desired vocab size.

Example:
text = “lower lower”
initial: l o w e r
frequent pair: “lo”
→ new token “lo”


## Pros & Cons

✔ Handles rare words  
✔ Efficient subword units  
❌ Fixed vocab after training :contentReference[oaicite:11]{index=11}
