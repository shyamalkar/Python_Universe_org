"""
In this lecture i discuss about some operation like, 
reverse()
sort()
count()
Membership operation()

"""
#Take a quick list here  for use (reverse) method.
days_of_week = ["Mon", "Tue", "Wed", "Thir", "Fri", "Sat"]
days_of_week.reverse()
print(days_of_week)

# Next we start using  sort()
num_list = [1, 2, 4, 56 ,6, 78, 45, 5, 3, 8 ]
num_list.sort()
print(num_list)


# So next we move to start count()
"""What exactly do this count() function , count function usage for 
for how many repeat value in a list i mean how many repeat element 
in a list ?  """
numbers = [1, 0, 3, 2, 4, 5, 9, 5, 8, 6, 8]
print(f"Chose a number from this list:{numbers}")
item_to_count = int(input("Enter the number to be counted from the above list:"))
c = numbers.count(item_to_count)
print(f"Occurence of {item_to_count} is {c}")

numbers = [1, 0, 3, 2, 4, 5, 9, 5, 8, 6, 8]
numbers.count(numbers)
print(numbers)


points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(4)

print(x)