import pandas as pd
import numpy as np
import sys
IPL = pd.read_csv(
    r"C:\Users\Mnv Sravan\Downloads\ipl-matches.csv"
)
print(IPL)
vk=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\kohli_ipl.csv", index_col='match_no')
vk.squeeze()
print(vk)
subs=pd.read_excel(r"C:\Users\Mnv Sravan\Downloads\subs.xlsx")
print(subs)
movies=pd.read_excel(r"C:\Users\Mnv Sravan\Downloads\bollywood.xlsx")
print(movies)
import sys
print(sys.getsizeof(vk))
print(sys.getsizeof(vk.astype('int16')))
print(sys.getsizeof(vk.astype('int8')))

# between , OnLY WORKS WITH DATA SERIES NOT DATAFRAMES
print(vk['runs'].between(90,100))
print(vk[vk['runs'].between(90,100)])

# clip
subs=subs.clip(100,200)
print(subs)
# What clip() does

# It limits values to a specified range:

# Values less than 100 become 100
# Values greater than 200 become 200
# Values between 100 and 200 stay unchanged


# drop_duplicates


temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp.drop_duplicates())
print(temp.drop_duplicates(keep='last')) # this will keep the last occurrence of each duplicate value instead of the first one
print(temp.duplicated().sum())
print(movies.drop_duplicates())
print()
temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
print(temp.isnull())
print(temp.isnull().sum())
print(temp.notnull())

#DROPNA
print(temp.dropna())
# print(temp.dropna(inplace=True)) # this will drop the null values from the original series and return None
# we dont use inplace true cuzz it will change the original temp

 #FILLNA
temp=temp.fillna(0) # u can fill with anything like mean median mode or any value
print(temp)

# isin

print(vk[vk.isin([1,99,100,67])])

#APPLY THIS IS IMP
movies['lead']=movies['lead'].str.split(' ').apply(lambda x: x[0].upper())
print(movies)

subs=subs['Subscribers gained'].apply(lambda x: 'High' if x>subs['Subscribers gained'].mean() else 'Low')
print(subs)

#COPY
print(vk.head())
new=vk
new.iloc[0]=999
print(new.head())
print(vk.head())

new1=vk.copy() # now this makes the original unaffected by changes in new1
new1.iloc[0]=1
print(new1.head())
print(vk.head())

