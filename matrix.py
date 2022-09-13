from numpy import *
arr1=array([
                [1,2,3,67,12,68],
                [4,5,6,56,78,17]
            ])
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
arr2=arr1.flatten()
print(arr2)
arr3=arr2.reshape(4,3)
print(arr3)
arr3=arr2.reshape(2,2,3)
print(arr3)
