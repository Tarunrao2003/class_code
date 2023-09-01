a=int(input("enter a number: "))
if a>20:
    for i in range(10):
        c=a*(i+1)
        print(c)
elif a<20:
    for i in range(5):
        c=a*(i+1)
        print(c)
else:
    print("enter 20")
    