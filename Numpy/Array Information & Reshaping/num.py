# MATHODS:- 

# In ML, you will constantly transform data shapes (e.g., flattening an image into a 1D vector).

# <!-- * **`arr.shape`**: Returns a tuple of array dimensions. *The most checked attribute in ML debugging!*
# * **`arr.reshape()`**: Changes the shape of an array without changing its data.
# * **`arr.flatten()` / `arr.ravel()`**: Converts a multi-dimensional array into a 1D array. `ravel()` is usually faster as it returns a view instead of a copy. -->
# * **`arr.transpose()` or `arr.T`**: Transposes the array. *Essential for matrix multiplication.*
# * **`np.expand_dims()`**: Expands the shape of an array. *Used to add a "batch" dimension.*
# * **`np.squeeze()`**: Removes single-dimensional entries from the shape of an array.


# import numpy as np
# array = np.array([[1,2,3]
#                  ,[4,5,6]
#                  ,[7,8,9]])

# print(array.shape) 

# print(array.reshape(1,9))

# print(array.flatten())

# print(array.ravel())

# print(array.T)

# print(np.expand_dims(array, axis=0))

# print(np.expand_dims(array, axis=1))

# print(np.squeeze(array))













