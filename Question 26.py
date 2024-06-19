'''
Q26- Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
'''
x=  input("Enter the String : ")
y=  input("Enter the Prefix you want to check : ")
z=  input("Enter the Suffix you want to check : ")
if  x.startswith(y):
    print("The string starts with Prefix: ",y)
else:
    print("The string does not starts with Prefix: ",y)

if  x.endswith(z):
    print("The string starts with Suffix: ",z)
else:
    print("The string does not starts with Suffix: ",z)
