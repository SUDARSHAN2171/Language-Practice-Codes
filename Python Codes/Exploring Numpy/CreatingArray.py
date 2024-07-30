import numpy as np

# 1-D array using numpy 
array1=np.array([1,2,3,4,5])
print(array1)
print(type(array1))

# 2-D array using numpy
array2=np.array([[1,2,3],[4,5,6]])
print(array2)
print(type(array2))

# 3-D array using numpy
array3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array3)
print(type(array3))

#check number of Dimensions
print("Number of Dimensions in array1 : ",array1.ndim)
print("Number of Dimensions in array2 : ",array2.ndim)
print("Number of Dimensions in array3 : ",array3.ndim)

# Higher Dimensional arrays
array4=np.array([1,2,3,4],ndmin=5)  #this creates a 5 dimensional array
print(array4)
print("Number of Dimensions in array4 : ",array4.ndim)
 

