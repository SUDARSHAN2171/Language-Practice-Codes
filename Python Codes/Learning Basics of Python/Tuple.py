#a built-in data type that lets us create immutable sequences of values
tup=(87,64,33,95,76)
print(type(tup))
#tup[0]=43 this is not allowed
tup1=(1)
print(type(tup1)) #this is not the correct way to waite tuple
tup2=(1,)
print(type(tup2)) #this is the correct way to write tuple

tup3=tup*5   #this is used to print n element n times in tuple
print(tup3)

#scaling in tuple
print(tup[3:len(tup)])

#methods in tuple
print(tup.index(95)) #returns the first index of the value
print(tup.count(95)) #returns the count of the value in tuple