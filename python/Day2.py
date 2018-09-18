"""
1.Get first name and last name from user and print your full name 

First_name=raw_input("Enter first name")
print(First_name)
Second_name=raw_input("Enter second name")
print(Second_name)
print("full name is %s%s"%(First_name,Second_name))


"""

"""
2.get ur full name, age as input from user and print first name and last name , age using string slicing
 i) 2 raw_input get name  and age 
 ii) print first name and last name and age 
 iii) WHEN age >= 18 , he/she is eligible to vote
 iv) WHEN age < 18 , he/she is not eligible to vote
Name=raw_input("Enter ur name")
Age=raw_input("Enter ur age")
print("First name: %s" %Name[0:6])
print("second name: %s" %Name[6:15])
print("Age is %s" %Age[0:2])

if Age>=18:
 print ("She is eligible to vote")
else:
 print ("She is not eligible to vote")

Enter ur nameswathichandran
Enter ur age21
First name: swathi
second name: chandran
Age is 21
She is eligible to vote
"""

"""
3.Calculating your birth number in numerology

26/11/1978

2+6+1+1+1+7+8 = 8

var="26/05/1997"
sum=int(var[0])+int(var[1])+int(var[3])+int(var[4])+int(var[6])+int(var[7])+int(var[8])+int(var[9])
print(sum)

"""

"""
4.Write a Python program to perform sum of three given integers. 
   However, if any of the two values are equal then sum will be zero (eg : 2+1+1 = 0)

a=input("first number")
b=input("second number")
c=input("third number")
if a==b or b==c or c==a:
 print("0")
else: 
 total=a+b+c
 print("sum is %s"%total)

first number2
second number0
third number0
0

first number2
second number4
third number6
sum is 12
"""
"""
5.Write a Python program to check whether a year is leap year or not


a=input("Enter a year")
if a%4==0:
 print("It is leap year")
else:
 print("It is not a leap year")

Enter a year 2020
It is leap year

Enter a year2018
It is not a leap year
"""
"""
6.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

a=raw_input("Enter a sentence")
count1=0
count2=0
for i in a:
  if i.isupper():
   count1=count1+1
  elif i.islower():
    count2=count2+1
print("UPPER CASE %s"%count1)
print("LOWER CASE %s"%count2) 

Enter a sentence"This is Swathi
UPPER CASE 2
LOWER CASE 10 
"""
"""
8.declare a list containing numbers
    a) get only even numbers
    b) perform sum of those even numbers


sum=0
for i in range(10):
 if i%2==0:
   sum=sum+i
print (sum)

20
"""

"""
9.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which 
contains every number.

a=raw_input("Enter the inputs")
list1=list(a)
tuple1=tuple(a)
print(list1)
print(tuple1)

Enter the inputs 3,4,5,6,7
[' ', '3', ',', '4', ',', '5', ',', '6', ',', '7']
(' ', '3', ',', '4', ',', '5', ',', '6', ',', '7')

"""
