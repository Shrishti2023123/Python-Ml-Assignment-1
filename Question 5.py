'''
Q5- Write a program that takes a string input from the user and writes it to a text file.
'''
x = input("Please Enter a String : ")
y = "output.txt"
with open(y,"w") as file :
    file.write(x)
print(f"The file is written in the file {y}")