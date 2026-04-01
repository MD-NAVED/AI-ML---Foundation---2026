import numpy as np

  # print(x.shape,x.dtype) #.shape and .dtype are attributes of the numpy array. .shape gives the dimensions of the array, and .dtype gives the data type of the elements in the array.

# x = np.array([[1, 2, 3,4 ],
#               [4, 5, 6,7 ],
#               [7, 8, 9,10]])                            

# x = np.array([[1, 2, 3],
#               [4, 5, 6],])

# # print(x.shape,x.dtype)

# x.__array__(float)
# print(x.__array__((float)))


 # .ndim is an attribute of the numpy array that gives the number of dimensions of the array. In this case, since  
#  x is a 2D array (a matrix), x.ndim will return 2.

# x = np.array([[1, 2, 3,4 ],   
#               [4, 5, 6,7 ],
#               [7, 8, 9,10]])
                         
# print(x.ndim)


# .astype() is a method of the numpy array that allowas you to cast the elements of the array to a different data type. In this case, x.astype
# (float) willreturn a new array with the same shape as x but with all elements converted to the float data type.


# x = np.array([[1.2,2.5,3.8,]
#               ,[4.1,5.6,6.3]
#               ,[7.4,8.9,9.0]])
# print(x)
# print(x.dtype)
# print(x.astype(int))
 
 
 # mathamatical operations on numpay arrays are performed element-wise.This means that when you perfornm an operation on a numpay array, the operation is applied to each elements of the array individually.For example, if you add two numpay arrays togather, the result will be a new array where each elements is the sum of the corresponding elements from the original arrays.
 
 
 
# arr = np.array([10,20,30])
# print(arr + 5)
# print(arr * 2)
# print((arr / 2))
# print(arr **2)

#Agrigation functions in numpy are used to perform operation that summarize or reduse the data in an array. This functions include sum(), mean(),min(),max(),std(),and var().This function can be applied to the entire array or along a specific axis. For example,if you have a 2D array,you can use these functions to calculate the sum or mean of each row or each colum by specifying the axis parameter.


# agri_arr = np.array([10,20,30,40,50])

# print(np.sum(agri_arr))    #This will calculate the sum of all eliment in the array and return 150.
# print(np.mean(agri_arr))   #This will calculate the mean of all elements in the array and return 30.0.
# print(np.min(agri_arr))    #This will calculate the minimum value in the array and return 10.
# print(np.max(agri_arr))    #This will calculate the maximum value in the array and return 50.
# print(np.std(agri_arr))    #This will calculate the standard deviation of all elements in the array and return approximately 14.14.
# print(np.var(agri_arr))    #This will calculate the variance of all elements in the array and return approximately 200.0.



