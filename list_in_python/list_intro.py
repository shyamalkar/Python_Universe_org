# What is list ?
# list is a collection where multiple value store into one variable and it's mutable and flexible.


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

 
nums[0] = 100 # replace 1 and place 100.

print(nums)

# Duplicate allowed

nums = [1, 1, 2, 2, 3]

print(nums)

# Different data types can store in list 
data = [10, 10, 3.14, "Python", True]# integer and decimal and string and boolean all are enable.

print(data)

#Create list 
numbers = [1, 2, 3]

names = ["Rahul", "Shyamal"] # string list 

mixed = [1, "Hello", True]

empty = []

# Accessing elements (Indexing)
fruits = ["Apple", "Banana", "Mango", "manago", "chia seed"]

print(fruits[0])

# negative indexing

print("if you use minus 1 that means python always print last one.", fruits[-1]) 


# Update element 

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange" # replace banana and add Orange.


print(fruits)

# Adding number element 
nums = [1, 2]

nums.append(3)

print("append number 3",nums)

# Add specific index
nums = [1, 3]

nums.insert(1, 2) # it's doesn't allowed duplicate value. it can allow only 3 but not number 1, and it automatically present step by step which should be come after another number. 

print("Insert", nums)

# extend(), it can add a list .
a = [1, 2]
b = [3, 4]

a.extend(b) # it help to present double list in a single list = [1, 2, 3, 4] .

print("extend", a)

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

print("delete 0 position value which was 1",nums)

# clear()
nums = [1, 2, 3]

nums.clear()

print(nums)

# slicing , take a element from list.
nums = [10, 20, 30, 40, 50]

print("nums", nums[1:4]) # In Python, nums[1:4] means you are slicing the list from index 1 up to (but not including) index 4

#contatenation  , use for add 2 list .

a = [1, 2]
b = [3, 4]

print("use + method convert array into list .", a + b)

# Repetition 

print("Repetition ",[1, 2] * 3) # 1 and 2 repreate 3 times.

# Membership Operators 
nums = [1, 2, 3]

print(2 in nums) # checking does 2 present in nums ?
print(5 not in nums) # checking 5 is not in nums ? if not present then True

# length 

nums = [1, 2, 3]

print("number of length",len(nums))

# sorting 
nums = [4, 2, 5, 1] # sorting number step by step which number come first and which one second .

nums.sort()

print(nums)

# Reverse sorting 
nums.sort(reverse=True) # reverse usefor backward process. 

print(nums)

# Reversing 
nums = [1, 2, 3]

nums.reverse()

print(nums)

# Counting 
nums = [1, 2, 2, 3]

print("How many times 2 present in nums columns", nums.count(2))

# Finding index 
nums = [10, 20, 30]

print(nums.index(20))