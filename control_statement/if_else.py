#For example 
input_age = int(input("Enter your age : "))
input_has_id = bool(input("Input your id enter True or Flase . if you has id then True if not just write it False: "))
input_ticket = int(input("Enter your ticket number 0-9: "))
input_cinema_seat = int(input("Enter your cinema seat: "))
couple_or_single = int(input("Enter couple or single ? :"))

if input_age >= 18:
    if input_has_id:
        if input_ticket:
            if input_cinema_seat == 0:
                if couple_or_single == 2:
                    print("couples are not allowed.")

                else:
                    print("You are eligible for this cinema room.")

            else:
                print(" your cinema seat must be grather than 0. ")       
        else: 
            print("Buy a ticket first")
    else:
        print("Bring your ID")
else: 
    print("Not allowed You must be 18+")


# There are all the condition depended with each other , 
"""Is the person 18 or older ?
 If yes, do they have an ID ?
 If yes, Do they have a ticket ?""" # That is how a nested loop work and it is usefull.

