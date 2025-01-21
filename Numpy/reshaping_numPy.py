# Reshaping 
import numpy as np
a1=[[1,2,3,4],
    [5,6,7,8]]
print(np.transpose(a1))

#=>>>>(Ravel) it converts (nD) array to a (1D) array 

a3=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

print("Here 3D array converted into 1D",a3.ravel())