def calc():
    while True:
        num1 = int(input("enter the number : "))
        num2 = int(input("enter the number : "))
        opr = input("enter the number : ")
        #print ( num1, num2, opr)
        if opr=='+':
            print(num1+num2)
        elif opr=='-':
            print(num1-num2)
        elif opr=='*':
            print(num1*num2)
        elif opr=='/':
            print(num1/num2)
        else:
            print('invalid')
        x = input("y/n : ")
        if x =='y':
            continue
        else:
            break