# list in python is collection which is ordered and list can be changeable
marks=[67,89,90,55,66]
print(marks)
marks[0]=96
print(marks[0])
print(marks)
# append method add at the end of list
marks.append(88)
print(marks)
# remove method remove item from the list if item present in list otherwise it gives error
marks.remove(55)
print(marks)
# sort method help to sort the list
marks.sort()
print(marks)
# reverse method reverse the list 
marks.reverse()
print(marks)
# list comprehension
square=[]
for number in range(1,6):
    square.append(number*number)

print(square)    

# other method to do this thing is
square=[number*number for number in range(1,6)]
print(square)
