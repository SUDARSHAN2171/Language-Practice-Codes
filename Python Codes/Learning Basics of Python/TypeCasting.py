# a ="2"
# b=3
# print(a+b) 
#this is wont run and will give an erroe is the a is "a" is string and it cant be added into integer
a=int("2")
b=4.5
print(type(a))
print(a+b)

#similarlly 
a=float("7")
b=2.1
print(type(a))
print(a+b)

# a= char("5")
# b=Sudarshan
# print(type(a))
# print(a+b)
#even this also cant run an will goive error  
 
 #now this is how to type cast wwhile taking input
val = int(input("enter you age"))
print(type(val),val)

val =float(input("enter you decimal value"))
print(type(val),val)