"""
Create a program that will ask the user for their age and height (cm).
The program will display a message whether or not they are able
to ride on the "Mega Scream Machine". They must be 16 or older and 120 cm or taller to ride.
"""

age = int(input("Enter your age: "))
height = int(input("Enter your height: "))

if age >= 16 and height >= 120:
    print("You are able to ride.")
else:
    print("You are not able to ride.")


"""
if-elif-else statements stop doing comparisons as soon as it finds one that's true.
However, if-if-if does every comparison. 
"""
