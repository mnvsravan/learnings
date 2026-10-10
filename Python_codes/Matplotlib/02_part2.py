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

# 3D Surface Plots
x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)
xx, yy = np.meshgrid(x,y)
z1=xx**2 + yy**2
fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.plot_surface(xx,yy,z1,cmap='viridis')
plt.show()

z=np.sin(xx) + np.cos(yy)
fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.plot_surface(xx,yy,z,cmap='plasma')
plt.show()

z = np.sin(xx) + np.log(xx)
fig = plt.figure(figsize=(12,8))
ax = plt.subplot(projection='3d')
p = ax.plot_surface(xx,yy,z,cmap='viridis')
fig.colorbar(p)
plt.show()

# Contour Plots-> Like it gives the contour lines of the surface plot. It is like a 2D representation of the 3D surface plot. It is useful to visualize the surface plot in 2D. It is also useful to visualize the gradient of the surface plot. It is also useful to visualize the level curves of the surface plot.

fig = plt.figure(figsize=(12,8))
ax = plt.subplot()
p = ax.contour(xx,yy,z1,cmap='viridis')
fig.colorbar(p)
plt.show() 

fig = plt.figure(figsize=(12,8))
ax = plt.subplot()
p = ax.contourf(xx,yy,z1,cmap='viridis') # counterf is like contour but it fills the area between the contour lines with color. It is useful to visualize the surface plot in 2D. It is also useful to visualize the gradient of the surface plot. It is also useful to visualize the level curves of the surface plot.
fig.colorbar(p)
plt.show() 

delivery=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\batters.csv")
temp_df = delivery[(delivery['ballnumber'].isin([1,2,3,4,5,6])) & (delivery['batsman_run']==6)]
grid = temp_df.pivot_table(index='overs',columns='ballnumber',values='batsman_run',aggfunc='count')
plt.figure(figsize=(20,10))
plt.imshow(grid)
plt.yticks(np.arange(0,20), list(range(1,21))) # this means that we are setting the y-ticks to be the overs from 1 to 20. The np.arange(0,20) means that we are setting the y-ticks to be from 0 to 19. The list(range(1,21)) means that we are setting the y-ticks to be from 1 to 20. This is because the index of the grid is from 0 to 19 but we want to show the overs from 1 to 20.
plt.xticks(np.arange(0,6), list(range(1,7)))
plt.colorbar()
plt.show()

