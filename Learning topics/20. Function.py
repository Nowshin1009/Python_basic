#                 Function
#------------------------------------------------------------------------------
# types of function :
#                   1. In-Built Functions
#                   2. Module Functions
#                   3. User defined Functions

def my_function():
  print("Hello from a function")

my_function()   # calling function

#Default Parameter Value:
def my_function(name = "Nowshin"):
  print("I am  " + name)

my_function("Taki")
my_function("Iffat")
my_function()
my_function("Taifa")

# Parameterize function :
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#If number of argument is unknown:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")