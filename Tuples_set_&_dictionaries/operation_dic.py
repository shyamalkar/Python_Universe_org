# WHat is dictionary 

# Dictionary is key -> Value Mapping 
student = {
    "name": "Shyamal",
    "age": 21
}

print(student["name"])

#  get()

# if don't have key then not showing error 


# update value 
student["age"] = 22

print(student)

# remove item 
student.pop("age")

print(student)

# del 
del student["city"]

# clear

student.clear()

print(student)

#key, values, items 
