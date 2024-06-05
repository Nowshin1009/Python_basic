#                     Set
#------------------------------------------------------------------------------
# A set is a collection which is unordered, unchangeable, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# We use { } brackets to intial set

marks = { 95 , 95, 98, 97, 97, 97 }
print (marks)    # it will print all the value only one time
 # sets has no index , means its not possible to find out any element's index number
 # error ---> print(marks[0])
# So, we can access any element by using loop

for score in marks :
    print (score)


