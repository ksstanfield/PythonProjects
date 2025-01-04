# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = ((tip / 100 * bill) + bill) / people
final_amount = "{:.2f}".format(bill_with_tip)
print(f"Each person should pay: ${final_amount}.")
