#union, intersection, difference
# operation on set  :- set is a unique collection 

A = {1, 2, 3} # set 
B = {3, 4, 5}

# add

A.add(6) # added 6 without replace anyone.
print("print A variable", A)

# update :- add multiple value . 
A.update([7, 8])
print('Adding multiple values', A)

# remove , if don't have then showing error
A.remove(2)  

#Discard() :- if don't have then not showing error 

A.discard(100) # it's help to remove specific element from a set .



# pop()

A.pop() # empty means last element remove
print("Removing element from set")

#Clear
A.clear()


# Set mathmetical operation 

A = {1, 2, 3}
B = {3, 4, 5}

#Union  :- Unique element in both set
print("Union", A | B)
print("Intersection", A.union(B))

#intersection :- both set common element 

print("",A & B)
print(A.intersection(B))

#difference (-), have in A but not in B 

print("minus",A - B)

# symmetric difference ˆ , which things are not common .
print("Symmetric",A ^ B)

# subset and superset
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))

# superset
print(B.issuperset(A))

#Disjoin :- does have common elemtn 
print({1, 2}.isdisjoint({3, 4}))