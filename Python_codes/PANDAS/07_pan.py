import pandas as pd
import numpy as np

courses=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\courseshahah.csv")
nov=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\reg-month1.csv")
dec=pd.read_excel(r"C:\Users\Mnv Sravan\Downloads\reg-month2.xlsx")
students=pd.read_excel(r"C:\Users\Mnv Sravan\Downloads\students.xlsx")

# pd.concat
# df.concat
# ignore_index
# df.append
# mullitindex -> fetch using iloc
# concat dataframes horizontally

regs = pd.concat([nov,dec],ignore_index=True) # this is the format and we use ignore_index to reset the index of the new dataframe  
print(regs)

# nov.append(dec,ignore_index=True) also words but it is deprecated in the latest version of pandas because it is less efficient than pd.concat()

multi = pd.concat([nov,dec],keys=['Nov','Dec'])
print(multi)
# Multiindex DataFrame
print(multi.loc[('Dec',4)])

# pd.concat([nov,dec],axis=1) this does column wise concatenation of the dataframes and it will create a new dataframe with all the columns of both the dataframes. If the number of rows in both the dataframes are not same then it will fill the missing values with NaN.
print(pd.concat([nov,dec],axis=1))


# inner join
print(students.merge(regs,how='inner',on='student_id'))

# left join
print(courses.merge(regs,how='left',on='course_id'))


# right join
temp_df = pd.DataFrame({
    'student_id':[26,27,28],
    'name':['Nitish','Ankit','Rahul'],
    'partner':[28,26,17]
})

students = pd.concat([students,temp_df],ignore_index=True)
print(students)
print(students.merge(regs,how='right',on='student_id'))


# outer join
print(students.merge(regs,how='outer',on='student_id').tail(10))

# nov1 = nov['student_id'].unique()
# print(nov1)
# dec2 = dec['student_id'].unique()
# print(dec2)
# print(nov1[np.isin(nov1,dec2)])
# sample = courses.merge(regs, how='inner', on='course_id')
# print(courses[~courses['course_id'].isin(sample['course_id'])])
sample = regs.merge(courses, how='inner', on='course_id')
print(students[~students['student_id'].isin(sample['student_id'])])

