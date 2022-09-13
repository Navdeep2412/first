def greet():
    print("hello")
greet()
x=int(input("enter the value of x"))
y= int(input("enter the value of y"))
def add(x,y):
    a=x+y
    print("addition of x and y is", a)
add(x,y)
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1, result2=add_sub(x,y)
print("result1 is",result1,"and result2 is",result2)

def add(*a):
    c=0
    for i in a:
        c=c+i
    print(c)
add(12,34,122,67)

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('navdeep',age=28,city='patiala',mob=9845454454)

def person(name,**data):
    print(name)
    print(data)

person('navdeep',age=28,city='patiala',mob=9845454454)

