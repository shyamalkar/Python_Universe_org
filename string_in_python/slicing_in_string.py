s1 = "Hello world"

"""Syntax of indexing: string[index]
syntx of slicing: string [start: end:step]
  
- start: starting index at which the slicing atops (excluded)
- step: integer that specifies the step for the slicing

"""
print(s1[2:7:1])   #(start : end : step) # last number is not included .

# at first understand the index
"""
H  e  l  l  o     w  o  r  l  d
0  1  2  3  4  5  6  7  8  9 10
      ↑              ↑
    Start          End (not included)

Take:

2 → l
3 → l
4 → o
5 → space
6 → w

Output:

llo w

What is the meaning of step ? 
2 step means
0 → 2 → 4 → 6 → 8 → 10

3 step means 
0 → 3 → 6 → 9 → 12 → 15

# 2 step

0 = H
2 = l
4 = o
6 = w
8 = r
10 = d

"""

s = "MachineLearning"
print(s[3:9:2]) 
print(s[::3])
#  