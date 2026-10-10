import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

s = pd.Series([1,2,3,4,5,6,7])
s.plot(kind='pie',labels=['A','B','C','D','E','F','G'],autopct='%1.1f%%',shadow=True,explode=[0,0,0,0.1,0,0,0],startangle=90)
plt.show()

tips = sns.load_dataset('tips')
tips['size'] = tips['size'] * 100
# Scatter plot -> labels -> markers -> figsize -> color -> cmap
tips.plot(kind='scatter',x='total_bill',y='tip',title='Cost Analysis',marker='+',figsize=(10,6),s='size',c='sex',cmap='viridis')
plt.show()


stocks = pd.read_csv('https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/weekly_stocks.csv')
print(stocks.head())
# line plot
stocks['MSFT'].plot(kind='line')
stocks.plot(kind='line',x='Date')
stocks[['Date','AAPL','FB']].plot(kind='line',x='Date')
plt.show()

tips.groupby('sex')['total_bill'].mean().plot(kind='bar')
plt.show()


temp=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\batsman_season_record (1).csv")
temp['2015'].plot(kind='bar')
temp.plot(kind='bar')
# stacked bar chart
temp.plot(kind='bar',stacked=True)
plt.show()


# histogram
# using stocks
stocks[['MSFT','FB']].plot(kind='hist',bins=40)
plt.show()


# pie -> single and multiple
df = pd.DataFrame(
    {
        'batsman':['Dhawan','Rohit','Kohli','SKY','Pandya','Pant'],
        'match1':[120,90,35,45,12,10],
        'match2':[0,1,123,130,34,45],
        'match3':[50,24,145,45,10,90]
    }
)
df['match1'].plot(kind='pie',labels=df['batsman'].values,autopct='%0.1f%%')

# multiple pie charts

df[['match1','match2','match3']].plot(kind='pie',subplots=True,figsize=(15,8))

# multiple separate graphs together
# using stocks

stocks.plot(kind='line',subplots=True)
plt.show()

tips.pivot_table(index=['day','time'],columns=['sex','smoker'],values='total_bill',aggfunc='mean').plot(kind='pie',subplots=True,figsize=(20,10))
plt.show()