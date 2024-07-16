#Block of statement that performs a specific task
'''
    def func_name(param1,param2..):  <--This is function definition
        #some work
        return val
    func_name(arg1,arg2..)#function call
'''
def cal_sum(a,b):
     print(a+b)
     return sum
a=5
b=10
#Calling the function
cal_sum (a,b)


def print_hello():
    print("Hello World")
#Calling the function

print_hello()
print_hello()
print_hello()
output=print_hello()
print(output) #the return type is not there so returns None

#average of 3 numbers
def average(x,y,z):
    print((x+y+z)/3)
q=int(input("Enter value for q : "))
p=int(input("Enter value for p : "))
r=int(input("Enter value for r : "))
average(q,p,r)

#function in python
#built-in function --> print(), len(), type(), range()


#default parameter

def greet(name="Sudarshan"): #if while calling the function there is no parameter passed in then the "Sudarshan" will be considered and code will run
    print("Hello",name)
greet()
greet("Suresh")

#WAF to print the length of list
cities=["Sangli","Miraj","Ichalkaranji","Pune"]
Hero=["Ironman","Batman","Ben10","Hulk","Thor"]
def print_c(list):
    print(len(list))

print_c(cities)
print_c(Hero)

#write a function for factorial 
def fact(num):
    i=1
    factor=1
    while i<=num:
        factor*=i
        i+=1
    return factor

s=int(input("Enter the number to remove factorial : "))
ans=fact(s)
print("Factorial for ",s," : ",ans)