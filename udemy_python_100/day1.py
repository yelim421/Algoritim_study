print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

price = total * (1 + tip / 100)
price_per_person = price / people

print(f"Each person should pay: ${price_per_person:.2f}")