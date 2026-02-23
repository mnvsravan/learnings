# first making a 2D and then making 3D from 2D
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def info(self):
        print(f"Point2D({self.x}, {self.y})")
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y) # this line calls the __init__ method of the parent class (Point2D) to initialize the x and y attributes. This allows us to reuse the code for initializing these attributes, instead of having to write it again in the Point3D class.
        self.z = z
    def info(self):
        print(f"Point3D({self.x}, {self.y}, {self.z})")
point2d = Point2D(1, 2)
point3d = Point3D(1, 2, 3)
point2d.info()  # Output: Point2D(1, 2)
point3d.info()  # Output: Point3D(1, 2, 3)

#. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"Animal: {self.name}")

class Pets(Animals):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
    def info(self):
        print(f"Pet: {self.name}, Species: {self.species}")

class Dog(Pets):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    def bark(self):
        print(f"{self.name} barks!")
    def info(self):
        print(f"Dog: {self.name}, Breed: {self.breed}")

#Create a class ‘Employee’ and add salary and increment properties to it.Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.
class Employee:
    def __init__(self, name, salary, withdrawal):
        self.name = name
        self._salary = salary
        self._withdrawal = withdrawal
        self._increment = 0

    # ---- Salary Property ----
    @property
    def salary(self):
        return self._salary

    # ---- Increment Property ----
    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        if value < 0:
            print("Increment cannot be negative")   # 🔥 No raise used
        else:
            self._increment = value

    # ---- Salary After Increment ----
    def salaryAfterIncrement(self):
        return self._salary + (self._salary * self._increment / 100)

    # ---- Withdrawal Property ----
    @property
    def withdrawal(self):
        return self._withdrawal

    @withdrawal.setter
    def withdrawal(self, value):
        if value < 0:
            print("Withdrawal cannot be negative")  # 🔥 No raise used
        else:
            self._withdrawal = value

    # ---- Salary After Withdrawal ----
    def salaryAfterWithdrawal(self):

        # 🔥 CHANGE 1:
        # Stored salary after increment in a variable
        # so we don't call the method multiple times
        final_salary = self.salaryAfterIncrement()

        if self._withdrawal > final_salary:
            print("Withdrawal cannot be greater than salary")
            print(f"You have to pay {self._withdrawal - final_salary} more to clear your dues")

            # 🔥 CHANGE 2:
            # Removed this wrong line from your original code:
            # self.salaryAfterIncrement = 0
            # Because that would overwrite the method.
            return 0

        else:
            return final_salary - self._withdrawal


# ---- Testing ----
employee = Employee("John", 50000, 10000)

print(employee.salary)

employee.increment = 1000000
print(employee.salaryAfterIncrement())

print(employee.salaryAfterWithdrawal())

# new withdrawal
employee.withdrawal = 1000000
print(employee.salaryAfterWithdrawal())



# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, c2):
        return Complex(self.real + c2.real, self.imag + c2.imag)

    def __mul__(self, c2):
        return Complex(self.real * c2.real - self.imag * c2.imag,
                       self.real * c2.imag + self.imag * c2.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"      # this __str__ method is defined to return the string representation of the Complex object. When we print a Complex object, it will call the __str__ method to get the string representation of the object, which in this case is the real part followed by the imaginary part in the format "real + imagi". This allows us to print the result of adding or multiplying Complex objects in a readable format.
c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)  # Output: 4 + 6i
print(c1 * c2)  # Output: -5 + 10i


# vector addition and multiplication
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):   # this is dot product not actualy multiplication of vectors
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    def length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    def __len__(self):
        return int(self.length())   # we can also use list methond to get the length of the vector like this
        # return len([self.x, self.y, self.z])  # this will return 3 because there are 3 components in the vector
        

# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)  # Same dimension vector

print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 * v2)  # Output: 32

print(v1 + v3)  # Output: Vector(8, 10, 12)
print(v1 * v3)  # Output: 50
print(v1.length())  # Output: 3.7416573867739413
print(len(v1))  # Output: 3 (length of the vector as an integer)

# now for the same problem i want to calc length of the vector
print("hello")
   

