n1=int(input("Enter The  Starting Number :"))
n2=int(input("Enter The  Ending Number :"))
for i in range (n1,n2+1):
     for j in range(2,i):
         if(i%j==0):
             print(f"The number {i} is not prime")
             break
     else:
        print(f"The number {i} is prime")

#
ch = input("Enter a character: ")

if ch.isdigit():
    print("It is a digit")

elif ch.islower():
    print("It is a lowercase character")

elif ch.isupper():
    print("It is an uppercase character")

else:
    print("It is a special character")
#
import array


lst = [1, 2, 3, 4]
arr_from_list = array.array('i', lst)


tup = (5, 6, 7, 8)
arr_from_tuple = array.array('i', tup)

print("Array from list:", arr_from_list)
print("Array from tuple:", arr_from_tuple)
#
def isPalindrome(str):
    for i in range(0,len(str)//2):
        if(str[i] != str[len(str)-i-1]):
            return False
    return True
result=isPalindrome("12321")
print(result)
#

def is_sorted(list):
    if list == sorted(list):
        return True
    return False
    
l=[1,3,6]
result=is_sorted(l)
print(result)
#

def duplicates(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                return True
    return False

lst = [1, 2, 3]
result = duplicates(lst)
print(result)
#

def read_dict(d):
    
    n = int(input("Enter number of items: "))
    
    for i in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        d.update({key:value})
    
    return d
    
def inverse(d):
    inv={}
    for i in d:
        key=d[i]
        value=i
        inv.update({key:value})
    return inv
c={}
d=read_dict(c)
print(d)
inverse=inverse(c)
print(inverse)

#

s = "Apple"
result = ""

for i in range(len(s)):
    result += s[i]
    if i != len(s) - 1:
        result += ","

print(result)

#

rows=int(input("Enter Number of rows"))
coloumns=int(input("Enter Number of coloumns"))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(coloumns):
        val=int(input(f"Enter the Value for M[{i}][{j}]: "))
        row.append(val)
    matrix.append(row)
for i in matrix:
    for values in i:
        print(f"{values}"+" ", end="")
    print()


#


rows1 = int(input("Enter the numbers of rows1: "))
rows2 = int(input("Enter the numbers of rows2: "))
col1 = int(input("Enter the numbers of col1: "))
col2 = int(input("Enter the numbers of col2: "))

matrix1 = []
matrix2 = []
matrix3 = []

# Input matrix1
for i in range(rows1):
    row1 = []
    for j in range(col1):
        value = int(input(f"Enter the value for M1[{i}][{j}]: "))
        row1.append(value)
    matrix1.append(row1)

# Input matrix2
for i in range(rows2):
    row2 = []
    for j in range(col2):
        value = int(input(f"Enter the value for M2[{i}][{j}]: "))
        row2.append(value)
    matrix2.append(row2)

# Check condition
if col1 != rows2:
    print("Matrix multiplication not possible")
else:
    # Multiplication
    for row in matrix1:
        row3 = []
        for j in range(col2):
            sum_val = 0
            for k in range(col1):
                sum_val += row[k] * matrix2[k][j]
            row3.append(sum_val)
        matrix3.append(row3)

    # Print result
    print("Result:")
    for row in matrix3:
        for val in row:
            print(val, end=" ")
        print()

        #


        # Function to validate phone number
def validate_phone(phone):
    if len(phone) == 10 and phone.isdigit():
        return True
    return False

# Function to validate email
def validate_email(email):
    # Must contain exactly one @
    if email.count('@') != 1:
        return False
    
    parts = email.split('@')
    local = parts[0]
    domain = parts[1]
    
    # Local part should not be empty
    if local == "":
        return False
    
    # Domain must contain at least one dot
    if '.' not in domain:
        return False
    
    # Domain should not start or end with dot
    if domain.startswith('.') or domain.endswith('.'):
        return False
    
    return True

# Input
phone = input("Enter phone number: ")
email = input("Enter email id: ")

# Validation
if validate_phone(phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

if validate_email(email):
    print("Valid email id")
else:
    print("Invalid email id")

    

    
