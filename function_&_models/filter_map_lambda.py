# What is map ?
# map() function usage for apply same rule for each line same value 

nums = [1, 2, 3]

result = list(map(lambda x: x * 2 , nums))

print(result)

# What is filter() ?
#Selects the element that meets the condition.
nums = [1, 2, 3, 4, 5]

result_1 = list(filter(lambda x: x % 2 == 0, nums)) # that means , remind these number which are divided by 2 , in nums list. 

print(result_1) 

#What is lambda ?
# lambda is a simple short anonymous function  which can write in one line .

# Normal function: 
def add(a, b):
    return a + b 
print(add(10, 20))

# this result using lambda
add = lambda a, b: a + b 
print(add(10, 20))

# Syntex 
# lambda parameter: expression 

# meaning 
# lambda -> keyword
# parameter -> return 
# expression -> which can return 
# It doesn't have to be written return in lambda because expression result return by his self.

# example 
def square(x): # x is a random value and here we can add any value
    return x * x  # our enter x value multiply with the same value like x = 5 , then x * x = 5 * 5  = 25 , if x = 6, 6 * 6  = 36
print(square(6))

# try with multiple parameter and example 
multiply = lambda a, b: a * b # * means multiply

print(multiply(5, 6))

# Three parameters

multiply = lambda a, b, c: a * b + c
print(multiply(5 ,7, 1))

# so many begginer ask why we don't use def function and using lambda 
# Actually lambda fuction use for use map(), filter(), reduce(), sorted(key=lambda...)
