# ML-DL-CV (Andrew Ng's Specialization)

**Complete Implementation Guide** - From Machine Learning Fundamentals to Deep Learning with Real Mathematical Examples

---

## 📚 Project Overview

This repository contains **comprehensive implementations** of machine learning and deep learning algorithms following **Andrew Ng's Specialization Courses**. All code is implemented from scratch or with proper explanations, including **real-time mathematical examples with matrix calculations**.

### Two-Phase Learning Path

#### **Phase 1: Machine Learning From Scratch** 
Learn ML fundamentals with **100% from-scratch implementations** using only NumPy and Pandas.

#### **Phase 2: Deep Learning with Libraries**
Build production-ready deep learning models using TensorFlow/Keras following modern best practices.

---

## 🗂️ Repository Structure

```
ML-DL-CV/
├── README.md                    ← You are here
│
├── Machine_learning/
│   └── ML_From_Scratch/
│       ├── 01_Linear_Regression_From_Scratch.ipynb
│       ├── 02_Logistic_Regression_From_Scratch.ipynb
│       ├── 03_Decision_Trees_From_Scratch.ipynb
│       ├── 04_KMeans_Clustering_From_Scratch.ipynb
│       ├── 05_Neural_Networks_From_Scratch.ipynb
│       ├── README_IMPLEMENTATION.md
│       └── ML_ALGORITHMS_QUICK_REFERENCE.md
│
├── DeepLearning/
│   ├── 01_CNN_Convolutional_Neural_Networks.ipynb
│   ├── 02_RNN_Recurrent_Neural_Networks.ipynb
│   ├── 03_Attention_Mechanisms.ipynb
│   ├── 04_Sequence_Models.ipynb
│   ├── 05_NLP_Introduction.ipynb
│   └── README_DEEPLEARNING.md
│
└── Dataset/
    └── tested.csv (Titanic dataset)
```

---

## 🎯 Phase 1: Machine Learning From Scratch

### What You'll Learn
✅ **Linear Regression** - Predicting continuous values with gradient descent  
✅ **Logistic Regression** - Binary classification with sigmoid function  
✅ **Decision Trees** - Non-linear classification using entropy  
✅ **KMeans Clustering** - Unsupervised learning with centroids  
✅ **Neural Networks** - Multi-layer perceptrons with backpropagation  

### Quick Example: Linear Regression Cost Function

**Problem**: Predict house price from area
```
Data: 3 houses
Area:   [1000, 1500, 2000] sq ft
Price:  [$100K, $150K, $200K]

Initial guess: w = 0.05, b = 10

Step 1: Predict
f(1000) = 0.05(1000) + 10 = 60K (actual: 100K) → error: -40K
f(1500) = 0.05(1500) + 10 = 85K (actual: 150K) → error: -65K
f(2000) = 0.05(2000) + 10 = 110K (actual: 200K) → error: -90K

Step 2: Calculate Cost (MSE)
J = (1/2m) × [(-40K)² + (-65K)² + (-90K)²]
  = (1/6) × [1.6B + 4.225B + 8.1B]
  = (1/6) × 13.925B = 2.32 Billion

Huge cost! Model needs adjustment.

Step 3: Calculate Gradient
dJ/dw = (1/m) × Σ(error × area)
      = (1/3) × [(-40K)(1000) + (-65K)(1500) + (-90K)(2000)]
      = (1/3) × [-40B - 97.5B - 180B]
      = -105.83 Billion (slope is negative - increase w!)

Step 4: Update Weight (learning_rate = 0.001)
w_new = 0.05 - 0.001 × (-105.83B) = 0.05 + 105.83M = 105.88

Next iteration will predict better!
```

**Full mathematical walkthrough** available in [ML_From_Scratch/README_IMPLEMENTATION.md](Machine_learning/ML_From_Scratch/README_IMPLEMENTATION.md)

---

## 🎯 Phase 2: Deep Learning with Libraries

### What You'll Learn
✅ **CNNs** - Image classification with convolutions  
✅ **RNNs** - Sequence modeling with LSTM/GRU  
✅ **Attention Mechanisms** - Transformer architecture  
✅ **Seq2Seq** - Encoder-decoder for translation  
✅ **NLP** - Text processing to BERT fine-tuning  

### Quick Example: Convolution Operation

