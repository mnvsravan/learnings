import numpy as np
import pandas as pd 
ipl= pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\deliveries.csv"
)
print(ipl.head())

# find the top 10 batsman in terms of runs
print(  ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

      )


# find the batsman with max no of sixes
six = ipl[ipl['batsman_runs'] == 6]
print(six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0])



# find batsman with most number of 4's and 6's in last 5 overs
temp_df = ipl[ipl['over'] > 15]
temp_df = temp_df[(temp_df['batsman_runs'] == 4) | (temp_df['batsman_runs'] == 6)]
print(temp_df.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1).index[0])




# find V Kohli's record against all teams
temp_df = ipl[ipl['batsman'] == 'V Kohli']
print(temp_df.groupby('bowling_team')['batsman_runs'].sum().reset_index())


# Create a function that can return the highest score of any batsman
def highest(batsman):
  temp_df = ipl[ipl['batsman'] == batsman]
  return temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

print(highest('V Kohli'))