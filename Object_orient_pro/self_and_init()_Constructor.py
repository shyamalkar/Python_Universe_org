"What is __init__() ?"
"__init__() is a special method (constructor) that is called automatically whenever you create a new object."

"What is self ?"

"This is the concept that confuses almost every beginner. let's make is simple,"
"Imagine you have three students:"

"Alice"

"Bob"

"Charlie"

'Each student has their own:'

'Name'
'Age'
'Marks'

'When Alice says:'

"My name is Alice."

"The word my refers to Alice."

"When Bob says:"

"My name is Bob."

"The word my refers to Bob."

"In Python, self means this current object."

"It refers to the object that is calling the method."


# using self to store data 

'Now make lets make objects store information'

class Student: # class is a attributes 

    def __init__(self, name): # name is a parameter and i can store multiple values in one parameter.
        self.name = name

s1 = Student("Alice") # add information data 
s2 = Student("Bob") # add another data 

print(s1.name) # print the parameter with adding data using variable , at first write data add variable and next write parameter .
print(s2.name)


# multiple attributes


class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks

s1 = Student("Alice", 20, 95) # alice is name parameter and 20 is age parameter and 95 is marks 
s2 = Student("Bob", 22, 88)
s3 = Student("Bobi", 23, 34)
s4 = Student("ABoba", 12, 90)
s5 = Student("Bob", 22, 98)




#accessing attributes
print(s1.name) # name parameter from s1 variable
print(s1.age) # age parameter from s1 variable
print(s1.marks) # marks parameter from s1 variable

# adding a method 
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("My name is", self.age)



s1 = Student("Alice", 20) # s1 variable calling student method and store name and age , here is the best part in oops parameter can detect auto so we only write name and age 

s1.introduce()



class Avenger:
    def __init__(self, name, power, weapon, nationality='american'):
        self.name = name
        self.power = power
        self.weapon = weapon
        self.nationality = nationality

    def introduction(self):
        print(f"Hello my name is {self.name}")

    def carrying_weapon(self):
        print(f"i am carrying the weapon {self.weapon}")

Iron_man = Avenger("Iron man", "Genius intelligence about technology")

print(Iron_man.introduction())
print(Iron_man.carrying_weapon())