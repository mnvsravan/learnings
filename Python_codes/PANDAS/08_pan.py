import numpy as np
import pandas as pd

# can we have multiple index? Let's try
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
a = pd.Series([1,2,3,4,5,6,7,8],index=index_val)
print(a)

# The solution -> multiindex series(also known as Hierarchical Indexing)
# multiple index levels within a single index

# how to create multiindex object
# 1. pd.MultiIndex.from_tuples()
index_val = [('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
multiindex = pd.MultiIndex.from_tuples(index_val)
print(multiindex.levels[1])
print(multiindex.levels[0])
print(multiindex)

# 2. pd.MultiIndex.from_product()
b=pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]]) # like this does cartisiean product
print(b.levels[1])
print(b.levels[0])
print(b)


# creating a series with multiindex object
s = pd.Series([1,2,3,4,5,6,7,8],index=multiindex)
print(s)

# how to fetch items from such a series
print(s['cse'])
print(s[('cse',2019)])


# unstack-> converts into data frame
temp = s.unstack()
print(temp)

#stack-> converts it back
temp = temp.stack()
print(temp)



branch_df1 = pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12],
        [13,14],
        [15,16],
    ],
    index = multiindex,
    columns = ['avg_package','students']
)
print(branch_df1)
print(branch_df1['students'])
print(branch_df1.loc[('cse', 2019)])
print(branch_df1.loc['cse'])



# multiindex df from columns perspective
branch_df2 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
    ],
    index = [2019,2020,2021,2022],
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

print(branch_df2)
print(branch_df2['delhi'])
print(branch_df2[('delhi','avg_package')])
print(branch_df2.loc[2019])


# Multiindex df in terms of both cols and index

branch_df3 = pd.DataFrame(
    [
        [1,2,0,0],
        [3,4,0,0],
        [5,6,0,0],
        [7,8,0,0],
        [9,10,0,0],
        [11,12,0,0],
        [13,14,0,0],
        [15,16,0,0],
    ],
    index = multiindex,
    columns = pd.MultiIndex.from_product([['delhi','mumbai'],['avg_package','students']])
)

print(branch_df3)
print(branch_df3.loc[('cse', 2019), ('delhi', 'avg_package')])

print(branch_df3.loc[
    [('cse', 2019), ('ece', 2020)],
    [('delhi', 'avg_package'), ('mumbai', 'avg_package')]
])

# we can do like these also 
# # multiple
# branch_df3.loc[('cse',2019):('ece',2020):2]
# # using iloc
# branch_df3.iloc[0:5:2]

# sort index
# both -> descending -> diff order
# based on one level
print(branch_df3.sort_index(ascending=False)) # both
print(branch_df3.sort_index(ascending=[False,True]))# branch desc , year arsc
print(branch_df3.sort_index(level=0,ascending=[False])) # level 0 is like branch , level 1 is year

# multiindex dataframe(col) -> transpose
print(branch_df3.transpose())

# swaplevel
print(branch_df3.swaplevel(axis=1)) # this like swaps the idx/col among themselves 