def add(a, b):
    return a + b
#positional arguments - pasting the arguments in order of their position
#Positional argument is which order growing with position that is positional argument

result = add(a=10, b=30)
print(result)

#Default arguments
def add(a=0, b=10, c=0):
    print(f"a:{a}, b:{b}, c:{c}")

    return a + b + c

result = add(a=10, b=20, c=30)
print(result)

result = add(a=10, c=20)
print(result)

#The non-default arguments should NOT follow the default argument

#What is Variable Length argument(*args) ?
#When you don't know how many value's are coming then *args use this time. that's mean you can access unlimited arguments
