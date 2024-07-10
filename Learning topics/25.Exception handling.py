#Exception can be two types. 1-->Syntax error(by programmer), 2--> Exception(by user)
try:
    n1 = input("input a number: " )
    n1 = int(n1)
    n2 = input("input another number: " )
    n2= int(n2)
    print(n1 / n2)
except ZeroDivisionError:
    print("Can not divide by 0. Please enter a non-zero number. ")
except ValueError:
    print("Enter number only!")
except TypeError:
    print("Error!!! Please contact the programmer")