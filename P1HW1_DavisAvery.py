# Avery Davis
# calculating exponents and addition and subtraction

# calculate exponents

print("------Exponents------")
print()

base = int(input("enter a base number: "))
exponent = int(input("enter a exponent: "))
result = base ** exponent
print(base, "raised to the power of", exponent, "is", result, "!!")

# calulate addition and subtraction
print("------Addition and Subtraction------")
print()

num1 = int(input("enter a starting integer: "))
num2 = int(input("enter a integer to add: "))
num3 = int(input("enter a integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result, "!!")