**Problem**: Detect edges in image
```
Image Patch (3×3):        Edge Detection Kernel:
[1  2  3]                 [-1  0  1]
[5  6  7]                 [-2  0  2]
[9 10 11]                 [-1  0  1]

Convolution = Sum of element-wise multiplication:
= 1×(-1) + 2×0 + 3×1 + 5×(-2) + 6×0 + 7×2 + 9×(-1) + 10×0 + 11×1
= -1 + 0 + 3 - 10 + 0 + 14 - 9 + 0 + 11
= 8

High value (8) detected at this location → Contains vertical edges!
```

**Full mathematical walkthrough** available in [DeepLearning/README_DEEPLEARNING.md](DeepLearning/README_DEEPLEARNING.md)

---

## 💡 Key Concepts with Real Examples

### 1. Gradient Descent - Finding the Minimum

```
Cost Function Landscape:
        Cost
          ▲
          │      ╱╲        High cost zone
          │    ╱    ╲
          │  ╱        ╲
          │╱____________╲    ← Minimum
    ──────┼──────────────────► Weights
          
With learning_rate = 0.01:
Iteration 0: w = 0.0,  Cost = 100
Iteration 1: w = 0.5,  Cost = 50   (improved 50%)
Iteration 2: w = 0.8,  Cost = 20   (improved 60%)
Iteration 3: w = 0.95, Cost = 5    (improved 75%)
Iteration 4: w = 0.99, Cost = 1.2  (converged!)
```

### 2. Activation Functions - Enabling Non-Linearity

**ReLU vs Sigmoid vs Tanh:**
```
Input x values: [-3, -1, 0, 1, 3]

ReLU(x) = max(0, x):
[-3 → 0, -1 → 0, 0 → 0, 1 → 1, 3 → 3]  ← Sparse, fast

Sigmoid(x) = 1/(1+e^(-x)):
[-3 → 0.047, -1 → 0.268, 0 → 0.5, 1 → 0.731, 3 → 0.953]  ← Probability [0,1]

Tanh(x) = (e^x - e^(-x))/(e^x + e^(-x)):
[-3 → -0.995, -1 → -0.762, 0 → 0, 1 → 0.762, 3 → 0.995]  ← Range [-1,1]
```

### 3. Backpropagation - Chain Rule Through Layers

**Forward Pass**: x → w₁ → h → w₂ → output → loss  
**Backward Pass**: loss → dw₂ → dh → dw₁  

```
Layer 1: h = w₁ × x
Layer 2: out = w₂ × h
Loss: L = (out - y)²

dL/dw₂ = dL/dout × dout/dw₂ = 2(out-y) × h  ← Gradient for w₂
dL/dw₁ = dL/dout × dout/dh × dh/dw₁ = 2(out-y) × w₂ × x  ← Chain rule!
```

---

## 🚀 Getting Started

### Prerequisites
```bash
# Core ML
pip install numpy pandas matplotlib jupyter

# Deep Learning
pip install tensorflow keras

# Optional: NLP
pip install transformers huggingface-hub
```

### Run Phase 1 (ML From Scratch)
```bash
cd Machine_learning/ML_From_Scratch
jupyter notebook 01_Linear_Regression_From_Scratch.ipynb
```

### Run Phase 2 (Deep Learning)
```bash
cd DeepLearning
jupyter notebook 01_CNN_Convolutional_Neural_Networks.ipynb
```

---

## 📊 Algorithm Comparison

| Algorithm | Task | Complexity | When to Use |
|-----------|------|-----------|-----------|
| Linear Regression | Continuous prediction | O(n²) - O(n³) | Linear relationships |
| Logistic Regression | Binary classification | O(n) | Probabilistic interpretation needed |
| Decision Trees | Classification | O(n log n) | Feature importance, non-linear |
| KMeans | Clustering | O(nk) | Unsupervised exploratory analysis |
| Neural Networks | Complex patterns | O(n×m) | Non-linear, lots of data |
| CNN | Image data | O(conv ops) | Computer vision |
| RNN | Sequences | O(seq len) | Time series, text |
| Transformer | Long sequences | O(n²) | Attention patterns needed |

---

## 🎓 Learning Resources

### Detailed Guides
- **Phase 1**: [ML_From_Scratch/README_IMPLEMENTATION.md](Machine_learning/ML_From_Scratch/README_IMPLEMENTATION.md)
  - Complete algorithm explanations
  - Real matrix calculations
  - Interview tips
  
