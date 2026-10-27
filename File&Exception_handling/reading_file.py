#Hello guys in this lecture i will teach you how to read a file 


#Read a file using --> 'r'

f = open("/Users/shyamalkar/Desktop/Coding/Python_Universe_org/File&Exception_handling/example_1.txt", 'r')
data = f.read()
print(data)
f.close()