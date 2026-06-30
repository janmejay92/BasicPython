# today we are going to learn about collection in python
# 1) list
student=["Janmejay" ,"ashish","akash","prafull"]
print(student)
print(student[0])
print(len(student))
for i in range(len(student)):
    print(student[i])
# taking input from the user in the list
for i in range(len(student)):
    name=input("Enter your name")
    student.append(name)
print(student)
# 2) tuple
marks=(23,45,67,89)
for m in marks:
 
 if m>=33:
    print(m)
#  set
number={1,3,4,6}
for i in range(3):
    num=int(input("Enter your number"))
    number.add(num)
print(number)   
# frozenset
subject=frozenset(["python","java","sql"])
print("python" in subject) 
print("Html" in subject)
# dictionary
student={}
for i in range(5):
    key=input("Enter the key name")
    val=input("Enter your key value name")
    student[key]=val
    
print(student
      )
