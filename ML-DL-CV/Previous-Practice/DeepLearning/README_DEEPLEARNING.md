# Deep Learning Implementation Guide

Following **Andrew Ng's Deep Learning Specialization**, this folder contains comprehensive implementations of key Deep Learning concepts using **TensorFlow/Keras**.

## 📚 Notebook Structure

### 1. **CNN - Convolutional Neural Networks** ✅
- **Focus**: Image classification and feature learning
- **Key Topics**:
  - Convolution operation ($\text{Conv}(X, W) = \sum \sum X \odot W$)
  - Pooling layers (Max, Average)
  - Batch Normalization and Dropout regularization
  - Transfer Learning with ResNet50
  
- **Models Implemented**:
  - Simple CNN: 3-layer architecture with Conv2D→BatchNorm→ReLU→MaxPool
  - Transfer Learning: Pre-trained ResNet50 + custom classification head
  
- **Dataset**: CIFAR-10 (32×32 RGB images, 10 classes)
- **Augmentation**: RandomFlip, RandomRotation, RandomZoom
- **Output**: Accuracy curves and model comparison

---

### 2. **RNN - Recurrent Neural Networks** ✅
- **Focus**: Sequence modeling and temporal dependencies
- **Key Topics**:
  - RNN fundamentals: Hidden states, unrolling through time
  - Vanishing gradient problem
  - LSTM (Long Short-Term Memory): Cell state + gating mechanisms
  - GRU (Gated Recurrent Unit): Simplified variant with fewer parameters
  
- **Models Implemented**:
  - SimpleRNN: Basic recurrent architecture
  - LSTM: 2-layer stacked with dropout
  - GRU: GRU variant for comparison
  
- **Dataset**: IMDB movie reviews (binary sentiment classification)
- **Architecture**: Embedding → RNN layers → Classification head
- **Output**: Training curves and model performance metrics

---

### 3. **Attention Mechanisms & Transformers** ✅
- **Focus**: Handling long sequences and parallel processing
- **Key Topics**:
  - Scaled Dot-Product Attention: $\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
  - Multi-Head Attention: Multiple attention subspaces in parallel
  - Transformer block: Attention + Feed-Forward + Layer Norm + Residuals
  - Self-attention for capturing relationships across sequence
  
- **Components**:
  - `MultiHeadAttention` layer: 8 parallel attention heads
  - `PositionalEmbedding` layer: Encodes sequence position
  - `TransformerBlock`: Attention + FFN with residual connections
  
- **Application**: Text classification with positional encoding
- **Architecture**: Embedding → 2 Transformer blocks → Classification

---

### 4. **Sequence Models (Seq2Seq)** ✅
- **Focus**: Encoder-decoder architectures for sequence transformation
- **Key Topics**:
  - Encoder: Processes input sequence → context vector
  - Decoder: Generates output sequence using context
  - Teacher forcing: Training strategy using ground truth inputs
  - Attention mechanism: Decoder focuses on relevant input parts
  
- **Models**:
  - Full Seq2Seq with encoder-decoder architecture
  - Support for variable-length sequences
  
- **Applications**:
  - Machine Translation: Source language → Target language
  - Chatbots: Question → Answer
  - Image Captioning: Image features → Description
  - Summarization: Long text → Summary
  
- **Dataset**: Synthetic data (demonstrating architecture)
- **Training**: Teacher forcing with categorical crossentropy loss

---

### 5. **NLP Introduction** ✅
- **Focus**: Text preprocessing to pre-trained models
- **Key Topics**:
  - Tokenization: Converting text to sequences (word, subword, character)
  - Word Embeddings: Word2Vec (CBOW/SkipGram), GloVe, FastText
  - Contextual Embeddings: BERT, ELMo, GPT
  - Transfer Learning: Pre-training → Fine-tuning strategy
  
- **Components**:
  - `TextPreprocessor`: Tokenization and padding utilities
  - Custom embedding layer in classifier
  - Bi-directional LSTM for context capture
  
- **Models**:
  - Text classification with Embedding + BiLSTM layers
  - BERT fine-tuning template (commented, requires internet)
  
- **Applications & Benchmarks**:
  - Sentiment Analysis (IMDB, SST-2)
  - Named Entity Recognition (medical, news)
  - Question Answering (SQuAD)
  - Text Summarization (BART, T5)

