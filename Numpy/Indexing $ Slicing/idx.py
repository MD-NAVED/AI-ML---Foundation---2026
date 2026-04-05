import numpy as np

# Indexing $ Slicing in arrays


# array_3d = np.array([
#     [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9, 10, 11, 12]
#     ],
#     [
#         [13, 14, 15, 16],
#         [17, 18, 19, 20],
#         [21, 22, 23, 24]
#     ]
# ])


# print(array_3d[1,2,2])

# arr = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12]])
# # print(arr[1,])

# print(arr[-0,-0])



# matrix = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ])


        # Practice qustions:-


# print(matrix[1,1])

# print(matrix[-1,-1]) # This is negative indexing

# print(matrix[1]) #Extracting the entire second row

# print(matrix[:,2]) #Extracting the entire third column

# print(matrix[0:2, 2:4]) # Extracting the first two rows and the last two columns

# print(matrix[0 ,::2]) # Extracting the first row and every second column


# import numpy as np

# cube = np.array([
#     [[1, 2, 3],
#      [4, 5, 6]],      
#     [[7, 8, 9],
#      [10, 11, 12]]
# ])

# print(cube[1,0,1]) # Extracting the element at the second depth, first row, and second column


# print(cube[0,:,:]) # Extracting the first depth

# print(cube[1, 1, :]) # Extracting the last row of the second depth

# print(cube[0,:,0],cube[1,:,0])# Extracting the first column of each depth

# print(cube[:,:,0]) # 