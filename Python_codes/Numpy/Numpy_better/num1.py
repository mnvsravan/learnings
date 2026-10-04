# 3D array 
import numpy as np
a= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a)

# We can use our own datatype
b= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],dtype=float) # You can use COMPLEX,BOOL, INT, FLOAT, STRING, etc. as the datatype for the array. By specifying dtype=float, we are telling NumPy to create an array of floating-point numbers. This means that all the elements in the array will be stored as floats, even if they are originally integers. For example, the integer 1 will be stored as 1.0 in the array.
print(b)

#We can use arrange , the syntax is np.arange(start, stop, step) , this creates an array
c= np.arange(0, 10, 2) 
print(c)  # Like the starting and ending values in the range function, the start value is inclusive, while the stop value is exclusive. This means that the generated array will include the start value but will not include the stop value. In this case, the generated array will include 0, 2, 4, 6, and 8, but it will not include 10. The step value of 2 indicates that we want to generate numbers with a step of 2 between them. Therefore, the resulting array will contain every second number starting from 0 up to (but not including) 10.

#reshape
d= np.arange(1, 13).reshape(2, 6,1) # This creates a 3D array with 2 layers, 6 rows, and 1 column. 
print(d) # Rember u can reshape array such that the product of the dimensions equals the total number of elements 

#np zeroes and ones
e= np.zeros((2, 3)) # This function creates a 2D array of shape (2, 3) filled with zeros. 
print(e)  
f= np.ones((3, 4)) 
print(f)  # This function creates a 2D array of shape (3, 4) filled with ones.

#Their syntax is np.zeros(shape, dtype=float, order='C') and order means whether the array should be stored in row-major (C-style) or column-major (Fortran-style) order in memory

# random
#syntax is np.random.default_rng(seed=None) and np.random.uniform(low=0.0, high=1.0, size=None) and np.random.choice(a, size=None, replace=True, p=None) and np.random.shuffle(x) also np.random.random(size=None) generates random floats in the half-open interval [0.0, 1.0). The size parameter specifies the shape of the output array. If size is None (the default), a single float is returned. If size is an integer, a 1D array of that length is returned. If size is a tuple, an array of that shape is returned. For example, np.random.random(size=(2, 3)) would generate a 2D array with 2 rows and 3 columns filled with random floats between 0 and 1.
 
ran=np.random.random(size=(2, 3)) # this only creates shape we we can use our own random numbers
print(ran)
ran1= np.random.uniform(0, 5, size=(2, 3)) 
print(ran1) 
ran2= np.random.choice([1, 2, 3, 4, 5], size=(2, 3), replace=True) # it replaces the values in the array with the values in the list [1, 2, 3, 4, 5] randomly
print(ran2)
np.random.shuffle(ran2) # this shuffles the values in the array
print(ran2) 


#Linespace and Identity
lin= np.linspace(-10, 10, num=10) # lowest, highest, number of points , all the points are equally spaced 
print(lin)  
iden= np.eye(4) 
print(iden)  


# ATTRIBUTES ndim, shape, size,itemsize
a=np.arange(1, 13).reshape(2,2,3)
print(a)
print(a.ndim) 
print(a.shape)
print(a.size)
print(a.itemsize) # all items in the array are of the same type

# To change space we use astype
# Like to reduce or increase the itemsize
Eg=np.arange(1, 13).reshape(2, 2, 3).astype(np.int32) 
print(Eg)

# Operations 
a=np.random.uniform(0,12, (2, 2, 3))
print(a)
print(a+2) # this adds 2 to each element in the array , similarly we can do subtraction, multiplication, division, etc. with a scalar value
print(a>5) # We can do relational operations like greater than, less than, equal to, etc. with a scalar value. This will return a boolean array
b=np.random.uniform(0, 12, (2, 2, 3))
print(a+b) # These are vector operations, we can do addition, subtraction, multiplication, division, etc. 
print(a>b) # We can do relational operations like greater than, less than, equal to, etc
