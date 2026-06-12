#What is Recursive function ?

# Recursive is a function where function call it self , that's called recursive function.
# e.g., factorial 

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5)) # Output should be := 120

#because

"""5 × factorial(4)
5 × 4 × factorial(3)
5 × 4 × 3 × factorial(2)
5 × 4 × 3 × 2 × factorial(1)
5 × 4 × 3 × 2 × 1
"""