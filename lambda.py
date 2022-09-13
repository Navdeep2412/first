from functools import reduce
nums=[2,6,23,45,12,8,90,11,12]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
doubles=list(map(lambda n:n*2,evens))
print(doubles)
sum=reduce(lambda a,b:a+b,doubles)
print(sum)