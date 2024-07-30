import pandas as pd

#a dataframe is a two dimensional data structure ,like a 2-D array, or a table with a rows and columns

#create a simple dataframe
data ={
    'Name':['Aadesh','Ashish','Tanay','Ujal'],
    'Age':[19,21,20,18],
    'City':['Pune','Baregav','Miraj','Sangli']
}
store=pd.DataFrame(data)
print(store)
print('\n')

#locate Row
#if we what any specific data then we can print it like
print(store.loc[3])
print('\n')

#if we want to return 2 data at the same time we can do it like this
print(store.loc[[0,3]])
print('\n')

#if we want to return a data with specific range we can do it like this
print(store.loc[0:2])
print("\n")

#named indexes
store=pd.DataFrame(data,index=[1,2,3,4])
print(store)
print("\n")

store=pd.DataFrame(data,index=["First","Second","Third","Forth"])
print(store)
print("\n")

#locate named Indexes
print(store.loc["Second"])
