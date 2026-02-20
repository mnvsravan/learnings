# inheritance means that one class can inherit the properties and methods of another class. The class that inherits is called the child class or subclass and the class that is inherited from is called the parent class or superclass. Inheritance allows us to create a new class that is a modified version of an existing class, which can save time and effort when creating new classes. The child class can override the methods of the parent class to provide its own implementation, or it can add new methods and attributes to extend the functionality of the parent class.
# example of inheritance
class Animal:
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")
class Dog(Animal):
    def bark(self):
        print("This dog is barking")
k=Dog()
k.eat()   # This animal is eating (inherited from Animal class)
k.sleep()  # This animal is sleeping (inherited from Animal class)
k.bark()   # This dog is barking (defined in Dog class)

# anopther example
class Employee:
    company_name = "Tech Company"  # class variable
    def show(self):
        print(f"The company name is {self.company_name}")
class Developer(Employee):
    company_name = "Google"  # class variable
    def showlanguage(self):
        print(f"The programming language is {self.language}")

a=Developer()
a.show()  # The company name is Google (overridden class variable)
a.language = "Python"
a.showlanguage()  # The programming language is Python (defined in Developer class)
b=Employee()
b.show()  # The company name is Tech Company (class variable from Employee class)




# multiple inheritance
# here we are linking two different classes A and B to class C. So class C can access the properties and methods of both class A and class B. This is called multiple inheritance because class C is inheriting from multiple classes (A and B). In this example, class C can access the company variable from class A and the language variable from class B, as well as the show method from class A and the showlanguage method from class B. This allows us to create a new class that combines the functionality of both parent classes, which can be useful in certain situations where we want to reuse code from multiple classes.
class A:
    company= "Company A"
    def show(self):
        name="default name"
        print(f"The company name is {self.company} and the name is {name}")

class B:
    language = "Python"
    def showlanguage(self):
        print(f"The programming language is {self.language}")
class C(A, B):
    company= "Company C"
    def showskills(self):
        print(f"The company name is {self.company} and the programming language is {self.language}")

one=C()
one.show()  # The company name is Company C and the name is default name (company
one.showskills()  # The company name is Company C and the programming language is Python (company variable from C class and language variable from B class)
one.showlanguage()  # The programming language is Python (language variable from B class)
b=B()
b.showlanguage()  # The programming language is Python (language variable from B class)
c=A()
c.show()  # The company name is Company A and the name is default name (company variable from A class)

#multilevel inheritance
# here we are linking class A to class B and class B to class C. So class
#the third can access the properties and methods of both class A and class B. This is called multilevel inheritance because class C is inheriting from class B, which is inheriting from class A. In this example, class C can access the company variable from class A and the language variable from class B, as well as the show method from class A and the showlanguage method from class B. This allows us to create a new class that combines the functionality of both parent classes, which can be useful in certain situations where we want to reuse code from multiple classes.

class D:
    company= "Company D"
    def show(self):
        name="default name"
        print(f"The company name is {self.company} and the name is {name}")
class E(D):
    language = "Python"
    def showlanguage(self):
        print(f"The programming language is {self.language}")
class F(E):
    company= "Company F"
    def showskills(self):
        print(f"The company name is {self.company} and the programming language is {self.language}")
two=F()
two.show()  # The company name is Company F and the name is default name (company
two.showskills()  # The company name is Company F and the programming language is Python (company variable from F class and language variable from E class)
two.showlanguage()  # The programming language is Python (language variable from E class)
