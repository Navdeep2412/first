def topten():
    yield 1
    yield 2
    yield 3
    yield 4
v=topten()
print(next(v))
for i in v:
    print(i)
def toptens():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
v1=toptens()
for i in v1:
    print(i)
