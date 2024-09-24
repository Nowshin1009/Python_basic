# Problem Statement
# Write a program where you will be given a number and it's exponent. You will have to calculate the power of the number.

# Input
# The input consists of two integer numbers.

# Output
# The output will be an integer number.

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter numbers.

# Input:
# 3 4
# Output:
# 81

def calculate_power(base, exponent):
    return base ** exponent

numbers = input()
base, exponent = map(int, numbers.split())

print(calculate_power(base, exponent))