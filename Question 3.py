'''
Q3 - Write a python program that calculates the factorial of a given number
'''
x = int(input("Enter the Number : "))
fact = 1
n=x
if(x==0) or (x==1):
    fact =1
elif x>0:
    while (x>0):
     fact = fact * x
     x= x-1 
else:
   fact = "Not Defined"
print("Factorial of", n , "is : ",fact )