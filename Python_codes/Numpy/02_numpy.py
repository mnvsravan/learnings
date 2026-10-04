#slicing in Numpy is similar to slicing in Python lists, but it can be applied to multi-dimensional arrays. The syntax for slicing in Numpy is as follows:
# array[start:stop:step]
import numpy as np
my_list=np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
print(my_list)
print(my_list[-1]) 
print(my_list[-2]) 
print(my_list[2]) 
print(my_list[2:])
print(my_list[1:3])
print(my_list[::-1])
print(my_list[::-2])
print(my_list[::-3])
print(my_list[::-4]) #This is the 4th element from the end, which is the first element of the array. So it will return the entire array in reverse order.

#Coloumn slicing in Numpy is done using the syntax array[:, start:stop:step], where the colon (:) indicates that we want to select all rows, and the start:stop:step specifies the range of columns we want to select. For example:
print()
print(my_list[:, 0])
print(my_list[:, 2:])
print(my_list[:, 1:3])
print(my_list[:, ::-1])
print(my_list[0:2, 1:2])
print(my_list[2:4, 2:4])







#Arthemtic operations in Numpy can be performed element-wise on arrays. This means that when you perform an operation on two arrays of the same shape, the operation is applied to each corresponding element. For example:
a = np.array([1, 2, 3])
print(a + 1)  # Output: [2 3 4], this adds 1 to each element of the array a
print(a * 2)  # Output: [2 4 6], this multiplies each element of the array a by 2
print(a - 1)  # Output: [0 1 2], this subtracts 1 from each element of the array a
print(a / 2)  # Output: [0.5 1.  1.5], this divides each element of the array a by 2
print(a ** 2)  # Output: [1 4 9], this raises each element of the array a to the power of 2
print(a % 2)  # Output: [1 0 1], this calculates the modulus of each element of the array a by 2
print(a // 2)  # Output: [0 1 1], this performs floor division on each element of the array a by 2

b= np.array([4, 5, 6])
print(a + b)  # Output: [5 7 9], this adds the corresponding elements of arrays a and b
print(a * b)  # Output: [ 4 10 18], this multiplies the corresponding elements of arrays a and b
print(a - b)  # Output: [-3 -3 -3], this subtracts the corresponding elements of arrays a and b
print(a / b)  # Output: [0.25 0.4  0.5], this divides the corresponding elements of arrays a and b
print(a ** b)  # Output: [ 1 32 729], this raises the corresponding elements of array a to the power of the corresponding elements of array b
print(a % b)  # Output: [1 2 3], this calculates the modulus of the corresponding elements of arrays a and b
print(a // b)  # Output: [0 0 0], this performs floor division on the corresponding elements of arrays a and b

c= np.array([[1, 2], [3, 4]])
d= np.array([[5, 6], [7, 8]])
print(c + d)  # Output: [[ 6  8] [10 12]], this adds the corresponding elements of arrays c and d
print(c * d)  # Output: [[ 5 12] [21 32]], this multiplies the corresponding elements of arrays c and d
print(c - d)  # Output: [[-4 -4] [-4 -4]], this subtracts the corresponding elements of arrays c and d
print(c / d)  # Output: [[0.2        0.33333333] [0.42857143 0.5       ]], this divides the corresponding elements of arrays c and d
print(c ** d)  # Output: [[    1    64] [  2187 65536]], this raises the corresponding elements of array c to the power of the corresponding elements of array d        
print(c % d)  # Output: [[1 2] [3 4]], this calculates the modulus of the corresponding elements of arrays c and d
print(c // d)  # Output: [[0 0] [0 0]], this performs floor division on the corresponding elements of arrays c and d    

b= np.array([1.21,2.56,3.89])
print(np.round(b))  # Output: [1. 3. 4.], this rounds each element of the array b to the nearest integer
print(np.floor(b))  # Output: [1. 2. 3.], this rounds each element of the array b down to the nearest integer
print(np.ceil(b))  # Output: [2. 3. 4.], this rounds each element of the array b up to the nearest integer  
print(np.trunc(b))  # Output: [1. 2. 3.], this truncates each element of the array b to the nearest integer towards zero
print(np.sqrt(b))  # Output: [1.1        1.6        1.97232753], this calculates the square root of each element of the array b
print(np.exp(b))  # Output: [3.35  12.82 48.81], this calculates the exponential of each element of the array b
print(np.log(b))  # Output: [0.19009444 0.939 1.357], this calculates the natural logarithm of each element of the array b
# ETC
print(np.pi*b**2)  # Output: [4.605 10.24 15.56], this calculates the value of pi multiplied by each element of the array b raised to the power of 2

marks= np.array([40, 50, 60, 70, 80,90,100])
print(marks==100)  # Like this we can use all comparision operatores

marks1= np.array([40, 50, 60, 70, 80,90,100])
marks1[marks1<70] = 0
print(marks1)  # Output: [ 0 0 0 70 80 90 100], this sets all elements of the array marks1 that are less than 70 to 0.
