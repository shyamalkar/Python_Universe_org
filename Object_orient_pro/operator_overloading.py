# What is Operator Overleading ? 
# Changing how Python operators work for your own classes.

# Normally
10 + 20 # works 
# but can this work ? 

#money1 + money2 # yes but variable needed

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __str__(self):
        return f"({self.x}, {self.y})"
    
# Objects 

v1 = Vector(2,3)
v2 = Vector(5,7)

# Now 
v3 = v1 + v2 
print(v3) # Output should be (7, 10)
# pythin internally 
v1.__add__(v2)

# With out operator overloading 

v3 = v1 + v2  # this is much more cleaner 

"""

| You Write          | Python Internally |
| ------------------ | ----------------- |
| `Student("Alice")` | `__init__()`      |
| `print(obj)`       | `__str__()`       |
| `repr(obj)`        | `__repr__()`      |
| `len(obj)`         | `__len__()`       |
| `a == b`           | `__eq__()`        |
| `a + b`            | `__add__()`       |
| `a < b`            | `__lt__()`        |
| `a > b`            | `__gt__()`        |

"""