#What is __name__ ?
#It indicates whether the Python file was executed directly or imported.
# IF direct run then output should be :-  __main__

def greet():
    print("Hello")

if __name__ == "__main__": # __name__ file run or import ?
    greet()

# Function arguments . 
# At first data send into function.
def greet(name): # name is a parameter .
    print("Hello", name)

greet("Shyamal") # output Hello Shyamal

# return 
# Return use for return the value outside of the function.
def add(a, b):
    return a + b

result = add(2, 3)
print(result)