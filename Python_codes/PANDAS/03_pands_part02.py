import pandas as pd
import numpy as np
IPL = pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\ipl-matches.csv"
)
print(IPL)
print()
Movies = pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\dataset.csv")
print(Movies)
print()
#Filetering
# In IPL
# find all the final winners
final = IPL['MatchNumber'] == 'Final'
final_match = IPL[final]
winner = final_match['WinningTeam']
print(winner)
# OR
final1 = IPL['MatchNumber'] == 'Final'
winner1 = IPL[final1]['WinningTeam']
print(winner1)

# how many super over finishes have occured
num= IPL['SuperOver'] == 'Y'
print(num) # this is how we count the number of true values in a boolean series
print(num.sum()) # this will give us the count of true values


# how many matches has csk won in kolkata
csk_kolkata = (IPL['WinningTeam'] == 'Chennai Super Kings') & (IPL['City'] == 'Kolkata')
print(csk_kolkata.sum())

# toss winner is match winner in percentage
toss_winner = IPL['TossWinner'] == IPL['WinningTeam']
print(toss_winner.sum()/len(IPL)*100)


# movies with rating higher than 8 and votes>10000
good_movies = (Movies['imdb_rating'] > 8) & (Movies['imdb_votes'] > 10000)
print(Movies[good_movies])


# Action movies with rating higher than 7.5

action= (Movies['genres'].str.contains('Action')) & (Movies['imdb_rating'] > 7.5)
print(Movies[action])
#OR
action1 = Movies['genres'].str.split('|').apply(lambda x: 'Action' in x) & (Movies['imdb_rating'] > 7.5)
print(Movies[action1])

# write a function that can return the track record of 2 teams against each other
def track_record(team1,team2):
    team1_wins = ((IPL['WinningTeam'] == team1) & ((IPL['Team1'] == team2) | (IPL['Team2'] == team2))).sum()
    team2_wins = ((IPL['WinningTeam'] == team2) & ((IPL['Team1'] == team1) | (IPL['Team2'] == team1))).sum()
    return f"{team1} has won {team1_wins} times against {team2}, while {team2} has won {team2_wins} times against {team1}."
print(track_record('Chennai Super Kings','Kolkata Knight Riders'))

#ADDING NEW COLUMN
IPL['Country']='India'
# Movies['lead actors']=Movies['actors'].str.apply(lambda x: x.split(',')[0]) this isnt working cuz nan values exist in actors column
IPL['Aura']=IPL['Margin'].apply(lambda x: 'Close' if x<10 else 'Decisive')
print(IPL)

#astype
print(IPL['Margin'].info())
print(IPL['Margin'].isna().sum())
print(IPL['Margin'].fillna(0).sum())
IPL['Margin'] = IPL['Margin'].fillna(0).astype('int32')
# What happens is:

# fillna(0) replaces only the missing values.
# astype('int32') converts every value in the column to int32.
print(IPL['Margin'].info())

# We use category also to reduce
# memory usage for columns with few unique values
print(IPL['City'].info())
IPL['City'] = IPL['City'].astype('category')
print(IPL['City'].info())