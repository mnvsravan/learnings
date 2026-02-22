# here the operator overloading is done by defining the special method __add__ in the class Point
# this __add__ method is called when we use the + operator to add two Point objects. It takes two parameters, self and other, which refer to the two Point objects being added. The method returns a new Point object with the x and y coordinates calculated by adding the corresponding coordinates of the two Point objects. This allows us to use the + operator to add two Point objects in a natural way, just like we would add two numbers or two lists.
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n
num1 = Number(5)
num2 = Number(10)
result = num1 + num2
print(result)  # Output: 5
# In this example, the __add__ method is defined to return the value of self.n, which is 5. When we add num1 and num2 using the + operator, it calls the __add__ method of num1, which returns 5, regardless of the value of num2. Therefore, the result of num1 + num2 is 5.

# hence we need to do like this 
class Number1:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n
num1 = Number1(5)
num2 = Number1(10)

result = num1 + num2
print(result)  # Output: 15
# In this example, the __add__ method is defined to return the sum of self.n and other.n. When we add num1 and num2 using the + operator, it calls the __add__ method of num1, which returns 5 + 10, resulting in 15. Therefore, the result of num1 + num2 is 15.

# if u want to more than 2 numbers then we can do like this
class Number2:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Number2(self.n + other.n) # we do this because we want to return a new Number2 object with the sum of the two numbers, instead of just returning the sum as a number. This allows us to chain multiple additions together, like num1 + num2 + num3 + num4, and still get a Number2 object as the result.

    def __str__(self):
        return str(self.n) # this __str__ method is defined to return the string representation of the Number2 object. When we print a Number2 object, it will call the __str__ method to get the string representation of the object, which in this case is the value of self.n converted to a string. This allows us to print the result of adding multiple Number2 objects in a readable format.


num1 = Number2(5)
num2 = Number2(10)
num3 = Number2(15)
num4 = Number2(20)

result = num1 + num2 + num3 + num4
print(result)


# just like def __add__ we can also define other special methods like __sub__, __mul__, __truediv__,,floor_div__, __mod__, __pow__, etc. to overload the corresponding operators for our custom class. This allows us to use these operators in a natural way with our custom objects, just like we would with built-in types.
# even __str__ , __len__ for string representation and length of the object respectively. and even __eq__, __ne__, __lt__, __le__, __gt__, __ge__ for comparison operators.
# example of __str and __ len is given below
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
point = Point(3, 4)
print(point)  # Output: Point(3, 4)
print(len(point))  # Output: 5

