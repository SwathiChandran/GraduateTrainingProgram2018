"""
str=raw_input("full name")
if(len(name)>0 and len(name)<1000):
  str=str.split()
for i in range(len(str)):
  if name[i].isalnum():
    str[i]=str[i].capitalize()
str=" ".join(str)
print(str)
"""
"""
student={}
stud_count=raw_input("enter the no of students")

for i in range(int(stud_count)):
    stud_name=raw_input("enter the name")
    stud_subcount=raw_input("enter the no of subjects")
    m_list=[]
    for j in range(int(stud_subcount)):
        j=j+1
        marks=int(input("enter the marks for the subject"+str(j)+":"))
        m_list.append(marks)
        student[stud_name]=m_list
print student
name=raw_input("enter the name")
if name in student:
    sum1=sum(student[stud_name])
    av1=sum1/3
    print(name)
    print(av1)

"""
"""
try:
  #n=input("Enter the no of test case")
  #for i in range(n):
      s=raw_input("Enter a and b");
      l=s.split(" ")
      print int(l[0])/int(l[1])
except ZeroDivisionError:
    print("Error Code: integer division or modulo by zero")
except ValueError,Argument:
    print("Error Code: invalid literal for int() with base 10:%s"%l[1])

"""
dict = {}
l = []
n = input("Enter the no of commands")
for i in range(n):
    s = raw_input()
    l1 = s.split(" ")
    dict[i] = l1
print dict
for i in range(n):
    if(dict[i][0] == "insert"):
        l.insert(int(dict[i][1]), int(dict[i][2]))
    elif(dict[i][0] == "print"):
        print l
    elif(dict[i][0] == "remove"):
        l.remove(int(dict[i][1]))
    elif(dict[i][0] == "append"):
        l.append(int(dict[i][1]))
    elif(dict[i][0] == "sort"):
        l.sort()
    elif(dict[i][0] == "pop"):
        l.pop(len(l) - 1)
    elif(dict[i][0] == "reverse"):
        l.reverse()
