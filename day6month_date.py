# 
month=int(input("Enter the month number"))
if month==1 or month==3 or month==7 or month==5 or month==10 or month==12 or month==8:
    print("number of days in a month is 31")
elif month==6 or month==4 or month==9 or month==11 :
    print("numbers of days in month is 30")
elif month==2:
    year=(int(input("Enter a year")))
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("number of days in month is 29 and this is leap year")
    else:
        print("number of month is 28 and this is not a leap year")