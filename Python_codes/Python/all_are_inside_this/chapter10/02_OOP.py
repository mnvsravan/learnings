# constructor in oop
class Employee:
    def __init__(self, name, company_name, salary, language): # this __init_ method is a constructor in Python. It is a special method that is called when an object is created from a class. It is used to initialize the attributes of the object with the values passed as arguments when the object is created. The self parameter is used to refer to the current instance of the class and it allows us to access the attributes and methods of that instance.
        self.name = name                                       # dunder init is a special method in Python that is used to initialize the attributes of an object when it is created. It is called automatically when an object is created from a class and it takes the self parameter as its first parameter, which refers to the current instance of the class. The other parameters are used to pass values to initialize the attributes of the object. In this example, name, company_name, salary and language are the parameters that are passed to the constructor to initialize the attributes of the Employee object.
        # this constructor calls directly when we create an object from the Employee class and it initializes the attributes of the object with the values passed as arguments. For example, when we create an object like this: sravan = Employee("Sravan", "Google", 5000000, "Python"), the __init__ method is called automatically and it initializes the name attribute with "Sravan", the company_name attribute with "Google", the salary attribute with 5000000 and the language attribute with "Python". This allows us to create objects with specific attributes without having to set them manually after creating the object.
        self.company_name = company_name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The name of the employee is {self.name} and the company name is {self.company_name} and the salary is {self.salary} and the language is {self.language}")


goat=Employee("Sravan", "Tech Company", 5000000, "Python")
goat.getInfo() # here we are creating an object named goat from the Employee class and passing the values "Sravan", "Tech Company", 5000000 and "Python" to the constructor to initialize the attributes of the goat object. Then we are calling the getInfo method of the goat object to print the information of the employee. The getInfo method uses the self parameter to access the attributes of the goat object and print them in a formatted string.