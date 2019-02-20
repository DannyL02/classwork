width = int(input("Please enter the width of the field in feet: "))
length = int(input("Please enter the length of the field in feet: "))

sq_feet_in_acre = 43560

area = (width * length) / sq_feet_in_acre

print(f"The area of the field in acres is {area} acres.")
