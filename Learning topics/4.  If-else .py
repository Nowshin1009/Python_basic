# If-Else statement :
# At first we need to write 'if' then the condition we want to check and then :
# here color(:) means we are going to write an statement or block. Then we give indentation, means-
# give a proper space or tab to address statement  '

age=16
if age >= 18:
    print ('You are adult')
    print ('You can vote ')   # these two line will print if the condition is true because it's written in indentation

print ('Thank You!!!')    # this line will be print in every case , because it's it does not contain indentation

#---------------------------------------------------------------------------------------------------------------------------
# Elif else:

if age >= 18:      # starting condiation
    print ('You are adult')
    print ('You can vote ')
elif age < 18 and age > 3:   # 2nd condition to check
    print ('You are in school')
else :                        #if no condition pass
    print('You are a child')

print ('Thank You!!!')

#----------------------------------------------------------------------------------------------------------------------------
# mini project
first = input ('Enter first number')
operator = input ("Enter operator(+ , - , * , / , %) : ")
second = input ('Enter second number :')

first=int(first)
second=int(second)
if operator == "+":
    print (first + second)
elif operator == "-":
    print (first - second)
elif operator == "*":
    print (first * second)
elif operator == "/":
    print (first / second)
elif operator == "%":
    print (first % second)
else :
    print ('Invalid operation!!!')


# If with logical operators :

s=""
print(not s)
 
if not s:
  print("string is empty")
else:
  print("String is not empty")

#-----------------------------------------
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  