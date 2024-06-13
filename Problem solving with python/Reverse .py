# Reverse a string.
# If the input is: Hello World.
# The output should be: .dlroW olleH

def reverse_string(str):
   reverse = ""
   for char in str:
       reverse = char + reverse
   return reverse
 
str = input("Enter your string: ")
result = reverse_string(str)
print(result)