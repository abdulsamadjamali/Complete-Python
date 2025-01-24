import numpy as np
# Spliting is just oposite  of stacking 
# means here we break down the array 
a1=np.arange(1,13).reshape(3,4)
print(a1)
print("\n\n\n")
print(np.hsplit(a1,2))

print("\n\n\n in actuall it's a horizantal split " )
print(np.vsplit(a1,3))

