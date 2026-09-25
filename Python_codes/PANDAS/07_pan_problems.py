import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

courses=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\courseshahah.csv")
nov=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\reg-month1.csv")
dec=pd.read_excel(r"C:\Users\Mnv Sravan\Downloads\reg-month2.xlsx")
students=pd.read_excel(r"C:\Users\Mnv Sravan\Downloads\students.xlsx")
regs = pd.concat([nov,dec],ignore_index=True) # this is the format and we use ignore_index to reset the index of the new dataframe
# 1. find total revenue generated
total = regs.merge(courses,how='inner',on='course_id')['price'].sum()
print(total)


# 2. find month by month revenue
temp_df = pd.concat([nov,dec],keys=['Nov','Dec']).reset_index() # this is very imp , once check this
print(temp_df)
result = temp_df.merge(courses,on='course_id').groupby('level_0')['price'].sum()
print(result)


# 3. Print the registration table
# cols -> name -> course -> price
result=regs.merge(students,on='student_id').merge(courses,on='course_id')[['name','course_name','price']]
print(result)


# 4. Plot bar chart for revenue/course
regs.merge(courses,on='course_id').groupby('course_name')['price'].sum().plot(kind='bar')
plt.show()



# 5. find students who enrolled in both the months
common_student_id = np.intersect1d(nov['student_id'],dec['student_id'])
print(common_student_id)
# SAME
# nov1 = nov['student_id'].unique()
# print(nov1)
# dec2 = dec['student_id'].unique()
# print(dec2)
# print(nov1[np.isin(nov1,dec2)])

# 6. find course that got no enrollment
# courses['course_id']
# regs['course_id']
course_id_list = np.setdiff1d(courses['course_id'],regs['course_id'])
print(courses[courses['course_id'].isin(course_id_list)])
#SAME
# sample = courses.merge(regs, how='inner', on='course_id')
# print(courses[~courses['course_id'].isin(sample['course_id'])])

# 7. find students who did not enroll into any courses
student_id_list = np.setdiff1d(students['student_id'],regs['student_id'])
print(students[students['student_id'].isin(student_id_list)].shape[0])

# u can use above course logic to find the students who did not enroll into any courses



# 8. Print student name -> partner name for all enrolled students
# self join
# students.merge(students,how='inner',left_on='partner',right_on='student_id') this gives us so many cols on x and y so we can select only the cols we want
print(students.merge(students,how='inner',left_on='partner',right_on='student_id')[['name_x','name_y']])


# 9. find top 3 students who did most number enrollments
print(regs.merge(students,on='student_id').groupby(['student_id','name'])['name'].count().sort_values(ascending=False).head(3))


# 10. find top 3 students who spent most amount of money on courses
print(regs.merge(students,on='student_id').merge(courses,on='course_id').groupby(['student_id','name'])['price'].sum().sort_values(ascending=False).head(3))
# Alternate syntax for merge
# students.merge(regs)

print(pd.merge(students,regs,how='inner',on='student_id'))



ipl=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\matches.csv")
print(ipl.head())

delivery=pd.read_csv(r"C:\Users\Mnv Sravan\Downloads\deliveries.csv")
print(delivery.head(3))

# IPL Problems

# find top 3 studiums with highest sixes/match ratio
# find orange cap holder of all the seasons


temp_df = delivery.merge(ipl,left_on='match_id',right_on='id')
print(temp_df)
six_df = temp_df[temp_df['batsman_runs'] == 6]

num_sixes = six_df.groupby('venue')['venue'].count()
num_matches = ipl['venue'].value_counts()

print((num_sixes/num_matches).sort_values(ascending=False).head(10))




df = temp_df.groupby(['season', 'batsman'])['batsman_runs'].sum()

df = df.reset_index()

df = df.sort_values('batsman_runs', ascending=False)

df = df.drop_duplicates(subset=['season'], keep='first')

df = df.sort_values('season')

print(df)