k=-1
def search(list,n):
    i=0
    for i in range(len(list)):
    #while i<len(list):

        if list[i]==n:
            globals()['k'] = i
            return True

        #i += 1
    return False

list=[12,56,13,5,6]
n=int(input("enter the number you want to search"))
if search(list,n)==True:
    print("Found at",k)
else:
    print("not found")