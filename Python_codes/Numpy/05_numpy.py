# Random Numbers
import numpy as np
# Numpy provides a module called numpy.random that contains functions for generating random numbers. Some common functions in this module include:
rng= np.random.default_rng(seed=1)  # This creates a random number generator object that can be used to generate random numbers.
a= rng.integers(1, 10, size=5)  # This function generates an array of random integers between 1 (inclusive) and 10 (exclusive) with a specified size. In this case, it generates an array of 5 random integers.
print(a)  # Output: [3 7 2 5 9], this will output an array of 5 random integers between 1 and 10. The actual values may vary each time you run the code because they are generated randomly.
b= rng.integers(1, 10, size=(3, 4))  # This function generates a 2D array of random integers between 1 (inclusive) and 10 (exclusive) with a specified shape. In this case, it generates a 3x4 array of random integers.
print(b)  # Output: [[3 7 2 5] [9 1 4 6] [8 2 3 7]], this will output a 3x4 array of random integers between 1 and 10. The actual values may vary each time you run the code because they are generated randomly.

# We use the seed parameter to ensure that the same sequence of random numbers is generated each time the code is run. This can be useful for reproducibility and debugging purposes. By setting the seed to a specific value (in this case, 1), we can ensure that the same random numbers are generated every time we run the code, which can help us verify that our code is working correctly and produce consistent results.
# if we keep seed 2 instead of 1, we will get a different sequence of random numbers. For example:
rng= np.random.default_rng(seed=2)  # This creates a random number generator object with a different seed value, which will generate a different sequence of random numbers.
c= rng.integers(1, 10, size=5)  # This function generates an array of random integers between 1 (inclusive) and 10 (exclusive) with a specified size. In this case, it generates an array of 5 random integers.
print(c)  # Output: [8 4 9 1 6], this  will output an array of 5 random integers between 1 and 10, but the actual values will be different from the previous example because we used a different seed value. The sequence of random numbers generated will be consistent each time we run the code with the same seed value, but it will differ from the sequence generated with a different seed value.


#Floating-point random numbers can be generated using the random() function in the numpy.random module. This function generates random numbers between 0 (inclusive) and 1 (exclusive). For example:
rng=np.random.uniform(0, 5, size=5)  # This function generates an array of random floating-point numbers between 0 (inclusive) and 1 (exclusive) with a specified size. In this case, it generates an array of 5 random floating-point numbers.
print(rng) 


# OR even this is fine 

rng=np.random.default_rng()
d= rng.uniform(0, 5, size=(3, 4))  # This function generates a 2D array of random floating-point numbers between 0 (inclusive) and 1 (exclusive) with a specified shape. In this case, it generates a 3x4 array of random floating-point numbers.
print(d) 





# Using random for arrays

rng= np.random.default_rng()
fruits= np.array(["apple", "banana", "cherry", "date", "elderberry"])
random_fruit= rng.choice(fruits)  # This function randomly selects a single element from the fruits array.
print(random_fruit)  # Output: "banana", this will output a randomly selected fruit from the fruits array. The actual output may vary each time you run the code because the selection is random.
rng.shuffle(fruits)  # This function randomly shuffles the elements of the fruits array in place.
print(fruits)  # Output: ["date", "elderberry", "banana", "cherry", "apple"], this will output the fruits array with its elements randomly shuffled. The actual order of the elements may vary each time you run the code because the shuffling is random.

lis_fruits=rng.choice(fruits, size=(3,3))
print(lis_fruits)

lis_fruits_replace=rng.choice(fruits, size=(3,3), replace=True) # this replace=True allows for the same fruit to be selected multiple times in the resulting array. If replace=False, each fruit can only be selected once, and the resulting array will contain unique fruits from the original array.
print(lis_fruits_replace)

