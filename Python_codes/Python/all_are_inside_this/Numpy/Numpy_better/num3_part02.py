#isin - Likes tells if its in or no
import numpy as np
a=np.array([11, 53, 28, 50, 38, 37, 94, 92,  5, 30, 68,  9, 78,  2, 21])
items = [10,20,30,40,50,60,70,80,90,100]
print(np.isin(a,items))
print(a[np.isin(a,items)])


#flip-reverses the order of array elements along the specified axis, preserving the shape of the array.

a=np.random.randint(1,100,10).reshape(2,5)
print(a)
print(np.flip(a))
print(np.flip(a,axis=1))
print(np.flip(a,axis=0))

#Put-replaces specific elements of an array with given values of p_array. Array indexed works on flattened array.

a=np.random.randint(1,100,10).reshape(2,5)
print(a)
# np.put(a,[[1:1],[1:2]],[4,5]) u cant do things like this , u need to use only actual indicers no more even if its 100
np.put(a, [6, 7], [101, 606]) # (array,indices,value)
print(a)

#Delete (deletes indices)
a=np.random.randint(1,100,10).reshape(2,5)
print(a)
a=np.delete(a,[0,2,4])
print(a)

#Set functions 
m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

print(np.union1d(m,n))
print(np.setdiff1d(n,m))
print(np.setxor1d(m,n))

#clip-used to Clip (limit) the values in an array.
k=np.array([110, 530,  28,  50,  38,  37,  94,  92,   5,  30,  68,   9,  78,
         2,  21])
k=np.clip(k,25,75)
print(k)
# Like the values more than 75 will be 75 and less than 25 will be 25
