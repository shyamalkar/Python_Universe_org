"""What is arthmetic in python refers to the use of physical symbols(Operators)
to perform standard mathmetical calculations-such as addition,
suctraction, multiplication, division, modulus, exponentiation and floor division.

"""
def arithmetic(num1, num2):
    addi = num1 + num2
    sub = num1 - num2
    multi = num1 * num2
    return addi, sub, multi

val_1 =int(input("Enter number:"))
val_2 =int(input("Enter number:"))

sem1, sem2, sem3 = arithmetic(val_1, val_2)

print(f"Addition {val_1} and {val_2} is {sem1}")
print(f"Subtraction {val_1} and {val_2} is {sem2}")
print(f"Multiplication {val_1} and {val_2} is {sem3}")
