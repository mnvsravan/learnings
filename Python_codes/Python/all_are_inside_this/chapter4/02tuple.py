# a tuple is a collection which is ordered and unchangeable. Tuples are defined by using parentheses () and separating items with commas.
# creating a tuple
my_tuple = (1, 2, 3, "Hello", True)
print(my_tuple)
# these are immutable, which means that once we create a tuple, we cannot change it. However, we can create a new tuple by concatenating or slicing existing tuples.
print(type(my_tuple)) # this will print the type of the variable my_tuple, which is <class 'tuple'> in this case.
singletuple = (1,) # this is how we create a tuple with a single item. The comma is necessary to indicate that it is a tuple, otherwise it would be interpreted as an integer.
print(type(singletuple)) # this will print <class 'tuple'>, confirming that singletuple is indeed a tuple.
# we can access individual items in a tuple using indexing:
first_item = my_tuple[0]
print(first_item)
# we can also use slicing to access a range of items in a tuple:
subtuple = my_tuple[1:4] # this will give us a new tuple containing
print(subtuple)
# we can use the len() function to get the number of items in a tuple:
length = len(my_tuple)
print(length)
# we can use the count() method to count the number of occurrences of a specific item in a tuple:
count_of_2 = my_tuple.count(2) # this will return the number of times the value 2 appears in the tuple, which is 1 in this case.
print(count_of_2)
# we can use the index() method to find the index of the first occurrence of a specific item in a tuple:
index_of_3 = my_tuple.index(3) # this will return the index of the first occurrence of the value 3 in the tuple, which is 2 in this case (indexing starts at 0).
print(index_of_3)
#print(my_tuple.find(2)) # this will raise an AttributeError because tuples do not have a find() method. The find() method is a string method, and it is not applicable to tuples. If you want to check if a specific value exists in a tuple, you can use the in keyword, like this: 2 in my_tuple, which will return True if the value 2 is in the tuple, and False otherwise.
# like lists, we can also concatenate tuples using the + operator:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2 # this will create a new tuple that contains all the items from tuple1 followed by all the items from tuple2.
print(concatenated_tuple)
# we can also use the * operator to repeat a tuple multiple times:
repeated_tuple = tuple1 * 3 # this will create a new tuple that contains the items from tuple1 repeated three times in a row.
print(repeated_tuple)
# more operations on tuples
# we can use the sorted() function to return a new sorted list from the items in a tuple:
numbers_tuple = (3, 1, 4, 2)
sorted_numbers = sorted(numbers_tuple) # this will return a new list containing the items from the tuple sorted in ascending order. If you want to sort in descending order, you can use sorted(numbers_tuple, reverse=True).
print(sorted_numbers)
# we can use the reversed() function to return an iterator that accesses the items in a tuple in reverse order:
reversed_tuple = tuple(reversed(tuple1)) # this will return an iterator that accesses the items in tuple1 in reverse order. To convert it to a tuple, we can use the tuple() function.
print(reversed_tuple) # this will print the reversed tuple, which is (3, 2, 1) in this case.
# we can use the zip() function to combine two or more tuples into a single tuple of tuples:
tuple_a = (1, 2, 3)
tuple_b = ("a", "b", "c")
zipped_tuple = tuple(zip(tuple_a, tuple_b)) # this will create a new tuple that contains tuples of corresponding items from tuple_a and tuple_b. The first item in the zipped tuple will be (1, "a"), the second item will be (2, "b"), and the third item will be (3, "c").
print(zipped_tuple)
#Tuple Unpacking (Very Important)
point = (3, 4)
x, y = point # this is called tuple unpacking. It allows us to assign the values from the tuple to individual variables in a single line of code. In this case, x will be assigned the value 3 and y will be assigned the value 4.
print(x) # this will print the value of x, which is 3 in this case.
print(y) # this will print the value of y, which is 4 in this case
# With star
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers # this will unpack the first item of the tuple into the variable first, the last item into the variable last, and all the items in between into a list assigned to the variable middle. In this case, first will be 1, middle will be [2, 3, 4], and last will be 5.
print(first) # this will print the value of first, which is 1 in this case.
print(middle) # this will print the value of middle, which is [2, 3, 4] in this case.
print(last) # this will print the value of last, which is 5 in this case
# also len max min sum etc functions work with tuples of numbers as well, just like they do with lists. For example:
numbers_tuple = (1, 2, 3, 4, 5)
print(len(numbers_tuple)) # this will return the number of items in the tuple, which is 5 in this case.
print(max(numbers_tuple)) # this will return the largest number in the tuple, which is 5 in this case.
print(min(numbers_tuple)) # this will return the smallest number in the tuple, which is 1 in this case.
print(sum(numbers_tuple)) # this will return the sum of all the numbers in the tuple, which is 15 in this case.
# memebership test
print(3 in numbers_tuple) # this will return True if the value 3 is in the tuple, and False otherwise. In this case, it will return True because 3 is indeed in the tuple.
