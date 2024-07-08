# Problem Statement
# Write a program where user will give height(height) and weight(kg) and then BMI will be calculated.

# Input
# The input consists of two double numbers which are height(meter) and weight(kg).

# Output
# *if bmi < 18.5 print "Underweight" *if bmi >= 18.5 & bmi < 25.0 print "Normal weight" *if bmi >= 25.0 & bmi < 30.0 print "Overweight" *else print "Obese"

# Constraints
# 0 ≤ |S| ≤ 109



height=float(input("Enter Height : "))
weight=float(input("ENter weight : "))

BMI=weight/height**2
print(f"BMI: {BMI:.2f}")
if BMI< 18.5 :
    print("Underweight")
elif 18.5<= BMI < 25.0 :
    print("Normal weight")
elif 25.0<= BMI <30.0 :
    print("Overweight")
else :
    print("Obese")


