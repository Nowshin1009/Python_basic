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

marks["physics"] = 99
print(marks)

# to change any value --->

marks["physics"] = 100
print(marks)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

#Another way to make dictionary:
#-----------------------------------
num_to_words = dict()
num_to_words[1]='One'
num_to_words[2]='two'
num_to_words[3]='three'
num_to_words[4]='Four'

print(num_to_words)


# To see if any item is available in dictionary :
# ------------------------------------------------

if 2 in num_to_words:        # key dite hobe
    print("Available")
else :
    print("Not available")

#To delete any item from dictionary :
del num_to_words[1]
print(num_to_words)

# See all keys by using loop:

for item in num_to_words: 
  print(item)      # will return only keys

# See all the key with values :

for item,value in num_to_words.items():    # items() function   
   print(item, value)

# items() function use :
print(num_to_words.items())

#value() & keys() function:
#-----------------------------

print(num_to_words.keys())
print(num_to_words.values())

#get() function :
print(num_to_words.get(2))

