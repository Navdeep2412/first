class Pycharm:
    def execute(self):
        print("compiling")
        print("executing")
class laptop:
    def code(self,ide):
        ide.execute()
class editor:
    def execute(self):
        print("spell check")
        print("editing")
        print("compiling")
ide=editor()
l1=laptop()
l1.code(ide)