---

## 🔧 Technical Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| TensorFlow | 2.x | Deep learning framework |
| Keras | Built-in | High-level API |
| NumPy | Latest | Numerical operations |
| Pandas | Latest | Data handling |
| Matplotlib | Latest | Visualization |
| Transformers | Optional | Pre-trained models (BERT, GPT) |

---

## 📊 Dataset Specifications

| Notebook | Dataset | Size | Task | Classes |
|----------|---------|------|------|---------|
| CNN | CIFAR-10 | 32×32 RGB | Image Classification | 10 |
| RNN | IMDB | Variable length | Sentiment Classification | 2 |
| Attention | Custom | Variable | Toy example | - |
| Seq2Seq | Synthetic | Custom | Sequence Transformation | - |
| NLP | Custom + IMDB | Sample | Text Classification | 2 |

---

## 🚀 Running the Notebooks

### Prerequisites
```bash
# Install required packages
pip install tensorflow keras numpy pandas matplotlib

# Optional: For BERT examples
pip install transformers huggingface-hub
```

### Execution
1. Open notebook in Jupyter/VS Code
2. Select Python kernel with TensorFlow installed
3. Run cells sequentially (top to bottom)
4. Adjust batch size/epochs based on your GPU memory

### GPU Acceleration
```python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))  # Check GPU availability
```

---

## � Real-Time Mathematical Examples with Matrix Calculations

### **1. CNN - Convolution Operation**

**Formula**: $(I * K)[m,n] = \sum_i \sum_j I[m+i, n+j] \cdot K[i,j]$

**Real Example with Image Patch:**
```
Input Image Patch (4×4):
I = [1  2  3  4]
    [5  6  7  8]
    [9  10 11 12]
    [13 14 15 16]

Kernel/Filter (3×3) - Edge Detection:
K = [-1  0  1]
    [-2  0  2]
    [-1  0  1]

Apply Convolution at position (0,0):
Conv[0,0] = Sum of element-wise multiplication

Extract 3×3 patch:
[1  2  3]
[5  6  7]
[9  10 11]

Multiply with kernel:
[1×(-1) + 2×0 + 3×1]   = [-1 + 0 + 3] = [2]
[5×(-2) + 6×0 + 7×2]   = [-10 + 0 + 14] = [4]
[9×(-1) + 10×0 + 11×1] = [-9 + 0 + 11] = [2]

Conv[0,0] = 2 + 4 + 2 = 8

Similarly for position (0,1):
Extract patch:
[2  3  4]
[6  7  8]
[10 11 12]

Conv[0,1] = [2×(-1) + 3×0 + 4×1] + [6×(-2) + 7×0 + 8×2] + [10×(-1) + 11×0 + 12×1]
          = [-2 + 0 + 4] + [-12 + 0 + 16] + [-10 + 0 + 12]
          = 2 + 4 + 2 = 8

Output Feature Map (2×2):
[8   8]
[8   8]

KEY INSIGHTS:
- Filters extract local patterns (edges, textures)
- Same filter applied across entire image
- Output smaller than input (depends on padding & stride)
- Multiple filters create multiple feature maps
```

---

### **2. RNN - Forward Pass Through Time**

**Formula**: $h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)$

