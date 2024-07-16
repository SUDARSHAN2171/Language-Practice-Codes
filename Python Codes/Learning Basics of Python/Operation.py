a=10
b=10
c=20
num1=11
num2=5
#ways to use arithmetic operators
sum=num1+num2
print(num1+num2)
print("Sum : ",sum) #this is another way of printing anything

difference=num1-num2
print("Difference : ",difference) #this is the way to subtract 2 numbers

product=num1*num2
print("Product : ",product) #this is the way to multiply 2 numbers

quotient=num1/num2
print("Quotient : ",quotient) #this is the way to divide 2 numbers

remainder=num1%num2
print("Remainder : ",remainder) #this is the way calculate a remainder 

power = num1**num2
print("Power : ",power) #this is the way to calculate the power of a number

 #ways to use relational /comparison operators
if(a==b):   #this is the way to relation operator "=="
    print("The condition is true")

if(a!=c):    #this is the way to use relation operator "!="
    print("The condition is true")

if(a<c):     #this is the way to use relation operator "<,>,<=,>="
    print("The condition is true")
    
#ways to use assignment operators
a==b
print("Value for a==b",a)
a+=b
print("Value for a+=b",a)
b-=c
print("Value for b-=c",b)
c*=b
print("Value for c*=b",c)
c/=b
print("Value for c/=b",c)
a%=b
print("Value for a%=b",a)
c**=a
print("Value for c**=a",c)

# use of logical operator 

    # "and" operator
if(a==10 and b==10):
    print("Both conditions are true")

# "or" operator
if(a==10 or b==10):
        print("At least one condition is true")
        
# "not" operator
if(not(a==b)) :
    print(not(True))