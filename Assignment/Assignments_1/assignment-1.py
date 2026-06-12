"""Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
 o	Addition
 o	Subtraction
 o	Multiplication
 o	Division
3.  Displays the results of each operation on the screen.
 Expected Output:
The output should include the result of each operation performed, for example:
"""

Input_1 = int(input("Enter 1st valid Number:"))
Input_2 = int(input("Enter 2nd valid Number:"))

if Input_1 == Input_2:
    print("Addition:",Input_1 + Input_2)
else:
    print("Enter Only number")
if Input_1 == Input_2:
    print("Subtraction:", Input_1 - Input_2)
if Input_1 == Input_2:
    print("Multiplication:", Input_1 * Input_2)
if Input_1 == Input_2:
    print("Division:", Input_1 / Input_2)

