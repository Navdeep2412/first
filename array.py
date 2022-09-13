from array import *
arr=array('i',[])
n= int(input(" enter the length of the array"))
for i in range(n):
    x=int(input("enter the value"))
    arr.append(x)
for i in range(n):
    print(arr[i])
newar = array(arr.typecode,(a for a in arr))

for e in range(len(newar)):
    if newar[e] % 2 == 0:
        continue
    print(newar[e])
    print("hello")
    print("het")
