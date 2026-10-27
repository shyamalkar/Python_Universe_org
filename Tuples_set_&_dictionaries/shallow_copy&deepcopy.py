# What is shallow copy ?
# A shallow copy creates a new outer object, but nested objects are still shared.

import copy 
a = [[1, 2], [3, 4]]
b = copy.copy(a) # If you write so many same thing just use copy() function. 

#When i use copy function inside looks like this .
# a = -----> 1, 2, 3, 4
#   |
#   |
#   V
# b = -----> 1, 2, 3, 4 # remember in inner list are same objects .

b[0][0] = 99
print(a) 
print(b)  

# What is deep copy ?
#Deep copy creats completely independent objects.



import copy 

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

"""
a
 │
 ▼
┌───────────────┐
│  ●────►[1,2]  │
│  ●────►[3,4]  │
└───────────────┘

b
 │
 ▼
┌───────────────┐
│  ●────►[1,2]  │
│  ●────►[3,4]  │
└───────────────┘
"""
# in a variable = list1 [[1,2],[3,4]]

b[0].append(100)
print("In b list",b)
