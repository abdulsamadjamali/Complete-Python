import numpy as np

# Indexing: Access one specific element.
# Slicing: Access multiple elements or range

# arr1=np.arange(1,13).reshape(3,4)
# print(arr1[1,0])

# Now getting element from tancer (3D array)
# arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr2)
# # first we have 2 2D matrics here first (1) is for 2nd 2D matric which is [7,8,9],[10,11,12] now same here secound (0) 
# # is to chose row  and (2)for   coloummn
# print(arr2[1,0,2])

# ********************************
# Now sliceing 
# ********************************
# arr3=np.array([1,2,3,4,5,6,7,8])
# print(arr3[1:5]) 
# 2D matrix
arr4=np.array([[1,2,3,4], 
               [4,5,6,7], 
               [8,9,10,11]])
# print(arr4[::2,0::2])
# print(arr4[1:,0::2]) 
# print(arr4[0:,1:])
# print(arr4[1,0::3])
print(arr4[0:2,1:])

# print(arr4[:,1])