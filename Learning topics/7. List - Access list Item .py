#1 Access with specific index :
thislist = ["Toma", "Mina", "cherry", "Nowshin" , "Iffat"]
print(thislist[1])  #--->Index 1 =  Mina

#2. Negative Indexing :
#_____________________________

# Negative indexing means start from the end
print(thislist[-1])  #---> This will print Iffat

#3. Range of Indexes :
#_____________________________

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #The search will start at index 2 (included) and end at index 5 (not included).
#output ---> ['cherry', 'orange', 'kiwi']

#By leaving out the start value, the range will start at the first item:
print(thislist[:4])  #---> index 0,1,2,3 (4 not include)

#By leaving out the end value, the range will go on to the end of the list:
print(thislist[2:])

#Range of Negative Indexes:
print(thislist[-4:-1])  #--> index -4 to -2 (-1 not include)

#Check if Item Exists: 
#_____________________________
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else :
  print("Doesn't exist")

# Or we can use "in" to check item. It will return in boolean

print ("apple" in thislist )
print ("Lichi" in thislist )







