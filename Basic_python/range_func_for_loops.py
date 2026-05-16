#range() - built-in function used to generate sequence of integers in a given into
#range(start, stop, step) stop is not included 
#range(start, stop) => step = 1 by default
#range(stop) => to stop-1 with a step of 1, start = 0 by default

profits = [10, 20, 30]

for index in range (len(profits)):
    q = index + 1 
    print(f"Hello the number {q} is {profits[index]}")