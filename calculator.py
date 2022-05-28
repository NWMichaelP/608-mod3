import math
#Loading math module

while True:
    try:
        value = float(input("Pick an integer number between 1 and 10:"))
        if value < 1 or value > 10:
            raise ValueError
        break
    except ValueError:
        print("That's not between 1 and 10, please try again.\n")
#This was fun to learn, I wanted to play around with different values so I thought I would make it an input.
#I found out pretty quickly that Python has a limit as to how high the values will go when raised to itself.
#The result: If I wanted to use the exp function, I needed a limit. 

print("\nYour value, rounded to the smallest integer not less then itself, is: ", math.ceil(value))
print("\nYour value, rounded to the largest integer not greater then itself, is ", math.floor(value))
print("\nThe trigonometric sine of your value is: ", math.sin(value))
print("\nThe trigonometric cosine of your value is: ", math.cos(value))
print("\nThe trigonometric tangent of your value is: ", math.tan(value))
print("\nThe exponential function of your value is: ", math.exp(value))
print("\nThe log of your value is: ", math.log(value))
print("\nThe log of your value is with a base 10 is: ", math.log10(value))
print("\nYour value raised to itself is: ", math.pow(value,value))
print("\nThe square root of your value is: ", math.sqrt(value))
print("\nThe absolute value of your value is: ", math.fabs(value))
print("Code by Michael Pogue")
#Result print out.