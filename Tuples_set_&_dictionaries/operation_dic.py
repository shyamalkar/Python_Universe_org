# What is dictionary 

# Dictionary is key -> Value Mapping 
student = {
    "name": "Shyamal",
    "age": 21
}

print(student["name"]) # before ading key at first write student variable . 


# update value 
student["age"] = 22 
print(student)

# remove item 
student.pop("age")
print(student)

# del 
del student["age"]

# clear

student.clear()

print(student)

#key, values, items   


