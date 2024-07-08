# Problem Statement
# Write a program where you will be given three numbers. You will have to find the next number.

# Input
# The input consists of three integer numbers.

# Output
# The output will be an integer number.

# Constraints
# 0 ≤ |S| ≤ 109

inputs = input().split()
A = int(inputs[0])
B = int(inputs[1])
C = int(inputs[2])

next_number = C + (C - B)

print(next_number)