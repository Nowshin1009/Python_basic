# We can declare a range in 3 ways:
li1=list(range(10))
li2=list(range(1,21))
li3=list(range(1,11,2))

print(li1)
print(li2)
print(li3)



range1= range(1,11)
for x in range1:
    print(x)

# Converting range into list:

li = list(range1)
for x in li:
    print(x)

# Even number print between 1 to 100 :

even_numbers = list(range(2,101,2))
print(even_numbers)

# Inverse way traverse:
numbers= list(range(10,0,-1))
print(numbers)


