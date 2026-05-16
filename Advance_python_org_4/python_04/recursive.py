"""
Recursion si a process in which a function calls itself till a certain condition is not set
factorial os n=> n _ (n-2) * . ...2 * 1
n!
4! = 4 + 3 + 2 + 1 same thing
"""

#With out recursion
"""
def fact(num): # 
    factorial = 1 # Here create a box for store the result, 
    while num > 1: # The loop will continue as long as there is a number greater than 1.

        factorial *= num #it's actually a factorial = factorial * num, currenly multiply by num
        num -= 1 # num -= 1 or num = -1 both are same. and decrease 1 step by step
       # 4 > 1 ✅
       # 3 > 1 ✅
       # 2 > 1 ✅
       # 1 > 1 ❌ (stop)


    return factorial
#print(fact(4))
n = 4
print(f"Factorial of {n} is {fact(n)}")

"""

#With recursion

"""
there are 2 parts to any recursive function
1. Base/terminal condition = Base / Terminal is a funcion where function stop work . if function are not situated then function work infinit recursion.
e.g., If you are going down the stairs if stop does't exist you fall in floor . 
example factorial:- 
def fact(n):
if n ==1:
return 1 #That mean if n is 1 then stop here. 
#Recursive condition(self call)
what is it ? 
Where the function calls itself again.
fact(n-1) #why use this ? because big problem divide by small problem.


2. Recursive condition

what is it ? 
    where  a function call itself again, but small value . 

    coding e.g., 

    def fact(n):
    if n == 1:      # Base case
        return 1

    return n * fact(n-1)#This line call again itself.    #Recursive condition

"""
#full example
def fact(n):

    if n == 1:          #Base case
        return 1
    n = 10
    return n * fact(n-1)   #Recursive case