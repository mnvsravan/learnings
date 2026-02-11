import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("FUCK YOU")
engine.runAndWait()


#Another problem


import os

# Change this to the directory you want to list
directory_path = "C:/Users/Chaitanya/Current codes/learnings"

# Get the list of all files and directories
contents = os.listdir(directory_path)

print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)
