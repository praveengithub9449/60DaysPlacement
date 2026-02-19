stds=[]
while True:
    print("\n1. create student")
    print("2. view student ")
    print("3. exit ")

    choice=input("enter choice")

    if choice =="1":
        name= input("enter student name ")
        branch=input("enter the branch")
        stds.append({"name":name,"branch":branch})
        print("created seccsesfully")

    elif choice =="2":
        for i in stds:
            print(i)

    elif choice =="3":
        break
    else:
        print("invalid")
    
    

        

    
        
