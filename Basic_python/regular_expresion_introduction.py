import re # python  Regrex use library

"""
Remember Basic pattern:

Pattern            Meaning         Example
\d                 Digit(0-9)          5
\w	           Word (a-z,A-Z,0-9,_)	  a, A, 1
.	               Any character	   a, #
^	                 Start	          ^Hello
$	                  End	           com$
+	               One or more	        a+
*	               Zero or more	        a*
[]                  	Group	      [abc]

"""


phone = "9876543210"

if re.fullmatch(r'\d{10}', phone):
    print("Valid number")
else:
    print("Invalid number")