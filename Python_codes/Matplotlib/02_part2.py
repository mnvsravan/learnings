import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\iris.csv")
print(iris.head())
batters=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\batter (1).csv")
print(batters.head())


fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(batters['runs'],batters['avg'],batters['strike_rate'],marker='+')
ax.set_title('IPL batsman analysis')
ax.set_xlabel('Runs')
ax.set_ylabel('Avg')
ax.set_zlabel('SR')
plt.show()


x = [0,1,5,25]
y = [0,10,13,0]
z = [0,13,20,9]

fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(x,y,z,s=[100,100,100,100]) # this s parameter controls the size of the points in the scatter plot. Here, we are using a list of sizes for each point.
ax.plot3D(x,y,z,color='red')
plt.show()