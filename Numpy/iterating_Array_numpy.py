import numpy as np
a1=([1,2,3,4,5,6,7,8,9,10,])

a2=([[1,2,3,4],
     [5,6,7,8]])

a3=([[[1,2,3,4]
      ,[5,6,7,8]]
     ,[[9,10,11,12]
       ,[13,14,15,16]]])

# for i in a2:
#     print(i)
# for i in np.nditer(a2):
#     print(i)
# (nditer) even 100D array it in to one and then iterate
for j in np.nditer(a3):
    print(j)
