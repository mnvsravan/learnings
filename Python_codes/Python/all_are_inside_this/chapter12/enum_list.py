# enum in python 
list1 = [1, 2, 3, 4, 5]
for i,item in enumerate(list1):
    print(i, item) # this will print the index and the value of each item in the list. The enumerate() function adds a counter to an iterable and returns it as an enumerate object, which can be used in a for loop to get both the index and the value of each item in the iterable.


# list comprehension 
list1 = [1,7,12,11,22,]
list2 = [item for item in list1 if item > 8]
print(list2) # this will print [12, 11, 22], because these are the items in list1 that are greater than 8. The list comprehension is a concise way to create a new list by filtering and transforming the items of an existing iterable. In this case, we are creating a new list (list2) that contains only the items from list1 that satisfy the condition (item > 8).

# dictionary comprehension
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {key: value**2 for key, value in dict1.items()}
print(dict2) # this will print {'a': 1, 'b': 4, 'c': 9}, because we are creating a new dictionary (dict2) where the keys are the same as in dict1 and the values are the squares of the values in dict1. The dictionary comprehension is a concise way to create a new dictionary by filtering and transforming the items of an existing iterable. In this case, we are creating a new dictionary (dict2) that contains the same keys as dict1 but with values that are the squares of the original values in dict1.

