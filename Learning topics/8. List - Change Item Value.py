#Change Item Value: 
#------------------------------------
#To change the value of a specific item, refer to the index number:
names = ["Toma", "Mina", "cherry", "Nowshin" , "Iffat", "Fatima" , "Taki", "Mim"]

names[1] = "Tonoy"
print(names)

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
names[1:3] = ["Rohim", "Korim"]  #index 3 is not included
print(names)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
#------------------------------------------------------------
names = ["Toma", "Mina", "cherry", "Nowshin" , "Iffat", "Fatima" , "Taki", "Mim"]
print(names)
names[1:2]=["Tufa", "Anonna"] #---> 
print(names)

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
names[1:4] = ["Raha", "Kiara"]  #it will replace the index value of 1,2 and 3 with two new value
print(names)


#Insert Items : 
#---------------------
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

newName = ["Ena", "Mina", "Tina"]
newName.insert(1,"Lipa")
print(newName)


# To remove a element from :
#---------------------------------------
list=[1,2,3,4,5,5,6]
list.remove(3)
print(list)




