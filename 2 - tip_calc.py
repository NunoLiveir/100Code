print("Welcome to the tip calculator! For all your tipping needs!")
total = input("What was the total bill? $")
percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people will split the bill? ")
tip_value = 1 + (int(percent) / 100)
final_tip = (float(total) / int(people) * tip_value)
rounded_tip = "{:.2f}.format{final_tip}
print(f"Each person should pay: ${rounded_tip}")
