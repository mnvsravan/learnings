# Broadcasting in Numpy is a powerful mechanism that allows operations to be performed on arrays of different shapes and sizes without the need for explicit loops. It enables element-wise operations to be applied to arrays of different dimensions, making code more concise and efficient.
# The basic idea behind broadcasting is that when performing an operation on two arrays, Numpy will automatically "broadcast" the smaller array across the larger array so that they have compatible shapes. This allows for operations to be performed on arrays of different sizes without the need for explicit loops or manual replication of data.
# For example, if we have a 1D array of shape (3,) and a 2D array of shape (3, 4), we can add them together using broadcasting. The 1D array will be automatically broadcasted to match the shape of the 2D array, allowing for element-wise addition to be performed.
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9], [10, 11, 12]])
result = a + b
print(result)  # Output: [[ 5  7  9] [ 8 10 12] [11 13 15]], this shows that the 1D array a has been broadcasted to match the shape of the 2D array b, allowing for element-wise addition to be performed. Each element of the resulting array is the sum of the corresponding elements from arrays a and b.
 
# Rules of broadcasting:
# 1. If the arrays have different numbers of dimensions, the shape of the smaller array is padded with ones on its leading (left) side until both shapes have the same number of dimensions.
# 2. If the shape of the arrays does not match in any dimension, the array with a shape of 1 in that dimension is stretched to match the other shape.
# 3. If the shapes of the arrays do not match and neither has a shape of 1 in any dimension, an error is raised.

# Like in multiplication if the shape of the arrays does not match and neither has a shape of 1 in any dimension, an error is raised. For example:
try:
    c = np.array([1, 2, 3])
    d = np.array([[4, 5], [6, 7]])
    print(c.shape)  # Output: (3,), this shows that array c has a shape of (3,)
    print(d.shape)  # Output: (2, 2), this shows that array d has a shape of (2, 2)
    result = c * d  # This will raise an error because the shapes of c and d are not compatible for broadcasting
    print(result)
except ValueError as e:
    print(e)  # Output: operands could not be broadcast together with shapes (3,) (2,2), this error message indicates that the shapes of arrays c and d are not compatible for broadcasting, and therefore the multiplication operation cannot be performed.

try:
    e = np.array([[1, 2, 3], [4, 5, 6]])
    f = np.array([[7, 8], [67, 78]])  # This is a 2D array with shape (2, 2)
    print(e.shape)  # Output: (2, 3), this shows that array e has a shape of (2, 3)
    print(f.shape)  # Output: (2, 2), this shows that array f has a shape of (2, 2)
    result = e + f  # This will raise an error because the shapes of e and f are not compatible for broadcasting
    print(result)
    print(result)
except ValueError as e:
    print(e)  # Output: operands could not be broadcast together with shapes (2,3) (2,2), this error message indicates that the shapes of arrays e and f are not compatible for broadcasting, and therefore the addition operation cannot be performed.

try:
    g = np.array([[1, 2]])
    h = np.array([[7, 8], [5, 6]])  # This is a 2D array with shape (2, 2)
    print(g.shape)  # Output: (1, 2), this shows that array g has a shape of (1, 2)
    print(h.shape)  # Output: (2, 2), this shows that array h has a shape of (2, 2)
    result = g + h  # This will work because the shapes of g and h are compatible for broadcasting   
    print(result)
except ValueError as e:
    print(e)  # This will not be executed because the addition operation will be successful due to broadcasting. The resulting array will have a shape of (2, 2) and will contain the sum of the corresponding elements from arrays g and h.