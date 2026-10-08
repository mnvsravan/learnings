import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\iris.csv")
print(iris.head())
batters=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\batter (1).csv")
print(batters.head())

plt.figure(figsize=(15,7)) # we must use this first cuz it sets the size of the figure before we plot anything.
iris['Species'] = iris['Species'].replace({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})
# Why? Because c= in scatter() works conveniently with numerical values to determine colors.
plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='jet',alpha=0.7)
#cmap means color map.It tells Matplotlib which color scheme to use for the values 0, 1, and 2. alpha controls transparency.
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.colorbar()
plt.show()


sample_df = batters.head(100).sample(25,random_state=5)
print(sample_df)
plt.figure(figsize=(18,10))
plt.scatter(sample_df['avg'],sample_df['strike_rate'],s=sample_df['runs']) # this s parameter controls the size of the points in the scatter plot. Here, we are using the 'runs' column to determine the size of each point.
for i in range(sample_df.shape[0]):
    plt.text(   # This function allows us to add text to the plot at specified coordinates.
        
        # instead of this iloc we can use values[i] cuz it converts pd to numpy array to get the value of the column at index i. But iloc is more explicit and clear.
        sample_df['avg'].iloc[i],
        sample_df['strike_rate'].iloc[i],
        sample_df['batter'].iloc[i]
    )
plt.show()


x = [1,2,3,4]
y = [5,6,7,8]
plt.scatter(x,y)
plt.text(1,5,'Point 1')
plt.text(2,6,'Point 2')
plt.text(3,7,'Point 3')
plt.text(4,8,'Point 4',fontdict={'size':12,'color':'brown'}) # we can also use fontdict to customize the font size and color of the text.
plt.show()

# Horizontal and Vertical lines

plt.figure(figsize=(18,10))
plt.scatter(sample_df['avg'],sample_df['strike_rate'],s=sample_df['runs'])
plt.axhline(y=130,color='red') # this is line parallel to x-axis at y=130. We can also use plt.axhline(y=130,color='red') to be more explicit.
plt.axhline(y=140,color='green')
plt.axvline(x=30,color='red')
for i in range(sample_df.shape[0]):
  plt.text(sample_df['avg'].values[i],sample_df['strike_rate'].values[i],sample_df['batter'].values[i])
plt.show()



# Subplots-> same like plt but this helps us to plot multiple plots in a single figure. It returns a tuple containing the figure and axes objects. The axes object is used to plot on the specific subplot.
# fucntions are also same as plt but we use ax instead of plt. For example, ax.scatter() instead of plt.scatter(). We can also use ax.set_title() instead of plt.title() to set the title of the subplot.
fig,ax = plt.subplots(figsize=(15,6))
ax.scatter(batters['avg'],batters['strike_rate'],color='red',marker='+')
ax.set_title('Something')
ax.set_xlabel('Avg')
ax.set_ylabel('Strike Rate')
plt.show()


fig, ax = plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(10,6)) # This nrows and ncols parameters are used to specify the number of rows and columns in the subplot grid. sharex=True means that the x-axis will be shared between the two subplots. This is useful when we want to compare two plots with the same x-axis.
# we have sharey too which means that the y-axis will be shared between the two subplots. This is useful when we want to compare two plots with the same y-axis.
ax[0].scatter(batters['avg'],batters['strike_rate'],color='red')
ax[1].scatter(batters['avg'],batters['runs'])
ax[0].set_title('Avg Vs Strike Rate')
ax[0].set_ylabel('Strike Rate')
ax[1].set_title('Avg Vs Runs')
ax[1].set_ylabel('Runs')
ax[1].set_xlabel('Avg')
plt.show()


fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(10,10))
ax[0,0].scatter(batters['avg'],batters['strike_rate'],color='red')
ax[0,1].scatter(batters['avg'],batters['runs'])
ax[1,0].hist(batters['avg'],bins=[0,10,20,30,40,50]) # bins parameter is used to specify the number of bins in the histogram. The default value is 10.
ax[1,1].hist(batters['runs'],bins=[1000,2000,4000,6000,8000,10000]) # bins parameter is used to specify the number of bins in the histogram. The default value is 10.
plt.show()


# WE CAN ALSO USE fig.add_subplot() TO CREATE SUBPLOTS. IT IS MORE FLEXIBLE THAN plt.subplots() BECAUSE IT ALLOWS US TO CREATE SUBPLOTS IN ANY POSITION IN THE GRID. BUT IT IS MORE VERBOSE THAN plt.subplots().
# fig = plt.figure()

# ax1 = fig.add_subplot(2,2,1) this means that we are creating a subplot in the first position of a 2x2 grid. The first two parameters are the number of rows and columns in the grid, and the third parameter is the position of the subplot in the grid.
# ax1.scatter(batters['avg'],batters['strike_rate'],color='red')

# ax2 = fig.add_subplot(2,2,2) this means that we are creating a subplot in the second position of a 2x2 grid. The first two parameters are the number of rows and columns in the grid, and the third parameter is the position of the subplot in the grid.
# ax2.hist(batters['runs'])

# ax3 = fig.add_subplot(2,2,3) this means that we are creating a subplot in the third position of a 2x2 grid. The first two parameters are the number of rows and columns in the grid, and the third parameter is the position of the subplot in the grid.
# ax3.hist(batters['avg'])
