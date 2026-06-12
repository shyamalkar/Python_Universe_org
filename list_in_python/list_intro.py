# What is list ?
# List is a collection where one value store into another variable.
#easy way
# list is a collection where multiple value store into a variable.


#e.g., if you want to store 5  student marks.
#witout list

mark1 = 80
mark2 = 75
mark3 = 90
mark4 = 85
mark5 = 70

# With list 
marks = [80, 75, 90, 85, 70]

# List are mutable , because list are mutable 
nums = [1, 2, 3]
 
nums[0] = 100

print(nums)

# Duplicate allowed

nums = [1, 1, 2, 2, 3]

print(nums)

# Different data types can store in list 
data = [10, 3.14, "Python", True]

print(data)

#Create list 
numbers = [1, 2, 3]

names = ["Rahul", "Shyamal"]

mixed = [1, "Hello", True]

empty = []

# Accessing elements (Indexing)
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])

# negative indexing

print(fruits[-1])


# Update element

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

# Adding element 
nums = [1, 2]

nums.append(3)

print(nums)

# Add specific index
nums = [1, 3]

nums.insert(1, 2)

print(nums)

# extend(), it can add a list .
a = [1, 2]
b = [3, 4]

a.extend(b)

print(a)

# removing element

nums = [1, 2, 3]

nums.remove(2)

print(nums)

# pop() , It deletes using the index and returns the value.
nums = [10, 20, 30]

x = nums.pop(1)

print(nums)
print(x)

# Del 
nums = [1, 2, 3]

del nums[0]

print(nums)

# clear()
nums = [1, 2, 3]

nums.clear()

print(nums)

# slicing , take a element from list.
nums = [10, 20, 30, 40, 50]

print(nums[1:4])

#contatenation  , use for add 2 list .

a = [1, 2]
b = [3, 4]

print(a + b)

# Repetition 

print([1, 2] * 3)

# Membership Operators 
nums = [1, 2, 3]

print(2 in nums)
print(5 not in nums)

# length 

nums = [1, 2, 3]

print(len(nums))

# sorting 
nums = [4, 2, 5, 1]

nums.sort()

print(nums)

# Reverse sorting 
nums.sort(reverse=True)

print(nums)

# Reversing 
nums = [1, 2, 3]

nums.reverse()

print(nums)

# Counting 
nums = [1, 2, 2, 3]

print(nums.count(2))

# Finding index 
nums = [10, 20, 30]

print(nums.index(20))