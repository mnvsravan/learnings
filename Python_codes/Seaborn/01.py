import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tips = sns.load_dataset('tips')
print(tips.head())

# scatter plot -> axes level function
sns.scatterplot(data=tips, x='total_bill', y='tip',hue='sex',style='time',size='size')
# we must pass data to the function, and then specify the x and y axes. We can also use hue, style, and size to add more dimensions to the plot.
#hue is used to color the points based on a categorical variable, style is used to change the marker style based on a categorical variable, and size is used to change the size of the points based on a numerical variable.
plt.show()

# relplot -> figure level -> square shape , figure level function is more used than axes level function, because it is more flexible and can be used to create multiple plots in a single figure.
sns.relplot(data=tips, x='total_bill', y='tip', kind='scatter',hue='sex',style='time',size='size')
plt.show()



# line plot
gap = px.data.gapminder()
print(gap.head())
temp_df = gap[gap['country'] == 'India']

# axes level function
sns.lineplot(data=temp_df, x='year', y='lifeExp')
plt.show()

# relplot -> figure level function
sns.relplot(data=temp_df, x='year', y='lifeExp', kind='line')
plt.show()


# hue -> style
temp_df = gap[gap['country'].isin(['India','Brazil','Germany'])]
sns.relplot(kind='line', data=temp_df, x='year', y='lifeExp', hue='country', style='continent', size='continent')
plt.show()

# facet plot -> figure level function -> work with relplot
# it will not work with scatterplot and lineplot
sns.relplot(data=tips, x='total_bill', y='tip', kind='line', col='sex', row='day')# we can use other parameters like hue, style, and size to add more dimensions to the plot.
plt.show() # we can use col_wrap to wrap the columns into multiple rows, and row_order and col_order to specify the order of the rows and columns.


# 2. Distribution Plots
# used for univariate analysis
# used to find out the distribution
# Range of the observation
# Central Tendency
# is the data bimodal?
# Are there outliers?
# Plots under distribution plot

# histplot
# kdeplot
# rugplot


# figure level -> displot
# axes level -> histplot -> kdeplot -> rugplot

# plotting univariate histogram
sns.histplot(data=tips, x='total_bill')
plt.show()

sns.displot(data=tips, x='total_bill', kind='hist')
plt.show()

# bins parameter
sns.displot(data=tips, x='total_bill', kind='hist',bins=2)
plt.show()

# It’s also possible to visualize the distribution of a categorical variable using the logic of a histogram. 
# Discrete bins are automatically set for categorical variables

# countplot
sns.displot(data=tips, x='day', kind='hist')
plt.show()

# hue parameter
sns.displot(data=tips, x='tip', kind='hist',hue='sex',element='step')# we can add other dimensions to the plot using the hue parameter, which will color the bars based on the categorical variable specified.
plt.show()

# faceting using col and row -> not work on histplot function
sns.displot(data=tips, x='tip', kind='hist',col='sex',element='step')
plt.show()