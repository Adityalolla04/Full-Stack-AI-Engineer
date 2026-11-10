import numpy as np

# Mock 2D embeddings
embeddings = {
    "king": np.array([10, 5]),
    "man": np.array([5, 2]),
    "woman": np.array([5, 8]),
    "queen": np.array([10, 11])
}

# Goal: King - Man + Woman = ?
target = embeddings["king"] - embeddings["man"] + embeddings["woman"]

# Find the closest match in our dictionary
def find_closest(v, embs):
    closest_word = None
    max_sim = -1
    for word, vec in embs.items():
        sim = np.dot(v, vec) / (np.linalg.norm(v) * np.linalg.norm(vec))
        if sim > max_sim:
            max_sim = sim
            closest_word = word
    return closest_word

result = find_closest(target, embeddings)
print(f"King - Man + Woman = {result}")