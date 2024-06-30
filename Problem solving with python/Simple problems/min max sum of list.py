# Without using max() function
li = [1,2,3,4,5,6,7,9]

max_num = float('-inf')  #to find the lowest number in list

for num in li:
    if num > max_num:
        max_num=num

print(max_num)


# without using sum() function:

li = [1,2,3,4,5,6,7,9]

result=0
for num in li:
    result=result+num

print(result)


# without using min() function:

min=li[0]

for num in li:
    if num<min:
        min=num
print(min)
