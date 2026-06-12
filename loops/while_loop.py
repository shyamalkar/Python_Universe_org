# While loop 

count = 1

while count <= 5:
    print(count)
    count += 1

# While infinite loop 

while True:
    print("Hello")

# infinite loop break 
while True:
    text = input("Type exit to stop: ")

    if text == "exit":
        break
