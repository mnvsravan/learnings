import numpy as np
### `Q-1` Create a null vector of size 10 but the fifth value which is 1.
a = np.zeros(10)
a[4] = 1
print(a)

# Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.
a,b=map(int, input("Enter two numbers a and b separated by space which give 6 as pdt: ").split())
array = np.random.randint(1, 10, 6).reshape(a, b)
print(array)
print("Average of the array:", np.mean(array))

# Q-3: Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array shape as (a,b) as parameter to function.
def borderArray(a,b):
    x = np.ones((a,b))
    x[1:a-1, 1:b-1] = 0    # Except the border, changing all other elements to 0
    return x
borderArray(4,5)

# Q-4 Create a vector of size 10 with values ranging from 0 to 1, both excluded.
array=np.linspace(0, 1, 12)[1:11]
print(array)

# Q-5 Can you create a identity mattrix of shape (3,4). If yes write code for it.
#NOT POSSIBLE
array1=np.eye(3) # eye means identity matrix of shape (3,3)
array2=np.eye(4)

#  Create a 5x5 matrix with row values ranging from 0 to 4.
matrix = np.arange(5).reshape(1,5)
matrix = np.repeat(matrix, 5, axis=0)
print(matrix)
# OR
# z = np.zeros((5,5))

# for i in range(z.shape[0]):
#     z[i] = np.arange(5)

# print(z)


# Q-7: Consider a random integer (in range 1 to 100) vector with shape (10,2) representing coordinates, and coordinates of a point as array is given. Create an array of distance of each point in the random vectros from the given point. Distance array should be interger type.
a = np.random.randint(1, 100, (10, 2))

p = [50, 50]

def distance(a, p, i):
    return ((a[i][0] - p[0])**2 + (a[i][1] - p[1])**2)**0.5

for i in range(a.shape[0]):
    print(distance(a, p, i))

    # Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
a = np.zeros((6,7,8))
a=np.unravel_index(100, (6,7,8))

#OR ONLY IF ALL ARE DISNTINCVT
a = np.zeros((6,7,8))
line = np.linspace(0, 335, 336)
ans = line[99]
x, y, z = np.where(a == ans)
print(x, y, z)

# You are given a space separated list of numbers. Your task is to print a reversed NumPy array with the element type float.

# Input Format:

# A single line of input containing space separated numbers.

# Output Format:

# Print the reverse NumPy array with type float.
numbers = input("Enter space separated numbers: ").split()
reversed_array = np.array(numbers[::-1], dtype=float)
print(reversed_array)


# Q-11: Softmax function
# Create a Python function to calculate the Softmax of the given numpy 1D array. The function only accepts the numpy 1D array, otherwise raise error.

# σ(z⃗ )i=ezi∑Kj=iezj

#Code here
def softmax(arr):
    if type(arr) != np.ndarray:
        raise TypeError("Requires Numpy Array")
    elif arr.ndim > 1:
        raise TypeError("Requires 1D Array")
    s = np.sum(np.exp(arr))
    return np.exp(arr)/s
softmax(np.array([86.03331084, 37.7285648,  48.64908087, 87.16563062, 38.40852563, 37.20006318]))