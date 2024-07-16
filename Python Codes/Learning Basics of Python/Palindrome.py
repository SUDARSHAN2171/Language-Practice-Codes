# racecar , [1,2,2,1] ,ma'am
list1=[1,5,3,3,5,1]
list2=[1,2,3,4,5,6]
copy1=list1.copy()
copy1.reverse()
print(copy1)
if(copy1==list1):
    print("Palindrome")
else:
    print("Not Palindrome")
    
copy2=list2.copy()
copy2.reverse()
print(copy2)
if(copy2==list2):
    print("Palindrome")
else:
    print("Not Palindrome")
