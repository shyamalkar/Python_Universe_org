"""
What is user defined module ? 
   My own create python file which fetch another file and use it, this is called user defined module.



Now we gonna try to build 2 main file
step-1 build a module file and another is main file 
"""
#Module file  code -
# mymath.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

#main file -> main.py
# main.py

import mymath

print(mymath.add(10, 5))
print(mymath.sub(10, 5))
print(mymath.mul(10, 5))