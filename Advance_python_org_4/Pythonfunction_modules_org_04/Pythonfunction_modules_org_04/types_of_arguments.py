#simple e.g., 
def add(a, b):
    print(a + b)

#Function call
add(10, 20)
# Logic is a = 10, b = 20 first value first parameter second value second parameter


#Default argument (Value added before)

def greet(name="Guest"):
    print("Hello", name)
#call
greet("Shyamal")
greet() #Logic is if user give value python take this . if not give python take default.


#Keyword Argument (Value taken by name )
def student(name, age):
   print(name, age)

    #Call
student(age=20, name="Shyamal")
print(student)

# Real life examle with all togather 
def info(name, course="Python", fee=0):
    print("Name:", name)
    print("Course:", course)
    print("Fee:", fee)

# Positional
info("Shyamal", "ML", 5000)

# Default use
info("Rahul")

# Keyword
info(name="Amit", fee=3000)