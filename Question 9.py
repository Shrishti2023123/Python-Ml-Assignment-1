'''
Q9 - Write a python program that checks if a substring is present in a given  string.
'''
str1 = input("Enter the String : ")
substr1 = input("Enter the Substring : ")

if substr1 in str1:
    print(f"The substring '{substr1}' is present in the main string.")
else:
     print(f"The substring '{substr1}' is not present in the main string.")
