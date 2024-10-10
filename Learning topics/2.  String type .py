# #                              STRING TYPE
# #-------------------------------------------------------------------------------------------

# # We can make changes in strings type in various ways by adding a dot (.) after variable name-

# name = "Iffat Ara Nowshin"

# # .upper() fucntion converts all the letters in upper case
# print (name.upper())

# # .lower() fucntion converts all the letters in lower case
# print (name.lower())

# # .find() - To search any character or substrinf inside a string variable
# print (name.find("in")) # it will return the index number where "in" will be found
# print (name.find("a")) # since 'a' dosen't exist in nowshin, so it will return -1

# # .replace() - to replace any character or substring temporary
# print (name.replace('Ara','Jahan'))

# # in - to check any character exist or not , result will be in boolean
# print ("Ara" in name)
# print ("Tara" in name)
# print ("M" in name)

# # Mulitple line string 
# multiple_line = '''Son: "Dad, can you tell me what a solar eclipse is??"
# Dad: "No,sun."
# Son: "Okay dad!"'''
# print(multiple_line)

today="Saturday"
print(today[-1])
print(today[0])
for letter in today:
    print(letter)
for letter in today[::-1]:
    print(letter)

opposite = today[::-1]
print(opposite)

print(today[2:4])

print('day' in today)

print(today.upper())
today=today.replace("Satur","Sun")
print(today)

cost_of_ice_bag = 1.33
profit_margin=.2
number_of_bags = 500

#template for output message:
output_template= """If a grocery sells ice bags at $ {} per bag, with total cost $ {}
then the total profit it makes by selling {} ice is $ {}."""
print(output_template)

#Inserting values:
total_profit = cost_of_ice_bag * profit_margin* number_of_bags

output_message = output_template.format(cost_of_ice_bag,profit_margin*100,number_of_bags,total_profit)
print(output_message)