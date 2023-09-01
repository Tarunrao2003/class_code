# A program for Simple Calculator : 
i =0 
while True:
    num1 = int(input("Enter a number 1 : "))
    num2 = int(input("Enter a number 2 : "))
    opr = input("Enter the operator : ") #opr = int(input("enter 1 for add, 2 for sub "))
    # calci logig : 
    if opr == '+':
        c=num1+num2
        print=(c)        
    elif opr == '-':
        c = num1 - num2
        print(c)
    elif opr == '*':
        print(num1*num2)
    elif opr == '/':
        print(num1/num2)
    else:
        print("invalid operator")
    # loop constraint :
    x=input("want to continue[y/n]: ")
    if x=='n':
        break
    else:
        i+=1
    
        

    