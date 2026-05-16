"""#File not found error . 
with open("data.txt", "r") as f:
    print(f.read()) #Show error because this file does't excist
"""
#solution 
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found") # Everytime check file exsit or not ?



#Forgetting Mode problem 
"""
with open("a.txt") as f:
    f.write("Hi") #Error :- Default does't write without r -> write
"""

#Solution
with open("a.txt", "w") as f:
    f.write("Hi")


#Overwrite by mistake (w)

with open("examkle.txt", "w") as f:
    f.write("New") # Old all data are delete

#Solution ---- use a if you want to keep data:

with open("data.txt", "a") as f:
    f.write("\nNew")

#And so on so for 