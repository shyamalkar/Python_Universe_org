"""What is encapsulation ? 
Encapsulation means wrapping data (attributes) and methods together inside a class 
and controlling how the data can be accessed or modified"""

#In short 
# Protecting the object's data from being changed in an uncontrolled way.

# suppose you have 50000 rupess in your bank account. can you directly open the bank database and do this ?
# Balance = ₹10 00 000 , the answer is No . 
# instead, the bank provides methods like: 
"""Deposite(), 
Withdraw(), 
Check Balance()
I con't touch the balance directly . the bank controls it. this is encapsulation.
"""

#Real life example 
"""
Imagine a car. 
Can you directly change the engine's internal state while driving. 
The answer is No 
Instead, you use : 

start(), 
brake()
Accelerate()
Stop(), so the engine is protected . 
My interact through safe methods . 
"""

# But the same question remain 
# Imagine this class, 
class BankAccount:
    def __init__(self):
        self.balance = 1000

# create an Object. 
account = BankAccount()

# Now anyone can do this . 

account.balance = -50000

#or 
account.balance = "Hello"

# Python allows because it's balance is Public . 
# Now the object is data becomes invalid .


#Problems is , Nothing stops users from writing incorrect values.
#For example

account.balance = -999999999
#Does a bank account normally allow a negative balance like this ?, usally no , we need some prediction 

# Encapsulation soluation 

#instead making the balance public , make it private . 

class Bankaccount:
    def __init__(self):
        self.__balance = 1000

# Notice: 
"__balance, this makes the attribute private. "

# Try accessing it 

#account = BankAccount()
#print(account.__balance) # The output is attribute error, python says you can't access directly



#Two underscore, make the attribute private (Remember this). 


# Then how do we real the balance ?
# we create a gatter
class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance
    
# Now 
account = BankAccount()

print(account.get_balance())

# i not touching __balance direcctly , make ask the class to give it to us  . 

# How do the change the balance 

account.__balance = 500

# we create a method . 

class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
# Now
account = BankAccount()

account.deposit(500)

print(account.get_balance()) # output should be  1500 . 

# Let's check validation , suppose someone does this 

account.deposite(-500)
# should that be allowed ? the answer is no 
# so we added check condition 

class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount

        else:
            print("Invalid Amount")

    def get_balance(self):
        return self.__balance

account.deposit(-100)

# Public vs private 

#Public

class student:
    def __init__(self):
        self.name = "Alice"
    
# Anyone can access it . 
student = student()
print(student.name )

# Private 

class student:
    def __init__(self):
        self.name = "Alice"

# Now 
student = student()
print(student.__name)


# So the real world analogy is 
"""
Capsule
│
├── Medicine (inside)
└── Cover (outside)
Don't touch the medicine directly. 
The capsule protects it . 

Similarly:

Object
│
├── Data (private)
└── Methods (public)


the methods are the safe way to interact with the data.
"""

