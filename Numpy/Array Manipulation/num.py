#  Array Manipulation:-

# Combining multiple sets of data (like features and labels, or train and test sets).

# * **`np.concatenate()`**: Joins a sequence of arrays along an existing axis.
# * **`np.vstack()` / `np.row_stack()`**: Stacks arrays in sequence vertically (row wise).
# * **`np.hstack()` / `np.column_stack()`**: Stacks arrays in sequence horizontally (column wise).
# * **`np.split()`**: Splits an array into multiple sub-arrays. *Useful for splitting Data into Train/Validation chunks.*

import numpy as np



# array1 = np.array([1,2,3,4,5])
# array2 = np.array([6,7,8,9,10])

# print(np.concatenate((array1,array2)))# Joins the arrays

# print(np.vstack((array1,array2)))# Stacks the arrays vertically

# print(np.hstack((array1,array2)))# Stacks the arrays horizontally

# print(np.split(array1,[2])) # Splits the array into multiple sub-arrays

