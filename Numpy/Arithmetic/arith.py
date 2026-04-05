import array
import numpy as np


# Scaler Arithmetic:- 
#  performing arithmetic operations on a scalar and an array.

# arr = np.array([1,2,3,4,5])


# # Array Arithmetic:- 
# #  performing arithmetic operations on two arrays.

# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([6,7,8,9,10])

# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)
# print(arr1 % arr2)
# print(arr1 ** arr2)

# Comparison arithmetic:- 
#  performing comparison operations on two arrays.

# array = np.array([1,2,3,4,5])
# array2 = np.array([6,7,8,9,10])

# print(array == array2)
# print(array != array2)
# print(array > array2)
# print(array < array2)
# print(array >= array2)
# print(array <= array2)


# print(np.sum(array))
# print(np.min(array))
# print(np.max(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))

#Brodcasting mean:- 
#  performing arithmetic operations on two arrays of different shapes. 

# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])


# arr2 = np.array([[1,2],[4,5],[7,8]])

# print(arr.shape)
# print(arr2.shape)
# print(arr * arr2)   


# arr = np.array([[1,2,3,4,5,6,7,8,9,10]])
# arr1 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

# print(arr.shape)
# print(arr1.shape)
# print(arr * arr1)   


# Aggregate Functions:- 
#  performing arithmetic operations on two arrays.And return a single value.


# arr = np.array([[1,2,3,4,5],
#                 [6,7,8,9,10]])


# print(np.sum(arr))
# print(np.min(arr))
# print(np.max(arr))
# print(np.mean(arr))
# print(np.std(arr))
# print(np.var(arr))


# print(np.sum(arr, axis=0)) # column wise
# print(np.sum(arr, axis=1)) # row wise


# print(np.min(arr, axis=0)) # column wise
# print(np.min(arr, axis=1)) # row wise

# print(np.max(arr, axis=0)) # column wise
# print(np.max(arr, axis=1)) # row wise

# print(np.mean(arr, axis=0)) # column wise
# print(np.mean(arr, axis=1)) # row wise

# print(np.std(arr, axis=0)) # column wise
# print(np.std(arr, axis=1)) # row wise

# print(np.var(arr, axis=0)) # column wise

 