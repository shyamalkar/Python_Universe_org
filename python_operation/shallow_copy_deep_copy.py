a_1 = [1, 2, 3]
b_1 = a_1      # Same memory reference

b_1[0] = 100

print(a_1)
print(b_1)

#Shallow cop - one lever copy.

import copy 
a = [[1, 2], [3, 4]]
b = copy.copy(a) # If you write so many same thing just use copy() function. 

b[0][0] = 99
print(a) 
print(b) 

#Deep Copy

import copy
b = copy.deepcopy(a)
print(f"b",b)

# Shallow copy without module
a = [[1,2], [3,4]]

b = a[:]        # slicing
c = list(a)


