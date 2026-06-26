# tuples in python refers to list but it cannot be changeble
point=(10,20)
print(point[0])
print(point[1])
# finding min and max number 
def find_min_max(numbers):
    minimum=min(numbers)
    maximum=max(numbers)
    return minimum,maximum

result=find_min_max([10,20,9,45,60])
print(result[0])
print(result[1])


