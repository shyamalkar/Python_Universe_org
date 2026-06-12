# Calculate the highest 
nums = [10, 50, 20, 90, 30]

highest = nums[0]

for num in nums:
    if num > highest:
        highest = num

print(highest)

# Calculate the lowest 


nums = [10, 50, 20, 90, 30]

lowest = nums[0]

for num in nums:
    if num < lowest:
        lowest = num

print(lowest)

# Highest and lowest togather 
nums = [10, 50, 20, 90, 30]

highest = nums[0]
lowest = nums[0]

for num in nums:
    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("Highest:", highest)
print("Lowest:", lowest) 