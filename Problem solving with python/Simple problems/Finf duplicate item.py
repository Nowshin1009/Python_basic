#Find the duplicate items from [1, 5, 6, 5, 1, 2, 3]
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