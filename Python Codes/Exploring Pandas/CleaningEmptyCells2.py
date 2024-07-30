import pandas as pd
#replace only for specified columns
'''
the above function replace all the null values in the dataframe
to only replace empty values for one column,specify the column name for the dataframe
'''
#replace Null values in calories column with number 130

df=pd.read_csv('data1.csv')
# data["Calories"].fillna(130,inplace=True)

#replace using mean,median or mode
'''
A common way to replace empty cells , is to calculate the mean, median or mode of the column
pandas uses the mean() median() & mode() method to calculate the respective values for a specified column
'''
x=df["Calories"].mean()
df["Calories"].fillna(x,inplace=True)