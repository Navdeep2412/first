class computer:
    def __init__(self):
        self.name="nav"
        self.age=28
    def compare(self,c2):
        if self.age==c2.age:
            return True
        else:
            return False
c1=computer()
c2=computer()
c1.age=12
if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
print(c1.name)
print(c2.name)