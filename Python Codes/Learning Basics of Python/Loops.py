#loops are used to repeat instructions

#while loop
count = 1 #iterator
while count<=10 : #the process is called iteration
    print("Hello World",count)
    count+=1
    
print(count)

#print table 
num=input("Enter the number of your choice : ")
i=1
while i<=10 :
    print(i,"*",num,"=",int(num)*i)
    i+=1

#print the lis num2=[1,4,9,16,25,36,49,64,81,100]
idx=0
num2=[1,4,9,16,25,36,49,64,81,100]
while idx<len(num2):
    print(num2[idx])
    idx+=1
    
#search for element in the tuple using loop
num3=(1,4,9,16,25,36,49,64,81,100)
i=0
key=int(input("find the element : "))
while i<=9:
    if(num3[i]==key):
        print("Element found at ", i)
        break  #break is used to terminate if you have reached you solution
    else:
        print("Finding...")
    i+=1
    
    
#for loop 
lst=[1,2,3,4,5]
for val in lst:
    print(val)
vegatable=["Tomato","Apple","Bannana"]
for val in vegatable:
    print(val)
tup=(9,8,7,4,5,6,1,2,3)
for val in tup:
    print(val)
anem="Sudarshan"
for char in anem:
    print(char)
#linear search
l=[1,4,9,16,25,36,49,64,81,100]
x=25
index=0
for i in l:
    print(i)
    if(x==i):
        print("Element found at ", index)
        break
    index+=1
    
#range
#range function return a numbers, starting from 0by default, and increments by 1(by default),and stops before a specificed number
#syntax (Start?,stop,step?)
print(range(5)) 
seq = range(10)
for i in seq: #this is stop condition
    print(i)
#or    
for i in range(10): 
    print(i)
    
for i in range(2,10): #this is start and stop condition 
    print(i)
    
for i in range(2,10,2): #here the last 2 is the number of increment in loop
    print(i) 
    
#pass statement
#pass is a null statement that does nothing. It is used as a placeholder for future code
#syntax
# for el in range(10):
#     pass

# for i in range(5):
#     #assume this loop is empty for some reason
# print("Something")
#the above will give error so there is an alternative

for i in range(5):
    pass
print("Something")

#wap to calculate sum of first five numbers
sum=0
for i in  range(1,6):
    sum=sum+i
print(sum)

#wap to find factorial of first n numbers
give=int(input("Enter a number to find its Factorial : "))
fact=1
anyno=1
while anyno<=give:
    fact*=anyno
    anyno+=1
print("Factorial of",give," : ",fact)