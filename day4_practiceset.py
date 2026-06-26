# create a fibbonacchi series
prev=0
prest=1
sum=0
n=int(input("Enter number from where you print fibbonacchi number"))
# print(prev)
# print(prest)
fibb=[0,1]
rev_fibb=[0,1]
for i in range(n):
    sum=prev+prest
    prev=prest
    prest=sum
    fibb.append(sum)
    rev_fibb.append(sum)
    
# printing n fibbonacci number
print("fibbonacci number",fibb)
# printing the reverse fibbonacci number
rev_fibb.reverse()
print("reverse fibbonacci series",rev_fibb)    

# reverse the number
number = int(input("Enter any number which you want to reverse: "))
reversed_num = 0 

while number > 0:
    remainder = number % 10              
    reversed_num = reversed_num * 10 + remainder
    number = number // 10               

print("Reversed number:", reversed_num)
 

    