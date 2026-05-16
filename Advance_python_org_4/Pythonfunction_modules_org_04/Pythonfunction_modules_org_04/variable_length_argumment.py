def add(a, b):
    print(a + b)
add(10, 5)
def total(*args): # *args means you don't know how many order are input in thsi tuple
    print(args)
    print(type(args))

total(10, 20, 30, 40)

#sum tuple

def total(*args):
    s = 0
    for i in args:
        s += i
        print(s)
total(5, 10, 15, 20)
#difference between if , elif, else and def 
"""Project using If, elif, else"""
m1 = 70
m2 = 80

if (m1+m2)/2 >= 60:
    print("Pass")
else:
    print("Fail")


m1 = 50
m2 = 40

if (m1+m2)/2 >= 60:
    print("Pass")
else:
    print("Fail")


"""Using def function, use one time but using so many times """
def result(m1, m2):
    avg = (m1+m2)/2
    if avg >= 60:
        print("Pass")
    else:
        print("Fail not")

result(70,80)
result(50,40)