#What is Recursive function ?

# Recursive is a function where function call it self , that's called recursive function.
# every recursive function must have 2 critical parts: 
# the base case: 
# the recursive case: 
# e.g., factorial 

def factorial(n):
    if n == 1:  #Base case: stop when you reach 1 . 
        return 1
    else:
        return n * factorial(n - 1) # Recursive case: multiply n by the factorical of (n - 1)


print(factorial(5)) # Output should be := 120

#because

"""
5 × factorial(4)
5 × 4 × factorial(3)
5 × 4 × 3 × factorial(2)
5 × 4 × 3 × 2 × factorial(1)
5 × 4 × 3 × 2 × 1 

"""