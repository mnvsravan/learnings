def myFuc():
    print("This is my function!!!!")
myFuc()


print(__name__) # Output: __main__ if this file is run directly, otherwise it will be the name of the module (in this case, 'module')
if __name__ == "__main__":
    print("This code is running directly!")
else:    
    print("This code is being imported as a module.")