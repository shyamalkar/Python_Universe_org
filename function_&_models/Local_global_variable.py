# What is local variable and what is global variable ?
# Local variable is nothing but where variable create inside of the function.

# you can't use outside of the function 

def test():
    x = 10
    print(x)

test()

# Global variable is nothing but where variable create outside of the function. 
# global variable is write outside of the function 
#e.g., 
name = "Shyamal"   # Global Variable 

def greet():
    print(name)

greet()

# Global variable and local variable example 
# This is a global variable
score = 100 # outside of the function .


def show_score():
  # This is a local variable
  bonus = 10 # inside the function . 
  print("Inside function - Score:", score)  # Can read global variable
  print("Inside function - Bonus:", bonus)  # Can read local variable


show_score()

# Trying to use variables outside the function
print("Outside function - Score:", score)  # Works fine
# print("Outside function - Bonus:", bonus) # This would cause an error!
