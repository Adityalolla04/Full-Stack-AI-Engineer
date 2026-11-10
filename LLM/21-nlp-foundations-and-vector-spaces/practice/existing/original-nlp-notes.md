# 📊 Sentiment Analysis with Logistic Regression

### 📝 Definition
In this concept, we don't feed raw text to the model. We represent each document (tweet) as a vector based on the **sum of positive and negative frequencies** of its words.

### ⚙️ Mechanism
1. **Preprocessing:** Tokenize, lowercase, remove stop words/punctuation, and perform stemming (e.g., "tuning" -> "tun").
2. **Frequency Mapping:** Build a dictionary `(word, label) -> count`.
3. **Feature Extraction:** Convert a tweet into a 3D vector: `[1, Sum_Pos, Sum_Neg]`.
4. **Logistic Regression:** Apply the sigmoid function to predict probability.

# 📐 Vector Spaces & Cosine Similarity

### 1. Definition
A **Vector Space** is a mathematical space where words are represented as vectors (lists of numbers). Similar words are "closer" together in this space.

### 2. Mechanism: Cosine Similarity
To find if two documents (like a UCC law and a user query) are similar, we don't look at the distance between the points, but the **angle** between the vectors.

**The Formula:**
$$\text{cos}(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$

- **1.0 (0° angle):** The words are identical in meaning.
- **0.0 (90° angle):** The words are completely unrelated.

# 💎 Word Embeddings & Analogies

### 📝 Definition
Embeddings capture hidden semantic relationships. The classic example is the "Analogy Task."

### ⚙️ Mechanism
- **CBOW (Continuous Bag of Words):** Predicting a "center" word based on surrounding "context" words.
- **Analogy Logic:** If the model learns well, then the vector math: `King - Man + Woman` should result in a vector closest to `Queen`.
