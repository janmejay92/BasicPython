# write a program according to greet person according to daynoon or nightnoon,
name=input("Enter name")
hour=float(input("Enter hour"))
minute=float(input("Enter minute"))

if hour >6 and hour<12:
    print("Good morning ",name)
elif hour==12:
    print(" GoodNoon",name )  
      
elif hour>12 and hour<=18:
    print("GoodAfternoon ",name)
    
elif hour>18 and hour<=21:
    print("good evening",name)

elif hour>21 and hour<24:
    print("good night ",name)
        
elif hour >= 00 or hour==24 :
    print(" it midnight", name)
    
elif hour>=1 and hour<=6:
    print(" It Early morning ",name)    

else:
    print("Enter time in between 00 to 24")