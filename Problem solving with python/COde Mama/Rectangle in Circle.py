# Problem Statement
# Write a program to create a function that takes three numbers — the width and height of a rectangle, and the radius of a circle — and returns true if the rectangle can fit inside the circle, false if it can't.

# Input
# The input consists of three double numbers: width, height, radius

import math

def can_fit_in_circle(width, height, radius):
    diagonal = math.sqrt(width**2 + height**2)
    
    diameter = 2 * radius
  
    return diagonal <= diameter

width, height, radius = map(float, input().split())

if can_fit_in_circle(width, height, radius):
    print("true")
else:
    print("false")
