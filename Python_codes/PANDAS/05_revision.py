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


# value_counts(series and dataframe)

marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=['iq','marks','package'])
print(marks)
print(marks.value_counts()) # returns a series with the counts of unique rows in the DataFrame
# u can use inplace , ascending, normalize, dropna, sort, etc. parameters with value_counts

#task: find the player who has won the most number of player of the match awards in matches where the match number is not a digit
print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())


# Toss decision plot
ipl['TossDecision'].value_counts().plot(kind='pie')
plt.show()

# how many matches each team has played
print((ipl['Team2'].value_counts() + ipl['Team1'].value_counts()).sort_values(ascending=False))




# sort_values(series and dataframe) -> ascending -> na_position -> inplace -> multiple cols

movies.sort_values('title_x',ascending=False)


students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)
print(students)
print(students.sort_values('name',na_position='first',ascending=False,inplace=True))

# movies yearwise with title in descending order
print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))


# rank(series)
# we rank the batsman based on the runs scored by them in descending order, and create a new column called 'batting_rank' to store the rank of each batsman 
batsman['batting_rank'] = batsman['batsman_run'].rank(ascending=False)
print(batsman.sort_values('batting_rank'))


# sort_index(series and dataframe)

print(movies.sort_index(ascending=False))


# set_index(dataframe) -> inplace
batsman.set_index('batter',inplace=True)
# reset_index(series + dataframe) -> drop parameter
batsman.reset_index(inplace=True)
# how to replace existing index without loosing
batsman.reset_index().set_index('batting_rank') # we must follow this order to avoid loosing the existing index, first we reset the index and then set the new index

# series to dataframe using reset_index
# marks_series.reset_index()

# rename(dataframe) -> index
movies.rename(columns={'imdb_id':'imdb','poster_path':'link'},inplace=True)
movies.rename(index={'Uri: The Surgical Strike':'Uri','Battalion 609':'Battalion'})

