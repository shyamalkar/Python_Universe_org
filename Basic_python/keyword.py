#Python keywords are special words that have specific, predefined meanings in Python. You cannot use them as variable names, function names, and so on.

#e.g., 
# If you write 
#if = 23 # It can show error because if is a special name or function
#Special function mostly use in python 

"""
False    None     True
and      as       assert
async    await    break
class    continue def
del      elif     else
except   finally  for
from     global   if
import   in       is
lambda   nonlocal not
or       pass     raise
return   try      while
with     yield    match
case 
"""

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")


# For use create loop.
for i in range(3):
    print(i)

# while loop run until true condition present .
count = 1

while count <= 3:
    print(count)
    count += 1

# break() use for  It continues until the necessary items arrive.
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue , Remove current iteration transfer into another iteration.
for i in range(5):
    if i == 2:
        continue
    print(i)


#Def use for create function
def greet():
    print("Hello")


#return

#return value from function

def add(a, b):
    return a + b

#class (class create for OOP)

class Student:
    pass


#import use for module
import math

print(math.sqrt(16))
# try and except , for handle error
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# How to see all keyword ? 

import keyword

print(keyword.kwlist)