# Working with mathemetical functions 
# we can create our some own functions 
import numpy as np

def sigmoid(array):
    return 1 / (1 + np.exp(-(array)))

a=np.random.randint(1,100,10).reshape(2,5)
print(sigmoid(a))




def meansqr(array1, array2):
    return np.mean((array1 - array2) ** 2)
b = np.random.randint(1, 100, 10).reshape(2, 5)
c = np.random.randint(1, 100, 10).reshape(2, 5)
print(b)
print(c)
print("MSE:", meansqr(b, c))

#Working with missing values
# first of all nan is like none is normal python
k=np.array([1,2,3,4,np.nan,6])
print(k)
print(np.isnan(k))
print(k[~(np.isnan(k))])


#GRAPHS


import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

plt.plot(x, y, label="Sigmoid")

x = np.linspace(0.1, 10, 100)  # avoid 0 and negatives
y = np.log(x)

plt.plot(x, y, label="Log")
plt.show() # used to show

x = np.linspace(0.1, 10, 100)  # avoid 0 and negatives
y = np.sin(x)

plt.plot(x, y, label="sin")
plt.show() # used to show





