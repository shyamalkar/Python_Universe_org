#What is modules ?
# module is a pythin file (.py) where function, variable, class etc presented.
# module = code separate in sevarel file .

import math

print(math.sqrt(16)) # output should be - 4


# user define module 
# e.g., if i have calculator.py  name file .
# calculator.py

def add(a, b):
    return a + b

# Another file 
#import calculator

#print(calculator.add(2, 3))