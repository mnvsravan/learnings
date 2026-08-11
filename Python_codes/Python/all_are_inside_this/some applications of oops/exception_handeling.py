# IndexError
# The IndexError is thrown when trying to access an item at an invalid index.
# L = [1,2,3]
# L[100]

# ModuleNotFoundError
# The ModuleNotFoundError is thrown when a module could not be found.
# import mathi
# math.floor(5.3)

# KeyError
# The KeyError is thrown when a key is not found
# d = {'name':'nitish'}
# d['age']

# TypeError
# The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
# 1 + 'a'

# ValueError
# The ValueError is thrown when a function's argument is of an inappropriate type.
# int('a')

# NameError
# The NameError is thrown when an object could not be found.
# print(k)

#  AttributeError
# L = [1,2,3]
# L.upper()

try:
  with open('sample1.txt','r') as f:
    print(f.read())
except:
  print('sorry file not found')


try:
  m=5
#   f = open('sample1.txt','r')
  print(f.read())
  m=4
  print(m)

  L = [1,2,3]
  L[100]
except FileNotFoundError:
  print('file not found')
except NameError:
  print('variable not defined')
except ZeroDivisionError:
  print("can't divide by 0")
except Exception as e: # imp
  print(e)


## else and finnally
with open('sample1.txt','w') as f:
    f.write('hello world')

try:
  with open('sample1.txt','r') as f:
    print(f.read()) 
except FileNotFoundError:
  print('file not found')
else:
  print('file read successfully')
finally:
  print('this will always execute')


# raise errors
# raise ZeroDivisionError('aise hi try kar raha hu')

class Bank:

  def __init__(self,balance):
    self.balance = balance

  def withdraw(self,amount):
    if amount < 0:
      raise Exception('amount cannot be -ve')
    if self.balance < amount:
      raise Exception('paise nai hai tere paas')
    self.balance = self.balance - amount

obj = Bank(10000)
try:
  obj.withdraw(15000)
except Exception as e:
  print(e)
else:
  print(obj.balance)


# creating own exceptions

class MyException(Exception):
  def __init__(self,message):
    print(message)

class Bank1:

  def __init__(self,balance):
    self.balance = balance

  def withdraw(self,amount):
    if amount < 0:
      raise MyException('amount cannot be -ve nigga')
    if self.balance < amount:
      raise MyException('paise nai hai tere paas F')
    self.balance = self.balance - amount

obj2 = Bank1(10000)
try:
  obj2.withdraw(-5000)
except MyException as e:
  pass
else:
  print(obj2.balance)

# a good practical example 

class SecurityError(Exception):

  def __init__(self,message):
    print(message)

  def logout(self):
    print('logout')

class Google:

  def __init__(self,name,email,password,device):
    self.name = name
    self.email = email
    self.password = password
    self.device = device

  def login(self,email,password,device):
    if device != self.device:
      raise SecurityError('bhai teri to lag gayi')
    if email == self.email and password == self.password:
      print('welcome')
    else:
      print('login error')



obj1 = Google('nitish','nitish@gmail.com','1234','android')

try:
  obj1.login('nitish@gmail.com','1234','windows')
except SecurityError as e:
  e.logout()
else:
  print(obj1.name)
finally:
  print('database connection closed')