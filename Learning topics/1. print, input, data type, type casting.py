'''
# we can use "" or '' to declare it as string
print ("Hello world")
print (' Hello world')

# variable declare - String,integer,boolean
name = "Nowshin"  #string type
age = 22          #int
is_coder= True    #boolean
print (name,age , is_coder)

#input() is used for taking input from user
name= input("Enter your name - \n")
print ("My name is " , name) # we can use + or comma( , ) sign for concatenaion

super_hero = input("Who's your favourite super hero???\n")
print ("My favourite super hero is " + super_hero)

#python takes every input as string type. To type casting we need to use int(),float(),str(),bool()
number= input ("Enter a number \n")
print (type(number))

# string can be concatenate with only string and same for other data types also.
old_age=input()
new_age=int(old_age) + 2 #here we have use int() for type casting
print (new_age)
'''
#Complex Number --> a+bi
a= 6+7j
print(a)
print(a.real)
print(a.imag)
print(type(a))

b=5+5j
print(a+b)

