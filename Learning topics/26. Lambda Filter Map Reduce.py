f = lambda a,b: a*b

result = f(5,6)
print(result)

nums = [1,0,6,7,4,2,7,8,9,3,2]

evens = list(filter(lambda n : n%2==0,nums))
print(evens)