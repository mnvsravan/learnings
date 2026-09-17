import pandas as pd
import numpy as np
import sys

ipl= pd.read_csv(r"c:\Users\Mnv Sravan\Downloads\kohli_ipl.csv")
print(ipl)
movies=pd.read_excel(r"c:\Users\Mnv Sravan\Downloads\bollywood.xlsx")
print(movies)

# astype
print(sys.getsizeof(ipl))
ipl = ipl.astype('int16') # size is reduced to 1/4th of original size
print(sys.getsizeof(ipl))


# between
ipl['runs'].between(90,100) # returns a boolean series
print(ipl[ipl['runs'].between(90,100)]) # returns the rows where the runs are between 90 and 100

# clip
print(ipl['runs'].clip(100,200)) # limits the values to a specified range, values less than 100 become 100, values greater than 200 become 200, values between 100 and 200 stay unchanged

# drop_duplicates
temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp.drop_duplicates()) # returns a series with duplicate values removed
print(temp.drop_duplicates(keep='last')) # returns a series with duplicate values removed, keeping the last occurrence of each duplicate value instead of the first one
print(temp.duplicated().sum()) # returns the number of duplicate values in the series

# isnull
temp1 = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
print(temp1.isnull().sum())
# dropna
print(temp1.dropna()) # drops the null values from the original series and returns None

# fillna
temp1.fillna(temp1.mean(), inplace=True) # fills the null values with the mean of the series
print(temp1)


#isin
print(ipl['runs'].isin([0,49,34,56,90,100])) # returns a boolean series indicating whether each value in the 'runs' column is in the list [90,100]

# apply
movies = movies.set_index('movie')['lead']
print(movies.apply(lambda x:str(x).split()[0].upper()))

print(ipl['runs'].apply(lambda x: 'Good' if x > 50 else 'Bad')) # applies a function to each element of the DataFrame, returning a new DataFrame with the results

# copy
# like when we make normal stuff and make changes it will change the original one also but if we use copy it will not change the original one
ipl_copy = ipl.head(10).copy()
# now if we do changes to ipl_copy it will not affect the original ipl DataFrame

