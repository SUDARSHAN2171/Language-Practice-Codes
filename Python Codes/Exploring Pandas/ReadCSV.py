import pandas as pd

#Read CSV Files
#A simple way to store a big data is to use CSV file(Comma Separated Files)
#CSV Files contains plain text and is a well know format that can be read by everyone including pandas
#in our example we will be using CSV file called 'data.cv'

#If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
data=pd.read_csv('data.csv')
print(data)
print("\n")

#load the csv into a dataframe
print(data.to_string())   #use to_string() to print the entire DataFrame.
print("\n")

#max_row
#the number of rows returned is defined in pandas option settings
#we can check th systems maximum rows with the pd.options.display.max_rows
print(pd.options.display.max_rows)  #check the systems maximum rows
print("\n")
#In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

#how to change the maximum number rows number with the some statement 
pd.options.display.max_rows=9999
print(data)     #now in this case the entire data will be printed just by writing data which no able to print at start
print("\n")