'''
Q21 -  Write a python program that counts the occurrences of a specific element in a list.
'''
list1 =[1,70,5,7,23,65,13,27,65,65,89,56,89,65,34,78]
x= int(input("Enter the element to search : "))
count = 0
for item in list1:
    if item == x:
        count = count +1
    else:
        continue    
print(f"occurence of element {x} is : " ,count)
