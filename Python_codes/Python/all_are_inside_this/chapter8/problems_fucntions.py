def greatest(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c

num = greatest(56, 87, 34)
print(f"The greatest number is {num}")


def conversion(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

answer = float(input("Enter the Celsius value: "))
answer1 = conversion(answer)
print(f"The value of Celsius in Fahrenheit is {round(answer1,2)}")


def sum(number):
    if(number==0):
        return 0
    elif(number==1):
        return 1
    return (number)+sum(number-1)
sum_of=sum(10)
print(f"the sum of till this number is {sum_of}")

def pattern(n):
    for i in range(0,n):
        print("*"*(n-i))
        i=i-1
pattern(3)

# using recusrion 
def recur(n):
    if n == 0:
        return 0
    else:
        for i in range(n):
            print("*" * n)
        return recur(n - 1)

recur(3)

# removing with stripping 
def rem(l, word):
    n = []
    for item in l:
        n.append(item.strip(word))
    return n

l = ["sravan", "ravan", "craven"]
print(rem(l, "an"))






