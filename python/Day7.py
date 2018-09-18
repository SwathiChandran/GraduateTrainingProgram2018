import os
for path,subdirs,files in os.walk("swathi",topdown=False):
    for name in files:
         print os.path.join(path,name)

os.chdir('swathi/lib')
out=os.listdir(os.cwd())
print len(out)
for path,subdirs,files in os.walk("swathi",topdown=False):
   for name in files:
      count+=1

print count

for root,dirs,files in os.walk("swathi"):
   for file in files:
       if file.endswith(".txt"):
         print(os.path.join(root,file))

import re
n=input("enter the numbers")

if (n>0) and (n<11):
    for i in range(n):
        c=raw_input("enter the card number")
        if len(c)>0 and len(c)<=25:
            s=re.match("([4-6][0-9]{15})|([4-6][0-9]{3}(-[0-9]{4}){3})",c)
            print(s)
            if(s==None):
			   print("Invalid")
            else:
               print("Valid")			
        else:
            print("Enter valid credit card number")
			
else:
    print("invalid")

