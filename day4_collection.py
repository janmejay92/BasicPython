#  tuple,set,dicitionaries,list
print("what you want to used python collection")
choice=int(input("Enter your choice"))
if choice==1:
    print("We are going to use tuples")
    tuple_=("janmejay","ashish","akash")
    print(tuple_)

    
    
elif choice==2:
    print("We are going to use list")
    list_=[]
    stop=True
   
    while stop:
         val=input("Enter your value or type to exit")
         if name=="exit":
             stop=False
         else:
          list_.append(name) 
    print("student name in list:",list_) 
           

elif choice==3:
    print("We are going to use set ")
    s=set()
    stop=True
    while stop:
        val=input("Enter your value or type exit ")
        if val=="exit":
            stop=False
        else:
         s.add(val)
    print(s)
    
elif choice==4:
    print("We are going to use dicitionary")  
    dict={}
    stop=True
    while stop:
         key=input("Enter your key value")
         if key=="exit":
            stop=False
         else:
           
            val=input("Enter your value of key")
            dict[key]=val
    print(dict)    

