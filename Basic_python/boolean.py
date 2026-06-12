# Boolean often call computer decision programming language.
# Boolean has only 2 value , one is True and another is False, also use for take decision
print(type(True))
print(type(False))

# Why Boolean use for ?
# We often use boolean for take Decision . 
#E.g., 
age = 20
print(age >= 18)

#Comparison Operators

print(5 > 3)    # True
print(5 < 3)    # False
print(5 == 5)   # True
print(5 != 5)   # False
print(5 >= 5)   # True
print(5 <= 4)   # False

#Boolean Operators

print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

#If any one True then it's true if not then false 

print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

weekend = False
holiday = True

print(weekend or holiday)

#not, not use also for convert into oposite 
print(not True)   # False
print(not False)  # True

# Bool can Behavior like int .
print(True + True)
print(True + False)