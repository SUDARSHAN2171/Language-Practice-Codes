#Slicing in python means taking elements from one given index to another given index.

import numpy as np

#in a array from index 1 to 5
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("This will print the element from index 0-5 in array1 :",array1[1:5])
print("This will automaticly print the array from index 4 to the last : ",array1[4:])
print("This will print the array from begin to the 4th index : ",array1[:4])

#Negative Slicing
array4=np.array([1,2,3,4,5])
print("This is a example of negative slicing : ",array4[-3:-1])


#step
#Use the step value to determine the step of the slicing:
array5 = np.array([1, 2, 3, 4, 5, 6, 7])
print("This is a example of negative slicing with incremanation : ",array5[1:5:2])        #the 2 in the block represents the increment while running this

array6 = np.array([1, 2, 3, 4, 5, 6, 7])
print("This will print all the old numbers : ",array6[::2])      #if there is no begin of end set but the step is set then

#Slicing 2-D arrays
array7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("This will print the value at array7[1, 1:4] : ",array7[1, 1:4])

#From both elements, return index 2:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("This will print the value at arr[0:2, 2] :",arr[0:2, 2])

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("This will print the value at arr[0:2, 1:4] : ",arr[0:2, 1:4])