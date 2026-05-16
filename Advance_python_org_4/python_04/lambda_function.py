#LAMBDA
"""
def add(a):
    return a + 1
res = add(1)
print(res)

"""
#syntax 
#lambda argument : expression
"""
fun = lambda a, b, c, d, e: a + b + c + d+ e
res = fun(2, 2, 3 ,4, 5)
print(res)"""
#How to work with 1 number


fun = lambda a: a + 1 # Lambda is best for short function not for big function , def is is condider to good for big function.
res = fun(2)
print(res)