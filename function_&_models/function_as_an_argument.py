# What is function as an argument ?
# In Python, functions can be passed around like data.
def add(a, b):
    return a + b

def calculate(func, x, y):
    return func(x, y)

print(calculate(add, 5, 3)) # here add function send as argument.