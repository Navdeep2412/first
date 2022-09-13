from array import *

arr = array('i', [])
n = int(input(" enter the length of the array"))
for i in range(n):
    x = int(input("enter the value"))
    arr.append(x)

print(arr)

val = int(input("enter the value you want to search"))
k = 0
for e in range(n):
    if arr[e] == val:
        print("value found")
        print("index is",k)
        break
    k=k+1
else:
    print("not matched")
