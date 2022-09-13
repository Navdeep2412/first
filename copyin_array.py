from numpy import *
arr=array([2,6,8,1,3])
arr2=arr.view()
print(arr2)
print(id(arr2))
print(id(arr))
arr2=arr.copy()
arr[3]=12
print(arr)
print(arr2)
