#set is the collection of the unordered items
#each element in the set must be unique & immutable

set1={1,2,3,4,5,5}
print(set1)
print(type(set1))
set2={1,1,1,2,3,3,7,9,2,"Home","World"}
print(set2)
#set when printed always return same answer in different order and will not repeat the number or world which you used more then one time 
print(len(set2)) #even len will ignore dublicates



info={}
subj=int(input("Enter Mark for Physics : "))
info.update({"Physic" : subj})

subj=int(input("Enter Mark for Chemistry : "))
info.update({"Chemistry" : subj})

subj=int(input("Enter Mark for Maths : "))
info.update({"Maths" : subj})
print(info)

store={
    ("float" , 9.0),
    ("int" , 9)
}
print(store)