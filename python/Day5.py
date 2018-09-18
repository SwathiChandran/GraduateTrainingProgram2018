from heapq import nlargest
name = list(raw_input("enter the name:"))
a = {}
if(len(name) > 3 and len(name) < 100):
    for i in name:
        a[i] = name.count(i)
    print(a)
    if(len(a) > 3):
        three_largest = nlargest(3, a, key=a.get)
        for i in three_largest:
            for k, v in a.iteritems():
                if(k == i):
                    print k, v
    else:
        print("enter atleast 3 distinct characters")
else:
    print("enter correct value")

test_no=int(input(''))
A=set()
B=set()
out=[]
try:
    if(test_no>0 and test_no<5):
        for i in range(test_no):
            no1=int(input(''))
            if (no1 > 0 and no1 < 100):
                for j in range(no1):
                    val=int(input())
                    A.add(val)
            else:
                print('Only 0-9 values in a set')
            no2=int((input('')))
            if (no2 > 0 and no2 < 100):
                for l in range(no2):
                    val1 = int(input())
                    B.add(val1)
            else:
                print('Only 0-9 values in a set')
            if(A.issubset(B)):
                out.append('True')
            else:
                out.append('False')
        for x in out:
            print x
    else:
        print('Enter 1-4 testcases')
except Exception as err:
    print(err)
