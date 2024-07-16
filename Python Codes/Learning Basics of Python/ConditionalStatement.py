#if-elif-else

age1 = 18

if (age1 < 18):
    print("You are under 18 years old.")
#elif is only checked if "if Statement is false"
elif (age1 == 18):          
    print("Under age")

light="Red"
if(light=="Yellow"):
    print("Get ready")
elif(light=="Red"):
    print("Stop")
#else acts as a default when the upper condition are false 
else:
    print("Stay calm")
#indentation:-giving proper spacing in code is "indentation"

marks=int(input("Enter you marks:"))
if(marks>=90):
    print("Grade : A")
elif(marks>=80 and marks<90):
    print("Grade : B")
elif(marks>=70 and marks<80):
    print("Grade : C")
else:
    print("Fail Zalayas next time abhayas karun ya")
    
#nesting
age=34
if(age>=18):
    if(age>=80):
        print("Can't drive")
    else:
        print("Can get a learnig licence")
else:
    print("Can't get a learnig licence")