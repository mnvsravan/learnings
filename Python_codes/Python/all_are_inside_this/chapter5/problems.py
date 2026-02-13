words={
    "mkc":"maki chuth",
    "bkl":"ben ke lowde",
    "ffs":"fuck sake"
}
shortform=input("Enter the short form: ")
print(words[shortform])


#
s=set()
n=input("enter the number")
s.add(int(n))
n=input("enter the number")
s.add(int(n))
n=input("enter the number")
s.add(int(n))
n=input("enter the number")
s.add(int(n))
n=input("enter the number")
s.add(int(n))
n=input("enter the number")
s.add(int(n))
n=input("enter the number")
s.add(int(n))
n=input("enter the number")
s.add(int(n))
print(s)
# we can use the same n multiple number of times

#
d={}
name=input("Enter your name: ")
language=input("Enter your favorite language: ")
d.update({name:language})
name=input("Enter your name: ")
language=input("Enter your favorite language: ")
d.update({name:language})
name=input("Enter your name: ")
language=input("Enter your favorite language: ")
d.update({name:language})
name=input("Enter your name: ")
language=input("Enter your favorite language: ")
d.update({name:language})
name=input("Enter your name: ")
language=input("Enter your favorite language: ")
d.update({name:language})
print(d)
# if u enter same key multiple times then it will update the value of that key and only the last value will be stored in the dictionary.
# but if u eneter same value multiple times then it will be stored in the dictionary as it is because the value can be same for different keys.
# we cant have list in set but we can have list in dictionary as value because the value can be mutable but the key cannot be mutable.


s1 = set()
s1.add(20)
s1.add(20.0)
s1.add('20') # length of s after these operations?
# the answer is 2 because 20 and 20.0 are considered the same in a set, so only one of them will be stored. The string '20' is different from the integer 20 and the float 20.0, so it will be stored as a separate element in the set. Therefore, the set s1 will contain two elements: {20, '20'}.