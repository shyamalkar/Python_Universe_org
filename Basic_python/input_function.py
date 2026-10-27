# Input function often use for  take input from user.
name = input("Enter your name: ")
print(name)

# always remember input always return string .

#E.g, 
age = int(input("Enter your age: "))

print(age)
print(type(age)) # always return as a string . 

#Then how to work with string ?
#With int() or float()  type conversion .
age = int(input("Enter your age: "))
print("always give you more 5 age",age + 5) # Because here add + 5  

# Float input 

price = float(input("Enter price: "))
print("Multiply by 2",price * 2) 

a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
print(a + b)

# let's build a application using these . 

input_1 = str(input("Enter your first name:"))
input_2 = str(input("Enter your second name:"))
input_age = int(input("Enter your age:"))
pan_input = int(input("Enter your CGPA, in float format:"))

# print the full name.
print("Your full name is:", input_1 + input_2)
# check condition 
if  input_age < 0  or input_age > 100:
    print("Something went wrong")
else:
    ("Good number")

if input_age >=18:
    print("You are eligible for vote, and your age is:", input_age)
else:
    print("Your age must be grather than or equal to 18")

if pan_input == 0.9:
    print("You are pass")
else:
    print("You are fail")

