#What is module ?
"""
Module is a nothing but module is a function where already axist ready made code, which we import and use.
In simple word:- Another people write usefull code and use this code. just like tool box .
e.g., import math, time, date, keyword, numpy , pandas


what happen if module is not present ? 
so many bug 
many code
time waste

if you want to import packegaes use:- pip import (library name)
"""
import math # calculate sqrt of number.
num = 100000000
output = math.sqrt(num)
print(f"Square root of {num} is {output}")

# calculate the are a of circle 
radius = 5
area_of_circle = math.pi * (radius ** 2)
print("Area of circle with radius:",area_of_circle)
print(math.pi)

# import module function 
import random 
rand_num = random.randint(1, 10)
print(rand_num)

# short name 
#Alias np.short cut
import numpy as np 
print(np.array([1, 2, 3]))# so here np is short cut so you don't write this numpy again  and again . 

#Special import 
from math import sqrt 
print(sqrt(25)) # we take sqrt only

# Built in modules (Inside in python)
#python have already module

import math
print(math.factorial(5))


#let's try with date and time
import datetime

print(datetime.datetime.now())


#I build my own module 
def add(a,b):
    return a+b

def sub(a,b):
    return a-b
sub()
print(a=10, b=10)

"""
What is __name__ ?
__name__ Is this file being run directly, 
or is it being imported and run?
"""

#Most importent line 
if __name__ == "__main__":
#This line of code almost everyprofesional code.

#def add(a, b):
 #   return a + b

# print("Hello from mymath")