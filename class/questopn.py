#Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.
d={}
s='abcdefghijklmnopqrstuvwxyz'
x=1
for i in range(0,len(s),3):
    d[x]=s[i:i+3]
    x+=1
    
print(d)