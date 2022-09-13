a=10
def some():
    a=15
    print(a)
print(a)
some()


b=14
def something():
    global b
    b=20
    print("in fun",b)
something()
print("outside",b)

c=15
print(id(c))
def aq():
    c=16
    x=globals()['c']
    print(id(x))
    print("inside",c)
    globals()['c']=19
aq()
print('outside',c)