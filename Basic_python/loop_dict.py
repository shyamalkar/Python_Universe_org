"""we have the following dictionary containing details:

user = {
    "user name": " my_user",
    "password":"test@123",
    "email": "my_user@example.com",
    "address":"ABC road. 111111",
    "country": "Australia"
}
Delete the sensitive information from the dictionary present in a list 
sensitive_info = ["password", "address"]
"""

user = {
    "user name": " my_user",
    "password":"test@123",
    "email": "my_user@example.com",
    "address":"ABC road. 111111",
    "country": "Australia"
}
sensitive_info = ["password", "address", "phone"]

for i in sensitive_info:
    if i in user:
        print(f"Deleted => key: {i}, Value: {user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present, cannot delete!")
print(user)

