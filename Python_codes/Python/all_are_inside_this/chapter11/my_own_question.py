class Employee:
    company = "Google"

    def __init__(self, name, age, ID, salary):
        self.ID = ID
        self.salary = salary
        self.age = age
        self.name = name
               

    @property
    def name(self):
        return (self.firstname + "." + self.lastname)

    @name.setter
    def name(self, value):
        parts = value.split()
        if (len(parts) == 2):
            self.firstname = parts[0]
            self.lastname = parts[1]
        else:
            print("Your first and last names are only valid !")

    @property
    def age(self):
        return self.finalage

    @age.setter
    def age(self, value):
        if (value < 0 or value > 60):
            raise ValueError("Your age is invalid")
        else:
            self.finalage = value

    @property
    def ID(self):
        return self.finalID

    @ID.setter
    def ID(self, value):
        if (len(value) < 0 or len(value) > 10):
            raise ValueError("You are not this company!")
        elif (value[0] != "G"):
            raise ValueError("You are not this company!")
        else:
            self.finalID = value

    @property
    def withdraw(self):
        return self.withdraw_amount

    @withdraw.setter
    def withdraw(self, amount):
        if amount > self.salary:
            raise ValueError("Cant withdraw more than salary")
        else:
            self.withdraw_amount = amount
            self.salary = self.salary - amount
            print(f"Amount of {amount} will be reduced. Remaining salary: {self.salary}")

    @property
    def credit(self):
        return self.credit_amount

    @credit.setter
    def credit(self, amount):
        if amount < 0:
            raise ValueError("There is no increment")
        else:
            self.credit_amount = amount
            self.salary = self.salary + amount
            print(f"Amount of {amount} will be Increased in your salary. New salary: {self.salary}")

    
    def display(self):   
        print(f"Your name is: {self.name}, age is: {self.age}, ID: {self.ID}, Salary: {self.salary}") 


E1 = Employee("Mnv Sravan", 18, "G5564855", 54665787685)

print(E1.name)
print(E1.age)
print(E1.ID)

E1.withdraw = 67985
E1.credit = 6565688
E1.display()