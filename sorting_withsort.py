number=[40,32,60,56]
number.sort()
print(number)
# using sorted function to sort the list
number1=[30,566,23,76]
new_number=sorted(number1)
print(new_number)
# reverse sorting
marks = [55, 90, 12, 71, 33]

marks.sort(reverse=True)

print(marks)
# reverseing list using sorted function
top_marks=sorted(marks,reverse=True)
print(top_marks)
# sorting a string
name=["janmejay","Ashish","piyush", "Rahul"]
name.sort()
print(name)
# sort without worry about capital and small letter
print(sorted(name,key=str.lower))
# sorting with key
print(sorted(name,key=len,reverse=True))
# sorting with lambda
students = [
    ("Amit", 70),
    ("Ravi", 90),
    ("Zoya", 85),
    ("Meena", 60)
]

students.sort(key=lambda student: student[0])

print(students)
# using compare function
from functools import cmp_to_key
def compare(a,b):
    return a-b
numbers=[40,10,30,20]
numbers.sort(key=cmp_to_key(compare))
print(numbers)
# decending order sorting
def compare(a,b):
    return b-a
numbers=[40,10,30,20]
numbers_sort=sorted(numbers,key=cmp_to_key(compare))
print(numbers_sort)
# using comparison clearly using if-else
from functools import cmp_to_key
def compare(a,b):
    if a<b:
        return -1
    elif a>b:
        return 1
    else:
        return 0
numbers=[66,43,76,80,90]
numbers.sort(key=cmp_to_key(compare),reverse=True)
print(numbers)
# using comparing function sort string using length
from functools import cmp_to_key
def compare_by_length(a,b):
    if len(a)>len(b):
        return 1
    elif len(a)<len(b):
        return -1
    else:
        return 0

names={"janmejay","ashish","Pradeep","jitendra"}
names_=sorted(names,key=cmp_to_key(compare_by_length))
print(names_)
from functools import cmp_to_key
def compare1(a,b):
    if a.lower()<b.lower():
        return -1
    elif a.lower()>b.lower():
        return 1
    else:
        return 0
names=["janmejay","ashish","Pradeep","jitendra"]
names.sort(key=cmp_to_key(compare1))
print(names)
# sort if length is same then sorted by alphbatical order
from functools import cmp_to_key
def compare2(a,b):
    if len(a.lower())!=len(b.lower()):
        return len(a.lower())-len(b.lower())
    if a.lower()<b.lower():
        return -1
    elif a.lower()>b.lower():
        return 1
    else:
        return 0
names=["cat","ant","elephant","Dog"]
names.sort(key=cmp_to_key(compare2))
print(names)
# sorting the list using last characters
from functools import cmp_to_key
def compare3(a,b):
    if a[-1]<b[-1]:
        return -1
    elif a[-1]>b[-1]:
        return 1
    else:
        return 0
fruits=["apple","mango","bananna","pineapple"]
fruits.sort(key=cmp_to_key(compare3))
print(fruits)
# sorting a function using marks of student not name
students=[{"name":"janmejay","marks":70},
          {"name":"aditi","marks":68},
          {"name":"ajeet","marks":96}
          ]
def compare4(a,b):
    if a["marks"]<b["marks"]:
        return -1
    elif a["marks"]>b["marks"]:
        return 1
    else:
        return 0

students.sort(key=cmp_to_key(compare4),reverse=True)
print(students)
# marks high to low and name a to z
students = [
    {"name": "Ravi", "marks": 90},
    {"name": "Amit", "marks": 70},
    {"name": "Zoya", "marks": 90},
    {"name": "Meena", "marks": 70}
]

def compare_students(a, b):
    if a["marks"] != b["marks"]:
        return b["marks"] - b["marks"]

    if a["name"] < b["name"]:
        return -1
    elif a["name"] > b["name"]:
        return 1
    else:
        return 0

students.sort(key=cmp_to_key(compare_students))

for student in students:
    print(student["name"], student["marks"])
    # sort products by price ascending and rating descending
    
    products = [
    {"name": "Keyboard", "price": 800, "rating": 4.5},
    {"name": "Mouse", "price": 500, "rating": 4.2},
    {"name": "Monitor", "price": 800, "rating": 4.8},
    {"name": "USB Cable", "price": 200, "rating": 4.0}
]
    def compare_products(a,b):
        if a["price"]!=b["price"]:
            return a["price"]-b["price"]
        if a["rating"]<b["rating"]:
            return 1
        elif a["rating"]>b["rating"]:
            return -1
        else:
            return 0
products.sort(key=cmp_to_key(compare_products))
# print(products)
for product in products:
    print(product["name"], product["price"], product["rating"])
# sortinh using key function
students = [
    {"name": "Ravi", "marks": 90},
    {"name": "Amit", "marks": 70},
    {"name": "Zoya", "marks": 90},
    {"name": "Meena", "marks": 70}
]

students.sort(key=lambda student: (student["marks"], student["name"]))

for student in students:
    print(student["name"], student["marks"])
# 
def comapare(a,b):
    if a<b:
         return -1
    elif a>b:
         return 1
    else:
         return 0
a=[1,2,3,6,-5,-9]
a.sort(key=cmp_to_key(compare))
print(a)


