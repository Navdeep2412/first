from array import *
arr=array('i',[])
n= int(input("enter th length of array"))
for i in range(n):
    val=int(input("enter the value"))
    arr.append(val)
for e in range(len(arr)):
    print(arr[e])
num=int(input("enter the index value you want to delete"))
arr.pop(num)
print(arr)

