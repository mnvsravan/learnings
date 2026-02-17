# the basic synatx for function in pyton is 
# we use def and then name with :
def greet():
    """Print a greeting."""
    print("Hello")
def add(a, b):
    return a + b
def power(x, n=2):
    return x ** n
def concat(*parts, sep=" "):   # The * tells Python:“Collect all extra positional arguments into a tuple.”
                               # string.join(list_or_tuple)
                               # here this * means like the parts is a tuple

    return sep.join(parts)

def show(**kwargs):              
    for k, v in kwargs.items():
        print(k, v) #The ** tells Python:“Collect all keyword arguments into a dictionary.”

a=concat("HELLOW","SRAVAN")
print(a)
show(name="SRAVAN",age=18)

def outer(x):
    def inner(y):
        return x + y
    return inner
a=outer(10)
print(a(5))  # gives 15

# if like both are same variables 
def outer1(x):
    def inner1():
        return x + x/2
    return inner1

b = outer1(10)
print(b())

# tricky
def outer2(x):
    def inner2(x):
        return x + x/2
    return inner2
c = outer2(10)
print(c(4))
# we get ouput as 6 cuz the inner becomes x=4 not x=10


#parameters 
def greet(name):
    print(f"Wekcome,{name}")

greet("sravan")

def greet1(name1,ending):
    print(f"Wekcome,{name1}")
    print(ending)

greet1("SRAVAN","Goat")

def greet2(name2,ending1="pro"):
    print(f"Wekcome,{name2}")
    print(ending1)
greet2("Sravan") # like it prints ending1 cuz i dint passs any argument 
greet2("fguhfgeduj","fweduiugf")
   



def average():
    a = int(input("enter the number: "))
    b = int(input("enter the number: "))
    c = int(input("enter the number: "))
    Average = (a + b + c) / 3
    return Average

c = average()
print(f"The average of numbers is {c}")




# recusrion with factorial example 
def fact(n):
    if(n==1 or n==1):
        return 1
    return n*fact(n-1) # we can use else statement also
answer=fact(5)
print(f"the factorial of the number is {answer}")