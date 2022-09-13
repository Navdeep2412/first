class cal:

    def add(self,a,b):

        self.a=a
        self.b=b
        c=a+b
        print("addition is",c)
    def sub(self,a,b):
        
        self.a = a
        self.b = b
        j=a-b
        print("subtraction is",j)

obj1=cal()
obj2=cal()
obj1.add(12,5)
obj2.sub(12,7)
