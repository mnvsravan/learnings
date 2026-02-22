#@PROPERTY DECORATORS and @ setter methods
# property decorators are used to define a method as a property of a class. This allows us to access the method as if it were an attribute of the class. The @property decorator is used to define a method as a property, and the @setter decorator is used to define a method as a setter for that property. This allows us to control the access and modification of the property, and it can be useful for encapsulation and data validation.
class Employee:
    def __init__(self , name , company_name , salary , language):
        self.name = name
        self.company_name = company_name
        self.salary = salary
        self.language = language

    @property
    def getInfo(self):
        return f"The name of the employee is {self.name} and the company name is {self.company_name} and the salary is {self.salary} and the language is {self.language}"

    @getInfo.setter
    def getInfo(self, info):
        name, company_name, salary, language = info.split(",")
        self.name = name.strip()
        self.company_name = company_name.strip()
        self.salary = int(salary.strip())
        self.language = language.strip()
e1=Employee(" MNV Sravan", "Tech Company" , 5000000 , "Python")
print(e1.getInfo)  # The name of the employee is Sravan and the company name is Tech Company and the salary is 5000000 and the language is Python (accessing the getInfo property)
e1.getInfo = "John , Google , 4000000 , Java"  # setting the getInfo property using the setter method
print(e1.getInfo)  # The name of the employee is John and the company name is Google and the salary is 4000000 and the language is Java (accessing the getInfo property after setting it using the setter method)







class Person:
    def __init__(self, name, age):
        self.name = name   # calls setter
        self.age = age     # calls setter

    # ---- NAME PROPERTY ----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        parts = value.split()

        if len(parts) < 2:
            raise ValueError("Please provide both first and last name")

        first_name = parts[0]
        last_name = parts[1]

        self._name = first_name + " " + last_name

    # ---- AGE PROPERTY ----
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age


# ---- Example ----
p = Person("John Doe", 7)
print(p.name)   # John Doe
print(p.age)    # 7




class Aura:
    a = 1

    def show(self):
        print(f"The class attribute of a is {self.a}")

    @property
    def name(self):
        return f" first name is {self.fname} and last name is {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Aura()
e.a = 45

e.name = "Harry Khan"
print(e.name)

e.show()