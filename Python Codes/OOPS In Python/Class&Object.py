#class is a blueprint for the creating object
'''
#creating class
class Student:
    name="Sudarshan Jadhav"
    
#creating object(instance)
s1=Student()
print(s1.name)
'''
class Student:
    name="Sudarshan Jadhav"
    
s1=Student() 
print(s1)           #s1,s2 both are the objects for the class 'Student' and since there is only one name in the class so both are printing the same name
print(s1.name)
s2=Student()
print(s2)
print(s2.name)


class Car:
    color='blue'
    brand='mercedes'
    
car1=Car()
print(car1.color)
print(car1.brand)