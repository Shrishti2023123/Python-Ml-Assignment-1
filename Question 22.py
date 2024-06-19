'''
Q22 - Write a python program that returns the minimum and maximum values in a list of numbers.
'''
list1= []
n= int(input("Enter Number of elements you want to add in list : "))
i=0
while(i<n):
    a =  int(input(f"Enter the Element {i+1}"))
    list1.append(a)
    i=i+1
min1 = min(list1)
max1 = max(list1)
print ("Minimum Value in the list is : ",min1) 
print ("Maximum Value in the list is : ",max1)