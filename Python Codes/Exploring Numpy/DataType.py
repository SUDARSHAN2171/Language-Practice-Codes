import numpy as np
'''
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
#Checking the Data Type of an Array
array1 = np.array([1, 2, 3, 4])
print(array1.dtype)

#Get the data type of an array containing strings
array2 = np.array(['apple', 'banana', 'cherry'])
print(array2.dtype)

#Create an array with data type string
array3 = np.array([1,2,3,4,5],dtype='S')
print(array3.dtype)

#create a array with data type of 4 bytes integer
array4 = np.array([1,2,3,4,5],dtype="i4")
print(array4)
print(array4.dtype)

#convert the data type of a existing array
array5 = np.array([1.1,2.2,3.3,4.4,5.5])
ugarray5 = array5.astype('i')
print(ugarray5)
print(ugarray5.dtype)

#change the data type of a float using int 
array6 = np.array([1.1,2.2,3.3,4.4,5.5])
uparray6 = array6.astype(int)
print(uparray6)
print(uparray6.dtype)

#change the data type from integer to a boolean
array7 = np.array([1,2,3,4,5,0])
ubarray7 = array7.astype(bool)
print(ubarray7)
print(ubarray7.dtype)