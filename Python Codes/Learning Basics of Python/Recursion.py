#when a function call itself repeatedly
def show(n):
    if(n==0):  #base case it is where the loop will end
        return
    print(n)
    show(n-1)
show(5) 


#factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
fact=int(input("Enter the number for factorial : "))
ans=factorial(fact)
print("Factorial of ",fact," : ",ans)


#WARF to calculate the sum of first n natural numbers
def sum_of_natural_numbers(n):
    if(n==1):
        return 1
    else:
        return n+sum_of_natural_numbers(n-1)
sum=int(input("Enter the number for sum : "))
ans=sum_of_natural_numbers(sum)
print("Factorial of ",sum," : ",ans)


#WARF to print all elements in list.

def print_list(list,index):
    if(index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)
cities=["Sangli","Miraj","Kolapur","Pune","Mumbai"]
print_list(cities,0)
