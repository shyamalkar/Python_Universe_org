"""Task 1: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
 
Expected Output:
For example, if the function is called with 5, it should return:
"""



import math

user_input = int(input("Enter a number: "))

result = math.factorial(user_input)

print(f"Factorial of {user_input} is: {result}")