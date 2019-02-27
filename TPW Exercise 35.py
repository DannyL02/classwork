human_years = int(input("Please enter the age of a dog in human years: "))

human_years = 0

if human_years <= 2:
	dogYears = human_years * 10.5
elif human_years > 2:
	dog_years = 2 * 10.5
	dog_years += (human_years-2) * 4

if human_years == 0:
	print("Please enter a positive integer.")
else:
	print(f"The dog is {dog_years} years old in dog years.")
