# Problem Statement
# Write a program where you have to find the GCD(Greatest Common Divisor) of two numbers.

# Input
# The input consists of two integer numbers.

# Output
# The output will be an integer number.

# Constraints
# 0 ≤ |S| ≤ 109
# Example:
# Enter two numbers.

# Input:
# 9 12
# Output:
# 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

numbers = input()
num1, num2 = map(int, numbers.split())

print(gcd(num1, num2))