import pandas as pd
import numpy as nmp
import math
import os
from numpy.random import default_rng
from pandas.io import sql
import sqlalchemy as sqlalch
from sqlalchemy import create_engine
from sqlalchemy import text


#data_frame = pd.read_csv("../employee.csv")
#print(data_frame.head())
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "employee.csv"))

filtered_df = df[['first_name','last_name', 'age','city']]


print(filtered_df) # filter out firstname, lastname, city


#Conditions

#1) Keep only the rows where age is greater than 25. 
filter_by_age_df = df[filtered_df['age'] > 25]
#print(filter_by_age_df)

#2) Add a New Column:
#Add a column named years_experience with values [2, 5, 1, 10, 7].
val = [2, 5, 1, 10, 7]
filter_by_age_df["years of exeperience"] = nmp.random.choice(val, len(filter_by_age_df))
print(filter_by_age_df)

#3) Rename Column City to Location
filter_by_age_df = filter_by_age_df.rename(columns={'city':'location'})
print(filter_by_age_df.axes[1].values) # print out the column names

# 4) Remove the Gender Column from the dataframe
print(filter_by_age_df.drop(columns=['department']))

# 5) Group the data by department and calculate the mean salary and the maximum age.
filter_by_age_df.groupby('location')['salary'].mean()
filter_by_age_df.groupby('location')['age'].max()
print(filter_by_age_df)

#6) Sort by descending order
print(filter_by_age_df.sort_values(by=['salary'], ascending=False))

#7)Replace values in the location column: 'New York' with 'NYC' and 'Los Angeles' with 'LA'
filter_by_age_df.loc[filter_by_age_df.location == 'New York', 'location'] = 'NYC'
filter_by_age_df.loc[filter_by_age_df.location == 'Los Angeles', 'location'] = 'LA'

print(filter_by_age_df.loc[filter_by_age_df['location'] == 'New York City'])


#8) Convert the salary column to thousands by dividing each value by 1000
filter_by_age_df['salary'] = filter_by_age_df['salary'].apply(lambda x : x // 1000)
print(filter_by_age_df['salary'])

#9) Create a pivot table with department as the index and the mean salary
print(pd.pivot_table(filter_by_age_df,values='salary',index='department', aggfunc='mean'))

#10 && 11 ) Fill in Missing Values and Merge the DataFrame with another DataFrame containing id and performance_score
scores = [1.0, 2.0, 3.0, 4.0,5.0]
bonuses = [1,2,3,4]
per_df = pd.DataFrame(columns=['id','performance_score'], index=range(1,len(filter_by_age_df.index)))
per_df['id'] = default_rng().choice(435,434,replace=False)
per_df['performance_score'] = nmp.random.choice(scores, len(per_df.index))
# 12) Add Additional Bonus Colum
per_df['bonus (thousands)'] = nmp.random.choice(bonuses, len(per_df.index))
print(per_df)
merged_df = filter_by_age_df.merge(per_df,left_on='id', right_on='id')
# 13) Create a new column total_compensation as the sum of salary and bonus.
merged_df['total_compensation'] = merged_df['salary'] + merged_df['bonus (thousands)']
print(merged_df)

#14) Find unique values in the department column.
#Create a Subset Based on Multiple Conditions:
#Filter rows where age is greater than 25 and salary is less than 90000.
subset_one = merged_df.loc[(merged_df['age'] > 25) & merged_df['salary'] < 90.0]
print(subset_one[['age', 'salary']])

#15 Calculate cumulative sum of salary
cumulative_sum = sum(merged_df['salary'])
print(f'Cumulative Sum of Salaries: {cumulative_sum} (in thousands)')

#16 Remove Duplicates and Melt
merged_df= merged_df.drop_duplicates(subset=['first_name','last_name'], keep=False)
print(merged_df)

melted_df = pd.melt(merged_df,('id','first_name', 'last_name'),['age','total_compensation'])
print(melted_df)


##CONNECT TO SQL
engine = create_engine('mysql+pymysql://root:password123!@localhost:3306/test', echo=True)
def check_for_db():
    with engine.connect() as conn:
        melted_df.to_sql(name='imported',con=conn, if_exists='replace')
        print(conn.closed)

check_for_db()





