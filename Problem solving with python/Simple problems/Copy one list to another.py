# 1.	Write a program to make another list of duplicate elements from the following list
# [1, 5, 6, 5, 1, 2, 3]

# list1=[1, 5, 6, 5, 1, 2, 3]

# list2=[]
# for item in list1:
#     list2.append(item)

# print(list2)


list1 = [1, 5, 6, 5, 1, 2, 3]
dup = []

check = set()

for item in list1:
    if item in check:
        if item not in dup:
            dup.append(item)
    else:
        check.add(item)

print("List of duplicate elements:", dup)





