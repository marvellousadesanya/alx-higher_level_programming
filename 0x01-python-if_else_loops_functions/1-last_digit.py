#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
prefix = f"Last digit of {number}"

# First convert number to string
repr(number)

# Then get the last digit using string formatting
last_digit = repr(number)[-1]
# Convert back to int
last_digit = int(last_digit)
# However, the number could be negative so check for that
if number < 0:
    last_digit = -(last_digit)

# Conditional statements
if last_digit > 5:
    print(f"{prefix} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{prefix} is {last_digit} and is 0")
else:
    print(f"{prefix} is {last_digit} and is less than 6 and not 0")
