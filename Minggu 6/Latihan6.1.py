def perkalian(a,b):
    print(a,"x",b ,"= ", end="")
    for i in range(a):
        print(f"{b} ",end="")
        if i < a -1:
            print("+ ",end="")
    print(f"= {a*b}.") 


perkalian(6,5)
perkalian(7,10)