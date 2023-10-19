x = int(input("Enter the value of x : "))
match x :
    case 1:
        print("x is 1")
    case 4:
        print("x is 4")
    case 9:
        print("x is 9")
    case _ if x!=40:
        print(x,"is not 40")
    case _ if x!=90:
        print(x,"is not 90")
        
    case _:
        print("only enter integers")
        
