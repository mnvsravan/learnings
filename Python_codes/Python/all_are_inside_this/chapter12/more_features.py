# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
 print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3

# we use this walrus operartor because 

while (line := input("Enter: ")) != "quit":
    print(line)


#DURING fucntions 
def add(a: int, b: int) -> int:
    return "hello"
# we give hints like to this a , b , return by doing so
def greet(name: str) -> str:
    return "Hello " + name

def say(msg:str) -> None:
    print(msg)
say("OKOKOKOKO")



from typing import List, Tuple, Dict, Union # This line imports type hint tools from Python’s built-in typing module
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5] # we can pass only one argument in list , buut u can do like int | str , like if udk what it should be 
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)        # and if u want to do more numbers then just do like Tuple[int,...] YES u must type the dots
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid
    

# EG
people: list[tuple[str, int, float]] = [
    ("Alice", 30, 5.6),
    ("Bob", 25, 5.9),
    ("Charlie", 28, 6.1)
]
people.append(("David", 35, 5.8))
print(people)



# MATCH STATUS

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status
 


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}
# The | operator (dictionary merge operator, introduced in Python 3.9) follows this rule:

# If the same key exists in both dictionaries,
# the value from the right dictionary wins
# similarly even |= is also there
dict1 |= dict2
print(dict1) # Output: {'a': 1, 'b': 3, 'c': 4} # the difference is that in the first case we are creating a new dict and in the second case we are updating the existing dict1 with the values of dict2

#we can also use this walrus operator in with statement to open multiple files at once
with (
 open('file1.txt') as f1,
 open('file2.txt') as f2
):
    content1 = f1.read()
    content2 = f2.read()
    print("File 1 content:", content1)
    print("File 2 content:", content2)


# try statementrs
try:
    a= int(input("Enter a number: "))
    b=25/a
    print(f"You entered: {b}")
except Exception as e:
    print(e)
    # like this else works if error occurs in try block then except block will execute and if no error occurs then else block will execute
else:    print("No error occurred.")






try:
    a = int(input("Enter a number: "))
    b = 25 / a
    print(f"You entered: {b}")

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

print("hello")



# RAISE EXCEPTION
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
        
    return a / b

#FILNALLY

try:
    a = int(input("Enter a number: "))
    b=25/a
    print(f"answer is: {b}")
except Exception as e:
    print(e)
finally:    print("This will always execute, regardless of exceptions.")
# like after the try and except block finally block will always execute whether there is an error or not, it is used to clean up resources or perform any necessary final actions.
# this might look same as the else or normal code but the difference is that if there is an error in try block then except block will execute and then finally block will execute but if there is no error in try block then else block will execute and then finally block will execute, so finally block will always execute regardless of whether an exception occurred or not.
# in functions we can also use finally block to clean up resources like closing files or database connections, it is a good practice to use finally block to ensure that resources are properly released even if an error occurs.
def divide(a: int, b: int) -> float:
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    finally:
        print("Cleaning up resources...") #The finally block runs no matter what

print(divide(10, 2)) # Output: 5.0 and then Cleaning up resources...
print(divide(10, 0)) # Output: Cannot divide by zero. and then Cleaning up resources...