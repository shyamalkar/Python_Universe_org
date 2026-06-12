import re


s1 = "We are learn"
pat = f"[A-Z][a-z]{0}" # A-Z mean start with 1 capital word under A-Z and after small word 
match_obj = re.match(pat, s1)
print(match_obj)

#take a another example , let's find another mobile number 
phones = "Shyamal - 1234567890, Milan-9832110003, push-767848433"
pat = r"[0-9]{10}"
match_obj = re.search(pat, phones)
print(match_obj)
 
phones = "Shyamal - 1234567890, Milan-9832110003, Dipa-7679816991"
pat = r"[0-9]+" # Here number tell us how mnay number must be , so i now use (+) plus mean 0-9 1 or more . 
match_obj = re.findall(pat, phones) # Generally findall usage forfind multiple matching order not only one and search do with only one and search only one.
print(match_obj)
 
#Now we fetch the all phone number, the phone number are at least 7 digits
pat = r"[0-9]{7, }" # 7 or more
match_obj = re.findall(pat, phones)
print(match_obj)
