# del 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
s1 = Student("Rohit", 20)
print(s1.name) # this will print the name of the student, which is "R
del s1
print(s1.name) # this will raise an error because the object s1 has been deleted using the del statement. The del statement is used to delete objects in Python, and once an object is deleted, it cannot be accessed or used anymore.
 
# priviate key attribute
class Student1:
    def __init__(self, name, age,marks):
        self.__name = name # this is a private attribute because it is prefixed with double underscores (__). It cannot be accessed directly from outside the class.
        self.__age = age # this is also a private attribute for the same reason as above.
        self.marks = marks # this is a public attribute because it does not have any prefix. It can be accessed directly from outside the class.
s2 = Student1("Rohit", 20, 85)
print(s2.__name) # this will raise an error because __name is a private attribute and cannot be accessed directly from outside the class. To access private attributes, we can use getter methods or property decorators within the class.
print(s2.marks) # this will print the marks of the student, which is 85, because marks is a public attribute and can be accessed directly from outside the class.
print(s2._Student1__name) # this will print the name of the student, which is "Rohit", by using name mangling to access the private attribute __name. In Python, private attributes are name-mangled to prevent accidental access, and they can be accessed using the syntax _ClassName__attributeName. However, it is generally not recommended to access private attributes directly from outside the class, as it goes against the principles of encapsulation and can lead to code that is difficult to maintain and debug.

# BUT WE CAN USE THE __ THING IN THE CLASS TO ACCESS THE PRIVATE ATTRIBUTES
class Student2:
    def __init__(self, name, age, marks):
        self.__name = name
        self.__age = age
        self.marks = marks
    
    def get_name(self):
        return self.__name # this is a getter method that allows us to access the private attribute __name from outside the class. It returns the value of __name when called.

    def get_age(self):
        return self.__age # this is a getter method that allows us to access the private attribute __age from outside the class. It returns the value of __age when called.
s3 = Student2("Rohit", 20, 85)
print(s3.get_name()) # this will print the name of the student, which is "Rohit", by calling the getter method get_name() that we defined in the Student2 class. This is a proper way to access private attributes from outside the class while maintaining encapsulation.
print(s3.get_age()) # this will print the age of the student, which is 20, by calling the getter method get_age() that we defined in the Student2 class. This is a proper way to access private attributes from outside the class while maintaining encapsulation.
print(s3.__name) # this will raise an error because __name is a private attribute and cannot be accessed directly from outside the class. We should use the getter method get_name() to access the name of the student instead of trying to access the private attribute directly.



# INHERITANCE
class Car:
    @staticmethod
    def start():
        print("Car is starting...") # this is a static method that belongs to the Car class. It can be called without creating an instance of the Car class.
    @staticmethod
    def stop():
        print("Car is stopping...") # this is another static method that belongs to the Car class. It can also be called without creating an instance of the Car class.
class Toyota(Car): # this is a subclass of the Car class, which means it inherits all the methods and attributes of the Car class.
    def __init__(self,brand):
        self.brand = brand # this is an instance attribute that belongs to the Toyota class. It is initialized when an instance of the Toyota class is created.
class Fortuner(Toyota): # this is another subclass of the Car class, which also inherits all the methods and attributes of the Car class.
    def __init__(self,type):
        self.type = type # this is an instance attribute that belongs to the Fortuner class. It is initialized when an instance of the Fortuner class is created.
fortuner = Fortuner("SUV") # this creates an instance of the Fortuner class with the type "SUV".
fortuner.start() # this will call the start() method from the Car class, which is inherited by the Fortuner class through the Toyota class. It will print "Car is starting..." to the console.
fortuner.stop() # this will call the stop() method from the Car class, which is inherited by the Fortuner class through the Toyota class. It will print "Car is stopping..." to the console.

# MULTIPLE INHERITANCE
class A:
    def method_a(self):
        print("This is method A from class A") # this is a method that belongs to class A. It can be called on instances of class A or any subclass that inherits from class A.
