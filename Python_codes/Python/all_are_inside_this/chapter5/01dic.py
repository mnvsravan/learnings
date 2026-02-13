#dictionary is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure in Python. Each key in a dictionary must be unique and immutable (such as strings, numbers, or tuples), while the values can be of any data type and can be duplicated.
#creating a dictionary
myMarks={
    "Maths": 90,
    "Science": 85,
    "English": 95,
    "History": 80,
    "hindi": 88,
    "telugu": 92
# we must keep , after each key-value pair except the last one. The keys are enclosed in quotes because they are strings, and the values are integers representing the marks obtained in each subject.

}
print(myMarks) # this will print the entire dictionary myMarks to the console, showing all the key-value pairs.
print(myMarks["Maths"]) # this will access the value associated with the key "Maths" in the dictionary myMarks and print it to the console. In this case, it will print 90, which is the marks obtained in Maths.
# we can do anything and aissign like our wish like 
stuff={
    "name": "John",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"],
    "is_student": False,
    70 : "my fav number"
}
print(stuff) # this will print the entire dictionary stuff to the console, showing all the key-value pairs, including the string keys and their corresponding values, as well as the integer key 70 and its associated value "my fav number".
# but the question is like can we keep tuple , list or dictionary as a key in a dictionary? The answer is no, we cannot use mutable data types like lists or dictionaries as keys in a dictionary because they are not hashable. However, we can use immutable data types like tuples as keys in a dictionary.
# for example, we can use a tuple as a key in a dictionary like this:
my_dict = {
    (1, 2): "This is a tuple key",
    (3, 4): "This is another tuple key"
}
print(my_dict) # this will print the entire dictionary my_dict to the console, showing the tuple keys and their corresponding values. The output will be: {(1, 2): 'This is a tuple key', (3, 4): 'This is another tuple key'}
#print(myMarks[90]) # this will raise a KeyError because 90 is not a key in the dictionary myMarks. The keys in myMarks are "Maths", "Science", "English", "History", "hindi", and "telugu". To access the value associated with the key "Maths", we should use myMarks["Maths"] instead of myMarks[90].
#before going to the functions in dictionary we will see how to add a new key-value pair to the dictionary and how to update the value of an existing key in the dictionary.
# adding a new key-value pair to the dictionary
myMarks["Geography"] = 87 # this will add a new key "Geography" with the value 87 to the dictionary myMarks. If the key "Geography" already exists in the dictionary, it will update its value to 87.
print(myMarks) # this will print the updated dictionary myMarks to the console, showing the new key-value pair "Geography": 87 added to the dictionary. The output will include all the previous key-value pairs along with the new one.
# updating the value of an existing key in the dictionary
myMarks["Maths"] = 95 # this will update the value associated with the key "Maths" in the dictionary myMarks to 95. If the key "Maths" does not exist in the dictionary, it will add a new key-value pair "Maths": 95 to the dictionary.
print(myMarks) # this will print the updated dictionary myMarks to the console, showing the updated value for the key "Maths". The output will include all the previous key-value pairs along with the updated value for "Maths".
# we can also use the update() method to add or update key-value pairs in a dictionary. The update() method takes a dictionary as an argument and adds its key-value pairs to the original dictionary. If a key already exists in the original dictionary, its value will be updated with the value from the new dictionary.
new_marks = {
    "Physics": 89,
    "Chemistry": 92,
    "Maths": 98 # this will update the value of "Maths" to 98 in the original dictionary myMarks.
}
myMarks.update(new_marks) # this will add the key-value pairs from the new_marks dictionary to the myMarks dictionary. If a key already exists in myMarks, its value will be updated with the value from new_marks.
print(myMarks) # this will print the updated dictionary myMarks to the console, showing the new key-value pairs from new_marks added to the original dictionary, as well as the updated value for "Maths". The output will include all the previous key-value pairs along with the new ones and the updated value for "Maths".
# functions or methods in dictionary
# 1. keys() method: This method returns a view object that displays a list of all the keys in the dictionary.
print(myMarks.keys()) # this will print a view object containing all the keys in the myMarks dictionary. The output will be: dict_keys(['Maths', 'Science', 'English', 'History', 'hindi', 'telugu', 'Geography', 'Physics', 'Chemistry'])
# 2. values() method: This method returns a view object that displays a list of all the values in the dictionary.
print(myMarks.values()) # this will print a view object containing all the values in the myMarks dictionary. The output will be: dict_values([98, 85, 95, 80, 88, 92, 87, 89, 92])
# 3. items() method: This method returns a view object that displays a list of all the key-value pairs in the dictionary as tuples.
print(myMarks.items()) # this will print a view object containing all the key-value pairs in the myMarks dictionary as tuples. The output will be: dict_items([('Maths', 98), ('Science', 85), ('English', 95), ('History', 80), ('hindi', 88), ('telugu', 92), ('Geography', 87), ('Physics', 89), ('Chemistry', 92)])
# 4. get() method: This method returns the value associated with a specified key in the dictionary. If the key is not found, it returns a default value (which can be specified as a second argument).
print(myMarks.get("Maths")) # this will return the value associated with the key "Maths" in the myMarks dictionary, which is 98. The output will be: 98
print(myMarks.get("Biology", "Key not found")) # this will return the value associated with the key "Biology" in the myMarks dictionary. Since "Biology" is not a key in the dictionary, it will return the default value "Key not found". The output will be: Key not found
# 5. pop() method: This method removes a specified key from the dictionary and returns its associated value. If the key is not found, it raises a KeyError.
removed_value = myMarks.pop("History") # this will remove the key "History" from the myMarks dictionary and return its associated value, which is 80. The output will be: 80
print(removed_value) # this will print the value that was removed from the dictionary, which is 80. The output will be: 80
print(myMarks) # this will print the updated dictionary myMarks to the console, showing that the key "History" has been removed along with its associated value. The output will include all the previous key-value pairs except for "History": 80.
# if i wanna updatae the value of a key in the dictionary, i can simply assign a new value to that key. For example, if i want to update the value of "Science" to 90, i can do it like this: with function
print(myMarks.update({"Science": 90})) # this will update the value associated with the key "Science" in the myMarks dictionary to 90. The output will be: None, because the update() method does not return any value.
print(myMarks) # this will print the updated dictionary myMarks to the console, showing the updated value for "Science".
# more fucntions in dictionary
# 6. clear() method: This method removes all the key-value pairs from the dictionary
myMarks.clear() # this will remove all the key-value pairs from the myMarks dictionary, leaving it empty. The output will be: None, because the clear() method does not return any value.
print(myMarks) # this will print the now empty dictionary myMarks to the console. The output will be: {}
# 7. copy() method: This method returns a shallow copy of the dictionary.
myMarks = {
    "Maths": 98,
    "Science": 90,
    "English": 95,
    "hindi": 88
}
myMarks_copy = myMarks.copy() # this will create a shallow copy of the myMarks dictionary and assign it to the variable myMarks_copy. The output will be: None, because the copy() method does not return any value.
print(myMarks_copy) # this will print the copied dictionary myMarks_copy to the console, which should have the same key-value pairs as the original myMarks dictionary. The output will be: {'Maths': 98, 'Science': 90, 'English': 95, 'hindi': 88}
# 8. fromkeys() method: This method creates a new dictionary with specified keys and a default value for all keys.
keys = ["Maths", "Science", "English", "hindi"] # this is a list of keys that we want to use for the new dictionary.
default_value = 0 # this is the default value that will be assigned to all keys in the new dictionary.
new_dict = dict.fromkeys(keys, default_value) # this will create a new dictionary using the fromkeys() method, where the keys are taken from the list keys and all values are set to the default_value (0 in this case). The output will be: None, because the fromkeys() method does not return any value.
print(new_dict) # this will print the newly created dictionary new_dict to the console, which will have the keys "Maths", "Science", "English", and "hindi" all with the value 0. The output will be: {'Maths': 0, 'Science': 0, 'English': 0, 'hindi': 0}
#9. setdefault() method: This method returns the value of a specified key in the dictionary. If the key does not exist, it adds the key with a specified default value and returns that value.
print(myMarks.setdefault("Geography", 87)) # this will return the value associated with the key "Geography" in the myMarks dictionary. Since "Geography" does not exist in the dictionary, it will add the key "Geography" with the default value 87 to the dictionary and return that value. The output will be: 87
print(myMarks) # this will print the updated dictionary myMarks to the console, showing that the key "Geography" has been added with the value 87. The output will be: {'Maths': 98, 'Science': 90, 'English': 95, 'hindi': 88, 'Geography': 87}
print(myMarks.setdefault("Maths", 100)) # this will return the value associated with the key "Maths" in the myMarks dictionary, which is 98. Since "Maths" already exists in the dictionary, it will not add a new key or update the existing value, and it will simply return the current value of "Maths". The output will be: 98
print(myMarks) # this will print the dictionary myMarks to the console, showing that the value for "Maths" has not been changed and remains 98. The output will be: {'Maths': 98, 'Science': 90, 'English': 95, 'hindi': 88, 'Geography': 87}
# 10. popitem() method: This method removes and returns an arbitrary key-value pair from the dictionary as a tuple. If the dictionary is empty, it raises a KeyError.
removed_item = myMarks.popitem() # this will remove and return an arbitrary key-value pair from the myMarks dictionary as a tuple. The output will be a tuple containing the removed key and its associated value, for example: ('Geography', 87)
print(removed_item) # this will print the removed key-value pair as a tuple to the console. The output will be something like: ('Geography', 87)
print(myMarks) # this will print the updated dictionary myMarks to the console, showing that one key-value pair has been removed. The output will include all the previous key-value pairs except for the one that was removed.
