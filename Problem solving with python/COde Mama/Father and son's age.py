# Problem Statement
# Write a program to create a function that takes two arguments: a father's current age fAge and his son's current age sAge. Сalculate how many years ago the father was twice as old as his son, or in how many years he will be twice as old.

# Input
# The input consists of two integers: father's age and son's age.

# Output
# The output will be an integer.

# Constraints
# 0 ≤ |S| ≤ 104
# Example:
# Enter numbers

# Input:
# 36 7
# Output:
# 22 

def years_to_twice_age(fAge, sAge):
    return abs(fAge - 2 * sAge)

fAge, sAge = map(int, input().split())

print(years_to_twice_age(fAge, sAge))