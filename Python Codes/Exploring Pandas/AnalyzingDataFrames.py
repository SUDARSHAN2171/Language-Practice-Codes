import pandas as pd

#viewing the data
#one of the most used method for the getting a quick overview of the dataframe is the head() method
#the head() method returns the header and the a specific number of the rows ,starting from the top 

data=pd.read_csv('data.csv')
print(data.head(10)) #this will help to read the first 10 columns
print("\n")

#first 5 rows of dataframe
print(data.head())
print("\n")

#last 5 rows of dataframe
print(data.tail())
print("\n")

#info about the data 
#the dataframe object has a method called info(),the gives you more information about the data set
print(data.info())
#Result Explained
'''
The result tells us there are 169 rows and 4 columns:


  RangeIndex: 169 entries, 0 to 168
  Data columns (total 4 columns):

And the name of each column, with the data type:


   #   Column    Non-Null Count  Dtype  
  ---  ------    --------------  -----  
   0   Duration  169 non-null    int64  
   1   Pulse     169 non-null    int64  
   2   Maxpulse  169 non-null    int64  
   3   Calories  164 non-null    float64
'''
#Null Values
'''
The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.
'''
