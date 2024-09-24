# Problem Statement
# Write a program to create a function that takes an array and finds the integer which appears an odd number of times.

# Input
# The program will take input until encounters a new line.

# Output
# The output will be an integer.

# Constraints
# 0 ≤ |S| ≤ 104
# Example:
# Enter numbers

# Input:
# 1 1 2 -2 5 2 4 4 -1 -2 5
# Output:
# -1 

def find_odd_occurrence(arr):

    count = {}
    
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    for num, freq in count.items():
        if freq % 2 != 0:
            return num

arr = list(map(int, input().split()))

print(find_odd_occurrence(arr))