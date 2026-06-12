try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero") # Out put should be :- can't divide by zero 

# Another example 
 
try: # Risky code 
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

else:
    print("No Error")
 
finally:
    print("Always Execute")


# Docstring 
# function, class and module description.

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add.__doc__)