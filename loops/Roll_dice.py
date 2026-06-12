# roll dice 
import random

dice = random.randint(1, 6)

print("Dice:", dice)


# Roll again and again 
import random

while True:
    print("Dice:", random.randint(1, 6))

    choice = input("Roll again? (y/n): ")

    if choice.lower() == "n":
        break 