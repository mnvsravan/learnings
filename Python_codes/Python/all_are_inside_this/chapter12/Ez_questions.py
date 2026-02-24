#1  Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same

# try:
#     with (
#         open('1.txt', 'r') as file1,
#         print(f.read()) # this will print the contents of file1 if it is opened successfully.
#         open('2.txt', 'r') as file2,
#         print(f.read()) # this will print the contents of file2 if it is opened successfully.
#         open('3.txt', 'r') as file3,
#         print(f.read()) # this will print the contents of file3 if it is opened successfully.
#     ):
#         print("All files opened successfully.")
# except FileNotFoundError as e:
#     print(f"Error: {e}. Please make sure the file exists.") # this will print an error message if any of the files are not found, prompting the user to check if the file exists. The program will continue to run without exiting, allowing the user to fix the issue and try again.
# The above methond is wrong 

# correct method
files = ['yoyo.txt', '2.txt', '3.txt']

for filename in files:
    try:
        with open(filename, 'r') as f:
            print(f"\nContents of {filename}:")
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} is not present. Please create the file.")
        
print("\nProgram continues running...")

# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for i,item in enumerate(my_list):
    if i in [2, 4, 6]: # since index starts from 0, the third element is at index 2, the fifth element is at index 4 and the seventh element is at index 6.
        print(f"The {i+1}rd/5th/7th element is: {item}") # this will print the third, fifth and seventh elements from the list. The enumerate() function adds a counter to an iterable and returns it as an enumerate object, which can be used in a for loop to get both the index and the value of each item in the iterable.

# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.

number = int(input("Enter a number to generate its multiplication table: "))
multiplication_table = [number * i for i in range(1, 11)] # this will create a list of the multiplication table of the entered number from 1 to 10.
print(f"Multiplication table of {number}: {multiplication_table}") # this will print the multiplication table of the entered number. The list comprehension is a concise way to create a new list by filtering and transforming the items of an existing iterable. In this case, we are creating a new list (multiplication_table) that contains the products of the entered number and the integers from 1 to 10.


# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.
try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    result = a / b
    print(f"The result of {a} divided by {b} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed. The result is infinite.")

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt
number = int(input("Enter a number to generate its multiplication table: "))
Table=[number * i for i in range(1, 11)]
with open("Tables.txt", "a") as f:
    f.write(f"Multiplication table of {number}:\n")
    for i, val in enumerate(Table):
        f.write(f"{number} x {i+1} = {val}\n")