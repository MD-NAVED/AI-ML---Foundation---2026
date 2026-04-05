# Essential NumPy Methods for Machine Learning

NumPy is the fundamental package for scientific computing in Python and forms the backbone of libraries like Pandas, Scikit-Learn, TensorFlow, and PyTorch. 

Here is a categorized list of the most important NumPy methods you will use continuously in Machine Learning.

---

## 1. Array Creation & Initialization
<!-- Creating arrays from scratch or based on existing data is the first step in any ML pipeline.

* **`np.array()`**: Converts a Python list or tuple into a NumPy array.
* **`np.zeros()` / `np.ones()`**: Creates arrays filled with 0s or 1s. *Crucial for initializing weights or creating dummy arrays.*
* **`np.empty()`**: Creates an uninitialized array (faster than zeros/ones, but contains garbage values).
* **`np.arange()`**: Returns evenly spaced values within a given interval.
* **`np.linspace()`**: Returns evenly spaced numbers over a specified interval. *Great for plotting functions or creating grid searches.*

### Random Data Generators (for weight initialization & sampling)
* **`np.random.rand()`**: Random values in a given shape spanning `[0, 1)`.
* **`np.random.randn()`**: Returns samples from the "standard normal" (Gaussian) distribution. *Highly used in neural network weight initializations.*
* **`np.random.randint()`**: Returns random integers from a specified range.
* **`np.random.seed()`**: Sets the seed for the random number generator. *Crucial for reproducibility in ML.* -->

---

## 2. Array Information & Reshaping
In ML, you will constantly transform data shapes (e.g., flattening an image into a 1D vector).

<!-- * **`arr.shape`**: Returns a tuple of array dimensions. *The most checked attribute in ML debugging!*
* **`arr.reshape()`**: Changes the shape of an array without changing its data.
* **`arr.flatten()` / `arr.ravel()`**: Converts a multi-dimensional array into a 1D array. `ravel()` is usually faster as it returns a view instead of a copy. -->
<!-- * **`arr.transpose()` or `arr.T`**: Transposes the array. *Essential for matrix multiplication.*
* **`np.expand_dims()`**: Expands the shape of an array. *Used to add a "batch" dimension.*
* **`np.squeeze()`**: Removes single-dimensional entries from the shape of an array. -->

---

## 3. Mathematical Operations & Linear Algebra
Machine learning relies heavily on matrix mathematics and aggregation.

### Matrix Operations
* **`np.dot(A, B)` or `A @ B`**: Dot product of two arrays / Matrix multiplication. *The backbone of Neural Networks and Linear Regression.*
* **`np.linalg.inv()`**: Computes the inverse of a matrix.
* **`np.linalg.norm()`**: Calculates the matrix or vector norm (L1 or L2 norms used in Regularization).
<!-- 
### Aggregation Operations (Reduction)
*Often used with the `axis` parameter (`axis=0` for columns, `axis=1` for rows).*
* **`np.sum()`**: Sum of array elements.
* **`np.mean()` / `np.median()`**: Computes the mean/median.
* **`np.std()` / `np.var()`**: Computes standard deviation and variance. *Essential for normalizing data.*
* **`np.max()` / `np.min()`**: Find the maximum or minimum value.
* **`np.argmax()` / `np.argmin()`**: Returns the **index** of the maximum / minimum value. *Crucial for finding the predicted class in Classification tasks.* -->

### Mathematical Functions
* **`np.exp()`**: Calculate the exponential of elements. *Used in Activation Functions like Softmax.*
* **`np.log()`**: Natural logarithm. *Used in Loss functions like Cross-Entropy.*
* **`np.sqrt()`**: Non-negative square-root.

---

## 4. Indexing, Slicing & Filtering
<!-- You will frequently need to filter out noise, replace missing values, or grab subsets of data.

* **Boolean Indexing (`arr[arr > 5]`)**: Selecting elements that satisfy a condition.
* **`np.where(condition, x, y)`**: Returns elements chosen from `x` or `y` depending on condition. *Used to apply thresholding.*
* **`np.clip(a, a_min, a_max)`**: Limit the values in an array. *Great for preventing exploding gradients.* -->

---

## 5. Array Manipulation
Combining multiple sets of data (like features and labels, or train and test sets).

* **`np.concatenate()`**: Joins a sequence of arrays along an existing axis.
* **`np.vstack()` / `np.row_stack()`**: Stacks arrays in sequence vertically (row wise).
* **`np.hstack()` / `np.column_stack()`**: Stacks arrays in sequence horizontally (column wise).
* **`np.split()`**: Splits an array into multiple sub-arrays. *Useful for splitting Data into Train/Validation chunks.*

---

### Machine Learning Example Snippet
```python
import numpy as np

# 1. Initialize weights and input data
W = np.random.randn(10, 5) # Shape (10, 5)
x = np.random.randn(5, 1)  # Shape (5, 1)

# 2. Matrix Multiplication
z = np.dot(W, x) # Shape (10, 1)

# 3. Activation function (e.g., Sigmoid)
a = 1 / (1 + np.exp(-z))

# 4. Find the predicted class (highest probability index)
prediction = np.argmax(a)
```

