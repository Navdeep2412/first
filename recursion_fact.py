import sys
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the number"))
result=fact(n)
print("The factorial of {} is :{}".format(n,result))
sys.setrecursionlimit(5)
def greet():
    print("hello")
    greet()
greet()
