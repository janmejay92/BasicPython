list_=[5,0,-1,-10]
start=0
end=len(list_)-1

x=int(input("Enter a number which you want to search in list"))
while True:
    mid=(start+end)//2
  
    if list_[mid]==x:
        print("Element is present at index:",mid)
        break
    if list_[mid]<x:
        end=mid-1
    elif list_[mid]>x:
        start=mid+1
    if start>end:
        print("Element not found",-1)
        break
        
