# This program calculates a person's BMI
# Based on input height and weight
# Height must be entered in cm.
# Weight must be entered in kg.

height = float(input("Please enter your height in cm: "))

weight = float(input("Please enter your weight in kg: "))

BMI = weight / ((height/100)**2)

print("Your BMI is", round(BMI,2))
