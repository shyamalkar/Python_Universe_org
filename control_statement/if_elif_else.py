# To check multiple condition 
marks = int(input("Enter your exame mark: "))

if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 40: 
    print("Grade C")

elif marks >= 25:
    print("You passout with minimum number required is grather than 25.")
    
else:
    print("Fail in this exame") 