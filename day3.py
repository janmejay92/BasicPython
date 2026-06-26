# loops in python
name="Janmejay"
for i in range(5):
    print(name)
# using loop 
for i in range(5):
    print(i)
# adding stopping condition
print("Adding starting and stopping condtion in loop")
for i in range(2,10):
    print(i)
print("using start ,stop,step condition in loop")
for i in range(1,7,2):
    print(i)
# loops in list
std_name=["janmejay","ashish","aditi","prafull","prakhar"]
for name in std_name:
    print(name) 
    
marks=[80,50,90,97,99]
total=0
for mark in marks:
    total+=mark

average=total/len(marks)
print(average)    
# while loop
count=1
while count<=5:
    print(count)
    count=count+1
    
count=5
while count>=0:
    print(count)
    count=count-1
password=""
while password!="janmejay23":
    password=input("Enter your password: ")
    
print("access granted")
# break condition and continue condition
numbers=[23,45,65,78,90]
for number in numbers:
    # if number==65:
        # print("loop will break")
        # break
    # else:
        # print(number)
#  continue condition
    if number==65:
     print("skip the item")
     continue
    else:
        print(number)
# function in python 
name=input("Enter your name")
def say_hello(name):
    print("hello",name)
for i in range(5): 

    say_hello(name)
def check_pass(marks):
    if marks>=33:
        print("pass")
    else:
        print("fail")         
for i in range(5):
    marks=int(input("Enter your marks"))
    check_pass(marks)    



# return type function
def averaga_calculator(numbers):
    total=0
    for number in numbers:
        total+=number
    average=total/len(numbers)
    return average
    
numbers=[23,45,67,89,99]
avg=averaga_calculator(numbers)
print(avg)