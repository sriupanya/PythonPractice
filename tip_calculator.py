print("Welcome to the tip calculator!")
total=input("What was the total bill? $")
tip=input("How much tip would you like to give? 10, 12, or 15? ")
split= input("How many people to split the bill? ")
total= float(total)
tip=int(tip)
split= int(split)

final= (total * (1+(tip/100)))/split
print(f"Each person should pay: ${round(final,2)}")
