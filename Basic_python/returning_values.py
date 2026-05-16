def even_odd(num):
    if num % 2 ==0:
        return "Even"
    else:
        return "Odd"

result = even_odd(9)
print(result)

#
def add(num1, num2): #1 usage
    result = num1 + num2
    return result
val_1 = int(input("Enter a number: "))
val_2 = int(input("Enter a number: "))

val = add(val_1, val_2)
print(f"Addition of {val_1} and {val_2} is {val}")
