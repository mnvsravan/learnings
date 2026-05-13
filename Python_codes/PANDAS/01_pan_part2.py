import numpy as np
import pandas as pd
vk = pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\kohli_ipl.csv",index_col='match_no')
vk = vk.squeeze()
print(vk)
print(vk.count()) # counts (exclude empty or blank ,  this is the diff betweeen this and size)
print(vk.sum()) # Even pdt same 
print(vk.mean()) # Even var , mode, std etc
print(vk.max())# Even min
print(vk.describe()) # This gives gist

#Series indexing
x = pd.Series([12,13,14,35,46,57,58,79,9])
print(x[4])
#print(x[-1]) # negative indexing wont work 

movies1 = pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\csv.csv"
)['lead']
movies1 = movies1.squeeze()
print(movies1)

print(movies1[0])

movies2 = pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\csv.csv",index_col='movie'
)
movies2 = movies2.squeeze()
print(movies2)

print(movies2['Uri: The Surgical Strike'])


print(vk[5:16:3])
print(vk[-5:]) # last 5 . here negative slicing works
print(vk[[1,6,7,65]]) # Fancy indexing

#editing

vk[0]=[100]
print(vk[0])
movies1['GOAT']=["Mnv Sravan"] # if nothing is found then it adds
print(movies1['GOAT'])

movies1[2:4]=["Mnv Sravan","Mnv Sravan"]
print(movies1[2:4])

vk[[1,5,35,7]]=[100,100,100,100]
print(vk[[1,5,35,7]])

movies1['2 States (2014 film)'] = 'Mnv Sravan'
print(movies1['2 States (2014 film)'])

#Series with python
print(len(vk))
print(type(vk))
print(dir(vk))

#Type conversion
print(list(vk))
print(dict(vk))

# membership operator
print('2 States (2014 film)' in movies1)
print('Mnv Sravan' in movies1.values)

for i in movies1.index:
  print(i)
for i in movies1:
  print(i)

# Arithmetic Operators(Broadcasting)
vk = pd.to_numeric(vk, errors='coerce')

print(100 + vk) # same for - + / and all

#relational 
print(vk<=50)
# IDK ITS GIVING SOME SUS INFO BUT THE METHOD IS THIS

#Boolean Indexing on Series
subs = pd.read_excel(
    r"C:\Users\Mnv Sravan\Downloads\subs.xlsx"
).squeeze()
print(subs)
print(subs[subs>=50])
print(subs[subs>=50].size)
# find actors who have done more than 20 movies
num_movies = movies1.value_counts()
print(num_movies[num_movies > 20])
subs.plot()
import matplotlib.pyplot as plt
plt.show()
movies1.value_counts().head(20).plot(kind='pie')
plt.show()
movies1.value_counts().head(20).plot(kind='bar')
plt.show()