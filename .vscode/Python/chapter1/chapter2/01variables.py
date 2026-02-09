# a variable is a name that refers to a value
# we can assign a value to a variable using the assignment operator (=)
x = 5
y=8
# we can also assign multiple variables at once
a, b, c = 1, 2, 3
# we can also assign the same value to multiple variables
m = n = o = 10
print("sum is ",x+y)

#DATA TYPES 
# Python has several built-in data types, including:
# the primitive data types: int, float, str, bool, none
#int
age = 10
#float
pi = 3.14
#str
name = "Chaitanya"
#bool
is_student = True
#none
nothing = None
#here none means that the variable "nothing" does not have any value assigned to it. It is a special value that represents the absence of a value. We can use None to indicate that a variable is empty or has no value.

#rulz for variable names in Python:
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# 2. Variable names can only contain letters, numbers, and underscores.
# 3. Variable names are case-sensitive (age and Age are different variables).
# 4. Variable names cannot be the same as Python keywords (e.g., if, else, while, for, etc.).
# 5. Variable names should be descriptive and meaningful to improve code readability.
# 6. no space is allowed in variable names, we can use underscores to separate words (e.g., first_name, last_name).

#opertors in Python:
# 1. Arithmetic operators: +, -, *, /, %, **, //
# 2. Comparison operators: ==, !=, >, <, >=, <=
# 3. Logical operators: and, or, not
#and, or, not are used to combine multiple conditions in an if statement or to negate a condition. For example:
x = 5
y = 10
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y) # this means x raised to the power of y
print(x//y) # this means floor division, it returns the quotient without the remainder. For example, 5//2 will return 2, because 5 divided by 2 is 2 with a remainder of 1.
# for remainder we can use the modulus operator (%), which returns the remainder of the division. For example, 5%2 will return 1, because 5 divided by 2 is 2 with a remainder of 1.
print(5%3) # this will return 2, because 5 divided by 3 is 1 with a remainder of 2.

#assignment operators: =, +=, -=, *=, /=, %=, **=, //=
x = 5
x += 3 # this is equivalent to x = x + 3
print(x) # this will print 8
x *= 2 # this is equivalent to x = x * 2
print(x) # this will print 16
x /= 4 # this is equivalent to x = x / 4
print(x) # this will print 4.0
x %= 3 # this is equivalent to x = x % 3
print(x) # this will print 1.0
x **= 2 # this is equivalent to x = x ** 2
print(x) # this will print 1.0
x //= 2 # this is equivalent to x = x // 2
print(x) # this will print 0.0

#comparison operators: ==, !=, >, <, >=, <=
x = 5
y = 10
print(x == y) # this will print False, because x is not equal to y
print(x != y) # this will print True, because x is not equal to y
print(x > y) # this will print False, because x is not greater than y
print(x < y) # this will print True, because x is less than y
print(x >= y) # this will print False, because x is not greater than or equal to y
print(x <= y) # this will print True, because x is less than or equal to y

#logical operators: and, or, not
x = 5
y = 10
print(x > 0 and y > 0) # this will print True, because both
print(x > 0 or y < 0) # this will print True, because at least one of the conditions is true    
print(not(x > 0)) # this will print False, because x is greater than 0, so the condition is true, and not true is false.
                # if we want to check if a number is even or odd, we can use the modulus operator (%) to check if the number is divisible by 2. For example:
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

    #input function in Python:
    # the input() function is used to take input from the user. It returns a string
name = input("Enter your name: ")
print("Hello, " + name + "!") # we can add strings using the + operator, this is called string concatenation. In this case, we are concatenating the string "Hello, " with the value of the variable name and the string "!" to create a greeting message.
# for integer input, we can use the int() function to convert the string input to an integer. For example:
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.") # we can use the str() function to convert the integer age back to a string for concatenation.
# type conversion in Python:
# we can convert between different data types using built-in functions like int(), float(), str(), bool(), etc. For example:
x = 5
y = float(x) # this will convert the integer x to a float
print(y) # this will print 5.0
z = str(x) # this will convert the integer x to a string
print(z) # this will print "5"
m="rdsgfdg"
h=int(m) # this will raise a ValueError, because the string "rdsgfdg" cannot be converted to an integer. We can use a try-except block to handle this error gracefully. For example:
l="56"
p=int(l) # this will convert the string "56" to the integer 56
print(p) # this will print 56

# sum of two numbers using input and type conversion:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)
# we can check the type of a variable using the type() function. For example:
x = 5
print(type(x)) # this will print <class 'int'>
# you can also do like 
d=input("Enter a value: ")
print(type(d)) # this will print <class 'int'>, because num1 is an integer variable.