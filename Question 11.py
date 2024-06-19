'''
Q11 - Write a python program that generates the first n numbers in theFibonacci sequence.
'''
x = 0
y = 1

n = int(input("Enter the no of fibonacci Series you want to display : "))
if n<=0 :
    print("Enter a Positive No ")
elif  n==1:
    print(x)
elif n==2:
    print(x,y)
else:
    print(x,y ,end=" ")  
    count = 2
    while count < n:
        z = x+y
        print(z, end = " ") 
        x= y
        y=z
        count = count +1