- **Phase 2**: [DeepLearning/README_DEEPLEARNING.md](DeepLearning/README_DEEPLEARNING.md)
  - Architecture deep dives
  - Tensor operations
  - Transfer learning strategies

### Quick Reference
- [ML_ALGORITHMS_QUICK_REFERENCE.md](Machine_learning/ML_From_Scratch/ML_ALGORITHMS_QUICK_REFERENCE.md)
  - All equations on one page
  - Code snippets
  - Metric formulas

---

## 🔑 Key Takeaways

### Must Know for Interviews
1. **How does gradient descent work?** → Iterative weight updates opposite to gradient
2. **Why normalize inputs by 255?** → Scale to [0,1] for faster convergence
3. **What is backpropagation?** → Chain rule applied through layers
4. **When to use each algorithm?** → See Algorithm Comparison table above
5. **How do CNNs extract features?** → Convolution with learned filters

### Must Know for Exams
- Cost functions for each algorithm
- Update rules for gradient descent
- Activation functions and their properties
- Forward and backward pass equations
- Trade-offs between algorithms

### Production Considerations
- Feature scaling and normalization
- Train-validation-test splits
- Regularization (L1, L2, dropout)
- Learning rate scheduling
- Batch size selection
- Early stopping criteria

---

## 📈 Progress Tracking

- ✅ **Phase 1**: 5 ML algorithms, all from scratch, fully documented
- ✅ **Phase 2**: 5 DL architectures with TensorFlow, production-ready
- ✅ **Documentation**: Real examples with matrix calculations
- ✅ **Quick Reference**: All formulas and code snippets
- ✅ **Interview Tips**: Common questions and answers

---

## 🤝 Contributing

Found an issue or want to improve examples? Create an issue or pull request!

---

## 📝 License

MIT License - Feel free to use for learning and teaching

---

## 🙏 Acknowledgments

Built following **Andrew Ng's Deep Learning Specialization**
- Course 1: Neural Networks and Deep Learning
- Course 2: Improving Deep Neural Networks
- Course 3: Structuring Machine Learning Projects
- Course 4: Convolutional Neural Networks
- Course 5: Sequence Models

---

## 📞 Quick Navigation

| Want to Learn? | Go to |
|---|---|
| **Linear Regression** | [01_Linear_Regression_From_Scratch.ipynb](Machine_learning/ML_From_Scratch/01_Linear_Regression_From_Scratch.ipynb) |
| **Logistic Regression** | [02_Logistic_Regression_From_Scratch.ipynb](Machine_learning/ML_From_Scratch/02_Logistic_Regression_From_Scratch.ipynb) |
| **Decision Trees** | [03_Decision_Trees_From_Scratch.ipynb](Machine_learning/ML_From_Scratch/03_Decision_Trees_From_Scratch.ipynb) |
| **KMeans** | [04_KMeans_Clustering_From_Scratch.ipynb](Machine_learning/ML_From_Scratch/04_KMeans_Clustering_From_Scratch.ipynb) |
| **Neural Networks** | [05_Neural_Networks_From_Scratch.ipynb](Machine_learning/ML_From_Scratch/05_Neural_Networks_From_Scratch.ipynb) |
| **CNNs** | [01_CNN_Convolutional_Neural_Networks.ipynb](DeepLearning/01_CNN_Convolutional_Neural_Networks.ipynb) |
| **RNNs & LSTMs** | [02_RNN_Recurrent_Neural_Networks.ipynb](DeepLearning/02_RNN_Recurrent_Neural_Networks.ipynb) |
| **Transformers** | [03_Attention_Mechanisms.ipynb](DeepLearning/03_Attention_Mechanisms.ipynb) |
| **Seq2Seq** | [04_Sequence_Models.ipynb](DeepLearning/04_Sequence_Models.ipynb) |
| **NLP** | [05_NLP_Introduction.ipynb](DeepLearning/05_NLP_Introduction.ipynb) |
| **Quick Formulas** | [ML_ALGORITHMS_QUICK_REFERENCE.md](Machine_learning/ML_From_Scratch/ML_ALGORITHMS_QUICK_REFERENCE.md) |

---

**Ready to master ML & DL? Start with [Phase 1](Machine_learning/ML_From_Scratch/README_IMPLEMENTATION.md)!** 🚀
