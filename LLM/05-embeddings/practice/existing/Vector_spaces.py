import numpy as np

def cosine_similarity(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

# Imagine 3D embeddings: [Finance, Legal, Tech]
word_law = np.array([0.9, 0.8, 0.1])
word_bank = np.array([0.8, 0.7, 0.2])
word_apple = np.array([0.1, 0.1, 0.9])

print(f"Similarity (Law vs Bank): {cosine_similarity(word_law, word_bank):.4f}")
print(f"Similarity (Law vs Apple): {cosine_similarity(word_law, word_apple):.4f}")