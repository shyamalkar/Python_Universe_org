"""
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
import re

print("Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

five_element =  num_list[0:5] # 0:5 means count 0-5
print(f"Extact first five elements:", five_element)


reverse_num = num_list[:5][::-1] #Here :5 means count 0-5 and ::-5 means count reverse

print(f"Reversed extracted elements:", reverse_num)
