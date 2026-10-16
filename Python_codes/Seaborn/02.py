import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
# Categorical Scatter Plot
# Stripplot
# Swarmplot
sns.scatterplot(data=tips, x='total_bill',y='tip')
# strip plot
# axes level function
sns.stripplot(data=tips,x='day',y='total_bill')
# using catplot
# figure level function
sns.catplot(data=tips, x='day',y='total_bill',kind='strip')
# jitter
sns.catplot(data=tips, x='day',y='total_bill',kind='strip',jitter=0.2,hue='sex')
# swarmplot
sns.swarmplot(data=tips, x='day',y='total_bill',hue='sex')
sns.catplot(data=tips, x='day',y='total_bill',kind='swarm',hue='sex')
plt.show()


# Boxplot
# A boxplot is a standardized way of displaying the distribution of data based on a five number summary (“minimum”, first quartile [Q1], median, third quartile [Q3] and “maximum”). It can tell you about your outliers and what their values are. Boxplots can also tell you if your data is symmetrical, how tightly your data is grouped and if and how your data is skewed.
# Box plot
sns.boxplot(data=tips,x='day',y='total_bill')
# Using catplot
sns.catplot(data=tips,x='day',y='total_bill',kind='box',hue='sex')
# single boxplot -> numerical col
sns.boxplot(data=tips,y='total_bill')


# Violinplot = (Boxplot + KDEplot)
# violinplot
sns.violinplot(data=tips,x='day',y='total_bill')
sns.catplot(data=tips,x='day',y='total_bill',kind='violin',hue='sex',split='True')
plt.show()

# barplot
sns.barplot(data=tips, x='sex', y='total_bill',hue='smoker',estimator=np.min)
sns.barplot(data=tips, x='sex', y='total_bill',errorbar=None)
plt.show()

# this ci is used to remove error bar

# point plot
sns.pointplot(data=tips, x='sex', y='total_bill',hue='smoker',errorbar=None)
# When there are multiple observations in each category, it also uses bootstrapping to compute a confidence interval around the estimate, which is plotted using error bars
plt.show()

# countplot
# A special case for the bar plot is when you want to show the number of observations in each category rather than computing a statistic for a second variable. This is similar to a histogram over a categorical, rather than quantitative, variable
sns.countplot(data=tips,x='sex',hue='day')



# faceting using catplot
sns.catplot(data=tips, x='sex',y='total_bill',col='smoker',kind='box',row='time')
plt.show()

