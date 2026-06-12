import re

#sub() ----> sub means replace

week_list = "Sunday, Monday, Tuesday, Monday, Sunday" #Here is the list we are create week list 
change = "Sunday" # I write (change) variabe for what i want to change ? i write sunday means sunday was replaced by replacement variable order --> Friday
replacement = "Friday"

result = re.sub(change, replacement, week_list)
print(result)

"""Another Example:- """ 
Name_list = "Shyamal, Milan, Supra, Bmw, kc, kc, Budha, "
change_1 = "kc"
replacement_1 = "Subhadip"

result = re.sub( change_1, replacement_1, Name_list)

print(result) 


message = """We are learning re ,  Using RE, we can search for a pattern in a given string.
Using the sub(), we can replace the pattern with a given strings as well.
"""
patt = r'\bre\b' # \b or \b mean atfirst mmust be space or finished the word, after must be space or finished the word that mean fully match with rereplacement = "Regular Expression"result = re.sub(patt, replacement, message) change only small word re . 
print(result)
