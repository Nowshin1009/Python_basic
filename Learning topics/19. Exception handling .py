#Example 1:
# If we use a read function on a file which doesn't exist then it will give an error and the program will be crushed, so handling this we can write like this--
try:
    fp= open("mynewfile.txt", "r")
    content = fp.read()
    fp.close()
except FileNotFoundError:
    print("Your file is not found")


print("Exception handled successfully!!")


#Example 2:

try: 
    n1 = 10
    n2 = 0
    print(n1/n2)
except ZeroDivisionError :
    print("You can't divide a number by zero!")


#Example 3:

while True :
    n1 = int(input("Please enter a number : "))
    n2 = int(input("Please enter another number : "))
    if n1 == 0 and n2 == 0:
        break
    try:
        print("Result of division : \n", n1/n2)
    except ZeroDivisionError:
        print("Number can't be zero")
    else : 
        print("Good work!")

    


