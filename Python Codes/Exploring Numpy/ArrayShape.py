import numpy as np
#shape of an array
#the shape of an array is the number of elements in each dimension

#get the shape of array
array1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("This will tell shape of array1 :",array1.shape)      #i.e the output will be(2,5) as the are 2 dimentions each have 5 elements

#create a array with dimensions using ndmin using a vector with value 1,2,3,4 and verify that last dimension has the value 4
array2=np.array([1,2,3,4],ndmin=5)
print(array2)
print("This will give the shape of array2 : ",array2.shape)     #Integers at every index tells about the number of elements the corresponding dimension has.In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.
