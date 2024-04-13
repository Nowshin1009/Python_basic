#                         Dictionary
#-------------------------------------------------------------------------------

#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates
#Dictionaries are written with curly brackets{}, and have keys and values:


marks = {"english" : 95 , "chemistry" : 98}
information = {"Fatima" : "Badol" , "Nowshin" : "Kowser"} # student name as key and her parents name as value

# to see any value --->
print(marks["chemistry"])

# to add any new value --->

marks["physics"] = 99;
print(marks)

# to change any value --->

marks["physics"] = 100;
print(marks)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)