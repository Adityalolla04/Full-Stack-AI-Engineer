# ML ALGORITHMS FROM SCRATCH - QUICK REFERENCE GUIDE

**Complete revision guide for Machine Learning fundamentals from deep learning.ai**

---

## TABLE OF CONTENTS
1. [Linear Regression](#linear-regression)
2. [Logistic Regression](#logistic-regression)
3. [Decision Trees](#decision-trees)
4. [KMeans Clustering](#kmeans-clustering)
5. [Neural Networks](#neural-networks)
6. [Key Mathematical Concepts](#key-concepts)
7. [Code Snippets Summary](#code-snippets)

---

## LINEAR REGRESSION

### What It Does
Predicts continuous values by fitting a linear relationship: $f(x) = wx + b$

### Key Equations
- **Hypothesis**: $f_{w,b}(x) = w \cdot x + b$
- **Cost Function (MSE)**: $J(w,b) = \frac{1}{2m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})^2$
- **Gradient Descent Updates**:
  - $w := w - \alpha \frac{\partial J}{\partial w} = w - \alpha \frac{1}{m}\sum (f - y) \cdot x$
  - $b := b - \alpha \frac{\partial J}{\partial b} = b - \alpha \frac{1}{m}\sum (f - y)$
- **Normal Equation** (closed-form): $w = (X^T X)^{-1} X^T y$

### Two Implementation Approaches
1. **Gradient Descent**: Iterative, works for large datasets, requires learning rate tuning
2. **Normal Equation**: Direct solution, slower for large datasets, no hyperparameter tuning

### Evaluation Metrics
- **MSE** = $\frac{1}{m}\sum(y_{true} - y_{pred})^2$ ← penalizes large errors
- **RMSE** = $\sqrt{MSE}$ ← same units as target
- **MAE** = $\frac{1}{m}\sum|y_{true} - y_{pred}|$ ← median-robust
- **R²** = $1 - \frac{SS_{res}}{SS_{tot}}$ ← fraction of variance explained (0-1, higher better)
- **R² Adjusted** = $1 - (1-R^2)\frac{m-1}{m-p-1}$ ← penalizes extra features

### When to Use
- Predicting continuous variables (prices, temperatures, sales)
- When relationship is roughly linear
- First baseline model to try

### Key Hyperparameters
- **Learning Rate** ($\alpha$): Controls step size. Too high → diverges, too low → slow
- **Iterations**: Max training iterations before stopping
- **L2 Lambda** ($\lambda$): Regularization strength to prevent overfitting

---

## LOGISTIC REGRESSION

### What It Does
Binary classification: predicts probability of class 1 (0 ≤ $\sigma(z)$ ≤ 1)

### Key Equations
- **Sigmoid Activation**: $\sigma(z) = \frac{1}{1 + e^{-z}}$ ← maps to [0,1]
- **Hypothesis**: $f_{w,b}(x) = \sigma(w \cdot x + b) = P(y=1|x)$
- **Cost Function (Binary Cross-Entropy)**:
  $$J = -\frac{1}{m}\sum_{i=1}^{m}[y^{(i)}\log(f) + (1-y^{(i)})\log(1-f)]$$
- **Gradient**: Same form as linear regression!
  - $\frac{\partial J}{\partial w} = \frac{1}{m}X^T(\sigma(Xw+b) - y)$
  - $\frac{\partial J}{\partial b} = \frac{1}{m}\sum(\sigma(Xw+b) - y)$

### Decision Boundary
- If $f(x) \geq 0.5$ → predict class 1
- If $f(x) < 0.5$ → predict class 0
- Can adjust threshold for precision-recall tradeoff

### Evaluation Metrics
- **Accuracy** = $\frac{TP + TN}{Total}$ ← overall correctness
- **Precision** = $\frac{TP}{TP+FP}$ ← "When I predict positive, how often right?"
- **Recall** = $\frac{TP}{TP+FN}$ ← "Of all positives, how many did I catch?"
- **F1-Score** = $2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$ ← harmonic mean
- **ROC-AUC** ← area under curve, invariant to threshold

### When to Use
- Binary classification (spam/not spam, disease/healthy, survive/die)
- Probability estimates needed
- First classifier to try

### Key Insight
Despite using sigmoid, gradient has same form as linear regression. Difference in cost function!

---

## DECISION TREES

### What It Does
Recursively splits data into pure regions using information gain

### Key Equations
- **Entropy** (measure of impurity): 
  $$H(S) = -\sum_{i=1}^{k} p_i \log_2(p_i)$$
  - $H = 0$ → pure (all one class)
  - $H = 1$ → maximum impurity (50-50 split)
  
- **Information Gain** (how much split reduces entropy):
  $$IG = H(S) - \sum_{v} \frac{|S_v|}{|S|} H(S_v)$$
  - Higher IG = better split

### Algorithm
1. For each feature and each possible threshold:
   - Split data into left (≤ threshold) and right (> threshold)
   - Calculate information gain
2. Choose split with highest IG
3. Recursively build left and right subtrees
4. Stop when: pure node (all one class) OR max depth OR min samples split

### Tree Building
- **Greedy**: Locally optimal split, not globally
- **Recursive**: Treats each node independently
- **Non-parametric**: No assumptions about data distribution

### Evaluation
- **Accuracy** for classification
- **Gini Impurity** = $1 - \sum p_i^2$ ← alternative to entropy

### When to Use
- Non-linear relationships
- Feature importance needed
- Interpretability important
- Can handle categorical features

### Key Hyperparameters
- **max_depth**: Limit tree depth to prevent overfitting
- **min_samples_split**: Minimum samples required to split
- **min_samples_leaf**: Minimum samples in leaf node

### Advantages & Disadvantages
✓ Interpretable, handles non-linear, feature importance, categorical features  
✗ Tends to overfit, unstable (small data change → big tree change)

---

## KMEANS CLUSTERING

### What It Does
Partitions data into K clusters minimizing within-cluster variance (unsupervised)

### Algorithm
1. **Initialize**: Randomly select K centroids from data
2. **Assign**: For each point, assign to nearest centroid (Euclidean distance)
3. **Update**: Recalculate each centroid as mean of assigned points
4. **Repeat** steps 2-3 until convergence (centroids stop moving)

### Cost Function (Inertia)
$$J = \sum_{i=1}^{K} \sum_{x \in C_i} ||x - \mu_i||^2$$
- Lower inertia = tighter clusters
- Minimized iteratively through EM algorithm

### Convergence
Guaranteed to converge (non-negative, decreases monotonically)

### Finding Optimal K
- **Elbow Method**: Plot inertia vs K, look for "elbow"
- **Silhouette Score**: $\frac{b - a}{\max(a, b)}$ where $a$ = intra-cluster, $b$ = inter-cluster distance
  - Range: [-1, 1], higher better

### Evaluation Metrics
- **Inertia**: Sum of squared distances to centroids (lower better)
- **Silhouette Score**: Measures cluster cohesion/separation (-1 to 1, higher better)

### When to Use
- Customer segmentation
- Identify data groups/patterns
- Preprocessing before supervised learning
- No labeled data available

### Limitations
- Must specify K in advance
- Sensitive to initialization (run multiple times)
- Assumes spherical clusters
- Sensitive to outliers and scaling

### Pro Tips
- Scale features first (standardization)
- Try multiple random initializations
- Use elbow method or silhouette for K selection

---

## NEURAL NETWORKS

### What It Does
Learn complex non-linear functions through multiple layers of neurons

### Architecture
```
Input Layer → Hidden Layers → Output Layer
    (4)    →    (8,4)     →    (1)
```

### Forward Propagation
For each layer $l$:
$$Z^{[l]} = W^{[l]} A^{[l-1]} + b^{[l]}$$
$$A^{[l]} = \text{activation}(Z^{[l]})$$

### Activation Functions
| Function | Formula | Use Case | Range |
|----------|---------|----------|-------|
| **ReLU** | $\max(0, z)$ | Hidden layers | [0, ∞) |
| **Sigmoid** | $\frac{1}{1+e^{-z}}$ | Binary output | [0, 1] |
| **Tanh** | $\frac{e^z - e^{-z}}{e^z + e^{-z}}$ | Hidden layers | [-1, 1] |
| **Softmax** | $\frac{e^{z_i}}{\sum e^{z_j}}$ | Multi-class output | [0, 1] |

### Cost Functions
- **Binary Cross-Entropy**: $-\frac{1}{m}\sum[y\log(a) + (1-y)\log(1-a)]$
- **Categorical Cross-Entropy**: $-\frac{1}{m}\sum y \log(a)$
- **MSE**: $\frac{1}{m}\sum(y - a)^2$

### Backpropagation
Computes gradients layer by layer (chain rule):
$$dA^{[l-1]} = W^{[l]T} dZ^{[l]}$$
$$dW^{[l]} = \frac{1}{m} dZ^{[l]} A^{[l-1]T}$$
$$db^{[l]} = \frac{1}{m} \sum dZ^{[l]}$$

Then update: $W^{[l]} := W^{[l]} - \alpha dW^{[l]}$

### Key Hyperparameters
- **Learning Rate** ($\alpha$): Controls gradient descent step size
- **Epochs**: Number of passes through training data
- **Batch Size**: Samples per gradient update
- **Hidden Layer Sizes**: Number of neurons per layer
- **L2 Lambda**: Regularization strength

### When to Use
- Complex non-linear patterns
- Large datasets
- Computer vision, NLP
- Want to learn representations

### Architecture Choices
- **Shallow (1-2 hidden)**: Simple relationships
- **Deep (3+ hidden)**: Complex hierarchical features
- **Wide (many neurons)**: More model capacity
- **Narrow (few neurons)**: Regularization effect

### Training Tips
✓ Normalize features, initialize weights properly, learning rate scheduling  
✓ Monitor training/validation loss, use early stopping  
✗ Don't train too long (overfitting), too complex (underfitting)

---

## KEY MATHEMATICAL CONCEPTS

### Gradient Descent
Update rule: $\theta := \theta - \alpha \nabla J(\theta)$
- Converges to local minimum for convex functions
- Learning rate $\alpha$ critical: too high → diverge, too low → slow

### Vectorization
Replace loops with matrix operations for speed:
```
# Slow (loop)
predictions = []
for x in X:
    predictions.append(model.predict(x))

# Fast (vectorized)
predictions = X @ w + b
```

### Feature Scaling
Makes gradient descent faster and more stable:
- **Standardization**: $x_{scaled} = \frac{x - \mu}{\sigma}$ (mean 0, std 1)
- **Normalization**: $x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$ (range [0,1])

### Regularization
Prevents overfitting by penalizing large weights:
- **L1 Regularization**: $J + \frac{\lambda}{2m}\sum|w|$ ← leads to sparse weights
- **L2 Regularization**: $J + \frac{\lambda}{2m}\sum w^2$ ← smoother weights

### Train/Test/Validation Split
- **Training**: Learn parameters (60-70%)
- **Validation**: Tune hyperparameters (10-15%)
- **Testing**: Final evaluation (15-20%)

### Confusion Matrix
```
           Predicted
           Pos  Neg
Actual Pos  TP   FN
       Neg  FP   TN
```
- **TP**: Predicted positive, actually positive (correct!)
- **FP**: Predicted positive, actually negative (false alarm)
- **TN**: Predicted negative, actually negative (correct!)
- **FN**: Predicted negative, actually positive (missed)

---

## CODE SNIPPETS SUMMARY

### Data Splitting
```python
def train_test_split(X, y, test_size=0.2, seed=42):
    np.random.seed(seed)
    idx = np.random.permutation(len(X))
    split = int(len(X) * (1 - test_size))
    return X[idx[:split]], X[idx[split:]], y[idx[:split]], y[idx[split:]]
```

### Feature Scaling
```python
mu = X.mean(axis=0)
sigma = X.std(axis=0)
X_scaled = (X - mu) / sigma
```

### Sigmoid Function
```python
def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))
```

### Gradient Descent Update
```python
# Forward
predictions = X @ w + b

# Compute gradient
gradient = X.T @ (predictions - y) / m

# Update
w = w - learning_rate * gradient
```

### Entropy (Decision Trees)
```python
def entropy(y):
    value_counts = np.bincount(y)
    probabilities = value_counts / len(y)
    return -np.sum(probabilities[probabilities > 0] * np.log2(probabilities[probabilities > 0]))
```

### Euclidean Distance (KMeans)
```python
distances = np.linalg.norm(X - centroid, axis=1)
```

---

## ALGORITHM COMPARISON TABLE

| Algorithm | Type | Output | Time | Space | Best For |
|-----------|------|--------|------|-------|----------|
| Linear Reg | Regression | Continuous | O(mn²) | O(n) | Linear relationships |
| Logistic Reg | Classification | Binary | O(mn) | O(n) | Simple boundaries |
| Decision Trees | Classification | Categorical | O(m·n·log m) | O(tree) | Non-linear, interpretability |
| KMeans | Clustering | Cluster ID | O(kmi) | O(kn) | Segmentation |
| Neural Net | Universal | Any | O(m·layers) | O(weights) | Complex patterns |

---

## TIPS FOR QUICK REVISION

1. **Memorize Core Equations**: Cost functions, gradient descent update rules
2. **Understand Activation Functions**: When to use sigmoid vs ReLU
3. **Know Metrics**: What to measure for each task
4. **Practice Math**: Matrix multiplication, derivatives, logarithms
5. **Code From Scratch**: Reinforces understanding
6. **Debug Systematically**: Visualize data, check gradients, monitor loss
7. **Hyperparameter Tuning**: Learning rate, regularization, architecture

---

**Created for Deep Learning.ai Course Revision**
