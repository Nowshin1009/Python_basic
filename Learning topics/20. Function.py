#                 Function
#------------------------------------------------------------------------------
# types of function :
#                   1. In-Built Functions
#                   2. Module Functions
#                   3. User defined Functions

def my_function():
  print("Hello from a function")

my_function()   # calling function

# Parameterize function :
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")