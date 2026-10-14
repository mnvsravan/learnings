import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
tips = sns.load_dataset('tips')
print(tips.head())

# kdeplot
# Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continuous density estimate
sns.kdeplot(data=tips,x='total_bill')
sns.displot(data=tips,x='total_bill',kind='kde')
# hue -> fill
sns.displot(data=tips,x='total_bill',kind='kde',hue='sex',fill=True,height=10,aspect=2)
plt.show()


# Rugplot
# Plot marginal distributions by drawing ticks along the x and y axes.
# This function is intended to complement other plots by showing the location of individual observations in an unobtrusive way.
sns.kdeplot(data=tips,x='total_bill')
sns.rugplot(data=tips,x='total_bill')
plt.show() # we use this ruge plot on other graphs to show the distribution of the data points. It is used to show the distribution of the data points on the x-axis. It is used to show the distribution of the data points on the y-axis



# Bivariate histogram
# A bivariate histogram bins the data within rectangles that tile the plot 
# and then shows the count of observations within each rectangle with the fill color
# sns.histplot(data=tips, x='total_bill', y='tip')
sns.displot(data=tips, x='total_bill', y='tip',kind='hist',cbar=True)
plt.show()


# Bivariate Kdeplot
# a bivariate KDE plot smoothes the (x, y) observations with a 2D Gaussian
sns.kdeplot(data=tips, x='total_bill', y='tip',cbar=True,cmap='summer')
plt.show()


# 2. Matrix Plot
# Heatmap
# Clustermap

# Heatmap

# Plot rectangular data as a color-encoded matrix
gap = px.data.gapminder()
temp_df = gap.pivot(index='country',columns='year',values='lifeExp')
# axes level function
plt.figure(figsize=(15,15))
sns.heatmap(temp_df)
plt.show()


# annot
temp_df = gap[gap['continent'] == 'Europe'].pivot(index='country',columns='year',values='lifeExp')
plt.figure(figsize=(15,15))
sns.heatmap(temp_df,annot=True,linewidth=0.5, cmap='summer')
plt.show()



# Clustermap
# plot a matrix dataset as a hierarchically-clustered heatmap.
# This function requires scipy to be available.
iris = px.data.iris()
sns.clustermap(iris.iloc[:,[0,1,2,3]])
plt.show()