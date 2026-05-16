import re
with open ("student_details", "rt") as fh: #fh mean file handler
    data = fh.read()#read full file

pattern = r"[a-zA-Z0-9_.-]+[@][a-z]+[.][a-z]+"
# usage for email pattern, [a-zA-Z0-9_.-]+ this part use before @
# \b[a-zA-Z0-9_.-]+@[a-zA-Z]+\.[a-zA-Z]+\b

"""a-z  small letters
A-Z   capital letters
0-9 numbers
- underscroe
. dot for . before com
- hyphen
+ = 1 1 or more  
@ only match with @ symbol
[a-z]+ Domain name e.g., gmail, yahoo
[a-z]+ extension part com , net, org, in
 """

match_obj = re.finditer(pattern,data) # finditer do that full text search , every match , every object found with loop

for matches in match_obj:
    print(matches)

# What is the meanign of output span = (50, 71) ? 
"""span = (start_index, end_index) 
50 ->  match starting from string 50 number position
71 ->  match finished 71 number position (71) except
"""