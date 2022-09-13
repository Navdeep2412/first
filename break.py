avl=50
x=int(input("enter the amount of candies"))
i=1
while i<=x:
    if i>avl:
        print("out of stock")
    print("candy")
    i+=1
print("bye")
for a in range(1,101):
    if(a%2!=0):
        pass
    else:
        print(a)
for j in range(1,100):
    if j%3==0 or j%5==0 or j%8==0:
        continue
    print(j)
print ("bye")
