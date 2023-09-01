def add(a,b):
    return a+b
    
def add_t(x,y):
    print(x+y)
    
num1= int(input("enter a number : ")) 
num2= int(input("enter a number : "))
num3= int(input("enter a number : "))

b=add(num1, num2)
print(b)
add_t(b, num3)