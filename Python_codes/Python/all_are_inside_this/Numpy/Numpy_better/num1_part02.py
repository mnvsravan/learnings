#Array functions 
import numpy as np
array=np.random.random((2, 3))*100 # this creates a 2D array of shape (2, 3) filled with random floats between 0 and 100
# SUM,PDT,MIN,MAX,MEAN,MEDIAN,STD,VAR
print(array)
# We can use axis for these operations, axis=0 means we are performing the operation along the columns and axis=1 means we are performing the operation along the rows. 
#Syntax is np.sum(array, axis=0) and np.sum(array, axis=1) and similarly for other operations
print("Sum:", np.sum(array))
print("Product:", np.prod(array))
print("Minimum:", np.min(array))
print("Maximum:", np.max(array))
print("Mean:", np.mean(array))
print("Median:", np.median(array))
print("Standard Deviation:", np.std(array))
print("Variance:", np.var(array))

#TRIGONOMETRIC FUNCTIONS, LOGARITHMIC FUNCTIONS, EXPONENTIAL FUNCTIONS
#Syntax is np.sin(array) and np.cos(array) and np.tan(array) and np.log(array) and np.exp(array)
print("Sine:", np.sin(array))
print("Cosine:", np.cos(array))
print("Tangent:", np.log(array))
print("Logarithm:", np.exp(array))
# We can use axis for these operations as well

#Round, floor, ceil
#Syntax is np.round(array, decimals=0) and np.floor(array) and np.ceil(array)
print("Rounded:", np.round(array, decimals=2)) # this rounds the values in the array to 2 decimal places
print("Floor:", np.floor(array)) # this rounds the values in the array down to the nearest integer
print("Ceil:", np.ceil(array)) # this rounds the values in the array up to the nearest integer
# We can use axis for these operations as well

#Indexing YOU ALREADY KNOW , 1D IS SAME AS LIST , 2D IS SAME AS MATRIX , 3D IS SAME AS TENSOR LIKE THIS (BLOCK,ROW,COL)
#SLICING
#1D same as list
a=np.arange(10)
print(a)
print(a[2:8]) 
print(a[:5])
print(a[5:])
print(a[::2]) 
print(a[::-1])


arr = np.array([
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
])
print(arr[0,:1]) # this gives 0
print(arr[:1,0]) # this gives 0
print(arr[1:,2:]) # this gives 6 7 10 11
print(arr[::2,::3]) # this gives 0 3 8 11
print(arr[1:,1::2]) # this gives 5 7 9 11
print(arr[1::-1,1::-1]) # this gives 5 4 1 0
print(arr[1::,1::-1]) # this gives 5 4 9 8
print(arr[1,1:3:2]) # this gives 5 


blah = np.array([
    [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]],

    [[9, 10, 11],
     [12, 13, 14],
     [15, 16, 17]],

    [[18, 19, 20],
     [21, 22, 23],
     [24, 25, 26]]
])

print(blah[1]) # Like this we can select block
print(blah[0::2,0,0::2]) # this gives 1 3 

#ITERATION
i1= np.array([1, 2, 3, 4, 5])
for i in i1:
    print(i) # this iterates through the elements in the array
i2= np.array([[1, 2, 3], [4, 5, 6]])
for i in i2:
    print(i) # this iterates through the rows in the array
i3= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for i in i3:
    print(i) # this iterates through the blocks in the array
for i in np.nditer(i3):
    print(i) # this iterates through all the elements in the array regardless of the number of dimensions , it converts into 1d


# Transpose
t= np.array([[1, 2, 3], [4, 5, 6]])
print(t.T) # this transposes the array, it converts rows into columns and columns into rows

#ravel
r= np.array([[1, 2, 3], [4, 5, 6]])
print(r.ravel()) # this converts the array into a 1D array

#Stacking , Vertical and Horizontal
a= np.array([[1, 2, 3], [4, 5, 6]])
b= np.array([[7, 8, 9], [10, 11, 12]])
print(np.vstack((a, b))) # this stacks the arrays vertically, it adds the rows of the second array to the first array
print(np.vstack((a, b,a,b,a))) # we can do how mnay times we want to stack the arrays
print(np.hstack((a, b))) # this stacks the arrays horizontally, it adds the columns of the second array to the first array

#Splitting , vertical and Horizontal
a= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(np.vsplit(a, 2)) # this splits the array vertically into 2 equal parts
print(np.hsplit(a, 3)) # this splits the array horizontally into 3 equal parts

