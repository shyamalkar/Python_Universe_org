#I cover all of these operation in sets function
#like - Union, Intersection, Difference, Symmetric Difference
#Subset, Superset, Disjoin, 

#Union = All duplicate are remove and build step by step

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)

print(f"Union:",A.union(B))

#Intersection = How many common value in this A & B 

print( A & B )
print("Intersection:", A.intersection(B))

#Difference = Difference means a value present in a list but never situated in B list
print( A - B )
print("Difference:",A.difference(B))

#Symmetric Difference- remove all common
print( A ^ B )
print("Symmetric:",A.symmetric_difference(B))

#Disjoint - Any common have in this variable ?

print("Disjoint:", A.isdisjoint(A))