"""Write a program to simulate a roll of a die/dice
A die has 6 faces with numbers 1 to 6 writter on them 
The program should randomly prints a number between 1 to 6
"""

import random 

print("welcome to the game of rolling dice.")

while True:
    choice = input("press 'Enter' to roll the dice or 'q' to quit.")
    choice = choice.strip()
    if choice == 'q':
        print("Thanks for playing the game, bye!")
        break
    elif choice == '':
        number = random.randint(1, 6)
        print(f"your number is number {number}")
    else:
        print("invalid input!!")
print("GAME OVER!!!")