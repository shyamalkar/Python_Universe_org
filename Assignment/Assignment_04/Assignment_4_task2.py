"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
 
"""

"""For open python file :- 

| Mode   | Name           | Use for                           
| ------ | ------------- | -----------------------------------
| `"r"`  | Read          | For read the file                      
| `"w"`  | Write         | Erase the old data and write new   
| `"x"`  | Create        | Create ne file if file is present it give error  
| `"a"`  | Append        | Add new data at last              
| `"r+"` | Read + Write  | read and write file must be         
| `"w+"` | Write + Read  | write and read all erase                
| `"a+"` | Append + Read | Read and  append                       

"""

# File name
filename = "output.txt"

# Take input from user (for writing)
text_to_write = input("Enter text to write to the file: ")

# Write data to file (write mode - overwrites old data)
with open(filename, "w") as file:
    file.write(text_to_write + "\n")

print("Data successfully written to output.txt.\n")

# Take input from user (for appending)
text_to_append = input("Enter additional text to append: ")

# Append data to same file (append mode)
with open(filename, "a") as file:
    file.write(text_to_append + "\n")

print("Data successfully appended.\n")

# Read and display final content
print("Final content of output.txt:\n")

with open(filename, "r") as file:
    # Read entire file
    content = file.read()
    
    # Print file content
    print(content)