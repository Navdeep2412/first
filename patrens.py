for j in range(4):
    for i in range(4):
        print("# ", end="")
    print()
for a in range(4):
    for b in range(a+1):

        print("@ ",end="")

    print()
for q in range(4):
    for r in range(4-q):
        print("$ ",end="")
    print()
rows=int(input("enter the no of rows"))
ascii=65
for i in range(0,rows):
    for j in range(i+1):
        alphabet=chr(ascii)
        print( alphabet,end="")
    ascii+=1
    print()
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
