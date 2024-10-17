# Write a program to create a function that determines whether elements in an array can be re-arranged to form a consecutive list of numbers where each number appears exactly once. The difference between two numbers will be 1 always.

# Input
# The program will take an integer N as the size of an array. Then it will take the integer values of the array M[]
# Output
# The output will print either "true" or "false"

def can_be_consecutive(arr):
    if len(arr) == 0:
        return True  
    if len(arr) != len(set(arr)):
        return False  
    
    min_val = min(arr)
    max_val = max(arr)
    
    return max_val - min_val == len(arr) - 1

n = int(input())
if n > 0:
    arr = list(map(int, input().split()))
    print("true" if can_be_consecutive(arr) else "false")
else:
    print("true")  