# Avery Davis
# september 13, 2026
# P1HW2 Travel budget
# This program will calculate the total cost of a trip based on user input for various expenses.

budget = float(input("Enter your total travel budget: $"))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas?: $"))
accommodation = float(input("Approximately how much will you need for accommodations?: $"))
food = float(input("Last how much will you need for food?: $"))

total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses
print()
print("------Travel Budget Summary------")
print(f"Destination: {destination}")
print(f"Total Budget: ${budget:.2f}")
print(f"Estimated Expenses: ${total_expenses:.2f}")
if remaining_budget >= 0:
    print(f"Remaining Budget: ${remaining_budget:.2f}")