'''
Q6 - Write a program that reads the content of a text file and prints it to theconsole.
'''
x = "output.txt"
try:
 with open(x, "r") as file:
        content = file.read()
 print("File content:")
 print(content)        
except FileNotFoundError:
    print(f"The file {x} does not exist.")