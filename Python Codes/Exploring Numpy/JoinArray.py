import numpy as np
#Joining means putting contents of two or more arrays in a single array.
array1=np.array([1,2,3,4,5])
array2=np.array([6,7,8,9,10])
array3=np.concatenate((array1,array2))
print("This will print in combination of array1 and array2 : ",array3)
