import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bar chart
# Bivariate Analysis
# Numerical vs Categorical
# Use case - Aggregate analysis of groups

# simple bar chart
children = [10,20,40,10,30]
colors = ['red','blue','green','yellow','pink']
plt.bar(colors,children, color=colors) # like random colors
plt.show()

# horizontal bar chart
plt.barh(colors,children,color='black')
plt.show()


df=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\batsman_season_record.csv")
plt.bar(df['batsman'],df['2015'],color='orange')
plt.show()

#this is a bit tricky part, we need to set the width of the bars and also set the x-ticks to be the batsman names. We will use numpy arange to get the index of the batsman names and then set the x-ticks to be the batsman names. We will also set the width of the bars to be 0.2 and then plot the bars for each year.
plt.bar(np.arange(df.shape[0]) - 0.2,df['2015'],width=0.2,color='yellow')
plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2,color='red')
plt.bar(np.arange(df.shape[0]) + 0.2,df['2017'],width=0.2,color='blue')
plt.xticks(np.arange(df.shape[0]), df['batsman']) # this is to set the x-ticks to be the batsman names
plt.show()


# a problem
children = [10,20,40,10,30]
colors = ['red red red red red red','blue blue blue blue','green green green green green','yellow yellow yellow yellow ','pink pinkpinkpink']
plt.bar(colors,children,color='black')
plt.xticks(rotation='vertical')
plt.show()



# Stacked Bar chart
plt.bar(df['batsman'],df['2017'],label='2017')
plt.bar(df['batsman'],df['2016'],bottom=df['2017'],label='2016')
plt.bar(df['batsman'],df['2015'],bottom=(df['2016'] + df['2017']),label='2015')
plt.legend()
plt.show()



# Stacked Bar chart
plt.bar(df['batsman'],df['2015'],label='2015')
plt.bar(df['batsman'],df['2016'],bottom=df['2015'],label='2016')
plt.bar(df['batsman'],df['2017'],bottom=(df['2016'] + df['2015']),label='2017')
plt.legend()
plt.show()



# Histogram
# Univariate Analysis
# Numerical col
# Use case - Frequency Count


# simple data
data = [32,45,56,10,15,27,61]
plt.hist(data,bins=[10,25,40,55,70])
plt.show()

vk=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\vk.csv")
plt.hist(vk['batsman_runs'],bins=[0,10,20,30,40,50,60,70,80,90,100,110,120])
plt.show()


# logarithmic scale-> WHEN THE GRAPH IS TOO BIG AND WE WANT TO SEE THE SMALLER VALUES AS WELL, WE USE LOGARITHMIC SCALE. IT WILL SHOW THE SMALLER VALUES IN A BETTER WAY.
arr = np.load(r"C:\Users\Mnv Sravan\Downloads\big-array.npy")
plt.hist(arr,bins=[10,20,30,40,50,60,70],log=True)
plt.show()


# Pie Chart
# Univariate/Bivariate Analysis
# Categorical vs numerical
# Use case - To find contibution on a standard scale

# simple data
data = [23,45,100,20,49]
subjects = ['eng','science','maths','sst','hindi']
plt.pie(data,labels=subjects)
plt.show()

runs=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\gayle-175.csv")
plt.pie(runs['batsman_runs'],labels=runs['batsman'],autopct='%0.1f%%',shadow=True,explode=(0.1,0,0,0.3,0,0)) # this autopct is a format we must follow
# We can give own colours like this too
# plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',colors=['blue','green','yellow','pink','cyan','brown'])
plt.show()



