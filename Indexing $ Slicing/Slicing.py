import numpy as np

# arr = np.array([0,1,2,3,4,5,6,7,8,9])

# print(arr[2:8:])

# print(arr[0::2])

# print(arr[::-1])



         # Positive Slicing:-



# arr = np.array( [[ 0 , 1 , 2 , 3 , 4],
#                  [ 5 , 6,  7 , 8,  9],
#                  [10, 11 ,12 ,13, 14],
#                  [15 ,16, 17, 18, 19],
#                  [20, 21, 22, 23, 24]])

# print(arr[0:2:4],arr[1:3:5],) # This is 3d slicing
# print(arr[:,0:2]) # This is 2d slicing
# print(arr[0:2]) # This is 1d slicing

# print(arr[:,3:]) # This is 2d slicing

# print(arr[1:4 , 1: 4]) # 3x3 sub-array slicing

# print(arr[:4 , 4:]) # extrecing last column 4 elements


# arr = np.array([[[1,2,3,4],
#                  [5,6,7,8],
#                  [9,10,11,12]],

#                 [[13,14,15,16],    
#                  [17,18,19,20],
#                  [21,22,23,24]]])

# print(arr[0:1:]) # Extract the entire first 2D array 


# print(arr[1:2, 2:3]) #From the second 2D array, extract only the last row.

# print(arr[:,:,1:2: ]) # Extract the second column from all 2D arrays

# print(arr[0:2 , 2:2],[1:])

# print(arr[0:1, :2, :2]) # Extract the first 2x2 sub-array from the first 2D array
# print(arr[1:, :2, :2]) # Extract the first 2x2 sub-array from the second 2D array



        #Negative Slicing:-

# arr = np.array([0,1,2,3,4,5,6,7,8,9]) # 1D array

# print(arr[-1:-4:-1]) #Extract the last 3 elements using negative indexing.

# print(arr[-2:-6:-1]) #Extract the last 3 elements using negative indexing.


# arr = np.array( [[ 0 , 1 , 2 , 3 , 4], #2D array
#                  [ 5 , 6,  7 , 8,  9],
#                  [10, 11 ,12 ,13, 14],
#                  [15 ,16, 17, 18, 19],
#                  [20, 21, 22, 23, 24]])


# print(arr[-1:2:-1 , -1:2:-1]) #Extract the 2x2 grid from the bottom-right corner.

# print(arr[-2:-3:-1 ,::-1]) # Extract the second-to-last row, but reverse the order of its elements.

# print(arr[1:-1, 1:-1]) # Extract the inner 3x3 grid (excluding the border rows and columns).

# arr = np.array([[[1,2,3,4],
#                  [5,6,7,8],
#                  [9,10,11,12]],

#                 [[13,14,15,16],    
#                  [17,18,19,20],
#                  [21,22,23,24]]])

                 
# print(arr[0,:,-2:-1])

# print(arr[::-1 , ::-1])