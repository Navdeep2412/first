# Enter your code here. Read input from STDIN. Print output to STDOUT
list=['a','b','a','b','a']
list1=['a','c']
for i in list1:
    if i in list:
        print(" ".join(map(str, list[i])))
    else:
        print ("-1")




