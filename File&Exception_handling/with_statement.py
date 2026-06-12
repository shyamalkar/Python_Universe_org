#read
with open("New_file_using_with.txt", "r") as f: # r means read
    data = f.read()
    print(data)

#write file (w) - overwrite
#old data delete and write new data

with open("New_file_using_with.txt", 'w') as f:
    f.write("Name: Shyamal\n")
    f.write("Marks: 85")


#appennd data using with 

with open("New_file_using_with.txt", 'a') as f:
    f.write("\nThis is a appended line\n")
    f.write("This is a second append line")


#Update file using with r+ read and write 

with open("New_file_using_with.txt", 'r+') as f:
    print(f.read()) #first read

    f.write("\n Updated Successfully")



# (wb) binary write (wb)
#for image, PDF, Audio 

with open("binaryfile.bin", 'wb') as f:

    f.write(b" Hello binary world")


#(rb)Binary read using with 

with open("binaryfile.bin", "rb") as f:
    data = f.read()
    print(data)

# Delete file (No with)

import os 

os.remove("New_file_using_with.txt")



#Always remeber 