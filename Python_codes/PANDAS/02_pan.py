import numpy as np
import pandas as pd
# A DataFrame in pandas is a table-like structure used to store data in rows and columns, similar to an Excel sheet or database table. Each column can contain different types of data like numbers or text, and pandas lets you easily read, analyze, sort, filter, and modify this data using Python.

#DATAFRAME
# using lists
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
student_data=pd.DataFrame(student_data,columns=['iq','marks','package'])
print(student_data)

# using dicts
print()
student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)
print(students)

IPL = pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\ipl-matches.csv")
print(IPL)
Movies = pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\dataset.csv")
print(Movies)
print()
print(IPL.shape,Movies.shape)
print()
print(Movies.dtypes)
print(IPL.dtypes)
print()
print(Movies.index)
print(IPL.index)
print(Movies.columns)
print(IPL.columns)
# We can use values also , it like gives whole rows step by step
# We can use head,tail and sample also as same way as pd series
print(IPL.info())
print(IPL.describe())
print(Movies.isnull())
print(Movies.isnull().sum())
print(Movies.duplicated())
print(Movies.duplicated().sum())
print()
ppl={
    'Name' : ['Sravan','Mnv','MNV','SRAVAN'],
    'Marks':[99,100,98,97],
    'IQ':[140,200,150,170],
    'LPA':[45,76,23,54],
    }
ppl = pd.DataFrame(ppl).set_index('Name') # sets index
print(ppl)
ppl.rename(columns={'Marks':'percent','LPA':'Annual Income'},inplace=True)
print(ppl)
ppl.sum(axis=0) # we can use axis 1 and with var,mean,std and all
print()
print()

#Selecting cols from a DataFrame
print(Movies['title_x'])
print(IPL['Venue'])
# multiple cols
print(Movies[['year_of_release','actors','title_x']]) # we select cols in any order


#Selecting rows from a DataFrame
# iloc - searches using index positions
# loc - searches using index labels

print(Movies.iloc[5])
print(Movies.iloc[:5])
print(Movies.iloc[[3,7,2,76]])

print()
print(ppl.loc['Mnv'])
print(ppl.loc[:'Mnv'])
print(ppl.loc[['MNV','Mnv','SRAVAN']]) # UNLIKE NUMBERS , IT INCLUDES THE LAST INDEX

#FETCHING BOTH ROWS AND COLS
print(Movies.iloc[0:3,0:3])
Movies = Movies.set_index('title_x')

#This is very imp 
# we made now the title_x as index and now its removed from cols so we do like this
#If we use loc we must use all labels only no integers
print(
    Movies.loc[
        'Uri: The Surgical Strike':'The Accidental Prime Minister (film)',
         'imdb_id':'is_adult'
    ]
)

