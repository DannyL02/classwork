number_sides = int(input("Please enter the number of sides of a shape: "))

if number_sides == 3:
	print("That is a triangle.")
elif number_sides == 4:
	print("That is a square.")
elif number_sides == 5:
	print("That is a pentagon.")
elif number_sides == 6:
	print("That is a hexagon.")
elif number_sides == 7:
	print("The is a heptagon.")
elif number_sides == 8:
	print("That is an octagon.")
elif number_sides == 9:
	print("That is a nonagon.")
elif number_sides == 10:
	print("That is a decagon")
else:
	print("Please enter an integer greater than 2")
