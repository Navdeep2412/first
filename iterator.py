nums=[2,7,1,4,5]
it=iter(nums)
print(next(it))
class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=topten()
for i in values:
    print(i)