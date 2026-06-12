# What is nested if statement ? nested statement is ine loop present another loop.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")

# All knowladge in one :-

#if use for checking condition
# if-else if condition got true then it's work if condition not get matched then another work .
# if elif else = checking multiple conditiion.
# nested if - one if present another if .
# ternary operator - if else write in one line . 

# One more example:- 
balance = 5000
amount = 2000
pin_correct = True

if pin_correct:
    if balance >= amount:
        print("Transaction Successful")
    else:
        print("Insufficient Balance")
else:
    print("Wrong PIN")