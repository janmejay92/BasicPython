a=[1,2,3,6,-5,-9]
n=len(a)
start=0
while start<=n-1:
    min,minpos=a[start],start
    for i in range(start+1,n):
        if a[i]<min:
            min=a[i]
            minpos=i
    a[start],a[minpos]=a[minpos],a[start]
    start+=1
print(a)