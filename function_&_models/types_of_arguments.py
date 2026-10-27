# There are 2 types of arguments in python like :- *args and **kwargs 

# What is *args ?
#*args allows a function to accept any number of positional, length arguments and parameter.
#coding example:- 
def numbers(*args): # *args is a tuple
    print(args)

numbers(10, 20, 30)
# Output
(10, 20, 30)
# another example
def numbers(*args):
    for i in args:
        print(i)

numbers(10, 20, 30, 40) # Output = 10, 20, 30, 40

# What is **kwargs
#It accepts named arguments (key=value).
def student(**kwargs): 
    print(kwargs)

student(name="Shyamal", age=20)

#another example 
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Shyamal", age=20, country="India") 