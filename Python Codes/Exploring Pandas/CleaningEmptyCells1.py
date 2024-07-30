import pandas as pd
#empty cells 
#empty cells can potentially give you a wrong result when you analyze data

#remove row
'''
one way to deal with empty cells is to remove rows that contain empty cells
This is usually OK,since the data sets can be very big, and removing a few rows will not have a big impact on the result
'''
data=pd.read_csv('data1.csv')
new_data=data.dropna()      #this will not change the original dataframe
print(new_data.to_string())
print("\n")

#if we want to change the original dataframe use the 'inplace=True' argument:
data.dropna(inplace=True)
print(data.to_string())
#Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

#replace empty values
'''
Another way of dealing with empty cells is to insert a new value instead 
This way you do not have to delete entire rows just because of some empty cells
the fillna() method allows us to replace cells with a value
'''
#Replace null with 130
data.fillna(130,inplace=True)
