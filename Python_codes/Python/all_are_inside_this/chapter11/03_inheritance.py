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
