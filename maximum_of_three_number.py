a=int(input("Enter a number first"))
b=int(input("enter a number second"))
c=int(input("enter number third"))
choice=int(input("Enter your choice"))
if choice==1:
    print("we are using method number 1")
    if a>b:
        if a>c:
            print("number first is maximum")
        else:
            print("number third is maximum")
    else:
        if b>c:
            print("number second is maximum")
        else:
            print("number third is maximum ")
elif choice ==2:
    if a>b and a>c:
        print("number first is maximum")
    elif b>c and b>a:
        print("number second is maximum")
    else:
        print("number third is maximum")    
elif choice==3:
    print("we are using choice third")
    sum1=a+b
    sum2=a+c
    if sum1>sum2:
        if a>b:
            print("number first is greather")
        else:
            print("second number is maximum")
    else:
        if a>c:
            print("number first is maximum")
        else:
            print("third number is maximum")
elif choice==4:
    max=a if a>=b and a>=c else b if b>=c else c
print(max)