# Input function often use for  take input from user.
name = input("Enter your name: ")
print(name)

# always remember input always return string .

#E.g, 
age = input("Enter your age: ")

print(age)
print(type(age)) # always return as a string . 

#Then how to work with string ?
#With int() or float()  type conversion .
age = int(input("Enter your age: "))
print(age + 5) # Because here add + 5 

# Float input 

price = float(input("Enter price: "))
print(price * 2) 

a = int(input("Enter your first number"))
b = int(input("Enter your second number:"))
print(a + b)
