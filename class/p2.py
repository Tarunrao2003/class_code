#ques: Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead
'''Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String

lolgic 1 : 
s='python'
print(s[0:2]+s[-2:])

'''

s = input("enter a String : ")
print(s[0:2]+s[-2:])