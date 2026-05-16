"""Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
 
"""

# File name to read
filename = "sample.txt" # This is a example file that attach in coding

try:
    # Try to open the file in read mode
    with open(filename, "r") as file:
        
        print("Reading file content:\n")
        
        # Read file line by line
        for i, line in enumerate(file, start=1):
            # Print each line with line number
            print(f"Line {i}: {line.strip()}")

# If file is not found, this block will run
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

# If any other error occurs
except Exception as e:
    print("Something went wrong:", e)