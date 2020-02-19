# Dervla Candon
# This program calculates a person's BMI
# Based on input height and weight
# Height must be entered in cm.
# Weight must be entered in kg.

height = float(input("Please enter your height in cm: "))   #specify centimetres to ensure calculation is correct

weight = float(input("Please enter your weight in kg: "))   #specif kg here to enjsure calculation is correct

BMI = weight / ((height/100)**2)        #BMI is calculated by squaring height in metres, then dividng weight by this figure

print("Your BMI is", round(BMI,2))      #using round function to give the result to 2 decimal places, a more user friendly result.
