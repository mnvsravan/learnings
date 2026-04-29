import numpy as np
print(np.__version__)  # Check the version of numpy

my_list=np.array([1,2,3,4,5])  # Create a numpy array from a list
my_list=my_list*2
print(my_list)  # Output: [ 2  4  6  8 10]

print(type(my_list))  # Output: <class 'numpy.ndarray'>, this shows that my_list is now a numpy array

# ndarray is a multi-dimensional array object in numpy, it can be 1D, 2D, 3D or more dimensions. It is a powerful data structure that allows for efficient storage and manipulation of large datasets. The ndarray object provides a wide range of functions and methods for performing operations on the data, such as mathematical operations, slicing, indexing, and more.

my_list_zero=np.array('A')
print(my_list_zero)  # Output: A this is array with 0 dimensions, it is a scalar value wrapped in an array. It can be useful for certain operations where you want to treat a single value as an array, but it does not have the same properties as a 1D or higher-dimensional array.
print(my_list_zero.ndim)  # Output: 0, this shows that my_list_zero is a 0-dimensional array
print(my_list_zero.shape)  # Output: (), this shows that my_list_zero has an empty shape, which is typical for a 0-dimensional array
print(my_list_zero.size)  # Output: 1, this shows that my_list_zero has a size of 1, which means it contains one element (the scalar value 'A')

my_list_one=np.array([1,2,3,4,5])
print(my_list_one)  # Output: [1 2 3 4 5], this is a 1-dimensional array, it is a simple array of values.
print(my_list_one.ndim)  # Output: 1, this shows that my_list_one is a 1-dimensional array
print(my_list_one.shape)  # Output: (5,), this shows that my_list_one has a shape of (5,), which means it has 5 elements in one dimension
print(my_list_one.size)  # Output: 5, this shows that my_list_one has a size of 5, which means it contains 5 elements

my_list_two=np.array([[1,2,3],[4,5,6],[7,8,9],
                      [3,4,5],[8,9,0],[0,1,2]])  # this is a 2-dimensional array, it is a matrix of values.
print(my_list_two)  # Output: [[1 2 3] [4 5 6] [7 8 9] [3 4 5] [8 9 0] [0 1 2]], this is a 2-dimensional array, it is a matrix of values.
print(my_list_two.ndim)  # Output: 2, this shows that my_list_two is a 2-dimensional array
print(my_list_two.shape)  # Output: (6, 3), this shows that my_list_two has a shape of (6, 3), which means it has 6 rows and 3 columns
print(my_list_two.size)  # Output: 18, this shows that my_list_two has a size of 18, which means it contains 18 elements (6 rows * 3 columns)

# WE MUST HAVE SAME NUMBER OF ELEMENTS IN EACH ROW TO CREATE A 2D ARRAY,
# OTHERWISE NumPy will raise a ValueError
try:
    my_list_two_wrong=np.array([[1,2,3],[4,5],[7,8,9],
                          [3,4,5],[8,9,0],[0,1,2]]) 
    print(my_list_two_wrong)
except ValueError as e:
    print(e)  # ValueError: setting an array element with a sequence

# we can access index by [][][] depending on the number of dimensions of the array, for example:

my_index=np.array([[[1,2,3],[4,5,6],[7,8,9], [3,4,5],[8,9,0],[0,1,2]],
                   [[1,2,3],[4,5,6],[7,8,9],[3,4,5],[8,9,0],[0,1,2]]])  # this is a 3-dimensional array 
print(my_index)  # Output: [[[1 2 3] [4 5 6] [7 8 9] [3 4 5] [8 9 0] [0 1 2]] [[1 2 3] [4 5 6] [7 8 9] [3 4 5] [8 9 0] [0 1 2]]], this is a 3-dimensional array.
print(my_index.ndim)  # Output: 3, this shows that my_index is a 3-dimensional array
print(my_index.shape)  # Output: (2, 6, 3), this shows that my_index has a shape of (2, 6, 3), which means it has 2 blocks, each block has 6 rows and 3 columns
print(my_index.size)  # Output: 36, this shows that my_index has a size of 36, which means it contains 36 elements (2 blocks * 6 rows * 3 columns)
print(my_index[1,2,2])  # Output: 9, this shows that we can access the element at index [1][2][2] in the my_index array, which is the value 9. The first index [1] selects the second block, the second index [2] selects the third row within that block, and the third index [2] selects the third element within that row.

# Block is like u see those [[1,2,3],[4,5,6],[7,8,9],
#                    [3,4,5],[8,9,0],[0,1,2]] is a block, and there are 2 blocks in the my_index array. Each block has 6 rows and 3 columns.


#Say:
word=my_index[0,0,0]  
word1=my_index[1,1,1] 
word2=my_index[0,5,2]  
print(word+word1+word2)  # Output: 6, this shows that we can add the values at index [0][0][0] and [1][1][1] in the my_index array, which are 1 and 5 respectively, resulting in 6.