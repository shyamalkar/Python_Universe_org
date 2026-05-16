# Mutability & Immutability 
# List are mutable
# Tuples and Strings are immutable 

# At first i start talking about list are Mutable (It's change so many time's)
my_list = [10, 20, 30]
print("Before:", my_list)

#Change first element
my_list[1] = 100
print("After:", my_list)

#Tuple = immutable (Never change)
my_tuple = (10, 20, 30)
print("Before:", my_tuple)

#Try to change first element
my_tuple[0] = 100  # Here showing a error becuase tuple() are not change able that mean immutable.

#String = immutable (Not change)
str = "Hello"
print("Before:", str)
#Try to change first character
str[0] = "Y" #Here showing a error becuase string are not changeable that mean immutable

