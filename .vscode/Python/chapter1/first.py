print("Hello, World!")
# unlike C and Java, we don't need to declare a main function in Python.
# we can just write our code at the top level and it will be executed when we run the script.
# "" are used in print statements to denote string literals. We can also use '' for the same purpose.
print('Hello, World!')
# we can also use triple quotes for multi-line strings.
print("""Hello tghgfhgfhghghghhg
      tyhtrhghgh
        hghghghg""")
# to write comments in Python. Comments are ignored by the interpreter and are used to explain the code to humans.
# This is a single-line comment.
# A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added. We can import modules to use their functions and variables in our code.
# For example, we can import the math module to use its functions.
# A PIP is a package manager for Python. It allows us to install and manage additional libraries and dependencies that are not included in the standard library. We can use pip to install packages from the Python Package Index (PyPI) or other sources. For example, we can use pip to install the requests library, which allows us to make HTTP requests in Python.    
import pyjokes
joke = pyjokes.get_joke()
print(joke)