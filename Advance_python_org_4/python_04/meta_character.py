#(Search) function

import re

language = "Python is a fevoraite language for chosen by begginer"

pat = r"[A-z]{6}"
result = re.search(pat,language)
print(result)

#(match) function , match() see from only first . 

pat = r"[A-z]{2}"

match_obj = re.match(pat, language)
print(match_obj)

#Let's use findall() function
Ph_number = "0987654321, 1234567890, 5678905432, 3092487561"

pat_ph = r"[0-9]{7,}" #7 or more

result_1 = re.findall(pat_ph, Ph_number)
print(result_1)
