#Change Item Value: 
#------------------------------------
#To change the value of a specific item, refer to the index number:
names = ["Toma", "Mina", "cherry", "Nowshin" , "Iffat", "Fatima" , "Taki", "Mim"]

names[1] = "Tonoy"
print(names)

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
names[1:3] = ["Rohim", "Korim"]  #index 3 is not included
print(names)

names[1:4] = ["Raha", "Kiara"]  #it will replace the index value of 1,2 and 3 with two new value
print(names)

#Change the second value by replacing it with two new values:
#------------------------------------------------------------
names = ["Toma", "Mina", "cherry", "Nowshin" , "Iffat", "Fatima" , "Taki", "Mim"]
print(names)
names[1:2]=["Tufa", "Anonna"]
print(names)
