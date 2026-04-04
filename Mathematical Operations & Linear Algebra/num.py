#  MATHODS :-

# * **`np.dot(A, B)` or `A @ B`**: Dot product of two arrays / Matrix multiplication. *The backbone of Neural Networks and Linear Regression.*
# * **`np.linalg.inv()`**: Computes the inverse of a matrix.
# * **`np.linalg.norm()`**: Calculates the matrix or vector norm (L1 or L2 norms used in Regularization).


import numpy as np

array_a = np.array([[1,2],
                    [3,4]])
array_b = np.array([[4,1],
                    [2,3]])

print(array_a @ array_b)
