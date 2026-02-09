import numpy as np

#1. Arithmetic operators
#Arithmetic operators: multiplying two array means each pair of elements will be multiplied
a = np.ones(shape=(10,4))
#following multiplies each row by its index
for i, row in enumerate(a):
            a[i,:]=i*row
print(a)

#.dot() --> matrix multiplication based on linear algebra
def powerA(n):
    A = np.array([[1, -1],
                  [-1, 1]])
    A_n = np.array([[1, 0],
                  [0, 1]])
    for i in range(n):
        A_n = A_n.dot(A)
        
    return A_n

print("A**2: \n", powerA(2), "\n")

def normalisation_min_max(X):
    # Create a copy of X to avoid modifying the original data
    X_tilde = np.zeros_like(X, dtype=float)
    
    # Compute for each column
    for j in range(X.shape[1]):
        min_Xj = np.min(X[:, j])  # Minimum value of the column
        max_Xj = np.max(X[:, j])  # Maximum value of the column
        
        # Handle cases where min == max to avoid division by zero
        if max_Xj - min_Xj == 0:
            X_tilde[:, j] = 0  # Set all values to zero if all elements are identical
        else:
            X_tilde[:, j] = (X[:, j] - min_Xj) / (max_Xj - min_Xj)
    
    return X_tilde

# Example usage
X = np.array([[24, 1.88],
              [18, 1.68],
              [14, 1.65]])

X_tilde = normalisation_min_max(X)

print(X_tilde)