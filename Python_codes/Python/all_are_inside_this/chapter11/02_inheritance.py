# super in inheritance OOPS
# super() is a built-in function in Python that allows you to call a method from a parent class. It is commonly used in inheritance to access the properties and methods of the parent class from the child class. When you use super(), it returns a temporary object of the parent class that allows you to call its methods and access its properties. This can be useful when you want to override a method in the child class but still want to call the original method from the parent class.

class Parent:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name of the parent is {self.name}")
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # calling the constructor of the parent class to initialize the name attribute
        self.age = age
    def show(self):
        super().show()  # calling the show method of the parent class to print the name
        print(f"The age of the child is {self.age}")
P1=Parent("Bob")
P1.show()  # The name of the parent is Bob (from the parent class)
child1 = Child("Alice", 10)
child1.show()  # The name of the parent is Alice (from the parent class)
                # The age of the child is 10 (from the child class)

# another example of super in inheritance
class A:
    def show(self):
        print("This is class A")
class B(A):
    def show(self):
        super().show()  # calling the show method of class A
        print("This is class B")
b = B()
b.show()  # This is class A (from class A)
            # This is class B (from class B)


# advanced example of super in inheritance
class C:
    def __init__(self, name, company,branch):
        self.name = name
        self.company = company
        self.branch = branch
    def show(self):
        print(f"The name is {self.name} and the company is {self.company} and the branch is {self.branch}")
class D(C):
    def __init__(self, name, company, branch, salary):
        super().__init__(name, company, branch)  # calling the constructor of class C to initialize the name, company and branch attributes
        self.salary = salary
    def show(self):
        super().show()  # calling the show method of class C to print the name, company and branch
        print(f"The salary is {self.salary}")
d1 = D("Alice", "Tech Company", "Software Development", 5000000)
d1.show()  # The name is Alice and the company is Tech Company and the branch
            # is Software Development (from class C)
            # The salary is 5000000 (from class D)  



#CLASS METHOD
class X:
    company = "Tech Company"
    @classmethod
    def showcompany(cls):
        print(f"The company name is {cls.company}")
k=X()
k.company = "Google"
k.showcompany()  # The company name is Google (class method accessing the class variable)
X.showcompany()  # The company name is Tech Company (class method accessing the class variable)

