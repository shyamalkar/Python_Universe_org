"First don't worry about the difficult word. "
"Poly = many and Morph = Forms"
"So "
"Polymorphism = One interface, many forms( or many behaviors)."

"Real life example"
"Imagine a remote control"
"Remote :-|_TV"
"         |_AC"
"         |_Projector"
"The botton is the same , this is the basic idea about polymorphism"

# Think about the word

#start()

# For a car 
#car.start()

#means start the engine 
#For a computer 

#computer.start()

#mathod is same but the operator 

#start()
#But the behavior depends on the object. 

# First Python Example 
# Create a parent class
class Animal:

    def sound(self):
        print("Animal makes a sound")

#Now create a chield class.
class Dog(Animal):

    def sound(self):
        print("Dog says Woof!")

# Another child
class Cat(Animal):

    def sound(self):
        print("Cat says Meow!")
#Creater objects
dog = Dog()
cat = Cat()
animal = Animal()

# call the same method 

animal.sound()

dog.sound()

cat.sound()