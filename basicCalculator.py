print("******calculator********")
print("************************")


opt = str

while opt !="2":
    n1 = int(input("type your first number "))
    n2 = int(input("type your second number "))
    opr = input("type your logic operator ")
    
    rslt = 0
    if(opr =="+"):
        rslt = n1 + n2
    elif(opr == "-"):
        rslt = n1 - n2
    elif(opr == "*"):
        rslt = n1 * n2
    elif(opr =="/"):
        rslt =n1 / n2
        
        
    print("\nThe operation {} {} {} results in {}!".format(n1, opr, n2, rslt))
    
    opt = input("\nDo you want to perform another operation? (1-yes or 2-no: ")
    
    print("*** END OF PROGRAM ***")