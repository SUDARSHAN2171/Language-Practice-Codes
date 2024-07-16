#list are mutable this can be changed
#built in data type 
marks=[90.7,97,93.4,93]
print(marks)
print(type(marks))
print(len(marks))
marks.append(66)
print(marks)
marks.append("Sudarshan")
print(marks)

#slicing in list
print(marks[1:3])
print(marks[-4:-1])
print(marks[-5:len(marks)])
print(marks[:4])

#methods in list
number=[2,1,3]
print(number)
number.append(4)
print(number)
number.sort()
print(number)
number.sort(reverse=True)
print(number)
number.reverse()
print(number)
number.insert(2,7)
print(number)
