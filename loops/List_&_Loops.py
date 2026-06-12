# list and loops 
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

# Dictionaries and loops 
student = {
    "name": "Shyamal",
    "age": 21,
    "city": "Kolkata"
}

#only key 
for key in student:
    print(key)

# Only value 
for value in student.values():
    print(value)

# key and value 
for key, value in student.items():
    print(key, ":", value)