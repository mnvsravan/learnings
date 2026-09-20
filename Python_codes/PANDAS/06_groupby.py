import numpy as np
import pandas as pd 
movies= pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\imdb-top-1000 - imdb-top-1000.csv"
)

ipl= pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\deliveries.csv"
)
# Ex1
genres = movies.groupby('Genre')
print(genres.std(numeric_only=True)) # this gives the standard deviation of the numerical columns in the dataframe for each group

# FEW agreegate operations on the groupby object


# find the top 3 genres by total earning
# print(movies.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(3))
print(movies.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3)) # more effective way


# find the genre with highest avg IMDB rating
print(movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

# find director with most popularity
movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending=False).head(1)

# find the highest rated movie of each genre
print(movies.groupby('Genre')['IMDB_Rating'].max())

# how to actual data of groupwise
for group,data in genres:
    print(group)
    print(data)



# GroupBy Attributes and Methods
# find total number of groups -> len
# find items in each group -> size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique

genres = movies.groupby('Genre')

print(len(movies.groupby('Genre')))  # number of groups
print(movies['Genre'].nunique())     # unique genres
print(movies.groupby('Genre').size()) # size of each group

print(genres.first())  # first row of every group
print(genres.last())   # last row of every group
print(genres.nth(6))   # 7th row of every group
print(movies['Genre'].value_counts())  # count of each genre

print(genres.get_group('Fantasy'))

# movies[movies['Genre'] == 'Fantasy']

print(genres.groups)  # dictionary of groups
print(genres.describe())# this gives the descriptive statistics of the numerical columns in the dataframe for each group
# # print(genres.sample(2,))  # random sample of 2 rows from each group
print(genres.nunique())




# agg method
# passing dict
print(genres.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min',
        'Series_Title':'count'
    }
)
)


print(genres.agg(
    {
        'Runtime':['mean','max','min'],
        'IMDB_Rating':['mean','max','min'],
        'No_of_Votes':['sum'],
        'Gross':['sum'],
        'Metascore':['min'],
        'Series_Title':['count']
    }
)
)


# looping on groups
df = pd.DataFrame(columns=movies.columns)
for group,data in genres:
  df = pd.concat([df, data[data['IMDB_Rating'] == data['IMDB_Rating'].max()]]) 
  # the append in this version of pandas so we have to use concat instead of append
print(df)


# split (apply) combine
# apply -> builtin function

def bruh(grp):
    return grp['Series_Title'].str.startswith('A').sum()

print(genres.apply(bruh)) # this gives the count of movies starting with A in each genre


def cal_rank(grp):
    grp['Rank'] = grp['IMDB_Rating'].rank(ascending=False)
    return grp

print(genres.apply(cal_rank))


def normal(group):
  group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min())/(group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
  return group

print(genres.apply(normal))




# groupby on multiple cols
duo = movies.groupby(['Director','Star1'])
print(duo)
# size
print(duo.size())
# get_group
print(duo.get_group(('Aamir Khan','Amole Gupte')))

# find the most earning actor->director combo
print(duo['Gross'].sum().sort_values(ascending=False).head(1))

# find the best(in-terms of metascore(avg)) actor->genre combo
print(movies.groupby(['Star1','Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False).head(1))

# we use reset_index() to convert the groupby object to a dataframe so that we can sort it by metascore and get the best actor->genre combo
# if u dont want to use then dont pass 'many' parameter in the groupby and use sort_values on the groupby object directly



# agg on multiple groupby
# print(duo.agg(['min','max','mean']))
print(duo.agg({
    'Runtime': ['mean', 'max', 'min'],
    'IMDB_Rating': ['mean', 'max', 'min']
}))