# Avery Davis
# september 13, 2026
# P1HW2 Travel budget
# This program will calculate the total cost of a trip based on user input for various expenses.

""""
Pseudocode:
1. Display the program title
2. Prompt the user for their total travel budget
3. Prompt the user for their travel destination
4. Prompt for gas accomidation, and food costs, converting each to a float
5. add gas, accomodation and food to get the total expenses
6. Subtract total expenses from the budget to get the remaining balance
7. Display the "Travel expenses" header
8. Display each label left aligned in a 20-character column, followed by its value with a $ and 2 decimal places
9. Display a dashed line
10. if the remaining balance is 0 or more display it with a $ and 2 decimal places
"""

print("This program calculates and displays travel expenses")

budget = float(input("Enter your total travel budget: $"))

destination = input("Enter your travel destination: ")

gas = float(input("How much will you spend on gas?: $"))

accommodation = float(input("Approximately how much will you need for accommodations/hotel?: $"))

food = float(input("Last, how much will you need for food?: $"))

total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

print()
print("------Travel Expenses------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print(f"{'Fuel':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("-" * 39)
if remaining_budget >= 0:
    print(f"Remaining Balance: ${remaining_budget:.2f}")