#condition statements are used to perform different actions based on different conditions.
# if statement is used to execute a block of code if a specified condition is true.
#the synatax is 
# if condition:
#     block of code
# elif condition:
#     block of code
# else:
#     block of code
# we leave space after the colon and we have to maintain the indentation of the block of code otherwise we will get an error.
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# we can have multiple elif statements in a if statement.
marks=int(input("Enter your marks: "))
if marks>=90:
    print("You got A grade.")
elif marks>=80:
    print("You got B grade.")
elif marks>=70:
    print("You got C grade.")
elif marks>=60:
    print("You got D grade.")
else:
    print("You got F grade.")
    # we can have nested if statements in a if statement.
number=int(input("Enter a number: "))
if number>0:
    print("The number is positive.")
    if number%2==0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is negative.")

    # we use elif statement to check multiple conditions and we use else statement to execute a block of code if all the conditions are false. We can have multiple elif statements in a if statement but we can have only one else statement in a if statement. We can have nested if statements in a if statement to check for multiple conditions.
    # we cant use elif and else without if statement because elif and else are used to check for conditions in a if statement. If we use elif and else without if statement then we will get an error.
    # nested if elif ladder and etc
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


 

