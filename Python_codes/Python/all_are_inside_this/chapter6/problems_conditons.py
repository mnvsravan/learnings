n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
n4=int(input("Enter fourth number: "))
if(n1>n2) and (n1>n3) and (n1>n4):
    print("The greatest number is:", n1)
elif(n2>n1) and (n2>n3) and (n2>n4):
    print("The greatest number is:", n2)
elif(n3>n1) and (n3>n2) and (n3>n4):
    print("The greatest number is:", n3)
else:
    print("The greatest number is:", n4)

    #
marks1 = int(input("Enter marks of first subject: "))
marks2 = int(input("Enter marks of second subject: "))
marks3 = int(input("Enter marks of third subject: "))

average = (marks1 + marks2 + marks3) / 3
marks = [marks1, marks2, marks3]                       # you can singly do each one , one by one instead of making a list but i did it like this

if average >= 40 and all(m >= 33 for m in marks):         # this all() function is used to check if all the marks are greater than or equal to 33 because if any one of the marks is less than 33 then the student will fail the exam even if the average is greater than or equal to 40. it returns True if all the elements of the iterable are true (or if the iterable is empty). In this case, it checks if all the marks in the list are greater than or equal to 33.
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have failed the exam.")


#
comment1 = "Make a lot of money"
comment2 = "Buy a lot of things"
comment3 = "subscribe to my here"
comment4 = "click here to win a prize"

list_of_comments = [comment1, comment2, comment3, comment4]    

m = input("Enter your comment: ")

if m in list_of_comments:                # "click here" == "click here to win a prize" it like sees if the input comment is exactly same as any of the comments in the list of comments. If it is then it will print "This comment is spam." otherwise it will print "This comment is not spam."

    print("This comment is spam.")
else:
    print("This comment is not spam.")


comment5 = "make a lot of money"
comment6 = "buy a lot of things"
comment7 = "subscribe to my channel"
comment8 = "click here for prize"

u= input("Enter your comment: ").lower()

if (u in comment5 or
    u in comment6 or
    u in comment7 or                # here we are checking if the input comment is present in any of the comments in the list of comments. If it is then it will print "This comment is spam." otherwise it will print "This comment is not spam."
    u in comment8):
    print("This comment is spam.")
else:
    print("This comment is not spam.")




    # 

text = input("Enter a text: ")

name = "sravan"

if name.lower() in text.lower():              # like even if i enter "Sravan" or "SRAVAN" or "sRaVaN" it will still consider it as the name "sravan" because we are converting both the input text and the name to lowercase before checking if the name is present in the text. This way we can ignore the case of the letters and check for the presence of the name in the text regardless of how it is written.
    print("The text contains the name sravan.")
else:
    print("The text does not contain the name sravan.")


#
marks11 = int(input("Enter marks of first subject: "))
marks22 = int(input("Enter marks of second subject: "))
marks33 = int(input("Enter marks of third subject: "))
average_of_all = (marks11 + marks22 + marks33) / 3
if(average_of_all<=100 and average_of_all>=90):
    grade = "A"
elif(average_of_all<90 and average_of_all>=80):
    grade = "B"
elif(average_of_all<80 and average_of_all>=70):
    grade = "C"
elif(average_of_all<70 and average_of_all>=60):
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade) # here we can see that grade is directly declared in the if elif ladder and we are not using any print statement in the if elif ladder because we are only assigning the grade to the variable grade and we are printing the grade after the if elif ladder. This way we can avoid writing multiple print statements in the if elif ladder and we can also avoid writing the same print statement multiple times. We can also use a single print statement to print the grade after the if elif ladder.
# if u want we can keep grade="" above the ladder and then assign the grade in the ladder and then print the grade after the ladder. This way we can avoid writing multiple print statements in the if elif ladder and we can also avoid writing the same print statement multiple times. We can also use a single print statement to print the grade after the if elif ladder.