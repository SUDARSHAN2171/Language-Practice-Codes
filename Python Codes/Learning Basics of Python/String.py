#string can be accessed but not mainpluted or they are inmutable
str1="This is a string"
str2="""This is another way to create string"""
str3='even this too'
#this is used to go to new line by using escape sequence character "\n","\t"
str4="This is string.\nthis is the way to go to next line\tthis the way to create a space"
print(str1)
print(str2)
print(str3)
print(str4)
print(str1+" "+str2)

#function in string 
print(len(str1))
print(str2.endswith("string")) #this returns true if the str2 ends with "string"
print(str2)
print(str3.capitalize()) #this returns true if
print(str3.replace("e","A"))#this is used to replae the alphabate,integer,or string in a string
print(str1.find("p"))#if the pass value is there in the string then we get the index and if not found then we get "-1"
#indexing in string called as slicing
print(str1[0])
print(str1[1:5])
print(str1[:4])
print(str1[3:])
print(str1[-1])
print(str1[-6:len(str1)])