""" 
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

"""

student_dict = {"Shyamal":89,
                "Subhadip":90,
                "Sibsankar":67,
                "Sumita":10, 
                "Sandipa":45, 
                "Saheli":70,
                "Alice":85}

student_input_name = str(input("Enter the student name:"))

if student_input_name in student_dict:
    print(f"{student_input_name} marks is: {student_dict[student_input_name]}")#f usage for formatted string, that means i can append variable inside.
    # :(Colon) format start from here.
    #.(dot)decimal point afterdot .
    # .2f means show 2 more value after dot
else:
    print(f"Student {student_input_name} not found!")

