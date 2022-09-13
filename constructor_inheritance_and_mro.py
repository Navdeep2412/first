class A:
    def __init__(self):
        print("in a")
    def f1(self):
        print("f1")
class B:
    def __init__(self):
        print("in b")
    def f2(self):
        print("f2")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("in c")
    def f2(self):
        super().f2()
        print("in c f2")
a1=C()
a1.f2()