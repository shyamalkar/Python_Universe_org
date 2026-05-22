#What map() do ?
#In list take  every element and change new that is map()

#every number double without lambda

nums = [10, 20, 30, 40, 50]

def double(x):
    return x * 2
result = list(map(double, nums))
print(result)

#With using lambda
nums = [10, 20 ,30, 40, 50]

nums = list(map(lambda x: x*2, nums))

print(result)

#Output

#example 2 , all number square
number = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * x , number))
print(result)

#filter() + lambda
#What do filter ? 
#Some elements are kept and some are removed according to the condition.
#e.g., only calculate the even number 
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2==0, nums))
print(result)

#example 2 
marks = [45, 67, 23, 89, 55, 40]
passed = list(filter(lambda x: x >= 50, marks))
print(passed)
#map() and filter () example 

nums = [1, 2, 3, 4, 5, 6]

result = list(
    map(lambda x: x * 2,
        filter(lambda x: x % 2 == 0, nums)) # first() filter then map() ,  so filter calculate the even number and after even number are calculate by odd number . 
)

print(result)
