#                              STRING TYPE
#-------------------------------------------------------------------------------------------

# We can make changes in strings type in various ways by adding a dot (.) after variable name-

name = "Iffat Ara Nowshin"

# .upper() fucntion converts all the letters in upper case
print (name.upper())

# .lower() fucntion converts all the letters in lower case
print (name.lower())

# .find() - To search any character or substrinf inside a string variable
print (name.find("in")) # it will return the index number where "in" will be found
print (name.find("a")) # since 'a' dosen't exist in nowshin, so it will return -1

# .replace() - to replace any character or substring temporary
print (name.replace('Ara','Jahan'))

# in - to check any character exist or not , result will be in boolean
print ("Ara" in name)
print ("Tara" in name)
print ("M" in name)

# Mulitple line string 
multiple_line = '''Son: "Dad, can you tell me what a solar eclipse is??"
Dad: "No,sun."
Son: "Okay dad!"'''
print(multiple_line)