import re # re mean regrex

message = "The currect Python version is 3.13 other previous version is 3.12, 3.11, 3.10."
pat = r"[A-z]{3}"
match_obj = re.search(pat, message)
print(match_obj)

#What happens here ? why out put is The but not currect ? 

"""here re mean regrex and in pat variable r"[A-z] mean Start with capital word and finished with small word
{3} mean search this like 3 word i mean search a word like start with capital and finished with small word and word like 3 word
so The is the great e.g, 
"""


pat = r"[A-Z][a-z]{2, 5}"
match_obj = re.search(pat, message)
print(match_obj)

# + => matches 1 or more repetitions of the previous pattern
pat = r"[A-Z][a-z]+"
match_obj = re.search(pat, message)
print(match_obj)
# * => 0 or more repetitions of the previous pattern
pat = r"[A-Z][a-z]*"
match_obj = re.search(pat, message)
print(match_obj)