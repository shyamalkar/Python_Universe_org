"""
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.

2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)

3.   Displays the calculated results.

"""



# Task 2: Using the Math Module for Calculations

import math   # Import math module

# Take input from user
num = float(input("Enter a number: "))

# Calculate using math module
square_root = math.sqrt(num)    # 
log_value = math.log(num)      # Natural log (base e)
sine_value = math.sin(num)     # Sine in radians

# Display results
print(f"Square root: {square_root}")
print(f"Logarithm: {log_value}") 
print(f"Sine: {sine_value}")