**Real Example with Sequence Processing:**
```
Sequence Input (e.g., words mapped to embeddings):
x₀ = [0.1, 0.2]ᵀ (word 0 embedding)
x₁ = [0.3, 0.4]ᵀ (word 1 embedding)

Weights:
W_xh = [[0.5, 0.6],   (input to hidden)
        [0.7, 0.8]]

W_hh = [[0.2, 0.3],   (hidden to hidden)
        [0.4, 0.5]]

b_h = [0.1, 0.1]ᵀ

Initial hidden state: h₋₁ = [0, 0]ᵀ

======== TIME STEP t=0 ========
h₀ = tanh(W_xh × x₀ + W_hh × h₋₁ + b_h)

W_xh × x₀ = [[0.5, 0.6], [0.7, 0.8]] × [0.1, 0.2]ᵀ
           = [0.5×0.1 + 0.6×0.2, 0.7×0.1 + 0.8×0.2]ᵀ
           = [0.05 + 0.12, 0.07 + 0.16]ᵀ
           = [0.17, 0.23]ᵀ

W_hh × h₋₁ = [[0.2, 0.3], [0.4, 0.5]] × [0, 0]ᵀ = [0, 0]ᵀ

h₀ = tanh([0.17, 0.23]ᵀ + [0, 0]ᵀ + [0.1, 0.1]ᵀ)
   = tanh([0.27, 0.33]ᵀ)
   = [tanh(0.27), tanh(0.33)]ᵀ
   = [0.265, 0.318]ᵀ

======== TIME STEP t=1 ========
h₁ = tanh(W_xh × x₁ + W_hh × h₀ + b_h)

W_xh × x₁ = [[0.5, 0.6], [0.7, 0.8]] × [0.3, 0.4]ᵀ
           = [0.5×0.3 + 0.6×0.4, 0.7×0.3 + 0.8×0.4]ᵀ
           = [0.15 + 0.24, 0.21 + 0.32]ᵀ
           = [0.39, 0.53]ᵀ

W_hh × h₀ = [[0.2, 0.3], [0.4, 0.5]] × [0.265, 0.318]ᵀ
           = [0.2×0.265 + 0.3×0.318, 0.4×0.265 + 0.5×0.318]ᵀ
           = [0.053 + 0.095, 0.106 + 0.159]ᵀ
           = [0.148, 0.265]ᵀ

h₁ = tanh([0.39, 0.53]ᵀ + [0.148, 0.265]ᵀ + [0.1, 0.1]ᵀ)
   = tanh([0.638, 0.895]ᵀ)
   = [tanh(0.638), tanh(0.895)]ᵀ
   = [0.562, 0.711]ᵀ

KEY INSIGHTS:
- h₀ depends on x₀ only
- h₁ depends on x₁ AND h₀ (memory!)
- Hidden state captures information from all previous inputs
- RNN processes sequences one step at a time
- Information flows backward through time during backprop
```

---

### **3. LSTM - Gate Mechanisms**

**Formulas:**
$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
$$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
$$h_t = o_t \odot \tanh(C_t)$$

**Real Example:**
```
Input: x_t = [0.5]
Previous hidden: h_{t-1} = [0.3]
Previous cell: C_{t-1} = [0.4]

Weights (simplified 1D for clarity):
W_f = 0.6, b_f = 0.1    (forget gate)
W_i = 0.7, b_i = 0.2    (input gate)
W_c = 0.5, b_c = 0.1    (cell candidate)
W_o = 0.8, b_o = 0.15   (output gate)

Concatenate: [h_{t-1}, x_t] = [0.3, 0.5]

======== FORGET GATE ========
z_f = W_f × [0.3, 0.5] + b_f = 0.6(0.3) + 0.6(0.5) + 0.1
    = 0.18 + 0.30 + 0.1 = 0.58

f_t = σ(0.58) = 1/(1 + e^(-0.58)) ≈ 0.641

f_t ≈ 0.641: Remember ~64% of old cell state

======== INPUT GATE ========
z_i = W_i × [0.3, 0.5] + b_i = 0.7(0.3) + 0.7(0.5) + 0.2
    = 0.21 + 0.35 + 0.2 = 0.76

i_t = σ(0.76) ≈ 0.681

i_t ≈ 0.681: Accept ~68% of new information

======== CELL CANDIDATE ========
z_c = W_c × [0.3, 0.5] + b_c = 0.5(0.3) + 0.5(0.5) + 0.1
    = 0.15 + 0.25 + 0.1 = 0.5

C̃_t = tanh(0.5) ≈ 0.462

======== CELL STATE UPDATE ========
C_t = f_t ⊙ C_{t-1} + i_t ⊙ C̃_t
    = 0.641 × 0.4 + 0.681 × 0.462
    = 0.256 + 0.314
    = 0.570

Cell state updated to 0.570 (balanced between old & new info)

======== OUTPUT GATE ========
z_o = W_o × [0.3, 0.5] + b_o = 0.8(0.3) + 0.8(0.5) + 0.15
    = 0.24 + 0.40 + 0.15 = 0.79

o_t = σ(0.79) ≈ 0.688

======== HIDDEN STATE ========
h_t = o_t ⊙ tanh(C_t)
    = 0.688 × tanh(0.570)
    = 0.688 × 0.516
    = 0.355

NEW HIDDEN STATE: h_t = 0.355

KEY INSIGHTS:
- Forget gate decides what to throw away from memory
- Input gate decides what new info to keep
- Cell candidate is the new information
- Output gate decides what to output
- Gates (0-1 range) enable gradients to flow better than plain RNN
```

