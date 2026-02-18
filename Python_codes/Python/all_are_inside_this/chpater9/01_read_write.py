
st='''rgeueriuyghrudibniurdguofdghn
gjghjghjgh
hgjhgjhgj
hjhjg

'''
f=open("create_a_new_file.txt","w")
f.write(st)
f.close

f=open("create_a_new_file.txt","r")
data=f.read()
print(data)
f.close

f=open("create_a_new_file.txt","a")
add="sravan goat"
f.write(add)
f.close

f=open("create_a_new_file.txt","r")
lines=f.readlines()
print(lines,type(lines))
f.close

f=open("create_a_new_file.txt","r")
line=f.readline()
while(line != ""):
 print(line,type(lines))
 line=f.readline()


f.close





# with statement 

with open("create_a_new_file.txt","r") as f:
 print(f.read())
 
# no need to use the f.close thing