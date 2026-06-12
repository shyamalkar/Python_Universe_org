"""
What is quantifiers ?
   Quantifiers tell us how many time come one character / patters .

[a-z]+ #That means small latter come 1 or more
* -> Zero or more
"" -> 0 times
+ -> one or more , minimum 1 time (a+)
"""

#example
#At first import a library
import re

text = "My age is 21 and my brother is 9"

pattern = r"\d+" # + use for (One or More)

result = re.findall(pattern, text)

print(result)
 
#Zero or More -> b have or not , attach both

import re
text = "ac abc abbc abbbbc"

pattern = r"ab*c" # * means b have or not  count both

result = re.findall(pattern, text)
print(result)

#Zero or One


import re

text = "color colour colouur"

pattern = r"colou?r"

result = re.findall(pattern, text)

print(result)

#Exact times {n}



import re

text = "Born in 1998, now in 2026, id: 12345"

pattern = r"\d{4}" #{} for exact 

result = re.findall(pattern, text)

print(result)

#{n, } (At least n)
#Aleast 3 words

import re

text = "hi hello bye yes python AI"

pattern = r"[a-zA-Z]{3,}" #Atleast 3 word or more

result = re.findall(pattern, text)

print(result)