class B:
    def method_b(self):
        print("This is method B from class B") # this is a method that belongs to class B. It can be called on instances of class B or any subclass that inherits from class B.
class C(A, B): # this is a subclass that inherits from both class A and class B, demonstrating multiple inheritance.
    def method_c(self):
        print("This is method C from class C") # this is a method that belongs to class C. It can be called on instances of class C.
c_instance = C() # this creates an instance of class C.
c_instance.method_a() # this will call the method_a() from class A, which is inherited by class C. It will print "This is method A from class A" to the console.
c_instance.method_b() # this will call the method_b() from class B, which is inherited by class C. It will print "This is method B from class B" to the console.
c_instance.method_c() # this will call the method_c() from class C. It will print "This is method C from class C" to the console. This demonstrates that class C has access to methods from both class A and class B due to multiple inheritance.

#super() function
class Parent:
    def __init__(self, name):
        self.name = name # this is an instance attribute that belongs to the Parent class. It is initialized when an instance of the Parent class is created.
class Child(Parent): # this is a subclass that inherits from the Parent class.
    def __init__(self, name, age):
        super().__init__(name) # this calls the __init__ method of the Parent class to initialize the name attribute for the Child class.
        self.age = age # this is an instance attribute that belongs to the Child class. It is initialized when an instance of the Child class is created.
child_instance = Child("Rohit", 20) # this creates an instance of the Child class with the name "Rohit" and age 20.
print(child_instance.name) # this will print the name of the child, which is "Rohit", by accessing the name attribute that was initialized in the Parent class using the super() function in the Child class.
print(child_instance.age) # this will print the age of the child, which is 20, by accessing the age attribute that was initialized in the Child class. The super() function allows us to call methods from the parent class, which is useful for initializing attributes that are defined in the parent class when creating an instance of the child class.


class Car:
    def __init__(self, brand):
        self.brand = brand
    @staticmethod
    def start():
        print("Car is starting...")


class Toyota(Car):
    def __init__(self, brand, type, model):
        super().__init__(brand)   # ✅ now brand exists
        self.type = type
        self.model = model
        super().start()  # ✅ this will call the start() method from the Car class, which is inherited by the Toyota class. It will print "Car is starting..." to the console when an instance of the Toyota class is created.


# creating object
t = Toyota("Toyota", "SUV", "Fortuner")

print(t.brand)
print(t.type)
print(t.model)


# classmethod
class Person:
    name="anpnymous"
    def changename(self, new_name):
        Person.name = new_name # U can also use like self.__class__.name = new_name
p1 = Person() # this creates an instance of the Person class.
print(p1.name) # this will print the name of the person, which is "anonymous
p1.changename("Rohit") # this will call the changename() method on the instance p1 and change the name attribute to "Rohit".
print(p1.name) # this will print the updated name of the person, which is "Rohit", after calling the changename() method on the instance p1. The changename() method modifies the name attribute of the instance, allowing us to change the name of the person after the instance has been created.

# CORRECT METHOD
class Person:
    name = "anonymous"
    
    @classmethod
    def changename(cls, new_name):
        cls.name = new_name # this will change the name attribute for the entire class, affecting all instances of the Person class.
p1 = Person() # this creates an instance of the Person class.
print(p1.name) # this will print the name of the person, which is "anonymous
Person.changename("Rohit") # this will call the changename() class method on the Person class and change the name attribute to "Rohit" for all instances of the Person class.
print(p1.name) # this will print the updated name of the person, which is "Rohit", after calling the changename() class method on the Person class. Since changename() is a class method, it modifies the name attribute for the entire class, affecting all instances of the Person class, including p1.

# PROPERTY DECORATOR

