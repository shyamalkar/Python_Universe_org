# Define factorial function
def factorial(n):
    result = 1
    
    # Loop to calculate factorial
    for i in range(1, n + 1):
        result *= i
    
    return result

# Take input from user
num = int(input("Enter a number: "))

# Call function and print result
fact = factorial(num)
print(f"Factorial of {num} is: {fact}")