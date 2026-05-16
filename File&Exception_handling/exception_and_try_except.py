"""
1. compile time error as syntax error & Indentation error
2. exception => errors during execution
"""
"""
num_1 = int(input("Enter a number (1-10): "))
num_2 = int(input("Enter a number (1-10): "))


variable_divi = num_1 / num_2

print(f"Your number{num_1} and {num_2} division is: {variable_divi}")"""


num_1 = int(input("Enter a number (1-10): "))
num_2 = int(input("Enter a number (1-10): "))

try:
    result = num_1 / num_2
    print(result)
except ZeroDivisionError:
    print("The demonitor cannot be 0")


#What is exception ?
"""Exception is a error , if you write a programm that showing a error,
 you want to fixed the bug and want to run this programm smoothly then use except for best option handle the error.
"""