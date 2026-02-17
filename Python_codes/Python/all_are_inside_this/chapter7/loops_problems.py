#1
number=int(input("Enter a number: "))
for i in range(1,11):
    print(f"{number}*{i} = {number*i}")

    # useing while loop
i=0
while(i<10):
        print(f"{number} x {i+1} = {number*(i+1)}")
        i+=1

    #2
list=["Sravan","Goat","Sython","Developer"]
for i in list:
    if ("S" in i):
        print(f"hello brother {i}")

        #3
        digit=int(input("Enter a digit: "))
        for i in range(2,len(digit)-1):
             if(digit%2==0):
                  print("the number is even")
                  break
             else:
                  print("the number is odd")

                
#4
sum_till=int(input("Enter a number: "))
sum=0
for i in range(1,sum_till+1):
    sum+=i
print(f"The sum of first {sum_till} natural numbers is: {sum}")

#5
factorial_of=int(input("Enter a number: "))
factorial_of_num=factorial_of
for i in range(1,factorial_of):
    factorial_of_num*=i
    i=i-1
print(f"The factorial of {factorial_of} is: {factorial_of_num}")


#6
n = 3

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")    # here the end="" is used to print the spaces in the same line and not move to the next line after printing the spaces. This way we can create the pyramid shape by printing the spaces and then printing the stars in the same line.
    for k in range(2*i + 1):
        print("*", end="")
    print()                 # here the print() is used to move to the next line after printing the stars in the current line. This way we can create the pyramid shape by printing the stars in the same line and then moving to the next line after printing the stars in the current line.
 # we get the output like this:
    #   *
    #  ***
    # *****
    #another way to do this is like this:
n1 = 3

for i in range(n1):
    print(" " * (n1 - i - 1), end="")
    for j in range(2*i + 1):
        print("*", end="")
    print()

#7
n2=3
for i in range(n2):
    for j in range(2*i+1):
        print("*", end="")
    print()
    # the output of this code will be like this:
    # *
    # ***
    # *****

    #8
n3=int(input("Enter the size of the square: "))
for i in range(n3):
    if i==0 or i==n3-1:
        print("*" * n3, end="")
    else:
        print("*", end="")
        print(" " * (n3 - 2), end="")
        print("*", end="")
    print()
    # the output of this code will be like this:
    # *****
    # *   *     
    # *   *
    # *   *
    # *****
    # another way to do this is like this:
    n8 = int(input("Enter number: "))

# Top row
print("*" * n8)

# Middle rows
for i in range(n8 - 2):
    print("*", end="")
    print(" " * (n8 - 2), end="")
    print("*")

# Bottom row
print("*" * n8)


#printing table in reverse order 

table_of = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{table_of} x {11-i} = {table_of * (11-i)}")
    i=i+1
