#  two sum problem
a=[0,1,2,3,4,5]
n=len(a)-1
target=int(input("Enter your target"))
targetfound=False
for i in range(n):
    for j in range(i+1,n):
        if(a[i]+a[j]==target):
           print(i,j)
           targetfound=True
        #    break
if not targetfound:
    print("not found")    
    
       

