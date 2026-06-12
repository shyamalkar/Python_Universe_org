import re 

message = "Hello there i am a Python Deploper, and in this lecture i will tech you how to learn python programming language version 13.4.12, are you ready for leqarn this Python programming language."

obj_re = re.findall("[0-9].[0-9][0-9]", message) #[0-9].[0-9] means  start from 0-9 number then after dot then 0-9 inside this message variable .

print(obj_re)

message_1 = "Hello there i am a Python Deploper, and in this lecture i will tech you how to learn python programming language version 13.4.12, are you ready for leqarn this Python programming language."

obj_re_1 = re.findall("[0-9].[0-9].[0-9][0-9]", message_1) #[0-9].[0-9] means  start from 0-9 number then after dot then 0-9 inside this message variable .

print(obj_re)

# \b and \D -> \b matches 1 digit character, it is similar to [0-9]
s1 = message_1 = "Hello there i am a Python Deploper, and in this lecture i will tech you how to learn python programming language version 13.4.12, are you ready for leqarn this Python programming language. shy12"

 
pat = r"[a-z][a-z][a-z]\d" # here r"[a-z][a-z][a-z]\d"r means raw string, means a-z, for 1 small latter, a-z meamns 1 small latter, a-z means again small latter \d for any number
match_obj = re.search(pat, s1)
print(match_obj)