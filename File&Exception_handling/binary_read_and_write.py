#Working with binary file 

f = open("binaryfile.bin",'wb') # wb for write binary
f.write(b"hello binary world")
f.close()

f = open("binaryfile.bin", "rb") #rb for read binary 
data = f.read()
print(data)
f.close()  
