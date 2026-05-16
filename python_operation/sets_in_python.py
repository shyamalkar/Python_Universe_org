#sets are non-sequential collection of items
# comma separated elements enclosed within {}

# Sets do not allow duplicate elements
# Sets  is a data structure where , 
#Don't have duplicate rows, order not fixed,but you 
s1 = {10, 2.5, 10, 30, 10}
print(s1)
s1.add(4) #add list
print(s1)

#Remove
s1.remove(2.5)
print(s1)
#Discard
s1.discard(100)
print(s1)