#File: ConvertUnits.py
#Student: David Lutsenko

#Date: 17 September, 2024
#Description: This program converts feet and inches into different units, such as inches, yards, miles, meters, centimeters, millimeters, and kilometers.
#Github: <lutsenkodavid>


feet1 = float(input("Enter number of feet: "))
inches2 = float(input("Enter number of inches: "))

inches = (feet1 * 12) + inches2

feet = inches / 12

yards = feet / 3

miles = feet / 5280

#metric units

meters = feet * 0.3048

centimeters = meters * 100

millimeters = centimeters * 10

kilometers = meters / 1000

print("English Units")

print(" feet:", feet)

print("inches:", inches)

print(" yards:", yards)

print(" miles:", miles)

print("Metric Units")

print(" meters:", meters)

print(" centimeters:", centimeters)

print(" millimeters:", millimeters)

print(" kilometers:", kilometers)