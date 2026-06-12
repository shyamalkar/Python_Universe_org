#Now we cover a topic like update

f = open("example_1.txt", "r+") # r+ read and write and w+ write and read a+ for append + read
print(f.read()) #Read first
f.write("\n Updated line")
f.close()
