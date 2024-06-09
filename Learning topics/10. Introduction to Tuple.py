#________________________________________________________________________________
#                            Tuple
#--------------------------------------------------------------------------------
# A tuple is a collection which is ordered and unchangeable.(immutablw)
# Lists are created using fisrt brackets --> () :

marks= (95,95,98,97,97,97)
print (marks)

# or if we declare a collection without any backets, it will save as tuple by default.

marks = 95,95,98,97,97,97
print (marks)

#we can't change any elements of any indexs like --> marks[0]=99

#                ||    count() function       ||
#-------------------------------------------------------------------------------
# if we want to check the repataion of any number or how many times the number exist in the tuple


print (marks.count(95))
print (marks.count(97))


#               ||   index() function       ||
#--------------------------------------------------------------------------------
# to check index of any elements. (It will print the index where it fount the element first time)

print (marks.index(97))