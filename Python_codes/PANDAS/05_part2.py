import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
batsman= pd.read_csv(
     r"c:\Users\Mnv Sravan\Downloads\batsman_runs_ipl.csv"
 )
ipl = pd.read_csv(
    r"c:\Users\Mnv Sravan\Downloads\ipl-matches - ipl-matches.csv"
)

diabaotes = pd.read_csv(
    r"c:\Users\Mnv Sravan\Downloads\diabetes - diabetes.csv"
)

movies = pd.read_csv(
    r"c:\Users\Mnv Sravan\Downloads\movies - movies.csv"
)

# unique(series)
temp = pd.Series([1,1,2,2,3,3,4,4,5,5,np.nan,np.nan])
print(temp)
print(len(temp.unique())) # we can use nunique() to get the count of unique values in a series, it excludes nan values by default, but we can include them by passing dropna=False  

df = pd.DataFrame({
    'name': ['nitish', 'ankit', 'rupesh', None, 'mrityunjay', None, 'rishabh', None, 'aditya', None],
    'college': ['bit', 'iit', 'vit', None, None, 'vlsi', 'ssit', None, None, 'git'],
    'branch': ['eee', 'it', 'cse', None, 'me', 'ce', 'civ', 'cse', 'bio', None],
    'cgpa': [6.66, 8.25, 6.41, None, 5.60, 9.00, 7.40, 10.00, 7.40, None],
    'package': [4.0, 5.0, 6.0, None, 6.0, 7.0, 8.0, 9.0, None, None]
})


# isnull(series + dataframe)
print(df['name'][df['name'].isnull()]) # this gives the values which are null in the series

# notnull(series + dataframe)
print(df['name'][df['name'].notnull()]) # this gives the values which are not null in the series

# hasnans(series)
print(df['name'].hasnans) # this gives a boolean value indicating whether the series contains any NaN values or not

print(movies.notnull()) # this gives a dataframe with boolean values indicating whether each value in the dataframe is not null or not


# dropna(series + dataframe) -> how parameter -> works like or
print(df['name'].dropna()) # this removes the null values from the series
print(df.dropna(how='any')) # this removes the rows where any of the values are null in the dataframe
print(df.dropna(how='all')) # this removes the rows where all the values are null in the dataframe


print(df.dropna(subset=['name','college'])) # this removes the rows where any of the values in the specified subset of columns are null in the dataframe    )

# fillna(series + dataframe)
df['name'].fillna('unknown')
df['package'].fillna(df['package'].mean())
df['name'].bfill() # bfill means backward fill, it fills the null values with the next non-null value in the series
df['name'].ffill() # ffill means forward fill, it fills the null values with the previous non-null value in the series


# drop_duplicates(series + dataframe) -> works like and -> duplicated()

temp = pd.Series([1,1,1,2,3,3,4,4])
print(temp.drop_duplicates(keep='first')) # this removes the duplicate values from the series and keeps the first occurrence of each value
print(temp.drop_duplicates(keep='last')) # this removes the duplicate values from the series and



# find the last match played by virat kohli in Delhi

ipl['all players']=ipl['Team1Players'] + ipl['Team2Players']
def vk_played( s):
    if 'V Kohli' in s:
        return True
    else:
        return False

ipl['vk_played'] = ipl['all players'].apply(vk_played)
print(ipl)
print((ipl[(ipl['City']== 'Delhi') & (ipl['vk_played']== True)]['Date'].max())) # this gives the last match played by virat kohli in Delhi

# drop(series + dataframe)
temp = pd.Series([10,2,3,16,45,78,10])
print(temp.drop(index=[0,5])) # this removes the values at the specified index from the series

print(movies.drop(index=[0,5], columns=['title_x','release_date'])) # this removes the values at the specified index and columns from the dataframe

#APPLY(series + dataframe)

points_df = pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)
def euclidean(row):
  pt_A = row['1st point']
  pt_B = row['2nd point']

  return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5

points_df['euclidean_distance'] = points_df.apply(euclidean, axis=1)
print(points_df)