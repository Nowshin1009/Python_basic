#To merge 2 lists :
#_--------------------

li1 = [1,2,3,4,5,6]
li2=[7,8,9,10,11,12]

li1.extend(li2)
print(li1)

#Insert Items : 
#---------------------
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.

newName = ["Ena", "Mina", "Tina"]
newName.insert(1,"Lipa")
print(newName)


# To remove a element from list:
#---------------------------------------
list=[1,2,3,4,5,5,6]
list.remove(3)
print(list)

#To pop a item from the last index :
#--------------------------------------

li =[1,4,6,3,5,2,3,0]
x=li.pop()
print(x)
print(li)
li.pop()
print(li)

#To pop a item from any index :
#--------------------------------------
li =[1,4,6,3,5,2,3,0]
x=li.pop(2)    #index number in the parenthesis
print(x)
print(li)


#To sort the list in ascending order:
#--------------------------------------
li =[1,4,6,3,5,2,3,0]
li.sort()
print(li)

#To sort the list in descending order:
li =[1,4,6,3,5,2,3,0]
li.sort(reverse=True)
print(li)

# Or we can also use li.reverse()


name =['aa','bb','cc','dd']
name2=['ee','ff','gg','hh']
name3=['ii','jj','kk','ll']
name.append(name2)   #append add the items as 1 list in 1 index
print(name)
name2.extend(name3)   #extend add the intems as individual item in each index
print(name2)


#slice:
# s[::-1]--> s[start:stop:step]
str_list=["hello","python","django"]
s[::-1] for s in str_list:
    print(str_list)
print(dir(list))  #To know all the functions of list

print(help(list.copy))    # use help() to know how aany function works
