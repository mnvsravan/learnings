import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

# Regression Plots
# regplot
# lmplot
# In the simplest invocation, both functions draw a scatterplot of two variables, x and y, and then fit the regression model y ~ x and plot the resulting regression line and a 95% confidence interval for that regression.

# axes level
# hue parameter is not available
sns.regplot(data=tips,x='total_bill',y='tip')
sns.lmplot(data=tips,x='total_bill',y='tip',hue='sex')
plt.show()

# residplot-> Like it shows how much it differs from the reg plot
sns.residplot(data=tips,x='total_bill',y='tip')
plt.show()




# A second way to plot Facet plots -> FacetGrid
# figure level -> relplot -> displot -> catplot -> lmplot
sns.catplot(data=tips,x='sex',y='total_bill',kind='violin',col='day',row='time')
plt.show()

g = sns.FacetGrid(data=tips,col='day',row='time',hue='smoker')
g.map(sns.boxplot,'sex','total_bill')
g.add_legend()
plt.show()


# Plotting Pairwise Relationship (PairGrid Vs Pairplot)
# pairplot finds all the num cols and plots all plots between them

sns.pairplot(iris,hue='species')
# pair grid
g = sns.PairGrid(data=iris,hue='species')
# g.map
g.map(sns.scatterplot)
plt.show()


# map_diag -> map_offdiag
h = sns.PairGrid(data=iris,hue='species')
h.map_diag(sns.boxplot)
h.map_offdiag(sns.kdeplot)
plt.show()

# map_diag -> map_upper -> map_lower
g = sns.PairGrid(data=iris,hue='species')
g.map_diag(sns.histplot)
g.map_upper(sns.kdeplot)
g.map_lower(sns.scatterplot)
plt.show()

# vars
o = sns.PairGrid(data=iris,hue='species',vars=['sepal_width','petal_width'])
o.map_diag(sns.histplot)
o.map_upper(sns.kdeplot)
o.map_lower(sns.scatterplot)
plt.show()

# JointGrid Vs Jointplot

sns.jointplot(data=tips,x='total_bill',y='tip',kind='hist',hue='sex')

# JointGrid-> u can use diff combo of grpahs instreead of one standard ones
g = sns.JointGrid(data=tips,x='total_bill',y='tip')
g.plot(sns.kdeplot,sns.violinplot)
plt.show()