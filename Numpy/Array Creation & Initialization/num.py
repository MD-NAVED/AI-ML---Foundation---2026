# MATHODS :-    

# 1. Array Creation & Initialization
# Creating arrays from scratch or based on existing data is the first step in any ML pipeline.

# * **`np.array()`**: Converts a Python list or tuple into a NumPy array.
# * **`np.zeros()` / `np.ones()`**: Creates arrays filled with 0s or 1s. *Crucial for initializing weights or creating dummy arrays.*
# * **`np.empty()`**: Creates an uninitialized array (faster than zeros/ones, but contains garbage values).
# * **`np.arange()`**: Returns evenly spaced values within a given interval.
# * **`np.linspace()`**: Returns evenly spaced numbers over a specified interval. *Great for plotting functions or creating grid searches.*

### Random Data Generators (for weight initialization & sampling)
# * **`np.random.rand()`**: Random values in a given shape spanning `[0, 1)`.
# * **`np.random.randn()`**: Returns samples from the "standard normal" (Gaussian) distribution. *Highly used in neural network weight initializations.*
# * **`np.random.randint()`**: Returns random integers from a specified range.
# * **`np.random.seed()`**: Sets the seed for the random number generator. *Crucial for reproducibility in ML.*

import numpy as np

# print(np.zeros((4,4),dtype=int))

# print(np.ones((4,4),dtype=int))

# print(np.empty((2,3)))

# print(np.arange(10))

# print(np.linspace(0,10,5))

# print(np.random.rand(4,4))

# print(np.random.randn(2,1)) 

# print(np.random.seed(12))

