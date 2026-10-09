# In school we often learn BODMAS rule in Math, But in Python we use PEMDAS(Parentheses, Exponents, Multiplication, Division, Addition, and Subtraction) for more and accurate result.

#Parentheses (P): Solve everything inside grouping symbols first (like (), {}, or).

#Exponents (E): Evaluate any numbers with powers or roots (e.g., 3² = 9).

#Multiplication (M) & Division (D): These are on the exact same priority level. Solve them from left to right as they appear in the equation.

#Addition (A) & Subtraction (S): These are also on the same priority level. Solve them from left to right as well

# 14 because * are  more precedence than +, so 3*4 = 12+2 = 14 
print(2 + 3 * 4)

#  e.g., 
print(2 ** 3 ** 2) # According to PEMDAS , calculation always left to right, so calculation is = 2 ** (3 ** 2)= 2 ** 9 = 512 .
# Double ** means :- E.g., 1 ** 2 that means 1 × 1 = 1 , 5 ** 2 means  5 × 5 = 25 . that was the hole concept behind the scence.
#In python operation BODMAS not help in this situation becausebadmas have not any special function like and ,or 
 

print("True or False and False is True :", True or False and False) # Output is = True Because, False and False = False True or False = True.



#============================ Warning ================================

# In PEMDAS we always calculate left to right only =    the left-to-right rule only applies to multiplication, division, addition, and subtraction.
