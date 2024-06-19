'''
Q12 - Write a python program that calculates the sum of the digits of a given number.
'''
n = int(input("Enter the Number : "))
sum = 0
while n>0:
    z = int(n%10)
    sum = sum + z
    n= n/10

print("Sum of Digits of given Number : ",sum)