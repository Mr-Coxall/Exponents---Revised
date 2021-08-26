# This will work for user input exponents both positive and negative integers

from exponents import *

# Collect the base value
base = input("What is the common base? ")

# Collect the first exponent
first_power = input("First term, " + base + " is raised to what power? ")

# Collect the second exponent
second_power = input("Second term, " + base + " is raised to what power? ")

# output a blacnk line
print()

# convert exponents to integers
first_power = int(first_power)
second_power = int(second_power)

# Add the exponents
power_sum = first_power + second_power

# Create empty string to collect x bases
result = ""
# Loop through and add base x times
for loop_counter in range(0, power_sum):
    # If it's not the last one, add multiplication sign
    if loop_counter < power_sum - 1:
        result = result + base + " * "
    else:
        result = result + base  # for last one, no sign

# Store the original problem
problem = base + exponent(first_power) + " * " + base + exponent(second_power)
# Store the final solution
solution = str(base + exponent(power_sum))

# Print the answer
print(problem)
print("= ", result)
print("= ", solution)

print("\nDone.")
