# Functions in numpy work very fast compared to normal python
import numpy as np
import time as t
a=np.array([i for i in range(1000000)])
b=np.array([i for i in range(1000000,2000000)])
start= t.time()
c=a+b
end= t.time()
print("Time taken by numpy:", end-start)
# It uses less space than normal python lists
import sys
a=np.array([i for i in range(1000000)],dtype=np.int32)
print("Size of numpy array:", sys.getsizeof(a))


#   Fancy Indexing
a=np.random.randint(0,100,24).reshape(3,8)
print(a)
print(a[[2,0,1]]) # Like this gives 3rd row then 1st row then 2nd row
print(a[:,[2,0,1]]) # Like this gives 3rd column then 1st column then 2nd column

#Boolean Indexing  like it resturns the elements in the array that satisfy the condition we get 1d array
print(a[a%2==0]) # this gives all the even numbers in the array
print(a[(a%2==0) & (a>50)]) # this gives all the even numbers greater than 50 in the array
# U USE & for and and | for or in boolean indexing NOT AND OR NOT LIKE THOSE IN NORMAL PYTHON



#BROADCASTING
# Broadcasting Rules
# 1. Make the two arrays have the same number of dimensions.
#    - If the numbers of dimensions of the two arrays are different,
#      add new dimensions with size 1 to the head of the array
#      with the smaller dimension.

# 2. Make each dimension of the two arrays the same size.
#    - If the sizes of each dimension of the two arrays do not match,
#      dimensions with size 1 are stretched to the size of the other array.
#    - If there is a dimension whose size is not 1 in either of the two arrays,
#      it cannot be broadcasted, and an error is raised.
# STRECHING CAN ONLY HAPPEN IF THE SIZE OF THE DIMENSION IS 1 IN ONE OF THE ARRAYS OTHERWISE IT GIVES ERROR
# More examples

a = np.arange(12).reshape(4,3) # here a is 4,3 and b is 3 so we add new dimension to b and make it 1,3 then we stretch it to 4,3
b = np.arange(3)
print(a)
print(b)
print(a+b)

try:
    # a has shape (3,4)
    a = np.arange(12).reshape(3, 4)

    # b has shape (3,)
    # It is treated as (1,3) for broadcasting
    b = np.arange(3)

    print(a)
    print(b)

    # Broadcasting comparison:
    # a → (3,4)
    # b → (1,3)
    # Compare from right:
    # 4 vs 3 → mismatch (neither is 1) → ERROR
    print(a + b)

except ValueError as e:
    print("Error:", e)



a = np.arange(3).reshape(1,3) # here a is 1,3 and b is 3 so we stretch a to 3,3 then we add it to b by stretching it also to 3,3
b = np.arange(3).reshape(3,1)

print(a)
print(b)

print(a+b)

a = np.arange(3).reshape(1,3) # here a is 1,3 and b is 3,1 so we stretch a to 4,3 and b to 4,3 then we add 
b = np.arange(4).reshape(4,1)

print(a)
print(b)

print(a + b)

a = np.array([1])  # here a is 1 and b is 2,2 so we make a 1,1 and stretch it to 2,2 then we add it to b
b = np.arange(4).reshape(2,2)


print(a)
print(b)

print(a+b)

try:
    a = np.arange(12).reshape(3, 4) # here a is 3,4 and b is 4,3 we cannot stretch a to 4,3 or b to 3,4 because both dimensions are not 1 so it gives error
    b = np.arange(12).reshape(4, 3)

    print(a)
    print(b)

    print(a + b)  # This will raise ValueError

except ValueError as e:
    print("Error:", e)


try:
    a = np.arange(16).reshape(4, 4) # here a is 4,4 and b is 2,2 we cannot stretch  b to 4,4 because both dimensions are not 1 so it gives error
    b = np.arange(4).reshape(2, 2)

    print(a)
    print(b)

    print(a + b)  # This will raise ValueError

except ValueError as e:
    print("Error:", e)

