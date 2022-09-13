from array import *
arr = array('i', [])
n = int(input("enter the length of array"))
for i in range(n):
    x = int(input("enter the value"))
    arr.append(x)
print(arr)
val = int(input("enter the value you want to inserted"))

arr.insert(2,val )
print(arr)
