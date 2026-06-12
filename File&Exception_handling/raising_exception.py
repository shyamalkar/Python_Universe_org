"""
But what is raising ?

Raising  means you handle error with your own programming language or .
"""


Age = float(input("Enter your Age: "))

if Age < 0:
    raise ValueError("Age can't be Zero")
else:

    if Age >= 10:
        print("You can vote")

    else:
        print("You can't vote")