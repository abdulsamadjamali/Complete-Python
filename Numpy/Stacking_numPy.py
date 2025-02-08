import numpy as np
# Stacking means joining two or more arrays along a new axis 
# (dimension). It can be done vertically (row-wise) or horizontally (column-wise).
# Combining Data from Multiple Sources
# usecase ===>>> When you have data from different sources (like different
# sensors or files), stacking helps to organize them into a single dataset for analysis

# ==>>(note) there must be same numb of row and column

a1=np.arange(1,13).reshape(4,3)
a2=np.arange(12,24).reshape(4,3)
print(a1)
print(a2)
print(np.hstack((a1,a2,a1,a2)))
print(np.vstack((a1,a2,a1,a2)))


