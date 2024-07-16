#dictionaries are used to stroe data values in key:value pairs
#dictionaries are mutable(changeable) & dont allow duplicate keys
dict={
    "name":"John",
    "age":30,
    "city":"New York",
    "subjects":["pthon","c++","java"],
    "topic":("inheritance","overriding")
}
print(type(dict))
print(dict)
print(dict["city"])
print(dict["age"])
dict["surname"]="patil"
print(dict["name"])
print(dict["surname"])

student={
    "name":"Sudarshan Jadhav",
    "PRN":"22UAI039",
    "Subject":{
        "Math":97,
        "Science":98,
        "English":95
    }
}
print(student)
#methods in dictonary
print(len(list(student.keys())))
print(student.keys())   #return all the keys
print(student.values()) #return all values
print(student.items())  #return all (key,value) pair in tuple
#print(student["name2"]) this will give error as the is no such name2 but the below wont give an error just it will return None
print(student.get("name2")) 
print(student.get("name")) #return the key according to value
new_student={"City":"Sangli","name":"Ujal"} # name will override over sudarshan as ujal
print(student.update(new_student))    #inserts the specified items to the dictionary
print(student)