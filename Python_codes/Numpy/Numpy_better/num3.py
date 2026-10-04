#Imp functions in numpy
#1.sort
import numpy as np
a=np.random.randint(1,100,20).reshape(2,10)
print(a)
print(np.sort(a))
print(np.sort(a,axis=0))
print(np.sort(a,axis=1))

#2.Append
print()
b = np.random.randint(1, 100, 20).reshape(2, 10)
print(b)

# b = np.append(b, 11, axis=1)   # this raises error
b = np.append(b, [[1],[1]], axis=1) # The number of elements in coloumn must be equal to the row to match now shape is (2 ,11)
print(b)
b = np.append(b, [[1]*11], axis=0)  # The number of elements in row must be equal to the col to match
print(b)

print()

b = np.random.randint(1, 10, 24).reshape(2, 3, 4)
print("Original shape:", b.shape)
print(b)
new_block = np.ones((1, 3, 4)) * 1  # like creates a new block and adds 
b = np.append(b, new_block, axis=0)
print(b)
print("After axis=0:", b.shape)

#3D

b = np.random.randint(1, 10, 24).reshape(2, 3, 4)
print(b)
new_rows = np.ones((2, 1, 4)) * 1
b = np.append(b, new_rows, axis=1)
print(b)
print("After axis=1:", b.shape)


b = np.random.randint(1, 10, 24).reshape(2, 3, 4)
print(b)
new_cols = np.ones((2, 3, 1)) * 1
b = np.append(b, new_cols, axis=2)
print(b)
print("After axis=2:", b.shape)

#CONCAN
c=np.random.randint(1,100,10).reshape(2,5)
d=np.random.randint(1,100,10).reshape(2,5)
e=np.concatenate((c,d),axis=0)
f=np.concatenate((c,d),axis=1)
print(e)
print(f)

#UNIQUE

k=np.random.randint(1,100,10).reshape(2,5)
print(k)
print(np.unique(k))


#N_dim
m=np.random.randint(1,100,10)
print(m.shape)
m1=np.expand_dims(m,axis=0)
print(m1.shape)
m2=np.expand_dims(m,axis=1)
print(m2.shape)
# m3=np.expand_dims(m,axis=1,axis=0)
# print(m3.shape) in valid


#np.where, syntax(condition,TRUE,FALSE)
print()
l=np.random.randint(1,100,10).reshape(2,5)
print(l)
x=np.where(l>50,0,l)
print(x)
# If no true or false values are passed then it returns indices
o=np.where(l>50)
print(o)    # gives row and col indices


#argmin and argmax , these return the indices of max and min 
print()
z=np.random.randint(1,100,10).reshape(2,5)
print(z)
print(np.argmax(z))
print(np.argmax(z,axis=1))
print(np.argmax(z,axis=0))


#CUMSUM and pdt
d=np.random.randint(1,100,10).reshape(2,5)
print(d)
print(np.cumsum(d))
print(np.cumprod(d))
#IF U WANT ROW OR COL JUST USE AXIS     

#PERCENTILE
v=np.random.randint(1,100,10).reshape(2,5)
print(v)
print(np.percentile(a,75)) #Like a score in which ur above 75% of competetion

#Histogram
z=np.random.randint(1,100,10).reshape(2,5)
t=np.histogram(z,bins=[10,20,30,40,50,60]) # Like histogram gives number of elements present inbetween the bins
print(t)

#Corelation
# 1 means it increases same as the other , 0 means no relation , -1 decrases 

salary = np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])
print(np.corrcoef(salary,experience)) # like it gives a 2x2 matrix of [[1.         0.25344572]  like a11 is salary with salary and a12 is salary and experience
                                                                    #  [0.25344572 1.        ]]   a22 is only exp with exp and a21 is exp with sal
 