'''
Q18 - Write a python program that checks if two strings are anagrams of eachother.
'''
str1 = input("Enter the String1 : ")
str2 = input("Enter the String1 : ")
x=len(str1)
y=len(str2)
if x==y:
  a=1
  i=0
  j=-1
  while(i<x):
    if str1[i]==str2[j]:
      i=i+1
      j=j-1
    else:
      a=0
      break
else:
  a=0
if a==0:
  print("The given string",str1, "is not Anagram of other string",str2)
else:
    print("The given string",str1, "is Anagram of other string",str2)