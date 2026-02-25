# A list contains the multiplication table of 7. write a program to convert it to vertical
# string of same numbers.
table_of_7 = [7 * i for i in range(1, 11)] # this will create a list of the multiplication table of 7 from 1 to 10.
vertical_string = "\n".join(str(num) for num in table_of_7) # this will convert the list of numbers into a vertical string by joining each number with a newline character.
print(vertical_string) # this will print the vertical string of the multiplication table of 7. The join() method is used to concatenate the elements of the list into a single string, with each element separated by a newline character. The str() function is used to convert each number in the list to a string before joining them together.
#or
table_of_7 = [str(7 * i) for i in range(1, 11)]
vertical_string = "\n".join(table_of_7) # this will convert the list of numbers into a vertical string by joining each number with a newline character.
print(vertical_string) # this will print the vertical string of the multiplication table of 7. The join() method is used to concatenate the elements of the list into a single string, with each element separated by a newline character. In this case, we have already converted each number to a string in the list comprehension, so we can directly join them together without needing to convert them again.



# Write a program to filter a list of numbers which are divisible by 5.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25]
def is_divisible_by_5(num):
    return num % 5 == 0
divisible_by_5 = filter(is_divisible_by_5, numbers) # this will apply the is_divisible_by_5 function to each element in the numbers list, resulting in a new iterator that yields only the numbers that are divisible by 5.
print(list(divisible_by_5)) # this will print the list of numbers that are divisible by 5, which is [5, 10, 15, 20, 25]. The filter() function is used to create a new iterator that contains only the elements of the original list that satisfy the condition defined in the is_divisible_by_5 function. The list() function is then used to convert the iterator into a list for easier display.




#Write a program to find the maximum of the numbers in a list using the reduce function

from functools import reduce
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
def find_max(x, y):
    return x if x > y else y # DIFF way of writing if else
max_number = reduce(find_max, numbers) # this will apply the find_max function cumulatively to the items of the numbers list, resulting in a single value that is the maximum number in the list.
print(max_number) # this will print the maximum number in the list, which is 9. The reduce() function is used to apply the find_max function cumulatively to the items of the numbers list, effectively comparing each element with the current maximum and updating it accordingly until it reduces the entire list to a single maximum value.
