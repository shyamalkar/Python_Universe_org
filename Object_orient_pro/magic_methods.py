"What is magic methods ?"

"""Magic methods are special methods in Python that begin and end with double underscores (__)."""

# These are magic methods,  because they has double under score, they are often called, magic methods , Dunder methods ("dunder" = double underscore)
"""
__init__
__str__
__repr__
__len__
__add__
__eq__
"""

# example :- 
class Student:
    def __init__(self, name):
        self.name = name

"This __init__() is actually a magic method."

# when i write 
s1 = Student("Alice")
# Python internally does something similar to :
Student.__init__(s1, "Alice")
# did't call __init__() yourself

# python did automatically 




# what does "Automatically" Mean ?
class Student:
    def __init__(self):
        print("Constructor called")

# Now 
s1 = Student() # out put should be = constructor called 
# did i write s1.__init__() ?  the answer is no , python called it internally 

# Another intuition is 

# suppose i write 
print(10 + 20)
# did python treat + as just symbol ?

#but internally =  10.__add__(20)


