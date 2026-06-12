# What is map ?
# map() function usage for apply same rule for each line same value 

nums = [1, 2, 3]

result = list(map(lambda x: x * 2, nums))

print(result)

# What is filter() ?
#Selects the element that meets the condition.
nums = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x % 2 == 0, nums))

print(result) 