---

### **4. Attention Mechanism - Scaled Dot-Product**

**Formula**: $\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$

**Real Example with 2 Queries and 3 Keys:**
```
Query (Q): What we're looking for
Q = [0.1  0.2]
    [0.3  0.4]  (2 queries, dimension 2)

Keys (K): What we have
K = [0.2  0.1]
    [0.4  0.3]
    [0.1  0.2]  (3 keys, dimension 2)

Values (V): Information associated with keys
V = [1  0]
    [0  1]
    [1  1]  (3 values, dimension 2)

d_k = 2

======== STEP 1: Query × Key^T ========
QK^T = [[0.1, 0.2], [0.3, 0.4]] × [[0.2, 0.4, 0.1], [0.1, 0.3, 0.2]]

Row 1: Q[0] · K^T
  0.1×0.2 + 0.2×0.1 = 0.02 + 0.02 = 0.04
  0.1×0.4 + 0.2×0.3 = 0.04 + 0.06 = 0.10
  0.1×0.1 + 0.2×0.2 = 0.01 + 0.04 = 0.05

Row 2: Q[1] · K^T
  0.3×0.2 + 0.4×0.1 = 0.06 + 0.04 = 0.10
  0.3×0.4 + 0.4×0.3 = 0.12 + 0.12 = 0.24
  0.3×0.1 + 0.4×0.2 = 0.03 + 0.08 = 0.11

QK^T = [0.04  0.10  0.05]
       [0.10  0.24  0.11]

======== STEP 2: Scale by √d_k ========
√d_k = √2 ≈ 1.414

Scaled = [0.04/1.414  0.10/1.414  0.05/1.414]   = [0.028   0.071   0.035]
         [0.10/1.414  0.24/1.414  0.11/1.414]     [0.071   0.170   0.078]

======== STEP 3: Apply Softmax ========
For row 1: [0.028, 0.071, 0.035]
exp_values = [e^0.028, e^0.071, e^0.035] = [1.028, 1.074, 1.036]
sum = 3.138
softmax = [1.028/3.138, 1.074/3.138, 1.036/3.138] = [0.328, 0.342, 0.330]

For row 2: [0.071, 0.170, 0.078]
exp_values = [1.074, 1.186, 1.081]
sum = 3.341
softmax = [0.321, 0.355, 0.324]

Attention Weights = [0.328  0.342  0.330]
                    [0.321  0.355  0.324]

======== STEP 4: Apply to Values ========
Output = Attention Weights × V

Row 1: [0.328, 0.342, 0.330] × [[1,0], [0,1], [1,1]]
     = 0.328×[1,0] + 0.342×[0,1] + 0.330×[1,1]
     = [0.328, 0] + [0, 0.342] + [0.330, 0.330]
     = [0.658, 0.672]

Row 2: [0.321, 0.355, 0.324] × [[1,0], [0,1], [1,1]]
     = 0.321×[1,0] + 0.355×[0,1] + 0.324×[1,1]
     = [0.321, 0] + [0, 0.355] + [0.324, 0.324]
     = [0.645, 0.679]

Output = [0.658  0.672]
         [0.645  0.679]

KEY INSIGHTS:
- Attention weights show which keys are relevant for each query
- Higher weights = more attention to that position
- Softmax ensures weights sum to 1 (probability distribution)
- Scaling by √d_k prevents very small gradients
- Query 1 attends most to Key 1 & 2 (weight ~0.33 each)
- Query 2 attends more to Key 2 (weight ~0.36)
```

---

### **5. Transformer Positional Encoding**

**Formula**: 
$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$
$$PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

