'''
Q23 - Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
'''
x= input("Conversion into (use 'c' for centigrage and 'f' for fehrenheit : ) ")
if x=='c' or x=='C' :
   a = int(input("Enter the Temperature in Centigrade : "))
   z= float((9/5 * (a)) +32)
   print("Temperature in Fehrenheit :", z)
elif x=='f' or x=='F':
   b =int(input("Enter the Temperature in Fehrenheit :"))
   c= float((b-32)*5/9)
   print("Temperature in Centigrade",c)
else:
   print("Wrong Input !!")