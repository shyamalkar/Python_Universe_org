"""
create a simple number guessing game.
The user gets 10 chances to guess a number.
If the user guesses the number before 10 chances,
stop asking the number from the user,
say Congrats and the game 
if the user never guesses the number, ask them 10 times and then the game!!
"""

print("Create a simple number guessing game.\n We have a number that needs to be guessed. You have 10 chances.")
print("Your secret number is between 1 to 50.\n You have only 10 attempt left's")

count = 0
max_try = 10
secret_number = 63

while count <= max_try:
    password =int(input("Enter guess number: "))
    if secret_number == password:
        print("You are right:")
        
        break

    else:
        print("wrong") 
        count += 1 
    print("Finished")