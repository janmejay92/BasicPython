# Check up the following operators in Python +, -, /, //, , %,*
first_number=int(input("Enter your first number"))
second_number=int(input("Enter your second number"))
# addition
sum=first_number+second_number
print("Sum of given two number is: ", sum)
# subtraction
sub=first_number-second_number
print("Subtraction of two number is: ",sub)
# multiplication 
multiply=first_number*second_number
print("multiplcation of two number is:",multiply)
# division 
divide=first_number/second_number
print("division of two number is ", divide)

# float division which used two remove two number
float_division=first_number//second_number
print("division of two number" , float_division)
#  remainder
remainder=first_number%second_number
print("remainder :", remainder)


# finding area of triangle
height=int(input("ENTER THE HEIGHT OF TRINAGLE"))
base=int(input("Enter the base of triangle"))
area=0.5*base*height
print("Area of triangle is ",area)

# calcultaing SI AND CI 
princpal_amount=float(input("Enter your princpal amount"))
rate_of_intrest=float(input("Enter the rate of intrest"))
time=float(input("Enter the year "))
si=(princpal_amount*rate_of_intrest*time)/100
print("Simple intrest of amount: ",princpal_amount,"is",si)

# compound intrest
ci=princpal_amount*(1+rate_of_intrest/100)**time-princpal_amount
print("compound intrest of amount:",princpal_amount,"is",ci)

# Find the area of a circle given the circumference 
radius=float(input("Enter the radius of circle"))
pi=3.14
area=pi*radius*radius
circumfrence=2*pi*radius
print("area of circle is ",area)
print("circumfrence of circle is",circumfrence)


#quadratic question
#  Solve x^2 - 5x + 6 = 0
a=1
b=-5
c=6
x1=(-b+(b**2-4*ac)**0.5)/2*a
x2=(-b-(b**2-4*ac)**0.5)/2*a
print("roots of quadratic equation is: ",x1,x2)

