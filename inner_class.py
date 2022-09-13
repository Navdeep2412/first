class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show1()

    class laptop:
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8
        def show1(self):
            print(self.brand,self.cpu,self.ram)

s1=student('nav',12)
s2=student('jai',13)


s1.show()




