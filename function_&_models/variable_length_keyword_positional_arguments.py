# What is variable length positional arguments (*args)
# How many argument can come we don't know before .


def add(*args):
    print(args)

add(1, 2, 3)

# In addition 
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))

# Variable length keyword arguments (**kwargs)
def details(**kwargs): 
    print(kwargs)

details(name="Shyamal", age=21)
 