# Write a Python function to find the maximum of three numbers.

# step 1 func define 
def max_value(*a):
    c = max(list(a))
    print(c)

# setp 2 input the number  
num1= int(input("enter number"))
num2= int(input("enter number"))
num3= int(input("enter number"))

#ste 3 function call
max_value(num1,num2,num3)