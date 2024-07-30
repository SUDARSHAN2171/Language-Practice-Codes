#Array indexing is the same as accessing an array element.


import numpy as np

# Access Array Elements
array1=np.array([1,2,3])
print("this will print the value at array1[2] : ",array1[2])

#add the elements in the array
array2=np.array([1,2,3])
print("this will print the value at array2[1]+array2[2] : ",array2[1]+array2[2])

#Access 2-D Arrays
array3=np.array([[1,2,3],[4,5,6]])
print("this will print the element at 2nd row and 3rd column : ",array3[1,2])       #this will print the element at 2nd row and 3rd column 
print("this will print the element at 1nd row and 2rd column : ",array3[0,1])       #this will print the element at 1nd row and 2rd column 

array4=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("this will print the value at array4[0,1,2] : ",array4[0,1,2])

'''
The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6
'''

#negative indexing
#this is used to access array fromm the end

print("this will print the last element of array1 : ",array1[-1])     #this will print the last element of array1
print("this will print the last element of array3 (which is 6) : ",array3[-1,-1])   #this will print the last element of array3 (which is 6)

