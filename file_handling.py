f1=open('Mydata','r')
print(f1.read())
print(f1.readline())
f=open("Names",'w')
f.write("some")
f3=open("abc",'a')
f3.write("laptop")
f3.write("mine")
for data in f1:
    f3.write(data)
f4=open("img.jpg",'rb')
f5=open("mypic.jpeg",'wb')
for i in f4:
    f5.write(i)