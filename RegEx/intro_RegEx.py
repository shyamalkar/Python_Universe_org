"""
What is RegEx ?

RegEx is a special pattern or rule,
where we use any text or any specific
text word, number, format, math, and 
replace, do valid . 


What we are do using RegEx ?

Is there any text in the correct format to apply the sin
we correct the wrong format 
We remove Unnecessary part .
We fetch importent document from huge dataset.

Why RegEx are need for work ?
Email list
Phone number list
Website data
From data
Log files
CSV/Text files

Using RegEx we clean, filter and check the word. 

"""
message_0 = "I hate love"
"""
#If Python is present in message ,
#  In use for only check , 
# this word or text inside this message box ?
print("Python" in message)
print("version" in message)
print("3.13" in message) 

print(message.find("Python")) # But find() function count Index position. and Python start from 12 number, so the actual reson is why output was 12
print(message.find("maer")) #When -1 showing outptu that mean this word can't detect in message variable.
"""
import re

match_obj = re.search('love', message_0)
print(match_obj)

if re.search('love', message_0): # If any wrong word are write here then 
    #Output showing error:-
    #OutPut is - None , and Another error message is :- Not found . what you are write here. 
    print("Found")
else:
    print("Not found")

#Output meaning is:-
#  where found it ? what found here ? what is similar ?
#What is the meaning of span

#span is a start and end index = span=(start, end)
#match='love' because i found love word . 

message_1 = "hello guys i am Shyamal kar , and i am a Python devloper"

match_obj = re.search("[A-Z].[a-z]", message_1) # Dot means not a dot character , Dot means match a new line character 
print(match_obj)