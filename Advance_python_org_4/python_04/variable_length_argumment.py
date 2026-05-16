#when you send so many data from key=value format then use **kwargs
#kwargs = keywoord argument
# * means give as come as you like
# args means add all togather 

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

#kwargs = keyword arguments e.g., 
def student(**kwargs):
    print(kwargs)
student(name="Rahul", age=20, city="kalinagar")

#kwargs and args all togather
def demo(*args, **kwargs): # * use for other all thing add togather 
    #*args mean as much value come all togather and made tuple
    all = (args, kwargs)
    print(all)
demo(10, 20, 30, name="Amit", age=25)



#Poaitional+ *args Togather
def show(a, b, *args): # a , b fixed and *args is rest
    print(a, b) #a mean 1 and b mean 2 so here 1 and 2 are out of tuple.
    print(args)
show(1, 2, 3, 4, 5)


# * use for value , Value is only number / text / data e.g., 10, 20, 30

#** use for key , key is only name and value e.g., name="Amit", age=20

#why * many value ? * collect many values -> tuple 
a, *b = 1, 2, 3, 4
print(a)
print(b) # *b catch others

#why ** many keys ?  ** = unlock dictionary e.g., ** collect many keys+value -> dict
d = {"x":10, "y":20}
def test(x, y):
    print(x, y)
test(**d) # broke the dictionary and create new parameter

