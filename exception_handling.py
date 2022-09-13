a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
try:
    print(a/b)
    k= int(input("enter the value of k"))
    print(k)

except ZeroDivisionError as e:
    print("hey, you are dividing the number by zero, ",e)
except ValueError as e:
    print("hey, you cant take a character value",e)
finally:
    print("bye")
