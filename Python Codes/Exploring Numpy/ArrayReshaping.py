import numpy as np

#reshaping means making the change in the shape of an array
#the shape of an array is the number of elements in each dimension
#by reshaping we can add or remove dimensions or change number of elements in each dimension

# reshape 1-D array to 2-D array
array3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarray3=array3.reshape(3,4)
print(newarray3)        #this will convert the 1-D array into 3-D array each containing 4 element in it

#can we reshape into any shape
#yes as long as the element required are equal in both shapes 
'''
array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarray4 = array4.reshape(3, 3)
print(newarray4)
'''
#the above code will give error
#because the number of elements in the new shape is not equal to the number of elements in the other

#return copy or view
#check weather the return type is a copy or a view
array4=np.array([1,2,3,4,5,6,7,8])
print(array4.base)
print(array4.reshape(2,4).base) #so this is a view as it didnt return None

#unknown dimension
#it is allow to have one unknown dimension
#Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.Pass -1 as the value, and NumPy will calculate this number for you.
array5=np.array([1,2,3,4,5,6,7,8])
newarray5=array5.reshape(2,2,-1)        #Note: We can not pass -1 to more than one dimension.
print(newarray5)

#flattening the array
#this means to convert the multidimensional array in 1-D array
#we can use reshape(-1) ot do this
array6=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
newarray6=array6.reshape(-1)
print(newarray6)
#Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.