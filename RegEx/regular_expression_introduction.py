import re 

s1 = "Python is a programming language"

pat = r"[a-z]{8}"
match_obj = re.search(s1 , pat) #set a single variable using re.search function 
print(match_obj)

# ^ - Caret. (Caret) means 8 small later must be and start first
pat = r"^[a-z]{8}"
match_obj = re.search(pat, s1)
print(f"caret:", match_obj)

# $ - dollar -  end of the string 

pat = r"[a-z]{8}"
match_obj = re.search(pat, s1)
print(f"dollar",match_obj)

# group - () + | (or) 

email = "abc_123@example.com random words and character. x1y2z3.abc. edu"
pat = r"(com|edu)"
match_obj = re.findall(pat, email) #search usage for first order print and findall usage for first and second order both print
print(f"group", match_obj) 

