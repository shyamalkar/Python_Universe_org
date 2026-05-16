# In this coding file , we can pass a function as argument of another function the result using another function ? 
def add_1(number):
    return number + 1 
print(add_1(4)) # THe output is 5 because we give a number 4 and it add +1 and return 4+1 = 5]

def square(number):
    return number ** 2

num = int(input("Enter a number: "))
re  = square(add_1(num)) # first number is add +1 and it's square e.g.,number is 4 and add +1 and become 5 square 5*5=25

print(f"Output is:{re}")