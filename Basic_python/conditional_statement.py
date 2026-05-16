"""#write a programe that pass or fail ? average number is 25% each subject. 
Input_1 = int(input("Enter your number for show the result:"))

if Input_1 >= 25:
    print("You are pass in this exame: ")
if Input_1 >= 95:
    print("Excellent you are upper of average:")

if Input_1 >= -8: 
    print("You enter a wrong number:")
else:
    print("You are not pass in this exame: ")
"""

marks = float(input("Enter your marks: "))

if marks >= 60:
    print("Your grade is A")

elif 80 <= marks < 90:
    print("Your grade is B")
elif 70 <= marks < 80:
    print("Your grade is C")
else:
    print("You faild this exame")
    