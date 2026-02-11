a=int(input("Enter an marks1: "))
b=int(input("Enter another marks2: "))
c=int(input("Enter another marks3: "))
d=int(input("Enter another marks4: "))
e=int(input("Enter another marks5: "))
marks = (a, b, c, d, e) # this will create a tuple called marks that contains the values of a, b, c, d, and e. The parentheses are used to define the tuple, and the values are separated by commas.
sum_of_marks = sum(marks) # this will calculate the sum of all the marks in the tuple using the sum() function.
average_marks = sum_of_marks / len(marks) # this will calculate the average marks by dividing the sum of marks by the number of marks, which is obtained using the len() function.
print("The average marks is:", average_marks) # this will print the average marks to the console. The string "The average marks is:" is concatenated with the value of average_marks using a comma, which allows us to print both the string and the value in a single print statement.

# now i want to make a list with these
list1=[]
list1.append(a) # this will add the value of a to the end of the list list1.
list1.append(b) # this will add the value of b to the end of the list
list1.append(c) # this will add the value of c to the end of the list
list1.append(d) # this will add the value of d to the end of the list
list1.append(e) # this will add the value of e to the end of the list
print(list1) # this will print the list list1, which now contains the values of a, b, c, d, and e in the order they were added.


a = (7, 0, 8, 0, 0, 9)
number_of_zeros = a.count(0) # this will count the number of times the value 0 appears in the tuple a using the count() method.
print("The number of zeros in the tuple is:", number_of_zeros) # this will print the number of zeros in the tuple a to the console. The string "The number of zeros in the tuple is:" is concatenated with the value of number_of_zeros using a comma, which allows us to print both the string and the value in a single print statement.