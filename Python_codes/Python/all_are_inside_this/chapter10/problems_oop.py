#1
class Employee:
    company_name = "Microsoft"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
    
    def getInfo(self):
        print(f"The name of the employee is {self.name} and the company name is {Employee.company_name} and the salary is {self.salary} and the language is {self.language}")

# Object should be created OUTSIDE the class
Employee1 = Employee("Sravan", 5000000, "Python")
Employee1.getInfo()
Employee2 = Employee("John", 4000000, "Java")
Employee2.getInfo()
for i in range(1, 11):
    emp = Employee(f"Employee{i}", i*100000, "Python")
    emp.getInfo()

for i in range(1, 11):
    input_name = input("Enter the name of the employee: ")
    input_salary = int(input("Enter the salary of the employee: "))
    input_language = input("Enter the programming language of the employee: ")
    emp = Employee(input_name, input_salary, input_language)
    emp.getInfo()


#2
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
    def sqaure(self):
        return self.num1 ** 2, self.num2 ** 2
    def cube(self):
        return self.num1 ** 3, self.num2 ** 3
    def sqaure_root(self):
        return self.num1 ** 0.5, self.num2 ** 0.5

calculate_for= Calculator(10, 5)
print(calculate_for.add())
print(calculate_for.subtract())
print(calculate_for.multiply())
print(calculate_for.divide())
print(calculate_for.sqaure())
print(calculate_for.cube())
print(calculate_for.sqaure_root())
#or 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
calculate_for= Calculator(num1, num2)
print(calculate_for.add())
print(calculate_for.subtract())
print(calculate_for.multiply())
print(calculate_for.divide())
print(calculate_for.sqaure())
print(calculate_for.cube())
print(calculate_for.sqaure_root())

#3
class Demo:
    age = 0   # class variable

    def __init__(self):
        pass

demo1 = Demo()
demo1.age = 30

print(demo1.age)   # 30 (instance overrides class variable)
print(Demo.age)    # 0 (class variable remains unchanged)

#4
from random import randint

class Train:
    def __init__(self, Train_number):
        self.Train_number = Train_number

    def book(self, From, To):
        print(f"Your train number is {self.Train_number} and you are travelling from {From} to {To}")

    def status(self):
        print(f"Your train number is {self.Train_number} and it's running on time")

    def cancel(self):
        print(f"Your train number is {self.Train_number} and your ticket is cancelled")

    def delay(self):
        print(f"Your train number is {self.Train_number} and your train is delayed by 1 hour")

    def arrival_time(self):
        print(f"Your train number is {self.Train_number} and it will arrive at the destination at 10:00 AM")

    def departure_time(self):
        print(f"Your train number is {self.Train_number} and it will depart from the source at 6:00 AM")

    def getfare(self, From, To):
        print(f"Your train number is {self.Train_number} and it's from {From} to {To} and the fare is {randint(500, 10000)} INR")


train1 = Train(12345)

train1.book("Hyderabad", "Bangalore")
train1.status()
train1.cancel()
train1.delay()
train1.arrival_time()
train1.departure_time()
train1.getfare("Hyderabad", "Bangalore")


# its not nessasry to only use self as the first parameter in the method of a class. We can use any name we want, but it is a convention to use self to refer to the instance of the class. The self parameter is used to access the attributes and methods of the instance within the class. It allows us to differentiate between instance variables and local variables within the method. Using self is a common practice in Python and it helps to improve code readability and maintainability.