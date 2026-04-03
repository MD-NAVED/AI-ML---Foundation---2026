import numpy as np


# Filltiring :-

# arr = np.array([[12,23,32,45,56,67,78,27,38,45],
#                 [11,12,64,14,15,36,17,74,19,20]])



# # teenagers = arr[arr >= 13]
# # adults = arr[arr>=25]
# # senior = arr[arr>=60]
# # even = arr[arr % 2 == 0]
# # odd = arr[arr % 2 != 0]

# adults = np.where(arr>=25, arr, 0)
# print(adults)

# First_que = arr[arr >= 50]
# print(First_que)


# second_que = arr[arr == 45]
# print(second_que)

# third_que = arr[(arr > 20) &  (arr < 40 )]
# print(third_que)

# forth_que = arr[arr % 3 == 0]
# print(forth_que)

# fifth_que = np.where(arr % 2 == 0, arr ,-1 )
# print(fifth_que)

# sixth_que = np.where(arr < 50 ,arr, 50)
# print(sixth_que)

#Filltring refers to selecting specific elements from an array based on a condition.

