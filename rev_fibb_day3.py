last=(int(input("enter the last number of fibbonacci series")))
sec_last=int(input("enter the second last number of fibbonacci series"))

print(last)
print(sec_last)

while sec_last!=0:
    sub=last-sec_last
    last=sec_last
    sec_last=sub
    print(sub)