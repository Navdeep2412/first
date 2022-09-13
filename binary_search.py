k=-1
def search(list,n):

    l=0
    u=len(list)-1

    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['k'] = mid
            return True

        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1

    return False

list=[12,13,67,90,91]
n=int(input("enter the number you want to search"))
if search(list,n)==True:
    print("Found at",k+1)
else:
    print("not found")