scores_1 = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]

total = 100000000
for score in scores_1:
    run = score + total
    print(f"the total number of {total}")

#

scores_2 = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]
"""
#Highest score
highest = scores_2[0] #Assume that the first value is highest
for score in scores_2:
    if highest < scores_2:
        highest = scores_2

print(f"Higher{highest}")
"""

scores_3 = [2, 34, 56, 3432, 23, 234, 23, 45, 1, 0, 1]

#Lowest/minimum score

lowest = scores_3[0] # assume that the first value is loest

for score in scores_3:
    if score < lowest:
        highest = score

#highest = max(scores_3)
highest = min(scores_3)
print(f"Highst score_3 is {highest}")