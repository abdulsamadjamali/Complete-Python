import numpy as np
# # a is a 1D array (vector).
# a=np.array([1,2,3])
# # b is a 2D array (matrix).
# b=np.array([[1,2,3,],[4,5,6]],dtype=float)
# # c is a 3D array (tensor)
# c=np.array([[[1,2,3],[1,2,3,]],[[3,4,5,],[6,7,8,]]])
# print(a)
# print(b,"\n")
# print(c)
# print("    ")
# # 4x3 NumPy array (d) with values ranging from 1 to 12, reshaped from a 1D array.
# d=np.arange(1,13).reshape(4,3) 
# print(d)
# #  creates a 2x3 NumPy array (e) filled with ones
# e=np.ones((2,3))
# print(e)
# f=np.zeros((4,3))
# print(f)

# g=np.random.random((3,4))
# print(g)
# # np.linspace makes a list of numbers between two values, spaced equally.
# #  You decide the start, end, and how many numbers to include.
# h=np.linspace(1,10,5)
# print(h)

# i=np.identity((3))
# print(i)

# # **************************
# # its  Attributes
# # **************************
# #  we will discuss just about the 5 attributes 
# # 1> ( ndim )tells the dimensions of given array
# print(c.ndim)

# # 2> (shape) tels how many number of rows and coloumn it contain
# print(b.shape)

# # 3> (size) tells the total number of elements in the array
# print(b.size)

  
# # 4> (itemsize) in NumPy tells how many bytes each element of the array takes in memorY
# print(c.itemsize)
# print(a.itemsize)

# # 5> (dtype) tells the data type of the elements in the array
# print(a.dtype)
# print(b.dtype)
# print(c.dtype)




# # *********************************
# # Changing Data Types
# #  ********************************
# # we do this when we don't want to accupy an extra space
# # like when we want to sotre the distnace between earth to other stars than we store it in int64
# # => (astype)
# a.astype(np.int32)
# print(a) 





# # *********************************
# # Array Operations
# #  ********************************


# a2=np.arange(12,24).reshape(4,3)
# print(a2)

# # ********************************
# # two tpes of operations 
# # *********************************
# #  1 > scalar 
# #  2 > vectors 

# # 1> Scalar Operations
# # All realtional operator we can applay in scalar operation
# a1=np.arange(12).reshape(3,4)
# print(a1*5)
# print(a1>5)


# # 2> vector Operations like when we are performing operations on two arrays
# vect1=np.arange(10).reshape(2,5)
# vect2=np.arange(10).reshape(2,5)
# print(vect1+vect2)
# print(vect1*vect2)
# print(vect1**vect2)


# # *********************************
# # Array Functions
# #  ********************************

# fun=np.arange(6,12).reshape(2,3)
# print(np.min(fun))
# print(np.max(fun))
# print(np.square(fun))
# print(np.sum(fun))
# print(np.prod(fun))

# fun2=np.array([[1,5,4],[8,6,2]])
# print(np.sort(fun2))
# # Q What if i want to find minimum number of each row
# # here  (0) means coloumn and (1) means row 
# print(np.prod(fun2,axis=0)) # here it means that we are multiplying each  column
# print(np.sum(fun2,axis=1)) # here it means that we are geting some of each row



# # ****************************************************************
# # Now somthing related to statistics 
# # ****************************************************************
# # Mean , Median, mode , standerd deviation (Std )
# # stat=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# # print(np.mean("Mean is " ,stat, axis=0))
# # print(np.median("Median is ",stat))
# # print(np.std(stat))
# # print(np.mode(stat)) # it will return the most frequent number in the array
# # print(np.var(stat)) # it will return the variance of the array, which is the average squared difference from the mean.


# # *********************************
# Functions => (log,exp,dot,round,flour,cell)
# ROUND IS USED TO ROUND OFF THE NUMBER => like 3.98 will be 31 so bassically float to integer


# ceil:
# Rounds a number up to the nearest integer.
# Example: numpy.ceil(3.2) → 4.0

# round:
# Rounds a number to the nearest integer (or specified decimal places).
# Example:
# numpy.round(3.6) → 4.0
# numpy.round(3.2) → 3.0

# floor:
# Rounds a number down to the nearest integer.
# Example: numpy.floor(3.8) → 3.0

# # ****************************************************************

# # DOt Product Funtion

# in dot there must be array like (x,y)and (y,x)
# =>(3,4),(4,3)
# => dot product not possible (3,4),(3,4)

az=np.array([[1,2,3],[4,5,6,],[6,7,8]])
az2=np.arange(1,10).reshape(3,3)
print(np.dot(az,az2))

# (Log) This is how we calculate the log of each element 
print(np.log(az2))
print(np.exp(az2))
arrrrr=np.random.randint((2,9))
print("Hello => ",arrrrr)














