#list is a collection of items which is ordered and changeable. It allows duplicate members. Lists are defined by using square brackets [] and separating items with commas.
# creating a list
my_list = [1, 2, 3, "Hello", True]
print(my_list)
# we can store any type of data in a list, including other lists:
nested_list = [1, 2, [3, 4], "Hello"]
print(nested_list)
# we can access individual items in a list using indexing:
first_item = my_list[0]
print(first_item)
last_item = my_list[-1] # you can do 4 as well but -1 is more common to access the last item in the list. This will give us the last item in the list, which is True in this case.
print(last_item)
# we can access all elements and unlike strings we can change the value of a list item by assigning a new value to a specific index:
my_list[0] = 10
print(my_list)
# we can also use slicing to access a range of items in a list:
sublist = my_list[1:4] # this will give us a new list containing the items from index 1 to index 3 (4 is not included).
print(sublist)
# there are immutable and mutable data types in python. Lists are mutable, which means that we can change their contents after they have been created. We can add, remove, or modify items in a list without creating a new list.
# before going to functions lets see more stuff
# we can use the len() function to get the number of items in a list:
length = len(my_list)
print(length)
# Functions in lists
# we can use the append() method to add an item to the end of a list:
list1 = [1, 2, 3]
list1.append(4)
print(list1)
# we can use the insert() method to add an item at a specific index in a list:
list1.insert(1, 10) # this will insert the value 10 at index 1 in the list. The existing items will be shifted to the right to make room for the new item.
print(list1)
# we can use the remove() method to remove the first occurrence of a specific item from a list:
list1.remove(2) # this will remove the first occurrence of the value 2 from the list. If the value is not found in the list, it will raise a ValueError.
print(list1)
# we can use the pop() method to remove and return an item at a specific index in a list:
popped_item = list1.pop(1) # this will remove the item at index
print(popped_item) # this will print the value of the popped item, which is 10 in this case.
# the difference between remove() and pop() is that remove() removes the first occurrence of a specific value from the list, while pop() removes and returns an item at a specific index. If you want to remove an item by its value, you would use remove(). If you want to remove an item by its index and also get the value of that item, you would use pop().
print(list1) # this will print the updated list after the pop() operation, which is [1, 3, 4] in this case.
list1.reverse() # this will reverse the order of the items in the list.
print(list1)
# we can use the sort() method to sort the items in a list in ascending order:
list2 = [3, 1, 4, 2]
list2.sort() # this will sort the items in the list in ascending order. If you want to sort in descending order, you can use list2.sort(reverse=True).
print(list2)
# remeber that we cant pass these reverse in print thing cuz it will reutnr none because the sort() method modifies the list in place and does not return a new sorted list. So if you try to print the result of list2.sort(), it will print None because the sort() method does not return anything. Instead, you should call list2.sort() to sort the list and then print list2 to see the sorted list.
# there are also built-in functions like min(), max(), sum() which can be used with lists of numbers:
numbers = [1, 2, 3, 4, 5]
print(min(numbers)) # this will return the smallest number in the list, which is 1 in this case.
print(max(numbers)) # this will return the largest number in the list, which is 5
print(sum(numbers)) # this will return the sum of all the numbers in the list, which is 15 in this case.
# There are more functions which advance people use it like 
# we can use the count() method to count the number of occurrences of a specific item in a list:
my_list = [1, 2, 3, 2, 4, 2]
count_of_2 = my_list.count(2) # this will return the number of times the value 2 appears in the list, which is 3 in this case.
print(count_of_2)
# we can use the index() method to find the index of the first occurrence of a specific item in a list:
index_of_3 = my_list.index(3) # this will return the index of the first occurrence of the value 3 in the list, which is 2 in this case (indexing starts at 0).
print(index_of_3)
# we can use the clear() method to remove all items from a list:
my_list.clear() # this will remove all items from the list, leaving it empty.
print(my_list) # this will print the empty list, which is [] in this case.
list2= [3, 1, 4, 2]
# now more advanced functions
# we can use the reverse() function to reverse the order of the items in a list:
reversed_list = list2[::-1] # this will create a new list that is a reversed version of list2. The slicing syntax [::-1] means to take the entire list and step through it backwards, effectively reversing the order of the items.
print(reversed_list) # this will print the reversed list, which is [2, 4, 1, 3] in this case.
# to create a copy of a list, we can use the copy() method:
original_list = [1, 2, 3]
copied_list = original_list.copy() # this will create a new list that is a copy of original_list. The copy() method creates a shallow copy of the list, which means that it creates a new list object but does not create copies of the items in the list. If the items in the list are mutable objects (like other lists), then both the original and copied lists will reference the same mutable objects.
print(copied_list) # this will print the copied list, which is [1, 2, 3] in this case.
# to extend a list with another list, we can use the extend() method:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2) # this will add all the items from list2 to the end
print(list1) # this will print the extended list, which is [1, 2, 3, 4, 5, 6] in this case.