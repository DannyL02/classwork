one_litre_or_less = int(input("How many bottles have one litre or less: "))
more_than_one_litre = int(input("How many bottles have more than one litre: "))

refund = (one_litre_or_less * 0.10) + (more_than_one_litre * 0.25)

print(f"The refund for returning these containers is ${refund}.")
