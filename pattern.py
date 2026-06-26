n=7
for row in range(n):
    
    for col in range(n):
        
        condtion= row>=col  
        
        
        if condtion:
            
            print(" *",end="")
            
        else:
            print("  ",end="")
    print(" ",end=" ")
    
    
    for col in range(n):
        
        condtion= col>=n-row-1
        
        
        if condtion:
            
            print(" *",end="")
            
        else:
            print("  ",end="")
    print()