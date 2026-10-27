# Continue 

for i in range(1, 6):
    if i == 3: # this 3 number not count , while loops are runing
        continue

    print("Using continue and inside this coding manually writen 3 are not countable",i)

# break 
# break function help us to break the loop while 3 comes then it stop count 
for i in range(1, 6):
    if i == 5: # when 5 come then break the fuction 
        break # break will help to run the function 

    print("Using break",i) 


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