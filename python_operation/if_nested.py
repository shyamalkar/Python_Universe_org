input_1 = int(input("Enter your age: "))

if input_1 >= 18:
    if input_1 >= 21:
        print("You can eat alcohol & Vote")
    else:
        print("You can Vote only")
else:
    print("You are Minor")