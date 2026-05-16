"""
Simple Interest = (p * R * T) / 100

P = Pricipal amount 
R = rate of interest
T = time duration

"""

principal = float(input("Enter principle amount:"))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: "))
si = (principal * rate * time) / 100
print("Simple interest is", si)