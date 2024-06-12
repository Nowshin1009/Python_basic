# Dictionary comprehension :
#-----------------------------------------
li = [(1, 'one'), (2 , 'two'), (3, 'three'), (4, 'four')]
dict = {k:v for k, v in li}
print(dict)

dict = {v:k for k, v in li}
print(dict)
print(type(dict))

# Set comprehension :
#-----------------------------------
s = "jfblridhvscnsfhvhdkjvh"
unique_letters = {letters for letters in s}
print(unique_letters)
print(type(unique_letters))

colors_choice = [ ('Nowshin', 'Black') , ('Taki', 'White'), ('Taifa', 'Blue') ,('Taif', 'Green') ,('Tanusha', 'pink') ]
print(type(colors_choice))
colors_dt = {name:color for name , color in colors_choice}
print(type(colors_dt), colors_dt)

colors_set = {color for color in colors_dt.values()}
print(type(colors_set), colors_set)
