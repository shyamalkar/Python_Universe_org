"Abstraction"

# What is Abstraction?

# The user knows what to do, but doesn't need to know how it is done.

# Definition

#**Abstraction means hiding the implementation details and showing only the essential features to the user.**

# Real Life Example 1: Car 

"""Imagine you're driving a car. You only know: text Start Engine Brake Accelerate Steering"""

"""Do you know exactly:- How the engine ignites the fuel ? How the gearbox changes gears? How the pistons move? """


#And you don't need to. You just use: python car.start()

"""The internal implementation is hidden.

This is abstraction."""

# Real-Life Example 2: ATM 

#I insert your ATM card. You press: , text Withdraw ₹500

"""Do you know:

* Which server is contacted?
* Which database is updated?
* How the bank verifies your PIN?"""
"No."

"""You only know:

Withdraw Money"""

#Everything else is hidden.
#That's abstraction.

# Difference Between Encapsulation and Abstraction
## Encapsulation

"""Question:

Who can access the data?**

Example:
python, self.__balance
The goal is to , protect data. """

## Abstraction

"""Question:

How does this feature work internally?

The goal is to hide complexity. """
"""
           Animal (Abstract)
                 │
         sound() [No Code]
                 │
      ┌──────────┴──────────┐
      │                     │
     Dog                   Cat
      │                     │
 sound()                sound()
"Woof!"                "Meow!"
"""

# How does python support abstraction ?
# Python provides a module called . abc, which stand for abstract base classes . let's us create abstract classes, 

# What is an abstract class ?
# an abstract class is a class that can't be used to create objects directly . 

# it's act's like blueprint that says: 
"Every child class must implement these methods "

from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class Animal(ABC): # Instead of writing, class Animal: we write class Animal(ABC):, this means Animal is an abstract class.

    @abstractmethod # this is called a decorator , it tells python every chield class must implement this method . 

    def sound(self): # notice please, there is no implementation, only the method name exists. we are saying: every animal must have a sound() method, but i won't define it here.

        pass

#  Now create a chield clas 
class Dog(Animal):

    def sound(self):
        print("Woof!")

# Now create an Object 
dog = Dog()

dog.sound()

# Another child 
class Cat(Animal):

    def sound(self):
        print("Meow!")
# Now 
cat  = Cat()
cat.sound()

# What happens if we forget 
class Dog(Animal):
    pass 

# Now 
dog = Dog()

# Python give a error , why ? because Animal said: every chield must implement sound(). dog did't , so the python prevents you from creating a dog object.


# Why use abstraction 
# Imagine you're building a payment system , every payment method must support pay() . 

# but the implementation differs.
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

#children
class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")

class PayPal(Payment):

    def pay(self):
        print("Paid using PayPal")



# Every payment method follows the same interface (pay()), but each implements it differently.