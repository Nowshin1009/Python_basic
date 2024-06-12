li= ["apple" , "orange", "mango" , "lichi" , "banana" ]
fruits = [fruit.capitalize() for fruit in li]   # This in list comprehension
print(fruits)

fruits_len = [len(x) for x in li] 
print(fruits_len)

cube_list = [x*x*x for x in range(1,11) ]
print(cube_list)

cube_list = [x for x in range(1,11) if x % 2 == 1 ]
print(cube_list)

cube_list = [x*x*x for x in range(1,11) if x % 2 == 1 ]
print(cube_list)