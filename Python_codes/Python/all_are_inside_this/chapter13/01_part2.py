# lamda function in python is a small anonymous function that can take any number of arguments, but can only have one expression. It is defined using the lambda keyword followed by the arguments, a colon, and the expression. The syntax for a lambda function is as follows:

# lambda arguments: expression
# The expression is evaluated and returned when the lambda function is called. Lambda functions are often used for short, simple functions that are not worth defining with a full function definition. They are commonly used in conjunction with higher-order functions like map(), filter(), and reduce().
# lambda arguments:expressions
sum=lambda a,b:a+b
print(sum(10,20)) # this will print the sum of 10 and 20
mul=lambda a,b:a*b
print(mul(10,20)) # this will print the product of 10 and 20

#join() method in python is a string method that is used to join a sequence of strings together with a specified separator. The syntax for the join() method is as follows:

l = ["apple", "mango", "banana"]
result = "::".join(l)
print(result)

# format() method in python is a string method that is used to format strings by replacing placeholders with specified values. The syntax for the format() method is as follows:

formatted_string1 = "{0} is a good {1}".format("harry", "boy") 
print(formatted_string1)
formatted_string2 = "{1} is a good {0}".format("harry", "boy")
print(formatted_string2)

# map() function in python is a built-in function that applies a specified function to each item of an iterable (such as a list, tuple, or set) and returns an iterator that yields the results. The syntax for the map() function is as follows:
sum=lambda a,b:a+b
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(sum, numbers1, numbers2) # this will apply the sum function to each pair of elements from numbers1 and numbers2, resulting in a new iterator that yields the sums of the corresponding elements.
print(list(result)) # this will print the list of sums, which is [5, 7, 9].

sqr=lambda x:x**2
numbers = [1, 2, 3, 4, 5]
result = map(sqr, numbers) # this will apply the sqr function to each element in the numbers list, resulting in a new iterator that yields the squares of the elements.
print(list(result)) # this will print the list of squares, which is [1, 4, 9, 16, 25].

#filter() function in python is a built-in function that constructs an iterator from elements of an iterable for which a specified function returns true. The syntax for the filter() function is as follows:
def is_even(num):
    return num % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers) # this will apply the is_even function to each element in the numbers list, resulting in a new iterator that yields only the even numbers.
print(list(even_numbers)) # this will print the list of even numbers, which is [2, 4, 6].

#reduce() function in python is a function from the functools module that applies a specified function cumulatively to the items of an iterable, from left to right, reducing the iterable to a single value. The syntax for the reduce() function is as follows:
from functools import reduce
def multiply(x, y):
    return x * y
numbers = [1, 2, 3, 4, 5]
result = reduce(multiply, numbers) # this will apply the multiply function cumulatively to the items of the numbers list, resulting in a single value that is the product of all the numbers.
print(result) # this will print the product of all the numbers, which is 120.
# like it keeps multiplying the first two elements, then multiplies the result with the next element and so on until it reduces the entire list to a single value.