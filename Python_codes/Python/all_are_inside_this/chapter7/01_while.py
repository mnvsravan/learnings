# the syntax for while loop is:
# while condition:
#     statement(s)
# here the condition is a boolean expression that is evaluated before each iteration of the loop. If the condition is true, the statements inside the loop are executed. If the condition is false, the loop is terminated and the program continues with the next statement after the loop.
i=0
while(i<10):
    print(i)
    i+=1                 # unlike c u cant write i++ and shit , but u can write i=i+1

#advanced usage of while loop
list=["sravan",34,False,]
i=0
while(i<len(list)):
    print(list[i])
    i+=1
    # similarly even in tuples, strings and other stuff
    s="hello world"
    i=0
    while(i<len(s)):
        print(s[i])
        i+=1



fruits = ("apple", "banana", "cherry")

i = 0
while (i < len(fruits)):
    print(fruits[i])
    i += 1


    #FOR LOOP
    #syntax for FOR loop is:
    #for variable in iterable:
    #    statement(s)
    # here the iterable is a sequence (list, tuple, string, etc.) and the variable is a loop variable that takes the value of each element in the iterable in turn.
    Games = ["Call of Duty", "Fortnite", "Minecraft", "Valorant"]
    for game in Games:
        print(game)
        # there exists something called like jump thing in for loop

        nums=[1,2,3,4,5]
        for num in range(len(nums)):
            print(nums[num])

            # this can even be written like 
            for num in range(1,6):    # this is like i=1 and it will go till 5 but it will not include 6 .. u can wirte like (0,5) or even (5) or (len(nums)) or (0,len(nums)) or even (0,10) but it will only print till 5 because we are only printing the value of num and num will only take the values from 1 to 5 because we are using range(1,6) which means it will start from 1 and go till 5 but it will not include 6.
                print(num)

for i in range(1, 6,2):  # this is like i=1 and it will go till 5 but it will not include 6 and it will only print the odd numbers because we are using step of 2 which means it will skip the even numbers and only print the odd numbers.
    print(i)
    # this third parameter is like the step parameter which is used to specify the step size of the loop. By default, the step size is 1, which means that the loop variable will take every value in the specified range. However, if you specify a different step size, the loop variable will take values at intervals of that step size. For example, if you specify a step size of 2, the loop variable will take every other value in the specified range. If you specify a step size of -1, the loop variable will take values in reverse order.



    # for loop with else statement
nigs=[1,44,45,456,65,57,657,6,78,678,7,8,78]
for nig in nigs:
    print(nig)
else:
    print("DONE") # this executes after this for loop is exhausted 



    # for loop with break, continue and pass

    exp=[4563,45,435,47,49,4,64,56,56,56]
    for e1 in exp:
        if(e1==4):
            break
        print(e1)
for e2 in exp:
    if(e2==4):
        continue
    print(e2)


    # PASS in for loop 
ok=[32,345,4,54,365,546,5,]
for o in range(len(ok)):
    if ok[o]==54:
        pass  # do nothing if the value is 54
    else:
        print(ok[o])

        # we use this pass to aviod things like error for example 
        for m in range(600):
            pass  # do nothing for each iteration in range(600)
        for n in range(len(ok)):
            print(ok[n])




#l = [1,7,8]
#for item in l:
#pass # without pass, the program will throw an error
            