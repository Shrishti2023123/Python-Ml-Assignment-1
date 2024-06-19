''' 
Q24 - Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) 
as input and print the result.
'''
x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
z= input("Enter an Operator : ")

if z=='+':
    print(f"Sum of {x} and {y} : ",x+y)
elif z=='-':
    print(f"Difference of {x} and {y} : ",x-y)
elif z=='*':
    print(f"Multiplication of {x} and {y} : ",x*y)        
elif z=='/':
    print(f"Division of {x} by {y} : ",x/y)