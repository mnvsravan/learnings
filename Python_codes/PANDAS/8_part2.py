import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
deaths=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\time_series_covid19_deaths_global.csv")
rates=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\time_series_covid19_confirmed_global.csv")

print(deaths.head())
print(pd.DataFrame({'cse':[120]}))
print(pd.DataFrame({'cse':[120]}).melt())
print(pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}))
print(pd.DataFrame({'cse':[120],'ece':[100],'mech':[50]}).melt(var_name='branch',value_name='num_students'))

print(pd.DataFrame(
    {
        'branch':['cse','ece','mech'],
        '2020':[100,150,60],
        '2021':[120,130,80],
        '2022':[150,140,70]
    }
).melt(id_vars=['branch'],var_name='year',value_name='students')) # id_vars keep the col non repeated like a fixed point


deaths = deaths.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_deaths')
rates = rates.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_cases')

o=rates.merge(deaths,on=['Province/State','Country/Region','Lat','Long','date'])[['Country/Region','date','num_cases','num_deaths']]

print(o.head())
print(o)


# Pivot Table
# The pivot table takes simple column-wise data as input, and groups the entries into a two-dimensional table that provides a multidimensional summarization of the data.
import seaborn as sns
df = sns.load_dataset('tips')
cf = sns.load_dataset('tips')
kf = sns.load_dataset('tips')
print(cf.head())
cf=cf.groupby(['sex','smoker'])[['total_bill']].mean()
print(cf)
cf=cf.unstack()
print(cf)

# pivot is short cut
print(df.pivot_table(index='sex',columns='smoker',values='total_bill'))
# aggfunc
df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='std')


# all cols together
print(kf.pivot_table(index='sex',columns='smoker',values='size'))


# multidimensional
print(df.pivot_table(index=['sex','smoker'],columns=['day','time'],aggfunc={'size':'mean','tip':'max','total_bill':'sum'},margins=True))




# margins-> it makes an all col and displays data
print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum',margins=True))

expenses=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\expense_data.csv")
print(expenses.head())

# A small function a step which u might not understand based on dates
expenses['Date'] = pd.to_datetime(expenses['Date'])
expenses['month'] = expenses['Date'].dt.month_name()

ans=expenses.pivot_table(index='month',columns='Category',values='INR',aggfunc='sum',fill_value=0) # we must use fill_value not fill na
# # .fillna() is a DataFrame method, so call it on the resulting table object
# expenses.pivot_table(
#     index="month", columns="Category", values="INR", aggfunc="sum"
# ).fillna(0) correct 
ans.plot(kind='bar')
plt.show()