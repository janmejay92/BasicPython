# dictionary in python stores key value pairs
student={
    "name":"janmejay", 
    "age":23,
    "Gender":"male"
}
print(student["name"])

print(student["Gender"])

student["city"]="varanasi"
student["age"]=22
print(student["city"])
print(student["age"])

for key,value in student.items():
    print(key,"=",value)

emplyoo={
    "emplyoo_id":230,
    "name":"janmejay kumar",
    "age":23,
    "city":"ghazipur"
}
for key ,value in emplyoo.items():
    print(key,"=",value)
    # list of dictionary
    
students=[
        {"name": "janmejay kumar","age":23,"gender": "male"},
        {"name":"ashish","age":30,"gender":"male"}
    ]
# print(student)
for student in students:
    print(student["name"], student["age"])