class Student:
    def __init__(self,name,maths,physics,chemistry):
        self.name = name
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry
    @property
    def average(self):
        return (self.maths + self.physics + self.chemistry) / 3 # this will calculate the average of the three subjects and return it when the average property is accessed. or the final value of the average will be the sum of the marks in maths, physics and chemistry divided by 3.
s1 = Student("Rohit", 85, 90, 80) # this creates an instance of the Student class with the name "Rohit" and marks in maths, physics and chemistry.
print(s1.name) # this will print the name of the student, which is "Rohit".
print(s1.maths) # this will print the marks in maths, which is 85
print(s1.physics) # this will print the marks in physics, which is 90
print(s1.chemistry) # this will print the marks in chemistry, which is 80
print(s1.average) # this will print the average marks of the student, which is calculated using the average property method. The @property decorator allows us to access the average as if it were an attribute, even though it is actually a method that calculates the average on the fly when accessed.


# Polymorphism

# LIKE these dunder methods are also used for operator overloading , overloading is like we have a method that can take different types of arguments and perform different operations based on the type of arguments passed. For example, the __add__ method can be used to add two numbers or concatenate two strings based on the type of arguments passed.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def getInfo(self):
        return f"{self.real} + {self.imag}i" # this will return a string representation of the complex number in the form "real + imagi".
    
    def __add__(self, other):
        new_complex=self.real + other.real
        new_imag=self.imag + other.imag
        return Complex(new_complex, new_imag) # this will add the real and imaginary parts
    def __str__(self):
        return f"{self.real} + {self.imag}i" # this will return a string representation of the complex number when the object is printed. The __str__ method is a special method that is called when the object is converted to a string, such as when it is printed. It allows us to define how the object should be represented as a string, which can be useful for debugging and displaying information about the object in a human-readable format.
    def __sub__(self, other):
        new_complex=self.real - other.real
        new_imag=self.imag - other.imag
        return Complex(new_complex, new_imag) # this will subtract the real and imaginary parts of two complex numbers and return a new Complex object with the result. The __sub__ method is a special method that is called when the subtraction operator (-) is used between two objects of the Complex class. It allows us to define how the subtraction operation should be performed for Complex objects, enabling us to use the - operator to subtract complex numbers in a natural way.
    def __mul__(self, other):
        new_complex=self.real * other.real - self.imag * other.imag
        new_imag=self.real * other.imag + self.imag * other.real
        return Complex(new_complex, new_imag) # this will multiply two complex numbers using the formula (a + bi)(c + di) = (ac - bd) + (ad + bc)i, where a and b are the real and imaginary parts of the first complex number, and c and d are the real and imaginary parts of the second complex number. The __mul__ method is a special method that is called when the multiplication operator (*) is used between two objects of the Complex class. It allows us to define how the multiplication operation should be performed for Complex objects, enabling us to use the * operator to multiply complex numbers in a natural way.
    # LIKE THESE SO MANY EXIST FOR DIFFERENT OPERATORS LIKE __truediv__ for division, __floordiv__ for floor division, __mod__ for modulus, __pow__ for exponentiation, etc. These dunder methods allow us to define how our custom objects should behave with respect to various operators, enabling us to use operator overloading to make our code more intuitive and easier to read when working with custom classes.










c1 = Complex(2, 3) # this creates an instance of the Complex class with real part 2 and imaginary part 3.
c2 = Complex(4, 5) # this creates another instance of the Complex class
c3= c1 + c2 # this will add the two complex numbers using the __add__ method defined in the Complex class. It will return a new Complex object with the real part equal to the sum of the real parts of c1 and c2, and the imaginary part equal to the sum of the imaginary parts of c1 and c2.
print(c3.getInfo()) # this will print the string representation of the resulting complex number c


#Q

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary   # normal attribute
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT",76000)
        
    def showDetails(self):
        
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)
        print("Age", self.age)
        print("name", self.name)
engg1 = Engineer("Elon Musk", 40)

engg1.showDetails()