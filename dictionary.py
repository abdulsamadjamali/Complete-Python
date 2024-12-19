# data={
#     "Name ":"Abdul samad",#Stroing a String
#     "Caste " :"Jamali",
#     "age "   :21,#Stroing a intiger value
#     "Subjects ":["Python ","C++","Java ","PHP"],#Stroing a list
#     "is_adult ":True,#Stroing a boolen value
#     "Marks ":87.5, #Stroing a float value
#     "Teachers ":("Naveen ","Sajad","Farhyal","Abdul aziz")#Storing a tuple
# }
# print(data)
# print(type(data))
# print(data["Name "])
# print(data["Caste "])
# print(type(data ["Teachers "]))#tuple

# #lets say i want to add somethignig in  dict
# data["Surname "]="jamali"
# # here iam changing the value name 
# data["Name "]="Muhammad"
# print(data)

# CREATING A EMPTY DICTIONARY
# my_dictionary={}
# my_dictionary["name "]="Abdul samad jamali"
# print(my_dictionary)




student={
    "name" : "Abdul samad jamali",
    #nested Dictionary
    "subject" :{
        "phy ":88,
        "Chemi":76,
        "Maths":87
    }

}
# print(student)

# print(student["subject"]["Maths"])

# Methods of Dictionary

# print(student.keys())

# print(type(student.keys()))

#Type Casting 
# print(list(student.keys()))
# print(type(list(student.keys())))

# print(student.values())

# print(student.items())

#converting dict-tuple  into  list and access by index number
# print((list(student.items())))
# my_list=(list(student.items()))
# print(my_list[1])



# print(student["name"]) # its shows error if we pass rong key
# print(student.get("name")) # it shows a none value 

# student.update({"City":"Karachi"})
# print(student)
# or we can do the same work like this 
# new_dict={"city ":"karachi"}
# student.update(new_dict)
# print(student)


# -> to delete any key we use pop
# student.pop("name") 
# print(student)





#-> to delete the last key of the dictionary we use popitem
# student.popitem()
# print(student)

#-> to delet the hole dictionary
# del student
# del student["name"]
print(student)









