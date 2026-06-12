balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)

def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
    else:
        print("Insufficient Balance")

def check_balance():
    print("Balance:", balance)


deposit(500)
withdraw(200)
check_balance()