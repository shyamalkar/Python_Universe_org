name = "Python is a most chosen programming language by devlopers today ."

# all capital letter uppercase .
print(name.upper()) # OUTPUT should be :- PYTHON

# all small letter lowecase . 
print(name.lower()) # Output should be :- hello

print(name.title())  # output = Hello World , title() fun

# capitalize(). only first text write in capital word.

print(name.capitalize()) # output = Python programming

#strip() help us to remove extra space last and first 
text = "   Python   "  
print(text.strip())  

#replace(), one place replace by another place.
text = "I like Java"
print(text.replace("Java", "Python")) # Python replace the Java word.

#find ()
text = "Python"
f = "Kila"
print("Find out where present n in python text ?", text.find("o"))
print('Find function',text.find("t")) # The output should be 2, because it tell us how many word after t presenting, and it always count start from 0 .
print('find function', f.find("K"))

#count() , count function use for  how many time a specific word use in a word language.
text = "banana"

print(text.count("a"))
