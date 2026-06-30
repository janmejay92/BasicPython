a=[13,20,18,17,26]
n=len(a)
start=0
number=int(input("Enter the nth smallest number which you want to find"))
if number<=n/2:
    while start<=number:
        min,minpos=a[start],start
        for i in range(start+1,n):
                if a[i]<min:
                    min=a[i]
                    minpos=i
        
        a[start],a[minpos]=a[minpos],a[start]
        start+=1
        # print(min)

    
    print(a)
    print(a[number-1])
elif number > n/2 and number <= n:
    while start <= number-1:
        min_val, minpos = a[start], start
        for i in range(start+1, n):
            if a[i] > min_val:
                min_val = a[i]
                minpos = i

        # Swap
        a[start], a[minpos] = a[minpos], a[start]
        start += 1

    print(a)
    print(a[number-1])

else:
    print("number must be in range of ",start,"to",n)