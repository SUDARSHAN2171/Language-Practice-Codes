#Python can be used to perform operations on a file.(read & write data)
'''
Type of all files
1.Text files:.txt,.docx,.log,etc.
2.Binary files:.mp4,.mov,.png,.jpeg,etc
All the variables are create in RAM, but RAM is volatile i.e when we will shut down or restart the pc then there will not be any data in it 
To avoid this we used this in files format
'''

#open, read & close file
#we have to open a file before reading or writing 
'''
Syntax:
f=open("file_name","mode")
             |       |
             |       |
 sample.txt<--       --> r:read mode
 demo.docx               w:write mode
 
 dta=f.read()
 f.close()
'''
 #if the file is present somewhere out the folder need to the entire path 
f = open("ML_LAB_CODES\Learning Python\demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

#if i want to specify i want to read only first 10 words including spaces then i can write it like this
e = open("ML_LAB_CODES\Learning Python\demo.txt", "r")
data = e.read(10) #by just writing 10 in bracket
print(data)
print(type(data))
e.close()

#Reading a file 
'''
data = f.read()  -->reads entire file 
data = f.readline()  -->reads one line at a time
'''
p = open("ML_LAB_CODES\Learning Python\demo.txt", "r")
line1 = p.readline()        #this is used to print the first line in file 
print(line1)

line2 = p.readline()        #this is used to print the second line in file 
print(line2)

line3=p.readline()
print(line3)                #if there in nothing in the next line in the file then space is printed
p.close()

#Writing to a file
'''
f=open("demo.txt","w")
f.write("this is a new line") overwrites the entire file

f=open("demo.txt","a")
f=write("this is a new line")#adds to the file

'''

b=open("ML_LAB_CODES\Learning Python\demo.txt","w")  
b.write("This statement will be overwritten")         #this will overwrite ont the file 
b.close()

c=open("ML_LAB_CODES\Learning Python\demo.txt","a")
c.write("This statement will be added no overwritten")  #this will add the statements at end
c.close()

#if there is no file which we are trying to write or append then the file will automatical created


#if we want to overwrite from the beginning we use r+ mode
d=open("ML_LAB_CODES\Learning Python\demo.txt","r+")
d.write("This will be overwritten")
print(d.read())
d.close()


#when we open a file in w+ mode then first full file will get empty then we can write on it

e=open("ML_LAB_CODES\Learning Python\demo.txt","w+")
e.write("This will be overwritten")
print(e.read())
e.close()