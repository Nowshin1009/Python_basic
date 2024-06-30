#search by predefined function:

li= [1,2,3,4,5,6,7,8,9,10]

el=li.index(6)         #to find a element's index number
print(el)

exist= 5 in li        # to know if an element exist in list or not
print(exist)


# Lenear search using loop:
key = 6
flag=False
for item in li:
    if key == item:
        flag= True
        break

if flag is False:
    print("Not exist in list")
else:
    print("Found")







