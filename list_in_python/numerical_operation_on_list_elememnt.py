# What is numerical operation ?
"""
These are very important because they are widely used in Data Science, ML, and even general Python programming.
"""

# These are very importent , because data science, ML , even we use general python programming.
numbers = [10, 20, 30, 40, 50]
print(sum(numbers))

print(min(numbers))
print(max(numbers))
import math

print(math.prod(numbers))

nums = [4, 1, 5, 2]

print(sorted(nums))


nums = [3, 1, 2]

nums.sort()

print(nums)


# Counting numeric values
nums = [1, 2, 2, 3, 2]

print(nums.count(2))

# Finding largest and smalest manually, largest 

nums = [5, 2, 9, 1]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print(largest)

# smallest 

smallest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num

print(smallest)

# even number addition 
nums = [1, 2, 3, 4, 5, 6]

total = 0

for num in nums:
    if num % 2 == 0:
        total += num

print(total)

# odd numbers addition 
total = 0

for num in nums:
    if num % 2 != 0:
        total += num

print(total)

# square of numbers 

nums = [1, 2, 3]

squares = []

for num in nums:
    squares.append(num ** 2)

print(squares)

# List Comprehension 
squares = [num ** 2 for num in nums]

print(squares)

# Median 

import statistics

nums = [1, 2, 3, 4, 5]

print(statistics.median(nums))

# mean 
import statistics

print(statistics.mean(nums))

#Mode 

nums = [1, 2, 2, 3]

print(statistics.mode(nums))


# A real e.g, 

marks = [80, 75, 90, 85, 70]

print("Total:", sum(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks)/len(marks))