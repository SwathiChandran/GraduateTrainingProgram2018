1.Get first name and last name from user and print your full name 

First_name=raw_input("Enter first name")
print(First_name)
Second_name=raw_input("Enter second name")
print(Second_name)
print("full name is %s%s"%(First_name,Second_name))

"""
2.Get your full name, age as input from user and print first name and last name , age using string slicing

 i) 2 raw_input get name  and age 

 ii) print first name and last name and age 

Name=raw_input("Enter the full name")
Age=raw_input("Enter the age")
print(Name[0:6],Name[6:16],Age[0:2])
"""
3.Calculating your birth number in numerology

26/11/1978

2+6+1+1+1+7+8 = 8

var="26/05/1997"
sum=int(var[0])+int(var[1])+int(var[3])+int(var[4])+int(var[6])+int(var[7])+int(var[8])+int(var[9])
print(sum)
"""
4.Write a Python program to perform sum of three given integers. 

 However, if any of the two values are equal then sum will be zero (eg : 2+1+1 = 0)
a=input("Enter first value")
b=input("Enter second value")
c=input("Enter three value")
if a==b or b==c or c==a:
 print(0)
else:
 print(a+b+c)
"""
5.Declare a string variable - try all string functions / try string slicing with few examples

str1.capitalize()
Swathi chandran

 str1.upper()
'SWATHI CHANDRAN'

 str2.lower()
'kavya chandran'

len(str1)
15

str1.split(",")
['swathi chandran']

 str1.replace("i","y")
'swathy chandran'

str1.replace("swathi","kavya")
'kavya chandran'

str1.isalpha()
False

 max(str1)
'w'
>>> min(str1)
' '
