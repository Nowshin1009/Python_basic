f = lambda a,b: a*b

result = f(5,6)
print(result)

nums = [1,0,6,7,4,2,7,8,9,3,2]

evens = list(filter(lambda n : n%2==0,nums))
print(evens)

def add(a, b):  
    return a + b  
  
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
  
# add function is passed as the first argument, and num_list is passed as the second argument  
sum = reduce(add, num_list)  
print(f"Sum of the integers of num_list : {sum}")  
  