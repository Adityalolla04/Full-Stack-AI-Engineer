import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

freqs = {("happi", 1): 20, ("glad", 1): 15, ("sad", 0): 18, ("bad", 0): 25}

def extract_features(tweet, freqs):
    x = np.zeros((1, 3))
    for word in tweet.split():
        x[0, 0] += freqs.get((word, 1), 0)
        x[0, 1] += freqs.get((word, 0), 0)
    return x

#test
tweet = "happi glad bad"
x = extract_features(tweet, freqs)
theta = np.array([[0.1, 0.5, -0.4]])
pred = sigmoid(np.dot(x, theta.T))

print(f"Predicted probability of positive sentiment: {pred[0][0]:.4f}")