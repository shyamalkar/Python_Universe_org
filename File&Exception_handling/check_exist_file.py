#Now we gonna checking file exist or not ? 
#os.path.exists()

import os  # Import os module . 
file_name = "/Users/shyamalkar/Desktop/Coding/Python_Universe_org/File&Exception_handling/example.csv" #Data set name contain here .

if os.path.exists(file_name):  #Checking if a file exists or not .
    print("File exist")
    
else:
    print("File does not exist")