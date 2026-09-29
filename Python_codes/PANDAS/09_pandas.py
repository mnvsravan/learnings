import pandas as pd
import numpy as np
# problem in vectorized opertions in vanilla python
# s = ['cat','mat',None,'rat']
# [i.startswith('c') for i in s] this dosent work cuz NONE is cooked

# How pandas solves this issue?

s = pd.Series(['cat','mat',None,'rat'])
# string accessor
s.str.startswith('c')

# fast and optimized

df=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\titanic.csv")

# Common Functions
# lower/upper/capitalize/title
print(df['Name'].str.upper())
df['Name'].str.capitalize()
df['Name'].str.title()
# len
df['Name'][df['Name'].str.len() == 82].values[0]
# strip
print("                   nitish                              ".strip())
df['Name'].str.strip()

# split -> get
df['lastname'] = df['Name'].str.split(',').str.get(0)
print(df.head())



df[['title','firstname']] = df['Name'].str.split(',').str.get(1).str.strip().str.split(' ', n=1, expand=True)
print(df.head())# n is like the number of time the split must work , expand is like it converts to data frame
print(df['title'].value_counts())
# replace
df['title'] = df['title'].str.replace('Ms.','Miss.')
df['title'] = df['title'].str.replace('Mlle.','Miss.')
print(df.head())
print(df['title'].value_counts())


# filtering
# startswith/endswith
print(df[df['firstname'].str.endswith('A')])
# isdigit/isalpha...
print(df[df['firstname'].str.isdigit()])


# applying regex
# contains
# search john -> both case
print(df[df['firstname'].str.contains('john',case=False)])
# find lastnames with start and end char vowel
print(df[df['lastname'].str.contains('^[^aeiouAEIOU].+[^aeiouAEIOU]$')])


# slicing
print(df['Name'].str[::-1])