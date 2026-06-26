# Take age as input and print whether the person is a child, teenager, adult, or senior citizen.
age=int(input("Enter your age"))
if age<=4:
    print("Child")

elif age>4 and age<=18:
    print("Tennager")

elif age>18 and age<=60:
    print("Adult")     

else:
    print("senior citizens")  

 # given number is Even or odd
number=int(input("Enter any positive number")) 
if number%2==0:
    print("Even")
else:
    print("odd")    
    
# taking three number and print greather number
number1=int(input("Enter first number")) 
number2=int(input("Enter second number"))
number3=int(input("Enter third number"))
if number1>number2:
    if number1>number3:
        print(number1)
    else:
        print(number3)    
else:
    if number2>number3:
        print(number2)   
    else:
        print(number3)     
         