def count(lst):

    for i in lst:
        if len(i) > 7:
            continue
        lst1.append(i)

    return(lst1)
lst1=[]
lst = ['navdeepkaur','navini','kanwar','jai','chuhi','gtd']
result=count(lst)
print(result)
def count1(ls):
    even=0
    odd=0
    for j in ls:
        if j%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
ls=[12,34,56,13,89,90]
a,b=count1(ls)
print("even:{} and odd:{}".format(a,b))
