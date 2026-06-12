# What is tuple ?
# Tumple is a ordered and immutable collection 
# It can store multiple value 
# But it can not change after build 

numbers = (10, 20, 30, 40)

# tuple are generally create 
fruits = ("Apple", "Banana", "Mango")

print(fruits)

# Empty tuple
empty = ()

print(type(empty)) 

# Indexing 
numbers = (10, 20, 30, 40)

print(numbers[0])

# Negative indexing 
print(numbers[-1])

#slicing , take a percentage from tuple 

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

#start from 
print(numbers[:3])


# at last 
print(numbers[2:])

#Reverse 
print(numbers[::-1])

# Loop upper in tuple 
numbers = (10, 20, 30)

for num in numbers:
    print(num)


# Membership operators 

numbers = (10, 20, 30)

print(20 in numbers)
print(50 not in numbers)


# length 
numbers = (10, 20, 30)

print(len(numbers))

#Concatenation +

#both tuple add togather
a = (1, 2)
b = (3, 4)

print(a + b)

# Repetition 
print((1, 2) * 3)

#count() how many time in , count this 

numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))

# index()

#which position calculate this

numbers = (10, 20, 30)

print(numbers.index(20))

# Tuple packing 
# multiple value store in tuple 
numbers = (10, 20, 30)

print(numbers.index(20))

#tuple unpacking 

point = (10, 20)

x, y = point

print(x)
print(y)

# one of the most fevoraite method using for swap 
a = 5
b = 10

a, b = b, a

print(a, b)

# Tuple immutable , most important things 

numbers = (10, 20, 30)

numbers[0] = 100
