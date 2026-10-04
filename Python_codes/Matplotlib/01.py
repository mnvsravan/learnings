# import the library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2D Line plot
# Bivariate Analysis
# categorical -> numerical and numerical -> numerical
# Use case - Time series data

# plotting a simple function
price = [48000,54000,57000,49000,47000,45000]
year = [2015,2016,2017,2018,2019,2020]
plt.plot(year,price)
plt.show()

batsman=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\sharma-kohli.csv")
print(batsman.head())
# plt.plot(batsman['index'],batsman['V Kohli'])
# plt.plot(batsman['index'],batsman['RG Sharma'])

# colors(hex) and line(width and style) and marker(size)
# plt.plot(batsman['index'],batsman['V Kohli'],color='#D9F10F')
# plt.plot(batsman['index'],batsman['RG Sharma'],color='#FC00D6')

# plt.plot(batsman['index'],batsman['V Kohli'],color='#D9F10F',linestyle='solid',linewidth=3)
# plt.plot(batsman['index'],batsman['RG Sharma'],color='#FC00D6',linestyle='dashdot',linewidth=2)

plt.plot(batsman['index'],batsman['V Kohli'],color="#F1620F",linestyle='solid',linewidth=3,marker='o',markersize=10,label='V Kohli')
plt.plot(batsman['index'],batsman['RG Sharma'],color="#1C83D7",linestyle='dashdot',linewidth=2,marker='o',label='RG Sharma')
plt.title('Rohit Sharma Vs Virat Kohli Career Comparison')
plt.xlabel('Season')
plt.ylabel('Runs Scored')
plt.legend(loc='best') # we must need to give label in the plot function to use legend, this will show the label in the plot
plt.gca().set_facecolor("black") # this is used to change the background color of the plot
plt.grid()


# to find like the intersection point of the two lines we can use the following code
x=batsman['index']
for i in range(len(x)):
    if batsman['V Kohli'][i] == batsman['RG Sharma'][i]:
        plt.scatter(x[i],batsman['V Kohli'][i],color='yellow',s=100) # s is used to change the size of the marker
plt.show()


# limiting axes
price = [48000,54000,57000,49000,47000,45000,4500000]
year = [2015,2016,2017,2018,2019,2020,2021]
plt.plot(year,price)
plt.ylim(0,75000)
plt.xlim(2017,2019)
plt.show()

# Scatter Plots
# Bivariate Analysis
# numerical vs numerical
# Use case - Finding correlation
# plt.scatter simple function
x = np.linspace(-10,10,50)
y = 10*x + 3 + np.random.randint(0,300,50)
plt.scatter(x,y)
plt.show()

df=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\batter.csv")
df=df.head(50)
plt.scatter(df['avg'],df['strike_rate'],color='red',marker='*',s=100) # this s is like how big the marker should be, we can multiply the s with some other column to make the size of the marker dynamic
plt.title('Avg and SR analysis of Top 50 Batsman')
plt.xlabel('Average')
plt.ylabel('SR')
plt.show()

#tips
tips=sns.load_dataset('tips') 
plt.scatter(tips['total_bill'],tips['tip'],color='green',marker='*',s=tips['size']*20) # this s is like how big the marker should be, we can multiply the s with some other column to make the size of the marker dynamic
plt.show()


# scatterplot using plt.plot
# faster
# plt.plot(tips['total_bill'],tips['tip'],'o') so it depends on our use , cuz the scatter is slow



