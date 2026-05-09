import numpy as np
import pandas as pd

### Pandas Series-A Pandas Series is like a column in a table. It is a 1-D array holding data of any type.
country = ['India','Pakistan','USA','Nepal','Srilanka']
print(pd.Series(country))
runs = [13,24,56,78,100]
runs_ser = pd.Series(runs)
print(runs_ser)
print()
# custom index
marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']
print(pd.Series(marks,index=subjects))
print()
# setting a name
marks = pd.Series(marks,index=subjects,name='Nitish ke marks')
print(marks)


# WE CAN DO THE SAME STUFF with dicts
print()
marks={
    "Maths":97,
    "English":89,
    "science":99,
    "Languages":89,
}
m=pd.Series(marks,name="Sravan")
print(m)


#Series attributes
#we declared m as an pd.series
print(m.size)
print(m.dtype)
print(m.is_unique)
print(m.index)
print(m.values)



#Series using read_csv , this is important for real life things 
#data set-A dataset is simply a collection of data organized together.

movies = pd.read_excel(
    r"C:\Users\Mnv Sravan\Downloads\bollywood.xlsx",
    index_col='movie'
)

movies = movies.squeeze()   # This squeeez converts dataframe to dataset 

print(movies) # The value in the data set is given Name:


# **** idk csv isnt working but rem that 
# File Extension	Function
# .csv	pd.read_csv()
# .xlsx	pd.read_excel()
movies1 = pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\csv.csv",
    index_col='movie'
)
movies1 = movies1.squeeze()
print(movies1)

#Series methods
print()
print(movies.head(10)) # This gives the first n number of elemnts from top ,if no arguments passed then it gives 5
print()
print(movies.tail(10))# This gives the first n number of elemnts from bottom,if no arguments passed then it gives 5
print()
print(movies.sample(1))# This gives the random n number of elemnts,if no arguments passed then it gives 5
print()
print(movies.value_counts()) #This gives the number of times values occur, we can pass argments also for how many we want
print()
print(movies.value_counts(ascending=False)) #Gives reverse
print()
print(movies.sort_values()) #This sorts the values
print()
print(movies.sort_values(ascending=False,inplace=True)) #This inplace inplace actually makes changes in the dataset ,This gives none cuz this makes changes in original dataset
print(movies)
print(movies.sort_index())# this sorts indicies
print(movies.sort_index(ascending=False,inplace=True))
print(movies)
