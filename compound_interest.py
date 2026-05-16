"""
What is the question ? 
 
  The code is trying to solve: 

  "GIven principal (p), rate (R), and time (T), Calculate compound interest."
 
Correct formula (Importent fix)
      
Amount = P * (1 + R/100) ** T 
CL = Amount - p 
 
 
Meaning of each variable

 P (principal) -> initial money
 R (rate) = interest rate 
 T (time) = number of years
 Amount = final money after interest
 CI = only the interest earned
"""
#Input features

principal = float(input("Enter principle amount:")) # Float for decimal number
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: "))

#amount1 = principal * (1 + rate/100) ** time


amount2 = principal * (1 + rate/100) ** time  #First start on bracket and divide / 100 then complete stepby step
ci = amount2 - principal

print("Total Amount:", round(amount, 2))
print("Compound Interest:", round(ci, 2))
