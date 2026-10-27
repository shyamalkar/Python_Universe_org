"""
__init__()
__str__()
__repr__()
__len__()
__eq__()
__add__()
__lt__()
__gt__()

"""
# When i write something simple like: 
# __init()__ (constructor) , i already learn this 

class Student:

    def __init__(self, name):
        self.name = name

#create object 
s1 = Student("Alice")
# Pythoon internally does something similar to: 
Student.__init__(s1, "Alice")
# Purpose , initialize onject data 

# __str__()
#problem

class Student:
    pass

s1 = Student()

print(s1)

# soluation 
class Student:

    def __str__(self):
        return "Student Object"
s1 = Student()
print(s1) #  but python internally does s1.__str__()

# Better example 

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"
    
s1 = Student("Alice")
print(s1)


# so no 3 is :- __repr__(), this is similar to __str__() but is intended for devlopers.


class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student('{self.name}')"
    

# Now  
s1 = Student("Alice")
print(repr(s1)) # python internally riten like :- s1.__repr__()

#The difference between __str__(), for users, student name: Alice and __repr__() for devloper student('Alice')
# in real projects: __str__() -> user friendly, __repr__() debugging and logging 

# __len__()
# suppose 
number = [1, 2, 3]
print(len(number)) # output should be 3 

# because python internally work like = numbers.__len__()

# my own class 
class BookShelf:
    def __len__(self):
        return 10 

shelf = BookShelf()
print(len(shelf)) # output should be :- 10 

# Another exmameple 
class Student:

    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)
s = Student(["Math","English","Physics"])

print(len(s)) # output should be 3 


# __eq__(), used for == 


class Student:

    def __init__(self, roll):
        self.roll = roll

    def __eq__(self, other):
        return self.roll == other.roll
    
#create objects 

s1 = Student(101)
s2 = Student(101)
s3 = Student(102)

# Now 
print(s1 == s2) # the output should be True 
print( s1 == s3) # the output should be False
# python internally 
#s1.__eq__(s2)

# __add__()
# + option 
# example:- 
print(10 + 20 ) 
# python internally 

#10.__add__(20)
#create your own class
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"{self.amount}"


m1 = Money(500)

m2 = Money(700)

m3  =  m1 + m2 
print(m3)

# Python internally 
m1.__add__(m2) # This is my first example of operator overloading 


# comparison magic methods 

#suppose we have 

class Student: 
    def __init__(self, marks):
        self.marks = marks 
# __lt__() (Less than) , used for < 

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks
    
s1 = Student(70)

s2 = Student(90)

print(s1 < s2) # The output should be True 

# Python internally 
#s1.__init__(s2)
#__gt__() , > 

class Student:

    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks
print(s2 > s1) # Output should be = True 

# s2.__gt__(s1)

"""
| Method   | Operator |
| -------- | -------- |
| `__lt__` | `<       |
| `__gt__` | `>`      |
| `__le__` | `<=`     |
| `__ge__` | `>=`     |
| `__eq__` | `==`     |
| `__ne__` | `!=`     |

"""

