# for loop 
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# for loop over a string 

name = "Python"

for ch in name:
    print(ch)

# for loop over dictionary 
student = {
    "name": "Shyamal",
    "age": 21,
    "city": "Kolkata"
}
# Only key 
for key in student:
    print(key)

# Only value 
for value in student.values():
    print(value)


# key and value both 
for key, value in student.items():
    print(key, value) 