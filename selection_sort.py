list_=[7,9,6,-2,8]
start=0
index=0
end=len(list_)-1

min=list_[0]
while start!=end:
    for i in range(start,len(list_)):
        if list_[i]<min:
            min=list_[i]
            index=i
        list_[0],list_[index]=list_[index],list_[0]
        start=start+1
        print(list_)
    
print(list_)
    
            