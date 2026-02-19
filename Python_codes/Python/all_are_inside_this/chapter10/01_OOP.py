# class in python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
class Employee: 
    # class variable          # object is created with the help of class like here it is sravan object is created with the help of Employee class
    company_name = "Tech Company"
    salary=5000000                           
    language="Python" # here company_name, salary and language are class variables because they are defined inside the class and shared among all instances of the class. They can be accessed using the class name or through any instance of the class.
    def getInfo(self):
          print(f"The name of the employee is {self.name} and the company name is {self.company_name} and the salary is {self.salary} and the language is {self.language}")
           # this self parameter is used to access the attributes and methods of the class. It is a reference to the current instance of the class and is used to access the attributes and methods of that instance. It is a convention to use self as the name of the first parameter of a method in a class, but it can be named anything else as well. The self parameter is automatically passed to the method when it is called on an instance of the class.
@staticmethod
def greet():
    print("Hello, welcome to the company!")
# we use this static cuz we dont need to access any instance variable or class variable in this method. It is a method that belongs to the class and can be called without creating an instance of the class. It is defined using the @staticmethod decorator and does not take the self parameter as its first parameter. It can be called using the class name or through any instance of the class.




sravan=Employee()
sravan.company_name="Google" # here we are changing the value of company_name for the sravan object, but it will not change the value of company_name for other objects created from the Employee class. This is because company_name is a class variable and it is shared among all instances of the class. When we change the value of company_name for one instance, it does not affect the value of company_name for other instances.
sravan.name="Sravan" # here name is an instance variable because it is defined inside the instance and it is unique to that instance. It can only be accessed through that instance and not through the class name or other instances of the class.
print(sravan.company_name)
print(sravan.salary)
print(sravan.language)
print(sravan.name)    # attributes are the variables that are defined inside a class and they can be accessed through the instances of the class. In this example, company_name, salary, language and name are attributes of the Employee class.
sravan.getInfo() # here we are calling the getInfo method of the sravan object, which will print the information of the employee. The getInfo method is defined inside the Employee class and it uses the self parameter to access the attributes of the instance and print them.
greet() # here we are calling the greet method of the Employee class, which will print a greeting message. The greet method is defined as a static method, so it can be called using the class name without creating an instance of the class.