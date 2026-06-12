"""
What is Special character ?
   
   Special character is a character where word is a her own power
   these are not normal word, 
   these python special word control pattern.

   those  character called meta charecter.
"""
#e.g.,  (.) Dot
message_number = "h.t hat hot hit hut Hello Hii bro ^Hi"
#dot is not a newline
import re
re.findall("h.t", "hat hot hit hut")

#^(carey) -> start line from here

object_vari = re.search("^Hi", "Hi bro")
print(object_vari)
 
#$Dollar sign end of the line

"""
a* star means 0 or more

"""