**Real Example with 4D Embedding:**
```
Position: pos = 0 (first word)
d_model = 4
Dimensions: i = 0, 1

======== POSITION 0 ========
For dimension i=0 (2i=0):
freq = 1 / 10000^(0/4) = 1 / 1 = 1
PE[0,0] = sin(0 × 1) = sin(0) = 0.000

For dimension i=0 (2i+1=1):
freq = 1 / 10000^(0/4) = 1
PE[0,1] = cos(0 × 1) = cos(0) = 1.000

For dimension i=1 (2i=2):
freq = 1 / 10000^(2/4) = 1 / 10000^0.5 = 1 / 100 = 0.01
PE[0,2] = sin(0 × 0.01) = sin(0) = 0.000

For dimension i=1 (2i+1=3):
freq = 1 / 10000^(2/4) = 0.01
PE[0,3] = cos(0 × 0.01) = cos(0) = 1.000

PE[0] = [0.000, 1.000, 0.000, 1.000]

======== POSITION 1 ========
For dimension i=0 (2i=0):
PE[1,0] = sin(1 × 1) = sin(1) = 0.841

For dimension i=0 (2i+1=1):
PE[1,1] = cos(1 × 1) = cos(1) = 0.540

For dimension i=1 (2i=2):
PE[1,2] = sin(1 × 0.01) = sin(0.01) = 0.010

For dimension i=1 (2i+1=3):
PE[1,3] = cos(1 × 0.01) = cos(0.01) = 1.000

PE[1] = [0.841, 0.540, 0.010, 1.000]

======== POSITION 2 ========
PE[2,0] = sin(2 × 1) = sin(2) = 0.909
PE[2,1] = cos(2 × 1) = cos(2) = -0.416
PE[2,2] = sin(2 × 0.01) = 0.020
PE[2,3] = cos(2 × 0.01) = 0.9998

PE[2] = [0.909, -0.416, 0.020, 0.9998]

Positional Encoding Matrix:
     Dim0   Dim1   Dim2   Dim3
[0:  0.000  1.000  0.000  1.000]  position 0
[1:  0.841  0.540  0.010  1.000]  position 1
[2:  0.909 -0.416  0.020  1.000]  position 2

KEY INSIGHTS:
- Different positions have unique encoding
- Each dimension oscillates at different frequencies
- High dimensions change slowly (position-agnostic features)
- Low dimensions change quickly (position-specific features)
- Encoding added to embeddings so model knows word position
```

---

✅ **CNN**: How convolutions extract features, transfer learning benefits, image augmentation

✅ **RNN**: Sequential processing, LSTM/GRU gating mechanisms, sentiment analysis

✅ **Attention**: Query-Key-Value mechanism, multi-head attention, transformer architecture

✅ **Seq2Seq**: Encoder-decoder pattern, teacher forcing, machine translation

✅ **NLP**: Tokenization, embeddings, BERT architecture, fine-tuning strategies

---

## 📚 Key Mathematical Formulas

### Convolution
$$\text{Conv2D}(x, w) = \sum_{i,j} x[i,j] \cdot w[i,j] + b$$

### LSTM Cell
$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$ (Forget gate)
$$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$ (Input gate)
$$\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$$ (Cell candidate)
$$C_t = f_t * C_{t-1} + i_t * \tilde{C}_t$$ (Cell state update)

### Scaled Dot-Product Attention
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

### Transformer Feed-Forward
$$\text{FFN}(x) = \text{ReLU}(xW_1 + b_1)W_2 + b_2$$

---

## 💡 Interview Tips

1. **CNN Architecture**: Explain why convolution reduces parameters vs fully connected
2. **LSTM vs GRU**: Discuss trade-offs (performance vs complexity)
3. **Attention Mechanism**: Why is scaling factor $\sqrt{d_k}$ important?
4. **Seq2Seq Limitations**: Discuss information bottleneck without attention
5. **Transfer Learning**: When to freeze/unfreeze pre-trained layers

---

## 🔗 Further Resources

- [Andrew Ng's Deep Learning Specialization](https://www.deeplearning.ai)
- [Transformers Documentation](https://huggingface.co/transformers/)
- [TensorFlow/Keras Guide](https://www.tensorflow.org/guide)
- [BERT Paper](https://arxiv.org/abs/1810.04805)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

---

## 📝 Notes

- All notebooks use Keras functional/sequential API
- Batch sizes and epochs reduced for faster demo execution
- Real training requires more data and longer training
- GPU recommended for faster convergence

**Created**: Following Andrew Ng's Deep Learning Course
**Purpose**: Comprehensive learning guide with practical implementations
