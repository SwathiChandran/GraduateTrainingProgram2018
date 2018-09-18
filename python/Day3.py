"""
inventory = {
                   'gold' : 500,
                   'pouch' : ['flint', 'twine', 'gemstone'],
                   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
                }



inventory ["pocket"]=["seashell","strange berry","lint"]
print(inventory)
inventory["backpack"].sort()
print(inventory["backpack"])
inventory["backpack"].remove("dagger")
print(inventory["backpack"])
inventory["gold"]+=50
print inventory
"""
"""
def func():
	Student={}
	Student["student1"]=[90,85,89]
	Student["student2"]=[78,67,39]
	print(Student)
	total1=sum(Student["student1"])
	total2=sum(Student["student2"])
	print("total1 %s"%total1)
	print("total2 %s"%total2)
	avg1=total1/3
	avg2=total2/3
	print("avg1 %s"%avg1)
	print("avg2 %s"%avg2)
func()
"""
"""
stud={}
stud_count=input("enter no of students")
for i in range(stud_count):
 name=raw_input("enter the name")
 sub_count=input("enter sub count")
 m=[]
 for j in range(sub_count):
   j=j+1
   marks=input("enter marks of sub%s" %j)
   m.append(marks)
   
 stud[name]=m
print(stud)
"""
"""
try:
 print(1/0)
except Exception as error:
 print(error)
finally:
 print("finally block")
 """
 """
def add_func(a,b):
  try:
   c=a+b
   print(c)
  except Exception as error:
   print(error)
  finally:
   print("finally block")
add_func(5,5)     
 """
 
 
