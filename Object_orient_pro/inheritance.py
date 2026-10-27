"What is inheritance ?"

"Inheritance is the process by which one class acquires the properties and methods of another class. "
"Think like a Grand parent"
"-> parent -> child"
# In short 
"""Store in one function main that use multiple function, instead of writing same thing multiple times.  """

'A child may inherit , eyes, hair, height,  the chield inherits characteristics the parent. similarly, in OOP, A new class inherits attributes and methods from an existing class.'



# With out inheritance
class Dog:
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

    def breathe(self):
        print("Breathing")

s = Dog() # store main Dog class in s variable. 
s.eat() 
s.sleep()
s.breathe()

#Let's take an example with inheritance and without inheritence 

"With out inheritance "

# suppose every animal can:
# eat(), sleep(), and a dog can also bark . 
# Without inheritance, we have to write everything ourselvs .

class Dog:

    def eat(self):
        print("Dog is eating")

    def sleep(self):
        print("Dog is sleeping")

    def bark(self):
        print("Woof!")

"How to create an Object:"

dog = Dog()

dog.eat()
dog.sleep()
dog.bark()

# Now suppose we also create a cat 

class Cat:
    def eat(self):
        print("Cat is eating")

    def sleep(self):
        print("cat is cleeping")

    def meow(self):
        print("meow") # Notice something ???

        # we wrote def sleep(self), def eat(self): 
        # twice, if we create 100 information . we will write eat() and sleep() 100 times. That's a lot repeated code . 

        # that's a lot a repeated code . 

        "With inheritance , Now let's improve design . "
        "Create 1 parent class. "


class Animal:

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

# Now Dog inherits from Animal
class Dog(Animal):

    def bark(self):
        print("Woof!")

# Cat also inherits 
class Cat(Animal):

    def meow(self):
        print("Meow!")

dog = Dog()
cat = Cat()

# call methods 

dog.eat()
dog.sleep()
dog.bark()

cat.eat()
cat.sleep()
cat.meow()

# notice something eat() writen once and sleep() writen once . Both Dog and cat can use them .

# instead of write every line for every info we use inheritant for better and short time periods . 

class Animal:
    def eat(self):
        print("Eating")
    
    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):
    def bark(self):
        print("Woof!")



class Cat(Animal):
    def meow(self):
        print("Meow")

my_dog = Dog()
my_dog.eat() # Notice something even in dog variable we don't write dog eat but even we use eat function for print the string word.
my_dog.bark()


# One of the best analogy is :- 

# Without inheritance 

"""Dog
├── eat()
├── sleep()
└── bark()

Cat
├── eat()
├── sleep()
└── meow()
"""
#With inheritance 
"""
Animal
├── eat()
└── sleep()
      ▲
      │
 ┌────┴────┐
 │         │
Dog       Cat
│          │
bark()    meow()


"""