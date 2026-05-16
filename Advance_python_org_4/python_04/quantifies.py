import re

pattern = r"[a-zA-Z][a-zA-Z0-9._-]*@[a-z]+\.[a-z]+"

with open("student_details", "rt") as fh:
    lines = fh.readlines()

for line in lines:
    words = line.split()

    for word in words:
        if re.fullmatch(pattern, word):
            print("Valid:", word)