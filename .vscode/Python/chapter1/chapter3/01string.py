name="MnvSravan"
print("Hello, " + name + "!")
# We can also use f-strings for string formatting, which is more concise and easier to read.
print(f"Hello, {name}!")
# We can also use the format() method for string formatting.
print("Hello, {}!".format(name))
# We can also use the % operator for string formatting, which is an older method.
print("Hello, %s!" % name)
# this %s is a placeholder for a string value, and it will be replaced by the value of the variable name when the string is printed. We can also use other placeholders like %d for integers and %f for floating-point numbers.
# we can use single quotes, double quotes, or triple quotes for string literals in Python. The choice is mostly a matter of style and convenience. For example, if we want to include a single quote in our string, we can use double quotes to define the string:
print("It's a nice day!")
# If we want to include a double quote in our string, we can use single quotes to define the string:
print('She said, "Hello!"')
# If we want to include both single and double quotes in our string, we can use triple quotes to define the string:
print("""She said, "It's a nice day!" """)
# these strings are immutable, which means that once we create a string, we cannot change it. However, we can create a new string by concatenating or slicing existing strings
# we can use the + operator to concatenate strings:
greeting = "Hello, " + name + "!"
print(greeting)
# we can also use the * operator to repeat a string multiple times:
echo = "Echo! " * 3
print(echo)
# we can use slicing to extract a portion of a string:
first_letter = name[0]
print(first_letter)
last_letter = name[-1]
print(last_letter)
substring = name[1:4]# this will extract the characters from index 1 to index 3 (4 is not included)
#the syntax is string[start:end], where start is the index of the first character to include and end is the index of the first character to exclude. If start is omitted, it defaults to 0. If end is omitted, it defaults to the length of the string.
print(substring)# negative indices work like this: -1 refers to the last character, -2 refers to the second-to-last character, and so on. So name[-1] gives us the last character of the string, which is 'n' in this case.
#slice with skipping characters
#syntax is string[start:end:step], where step is the number of characters to skip between each character in the slice. If step is omitted, it defaults to 1.
every_other_letter = name[::2]# this will extract every second character from the string, starting from the first character (index 0).
print(every_other_letter)
# usually if nothing is mentioned in the start it is zero and if nothing is mentioned in the end it is the length of the string. So name[::2] is equivalent to name[0:len(name):2], which means we are taking every second character from the entire string.
every_other_letter=name[1:3:4]
print(every_other_letter)
# string fuctions 
# we can use the len() function to get the length of a string:
length = len(name)
print(length)
# we can use the lower() method to convert a string to lowercase:
lowercase_name = name.lower()
print(lowercase_name)
# we can even write like this
print(name.lower())
# we can use the upper() method to convert a string to uppercase:
uppercase_name = name.upper()
# but we cant do like lower(name) because lower is a method of the string object, not a standalone function. We need to call it on a string object, like name.lower(), to convert the string to lowercase.
print(uppercase_name)
#strings also have a strip() method that removes any leading and trailing whitespace from the string:
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print(stripped_string)
# we can use the replace() method to replace a substring with another substring:
original_string = "Hello, World!"
new_string = original_string.replace("World", "Python")
print(new_string)
# we can use the split() method to split a string into a list of substrings based on a specified delimiter:
sentence = "Hello, how are you?"
words = sentence.split()# by default it splits on whitespace, but we can specify a different delimiter if needed.
print(words)
# we can use the join() method to join a list of strings into a single string with a specified delimiter:
word_list = ["Hello", "World", "Python"]
joined_string = " ".join(word_list)# this will join the words in the list with a space in between.
print(joined_string)
# there exists like also find,capitalize,startswith,endswith , count etc which we will see now 
goat="Goat"
print(goat.find("o"))# this will return the index of the first occurrence of the substring "o" in the string "Goat". In this case, it will return 1, because "o" is the second character in the string (indexing starts at 0).
print(goat.capitalize())# this will return a new string with the first character capitalized and
print(goat.startswith("G"))# this will return True if the string "Goat" starts with the substring "G", and False otherwise. In this case, it will return True, because "Goat" does indeed start with "G".
print(goat.endswith("t"))# this will return True if the string "Goat" ends with the substring "t", and False otherwise. In this case, it will return True, because "Goat" does indeed end with "t".
print(goat.count("o"))# this will return the number of occurrences of the substring "
# some more string functions
print(goat.isalpha())# this will return True if all characters in the string "Goat" are alphabetic (i.e., letters), and False otherwise. In this case, it will return True, because "Goat" consists entirely of alphabetic characters.
print(goat.isdigit())# this will return True if all characters in the string "Goat" are digits (i.e., numbers), and False otherwise. In this case, it will return False, because "Goat" contains alphabetic characters and does not consist entirely of digits.
print(goat.swapcase())# this will return a new string with all uppercase letters converted to lowercase and all lowercase letters converted to uppercase. In this case, it will return "gOAT", because the uppercase "G" is converted to lowercase "g", and the lowercase "o", "a", and "t" are converted to uppercase "O", "A", and "T".

# we can also use string slicing to reverse a string:
reversed_goat = goat[::-1]# this will reverse the string "Goat" by slicing it with a step of -1, which means we are taking every character in reverse order.
print(reversed_goat)
# we can also use the format() method to format strings with placeholders:
name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
# we can also use f-strings for the same purpose, which is more concise and easier to read:
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
# Escape characters are special characters that are used to represent certain characters in a string that would otherwise be difficult to include. For example, if we want to include a newline character in a string, we can use the escape character \n:
multiline_string = "Hello,\nWorld!"
print(multiline_string)
# we can also use the escape character to include a backslash in a string:
file_path = "C:\\Users\\Alice\\Documents\\file.txt"
print(file_path)
# we can also use raw strings to avoid having to escape backslashes. A raw string is defined by prefixing the string literal with an 'r' or 'R':
raw_file_path = r"C:\Users\Alice\Documents\file.txt"
print(raw_file_path)
# tab character can be included using \t:
tabbed_string = "Hello,\tWorld!"
print(tabbed_string)
#""" is used for multi-line strings in Python. It allows us to create strings that span multiple lines without having to use the newline character \n. For example:
multiline_string = """This is a multi-line string.
It can span multiple lines without needing to use the newline character."""
print(multiline_string)
# if we want single or double quotes in a multi-line string, we can include them without needing to escape them:
quote_string = """She said, "It's a nice day!" """
print(quote_string)
# even by / we can break a long string into multiple lines without using triple quotes:
long_string = "This is a long string that we want to break into multiple lines " \
              "without using triple quotes."
print(long_string)



# problems 
name3 = input("Enter your name: ")
print(f"{name3} Good Afternoon")




letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Enter name: ")
date = input("Enter date: ")

filled_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date) # replace chaining is a technique where we can call multiple replace() methods in a single line to replace multiple placeholders in the string. In this case, we first replace the <|Name|> placeholder with the value of the name variable, and then we replace the <|Date|> placeholder with the value of the date variable. This allows us to fill in both placeholders in one line of code.

print(filled_letter)


s = input("Enter a string with spaces: ")

print(s.find("  "))
print(s.replace("  ", " "))
