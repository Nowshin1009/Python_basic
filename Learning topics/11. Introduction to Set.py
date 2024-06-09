#                     Set
#------------------------------------------------------------------------------
# A set is a collection which is unordered, unchangeable, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# We use { } brackets to initial set

marks = { 95 , 95, 98, 97, 97, 97 }
print (marks)    # it will print all the value only one time
 # sets has no index , means its not possible to find out any element's index number
 # error ---> print(marks[0])
# So, we can access any element by using loop

for score in marks :
    print (score)

#To add an item :
#-----------------------
marks.add(77)
print(marks)

number=set()
print(number)    #Null set
number.add(1)
number.add(2)
number.add(3)
number.add(4)
print(number)


#To use union in two set:
#------------------------
set1={1,2,3,4}
set2={9,0,2,5,1}
set3= set1 | set2
print(set3)

# TO use intersection in two set:
#-------------------------------------

set1={1,2,3,4}
set2={9,0,2,5,1}
set3= set1 & set2  #common elements only
print(set3)

#To substract one set's elements from other:
#--------------------------------------------
S= set1 - set2    # it will substract the common elements exists in set2
print(S)

#To print unique item of two set:
#------------------------------------
Q= set1 ^ set2
print (Q)

#we can convert a set into list and a list into set : 
#-------------------------------------------------------
li=[1,2,1,5,6,7,2,3,9,0,3,4,5,7,8] 
print(li)
s = set(li)
print(s)       # it will remove the duplicates values from the list and converts it into set

# Again set to list convert:
li=list(s)
print(li)











