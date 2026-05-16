#In this .py file we create a simple banking application
"""
What we done here ?
show balance.  
withdraw. 
deposite. 
quite.
"""
def check_balance():
    pass


def deposite():
    pass


def withdraw():
    pass


current_balance = 1000

highest_withdraw_amount = 1000

print("=====Wellcome to my computer fake bank=====")

while True:

    print("1. check your balance (press 1)")
    print("2. Deposite an amount (press 2)")
    print("3. Withdraw an amount (press 3)")
    print("4. Quit (press 4)")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("Your balance is", current_balance)
        check_balance()
        break



    elif choice == 2:
        input_depo = int(input("Enter deposite amount :"))
        print(f"Your current amount is: {current_balance + input_depo}")
        break



    elif choice == 3:
        input_3 = int(input("Enter your withdraw amount:"))
        if input_3 >= highest_withdraw_amount:
            print("You cross the maximum amount of money please enter below 1000 ₹ ")
        else:
            print(f"Your amount {input_3} is successfull deposite . And your current amount is {input_3 - current_balance}")
        withdraw()
        break
    


    elif choice ==4:
        print("Okay have a good day visit again")
        break
    else:
        print("Invalid choice!!! Re-try.")

print("Thank you for banking with us!")